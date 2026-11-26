#!/usr/bin/env python3
"""蓝鱼 · 构建期修补（在上游源码树上就地应用）

修四件事：
  1. MapleSU runtime 的 CMake 目标集：公开快照里的 Ultra SDK 静态库还是 skroot 时代产物
     （导出 skroot_env:: 符号，0 个 maplesu::sdk::），libmaplesu_ultra_bridge.so 链接必挂。
     探针不进 APK，桥库由 -PbluewhaleSkipUltraBridge 决定要不要构建。
  2. provider 构建的 Maven 依赖：tools/specgen 的 cached_jar 只读 Gradle 缓存，而
     buildJailbreakProviders 比依赖解析先执行，缓存里没有 kotlinx-serialization-json
     等 jar，就报 ULTRA_HOST_DEPENDENCY_MISSING（run-23）。缓存里找不到时按 Maven 坐标现拉。
  3. Ultra 桥改成可选输入：跳过时既不构建、也不当成打包必需件。Normal 三条 root 路线不受影响。
  4. bridge 不再作为 buildMapleSuRuntime 的硬性输出声明，否则 Gradle 认为任务永远没产出完。

用法：python3 patch_runtime_targets.py <上游源码根目录>
"""
import pathlib
import sys

ROOT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "src").resolve()
failures: list[str] = []


def patch_text(rel: str, pairs: list[tuple[str, str]]) -> None:
    """逐项替换；每一项都必须唯一命中，否则记失败。"""
    path = ROOT / rel
    if not path.is_file():
        failures.append(f"缺文件: {rel}")
        return
    text = path.read_text(encoding="utf-8")
    for old, new in pairs:
        hits = text.count(old)
        if hits != 1:
            failures.append(f"{rel}: 期望 1 处，实际 {hits} 处 → {old.strip()[:60]!r}")
            return
        text = text.replace(old, new)
        print(f"改好 {rel}: {old.strip()[:48]}")
    path.write_text(text, encoding="utf-8")


# —— 1. runtime 目标集（bridge 是否构建由开关决定） ——
kt = ROOT / "manager/build.gradle.kts"
if kt.is_file():
    text = kt.read_text(encoding="utf-8")
    old = '"--build", runtimeBuild.get().asFile, "-j", "6")'
    new = ('"--build", runtimeBuild.get().asFile,\n'
           '            "--target", *(listOf("maplesu-runtime", "maplesu-su", "maplesu_bootstrap",\n'
           '                "maplesu_parasite") + if (providers.gradleProperty("bluewhaleSkipUltraBridge")\n'
           '                .orNull == "true") emptyList() else listOf("maplesu_ultra_bridge")).toTypedArray(),\n'
           '            "-j", "6")')
    hits = text.count(old)
    if hits == 1:
        text = text.replace(old, new)
        print("改好 build.gradle.kts: runtime 目标集按开关决定 bridge")
    elif "bluewhaleSkipUltraBridge" in text:
        print("已改过 build.gradle.kts: runtime 目标集")
    else:
        failures.append(f"manager/build.gradle.kts: runtime 构建目标行未命中（{hits} 处）")
    kt.write_text(text, encoding="utf-8")
else:
    failures.append("缺文件: manager/build.gradle.kts")

# —— 3. Ultra 桥改成可选输入 ——
patch_text("manager/build.gradle.kts", [
    ("    @get:InputFile abstract val ultraBridgeLibrary: RegularFileProperty",
     "    // BlueWhale：公开快照的 SDK 壳库缺 maplesu::sdk:: 符号，跳过 Ultra 桥时该输入可为空\n"
     "    @get:Optional @get:InputFile abstract val ultraBridgeLibrary: RegularFileProperty"),
    ('        ultraBridgeLibrary.get().asFile.copyTo(jniDirectory.get().file("arm64-v8a/libmaplesu_ultra_bridge.so").asFile,\n'
     "            overwrite = true)",
     "        ultraBridgeLibrary.orNull?.asFile?.copyTo(\n"
     '            jniDirectory.get().file("arm64-v8a/libmaplesu_ultra_bridge.so").asFile, overwrite = true)'),
    ('    ultraBridgeLibrary.set(runtimeBuild.map { it.file("libmaplesu_ultra_bridge.so") })',
     '    if (providers.gradleProperty("bluewhaleSkipUltraBridge").orNull != "true") {\n'
     '        ultraBridgeLibrary.set(runtimeBuild.map { it.file("libmaplesu_ultra_bridge.so") })\n'
     "    }"),
])

# bridge 作为 buildMapleSuRuntime 的声明输出也得摘掉，否则 Gradle 认为任务永远没产出完
if kt.is_file():
    text = kt.read_text(encoding="utf-8")
    out_old = '        runtimeBuild.map { it.file("libmaplesu_ultra_bridge.so") })'
    out_new = ('        *(if (providers.gradleProperty("bluewhaleSkipUltraBridge").orNull == "true") arrayOf<Any>()\n'
               '        else arrayOf<Any>(runtimeBuild.map { it.file("libmaplesu_ultra_bridge.so") })))')
    hits = text.count(out_old)
    if hits == 1:
        text = text.replace(out_old, out_new)
        kt.write_text(text, encoding="utf-8")
        print("改好 build.gradle.kts: bridge 不再作为硬性输出")
    elif "arrayOf<Any>()" in text:
        print("已改过 build.gradle.kts: bridge 输出声明")
    else:
        failures.append(f"manager/build.gradle.kts: bridge 输出声明未命中（{hits} 处）")

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
