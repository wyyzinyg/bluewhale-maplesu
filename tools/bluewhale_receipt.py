#!/usr/bin/env python3
"""蓝鱼构建回执：从 APK 里读出真正随包分发的 native 载荷，逐项统计包名。

为什么需要它：
  3.20.x 的构建只把上游预编译的 `libksud_ksu.so` 拷进 APK，源码里改的包名不会进去。
  而 ko 是 raw DEFLATE 压在 so 里的，`strings` 看不到解压后的内容——必须解压后统计。

做什么：
  1. 从 APK 取 `lib/arm64-v8a/libksud_ksu.so`（以及 libmaplesu_ksu.so 等同类），算大小与 SHA-256；
  2. 逐字节扫 raw DEFLATE 流；rust-embed 的真实流不保证 4 字节对齐；
  3. 只把 ET_REL 且含有效 vermagic / 模块名的 ELF 识别为 KO，排除 ksuinit 等用户态程序；
  4. 对 so 本体也统计一次（可执行段里的旧包名同样算残留）；
  5. 输出人类可读表格 + `build-receipt.json`。

用法：
    python3 tools/bluewhale_receipt.py <apk> [-o build-receipt.json] [--min-size 100000]

退出码：0 表示所有内嵌 ko 都已经是新包名且不含旧包名；1 表示有残留；2 表示参数/文件错误。
"""
from __future__ import annotations

import argparse
import hashlib
import os
import json
import re
import sys
import time
import zipfile
import zlib

NEW_PKG = b"com.blue.whale.mask"
OLD_PKG = b"dev.maplesu.manager"
SO_NAMES = (
    "lib/arm64-v8a/libksud_ksu.so",
    "lib/arm64-v8a/libmaplesu_ksu.so",
)
REQUIRED_KMIS = (
    "android12-5.10", "android13-5.15", "android14-6.1",
    "android15-6.6", "android16-6.12", "android17-6.18",
)


def find_elf_streams(data: bytes, min_size: int, step: int = 1):
    """扫 raw DEFLATE 流，返回解压后以 ELF 开头的 (offset, payload)。"""
    found = []
    n = len(data)
    offset = 0
    while offset < n - 64:
        try:
            engine = zlib.decompressobj(-15)
            head = engine.decompress(data[offset:offset + 65536])
            if not head:
                offset += step
                continue
            if not head.startswith(b"\x7fELF"):
                offset += step
                continue
            chunks = [head]
            total = len(head)
            cursor = offset + 65536
            while not engine.eof and cursor < n and total < 64 * 1024 * 1024:
                block = data[cursor:cursor + (1 << 20)]
                if not block:
                    break
                chunks.append(engine.decompress(block))
                total += len(chunks[-1])
                cursor += len(block)
            payload = b"".join(chunks)
            if len(payload) >= min_size and engine.eof:
                found.append((offset, payload))
        except zlib.error:
            pass
        offset += step
    return found


# ── 最小二进制 XML 解析：只为拿到 packageName / versionCode / versionName ──────────
ATTR_VERSION_CODE = 0x0101021B
ATTR_VERSION_NAME = 0x0101021C


def _string_pool(data: bytes, start: int) -> list[str]:
    header_size = int.from_bytes(data[start + 2:start + 4], "little")
    declared = int.from_bytes(data[start + 8:start + 12], "little")
    flags = int.from_bytes(data[start + 16:start + 20], "little")
    strings_start = int.from_bytes(data[start + 20:start + 24], "little")
    utf8 = bool(flags & 0x100)
    offsets = [int.from_bytes(data[start + header_size + i * 4:start + header_size + i * 4 + 4], "little")
               for i in range(declared)]
    base = start + strings_start
    out = []
    for offset in offsets:
        cursor = base + offset
        if utf8:
            # uleb128 字符数，然后 uleb128 字节数
            cursor += 2 if data[cursor] & 0x80 else 1
            length = data[cursor]
            if length & 0x80:
                length = ((length & 0x7F) << 8) | data[cursor + 1]
                cursor += 2
            else:
                cursor += 1
            out.append(data[cursor:cursor + length].decode("utf-8", "replace"))
        else:
            length = int.from_bytes(data[cursor:cursor + 2], "little")
            cursor += 2
            out.append(data[cursor:cursor + length * 2].decode("utf-16-le", "replace"))
    return out


