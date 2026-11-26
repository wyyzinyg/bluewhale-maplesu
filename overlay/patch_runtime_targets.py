#!/usr/bin/env python3
"""蓝鱼 · 构建期修补（在上游源码树上就地应用）

修七件事：
  1. MapleSU runtime 的 CMake 目标集：公开快照里的 Ultra SDK 静态库还是 skroot 时代产物
     （导出 skroot_env:: 符号，0 个 maplesu::sdk::），libmaplesu_ultra_bridge.so 链接必挂。
     探针不进 APK，桥库由 bluewhaleSkipUltraBridge 决定要不要构建。
  2. provider 构建的 Maven 依赖：tools/specgen 的 cached_jar 只读 Gradle 缓存，而
     buildJailbreakProviders 比依赖解析先执行，缓存里没有 kotlinx-serialization-json
     等 jar，就报 ULTRA_HOST_DEPENDENCY_MISSING（run-23）。缓存里找不到时按 Maven 坐标现拉。
  3. Ultra 桥改成可选输入：跳过时既不构建、也不当成打包必需件。Normal 三条 root 路线不受影响。
  4. bridge 不再作为 buildMapleSuRuntime 的硬性输出声明，否则 Gradle 认为任务永远没产出完。
  5. Release 的 Ultra claim 世代同样属于专有链路，跳桥时一并放行。
  6. Soter 内容提供者的 authority 写死了 dev.maplesu.manager.soter，会和官方 MapleSU
     抢授权，安装报 -13（INSTALL_FAILED_CONFLICTING_PROVIDER）。改成蓝鱼自己的 authority。
  7. 启动图标还原：overlay 会把图标换成矢量鲸鱼，用户要求保留 3.16 的蓝鱼女仆头像，
     这里从 CloudBase 上的 3.16 APK 取回五个密度的原图并改回引用。

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

# —— 6. Release 的 Ultra claim 门槛：没有专有 claim 世代时跳过 ——
# mergeReleaseAssets 的 doFirst 要求 -PmaplesuUltraClaimDirectory 指向新生成的 claim 世代，
# 公开快照缺 runtime/pro，也就没有生成 claim 的输入。Normal-only 构建允许跳过。
if kt.is_file():
    text = kt.read_text(encoding="utf-8")
    gate_old = '    doFirst { check(ultraManagerClaimDirectory != null) { "ULTRA_CLAIM_FRESH_GENERATION_REQUIRED" } }'
    gate_new = ('    doFirst {\n'
                '        check(ultraManagerClaimDirectory != null ||\n'
                '            providers.gradleProperty("bluewhaleSkipUltraBridge").orNull == "true") {\n'
                '            "ULTRA_CLAIM_FRESH_GENERATION_REQUIRED"\n'
                '        }\n'
                '    }')
    hits = text.count(gate_old)
    if hits == 1:
        kt.write_text(text.replace(gate_old, gate_new), encoding="utf-8")
        print("改好 build.gradle.kts: Ultra claim 门槛随跳过开关放行")
    elif "ULTRA_CLAIM_FRESH_GENERATION_REQUIRED\"" in text:
        print("已改过 build.gradle.kts: claim 门槛")
    else:
        failures.append(f"manager/build.gradle.kts: claim 门槛未命中（{hits} 处）")

# —— 5. 开关落进项目 gradle.properties（省得每次命令行传） ——
props = ROOT / "gradle.properties"
switch_line = "bluewhaleSkipUltraBridge=true"
if props.is_file():
    text = props.read_text(encoding="utf-8")
    if switch_line not in text:
        props.write_text(text.rstrip("\n") + "\n" + switch_line + "\n", encoding="utf-8")
        print("改好 gradle.properties: 落 bluewhaleSkipUltraBridge")
    else:
        print("已改过 gradle.properties: bluewhaleSkipUltraBridge")
else:
    props.write_text(switch_line + "\n", encoding="utf-8")
    print("新建 gradle.properties: bluewhaleSkipUltraBridge")

# —— 7. Soter 内容提供者：写死的 dev.maplesu.manager.soter 会和官方 MapleSU 抢授权 ——
# 装包报 INSTALL_FAILED_CONFLICTING_PROVIDER(-13)：两个不同包名的 App 声明了同一 authority。
patch_text("manager/src/main/AndroidManifest.xml", [
    ('android:authorities="dev.maplesu.manager.soter"',
     'android:authorities="com.blue.whale.mask.soter"'),
])
patch_text("manager/src/main/java/dev/maplesu/manager/soter/SoterTargetProvider.kt", [
    ('const val AUTHORITY = "dev.maplesu.manager.soter"',
     'const val AUTHORITY = "com.blue.whale.mask.soter"'),
])

# —— 8. 启动图标还原：overlay 把图标换成了矢量鲸鱼，用户要求保留 3.16 的蓝鱼女仆头像 ——
# 直接从 CloudBase 更新通道上的 3.16 APK 里取 5 个密度的原图，避免把二进制塞进仓库。
ICON_APK_URL = ("https://bluewhale-update-d8e0r9wc21f00b8-1541568372.tcloudbaseapp.com/"
                "bluewhale-manager-v3.16.0-bw-32730.apk")
ICON_MEMBERS = {
    "mdpi": "res/x5.png",
    "hdpi": "res/uK.png",
    "xhdpi": "res/iO.png",
    "xxhdpi": "res/DR.png",
    "xxxhdpi": "res/nV.png",
}
try:
    import io
    import urllib.request
    import zipfile

    archive = zipfile.ZipFile(io.BytesIO(urllib.request.urlopen(ICON_APK_URL, timeout=180).read()))
    for density, member in ICON_MEMBERS.items():
        target = ROOT / f"manager/src/main/res/mipmap-{density}/ic_launcher_foreground_bluewhale.png"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(archive.read(member))
    print("还原蓝鱼启动图标: 5 个密度")
    patch_text("manager/src/main/res/mipmap-anydpi/ic_launcher.xml", [
        ('<foreground android:drawable="@drawable/ic_launcher_foreground" />',
         '<foreground android:drawable="@mipmap/ic_launcher_foreground_bluewhale" />'),
    ])
    patch_text("manager/src/main/res/values/colors.xml", [
        ('<color name="ic_launcher_background">#FF08101F</color>',
         '<color name="ic_launcher_background">#FFFFFFFF</color>'),
    ])
except Exception as error:  # noqa: BLE001
    failures.append(f"启动图标还原失败: {error}")

if failures:
    print("\n修补失败：", file=sys.stderr)
    for item in failures:
        print(" - " + item, file=sys.stderr)
    sys.exit(1)
print("构建期修补已全部应用。")
