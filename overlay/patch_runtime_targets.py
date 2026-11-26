#!/usr/bin/env python3
"""蓝鱼 · 构建期修补（在上游源码树上就地应用）

修两件事：
  1. MapleSU runtime 的 CMake 目标集：公开快照里的 Ultra SDK 静态库还是 skroot 时代产物
     （导出 skroot_env:: 符号），而 ultra/probe 两个探针调 maplesu::sdk::get_sdk_version /
     parse_module_desc_from_zip_file，链接必挂。探针不进 APK，所以只构建发布真正需要的目标。
  2. provider 构建的 Maven 依赖：tools/specgen 的 cached_jar 只读 Gradle 缓存，而
     buildJailbreakProviders 比依赖解析先执行，缓存里没有 kotlinx-serialization-json
     等 jar，就报 ULTRA_HOST_DEPENDENCY_MISSING:kotlinx-serialization-json-jvm（run-23）。
     缓存里找不到时按 Maven Central 坐标现拉。

用法：python3 patch_runtime_targets.py <上游源码根目录>
"""
import pathlib
import sys

ROOT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "src").resolve()
failures: list[str] = []


# —— 1. runtime 目标集 ——
kt = ROOT / "manager/build.gradle.kts"
if kt.is_file():
    text = kt.read_text(encoding="utf-8")
    old = '"--build", runtimeBuild.get().asFile, "-j", "6")'
    new = ('"--build", runtimeBuild.get().asFile,\n'
           '            "--target", "maplesu-runtime", "maplesu-su", "maplesu_bootstrap",\n'
           '            "maplesu_parasite", "maplesu_ultra_bridge", "-j", "6")')
    hits = text.count(old)
    if hits == 1:
        kt.write_text(text.replace(old, new), encoding="utf-8")
        print("改好 build.gradle.kts: runtime 只构建发布所需目标（跳过 ultra 探针）")
    elif "maplesu_ultra_bridge" in text:
        print("已改过 build.gradle.kts: runtime 目标集")
    else:
        failures.append(f"manager/build.gradle.kts: runtime 构建目标行未命中（{hits} 处）")
else:
    failures.append("缺文件: manager/build.gradle.kts")


# —— 2. cached_jar 的 Maven 兜底 ——
product = ROOT / "tools/specgen/specgen/product.py"
if product.is_file():
    src = product.read_text(encoding="utf-8")
    anchor = '    if not files:\n        raise RuntimeError("ULTRA_HOST_DEPENDENCY_MISSING:" + artifact)'
    replacement = (
        '    if not files:\n'
        '        # 公开快照里 provider 先于 Gradle 依赖解析执行，缓存还没落盘；\n'
        '        # 这里按 Maven Central 坐标直接补齐，免掉 ULTRA_HOST_DEPENDENCY_MISSING。\n'
        '        import time\n'
        '        import urllib.request\n'
        '        target = (cache / "caches/modules-2/files-2.1" / group / artifact / version\n'
        '                  / "bluewhale-bootstrap" / (artifact + "-" + version + ".jar"))\n'
        '        target.parent.mkdir(parents=True, exist_ok=True)\n'
        '        url = ("https://repo1.maven.org/maven2/" + group.replace(".", "/") + "/"\n'
        '               + artifact + "/" + version + "/" + artifact + "-" + version + ".jar")\n'
        '        last = None\n'
        '        for _ in range(4):\n'
        '            try:\n'
        '                with urllib.request.urlopen(url, timeout=60) as response:\n'
        '                    target.write_bytes(response.read())\n'
        '                print("补拉 Maven 依赖 " + url)\n'
        '                return target\n'
        '            except Exception as error:  # noqa: BLE001\n'
        '                last = error\n'
        '                time.sleep(10)\n'
        '        raise RuntimeError("ULTRA_HOST_DEPENDENCY_MISSING:" + artifact + str(last))')
    hits = src.count(anchor)
    if hits == 1:
        product.write_text(src.replace(anchor, replacement), encoding="utf-8")
        print("改好 product.py: cached_jar 缺缓存时从 Maven 补拉")
    elif "bluewhale-bootstrap" in src:
        print("已改过 product.py: cached_jar Maven 兜底")
    else:
        failures.append(f"tools/specgen/specgen/product.py: cached_jar 未命中（{hits} 处）")
else:
    failures.append("缺文件: tools/specgen/specgen/product.py")

if failures:
    print("\n修补失败：", file=sys.stderr)
    for item in failures:
        print(" - " + item, file=sys.stderr)
    sys.exit(1)
print("构建期修补已全部应用。")