def read_manifest_identity(apk_path: str) -> dict:
    """从 AndroidManifest.xml（二进制 XML）里取包名与版本，取不到就留空。"""
    import zipfile as _zip
    with _zip.ZipFile(apk_path) as archive:
        data = archive.read("AndroidManifest.xml")
    result = {"packageName": "", "versionCode": 0, "versionName": ""}
    if len(data) < 8:
        return result
    position = 8
    strings: list[str] = []
    resource_ids: list[int] = []
    while position + 8 <= len(data):
        chunk_type = int.from_bytes(data[position:position + 2], "little")
        chunk_size = int.from_bytes(data[position + 4:position + 8], "little")
        if chunk_size <= 0:
            break
        if chunk_type == 0x0001:
            strings = _string_pool(data, position)
        elif chunk_type == 0x0180:
            count = (chunk_size - 8) // 4
            resource_ids = [int.from_bytes(data[position + 8 + i * 4:position + 12 + i * 4], "little")
                            for i in range(count)]
        elif chunk_type == 0x0102:
            header_size = int.from_bytes(data[position + 2:position + 4], "little")
            # node header（type/size/lineNumber/comment）= header_size，attrExt 紧跟其后；
            # attributeStart 是相对 attrExt 起点的偏移。
            ext = position + header_size
            attribute_start = int.from_bytes(data[ext + 8:ext + 10], "little")
            attribute_size = int.from_bytes(data[ext + 10:ext + 12], "little")
            attribute_count = int.from_bytes(data[ext + 12:ext + 14], "little")
            cursor = ext + attribute_start
            for _ in range(attribute_count):
                name_index = int.from_bytes(data[cursor + 4:cursor + 8], "little")
                raw_value = int.from_bytes(data[cursor + 8:cursor + 12], "little")
                value_type = data[cursor + 15]
                value_data = int.from_bytes(data[cursor + 16:cursor + 20], "little")
                name = strings[name_index] if 0 <= name_index < len(strings) else ""
                resource_id = resource_ids[name_index] if 0 <= name_index < len(resource_ids) else 0
                if name == "package" and not result["packageName"]:
                    value = strings[value_data] if raw_value == 0xFFFFFFFF else ""
                    result["packageName"] = value or (strings[raw_value] if raw_value < len(strings) else "")
                elif resource_id == ATTR_VERSION_CODE:
                    result["versionCode"] = value_data
                elif resource_id == ATTR_VERSION_NAME:
                    result["versionName"] = (strings[value_data] if 0 <= value_data < len(strings) else "")
                cursor += attribute_size
        position += chunk_size
    return result


def read_vermagic(payload: bytes) -> str:
    """只接受 vermagic 起始处的合法内核 release，绝不把相邻二进制当 KMI。"""
    match = re.search(rb"vermagic=([0-9]+\.[0-9]+\.[0-9]+[^\x00\s]*)", payload)
    return match.group(1).decode("ascii") if match else ""


def guess_kmi(payload: bytes) -> str:
    release = read_vermagic(payload)
    match = re.search(r"android(\d{2})-(\d+\.\d+)", release)
    if match:
        return f"android{match.group(1)}-{match.group(2)}"
    table = {(5, 10): "android12-5.10", (5, 15): "android13-5.15", (6, 1): "android14-6.1",
             (6, 6): "android15-6.6", (6, 12): "android16-6.12", (6, 18): "android17-6.18"}
    version = re.match(r"(\d+)\.(\d+)\.\d+", release)
    if version:
        return table.get((int(version.group(1)), int(version.group(2))), "")
    return ""


def summarize(payload: bytes) -> dict:
    is_elf = payload.startswith(b"\x7fELF") and len(payload) >= 20
    # Linux LKM 是 ET_REL(1)；ksuinit / maplesu_vrinit 是 ET_EXEC(2)，不能按 vermagic 字符串误判。
    is_rel = is_elf and int.from_bytes(payload[16:18], "little") == 1
    vermagic = read_vermagic(payload) if is_rel else ""
    if is_rel and vermagic and b"kernelsu\x00" in payload:
        role = "kernelsu"
    elif is_rel and vermagic and b"maplesu_vr\x00" in payload:
        role = "maplesu_vr"
    else:
        role = ""
    return {
        "kind": role or "elf-other",
        "role": role,
        "kmi": guess_kmi(payload) if role else "",
        "vermagic": vermagic,
        "size": len(payload),
        "sha256": hashlib.sha256(payload).hexdigest(),
        "newPkgCount": payload.count(NEW_PKG),
        "oldPkgCount": payload.count(OLD_PKG),
        "isElf": is_elf,
    }


def analyze(apk_path: str, min_size: int, gate_flags: dict, commit: str, run_id: str) -> dict:
    started = time.time()
    with open(apk_path, "rb") as handle:
        blob = handle.read()
    identity = read_manifest_identity(apk_path)
    receipt = {
        "schema": "bluewhale-build-receipt/1",
        "generatedAt": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "commit": commit,
        "ciRunId": run_id,
        "packageName": identity["packageName"],
        "versionCode": identity["versionCode"],
        "versionName": identity["versionName"],
        "apk": {
            "path": apk_path,
            "size": len(blob),
            "sha256": hashlib.sha256(blob).hexdigest(),
            # v2/v3 签名没有 META-INF/*.RSA，证书指纹由发布侧 apksigner 填
            "certSha256": "",
        },
        "native": {
            "libksudSha256": "", "libksudSize": 0, "soOldPackageCount": 0,
            "requiredKmis": list(REQUIRED_KMIS), "kmis": [], "companionKmis": [],
            "missingKmis": [], "duplicateKmis": [], "coverageOk": False,
        },
        "gates": {
            "buildChain": gate_flags.get("buildChain", False),
            "verifyPayload": gate_flags.get("verifyPayload", False),
            "unitTests": gate_flags.get("unitTests", False),
            "deviceRoot": gate_flags.get("deviceRoot", False),
            "homeUi": gate_flags.get("homeUi", False),
        },
        "channels": {"cloudbase": "", "cloudbaseBrand": "", "githubRaw": "", "tiana": ""},
        "notes": "",
    }
    archive = zipfile.ZipFile(apk_path)
    seen = set()
    for name in SO_NAMES:
        try:
            lib = archive.read(name)
        except KeyError:
            continue
        digest = hashlib.sha256(lib).hexdigest()
        receipt["native"]["soOldPackageCount"] += lib.count(OLD_PKG)
        if name.endswith("libksud_ksu.so"):
            receipt["native"]["libksudSha256"] = digest
            receipt["native"]["libksudSize"] = len(lib)
        for offset, payload in find_elf_streams(lib, min_size):
            payload_sha = hashlib.sha256(payload).hexdigest()
            if payload_sha in seen:
                continue
            seen.add(payload_sha)
            info = summarize(payload)
            if info["kind"] not in ("kernelsu", "maplesu_vr"):
                continue
            row = {
                "kmi": info["kmi"] or "unknown",
                "role": info["role"],
                "vermagic": info["vermagic"],
                "newPackageCount": info["newPkgCount"],
                "oldPackageCount": info["oldPkgCount"],
                "koSha256": payload_sha,
                "size": info["size"],
                "soOffset": offset,
            }
            target = "kmis" if info["role"] == "kernelsu" else "companionKmis"
            receipt["native"][target].append(row)
    native = receipt["native"]
    native["kmis"].sort(key=lambda row: row["kmi"])
    native["companionKmis"].sort(key=lambda row: row["kmi"])
    counts = {kmi: sum(row["kmi"] == kmi for row in native["kmis"]) for kmi in REQUIRED_KMIS}
    native["missingKmis"] = [kmi for kmi, count in counts.items() if count == 0]
    native["duplicateKmis"] = [kmi for kmi, count in counts.items() if count > 1]
    native["coverageOk"] = (not native["missingKmis"] and not native["duplicateKmis"]
                            and len(native["kmis"]) == len(REQUIRED_KMIS)
                            and all(row["newPackageCount"] > 0 and row["oldPackageCount"] == 0
                                    for row in native["kmis"]))
    receipt["elapsedSeconds"] = round(time.time() - started, 1)
    return receipt


def render(receipt: dict) -> str:
    apk = receipt["apk"]
    lines = [
        f"{receipt['versionName'] or '?'} ({receipt['versionCode'] or '?'})  {apk['path']}",
        f"  APK {apk['size']} bytes  sha256={apk['sha256']}",
        f"  libksud {receipt['native']['libksudSize']} bytes  sha256={receipt['native']['libksudSha256']}",
    ]
    kmis = receipt["native"]["kmis"]
    if not kmis:
        lines.append("  ko 载荷：未找到（so 里没有可解压的内核模块）")
    for row in kmis:
        state = "OK" if row["oldPackageCount"] == 0 and row["newPackageCount"] > 0 else "⚠ 包名异常"
        lines.append(
            f"  {row['kmi']:<20} size={row['size']:<9} 新 {row['newPackageCount']} / 旧 {row['oldPackageCount']}  {state}"
        )
    native = receipt["native"]
    lines.append(f"  maplesu_vr 伴生模块：{len(native['companionKmis'])} 份（独立识别，不冒充主 KO）")
    bad = (not native["coverageOk"] or native.get("soOldPackageCount", 0) > 0
           or any(row["oldPackageCount"] > 0 for row in native["companionKmis"]))
    if native["missingKmis"] or native["duplicateKmis"]:
        lines.append(f"  缺失={native['missingKmis']} 重复={native['duplicateKmis']}")
    lines.append("  结论：" + ("六 KMI 主 KO 覆盖及包名门禁通过" if not bad else "native 覆盖或包名门禁失败，不能据此发布"))
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="生成蓝鱼构建回执（按 bluewhale-build-receipt/1 模板）")
    parser.add_argument("apk")
    parser.add_argument("-o", "--output", default="build-receipt.json")
    parser.add_argument("--min-size", type=int, default=100_000)
    parser.add_argument("--commit", default=os.environ.get("GITHUB_SHA", ""))
    parser.add_argument("--ci-run-id", default=os.environ.get("GITHUB_RUN_ID", ""))
    for gate in ("buildChain", "verifyPayload", "unitTests", "deviceRoot", "homeUi"):
        parser.add_argument(f"--gate-{gate}", action="store_true", default=False)
    args = parser.parse_args()
    gates = {name: getattr(args, f"gate_{name}") for name in
             ("buildChain", "verifyPayload", "unitTests", "deviceRoot", "homeUi")}
    try:
        receipt = analyze(args.apk, args.min_size, gates, args.commit, args.ci_run_id)
    except FileNotFoundError:
        print(f"找不到文件: {args.apk}", file=sys.stderr)
        return 2
    except zipfile.BadZipFile:
        print(f"不是合法 APK: {args.apk}", file=sys.stderr)
        return 2
    text = render(receipt)
    print(text)
    with open(args.output, "w", encoding="utf-8") as handle:
        json.dump(receipt, handle, ensure_ascii=False, indent=2)
    print(f"\n回执已写入 {args.output}（耗时 {receipt['elapsedSeconds']}s）")
    return 1 if "不能据此发布" in text else 0


if __name__ == "__main__":
    raise SystemExit(main())
