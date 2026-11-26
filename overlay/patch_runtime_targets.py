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
  7. 品牌资产还原：overlay 会把启动图标和启动页换成矢量鲸鱼，用户要求保留 3.16 的蓝鱼女仆头像，
     这里从 CloudBase 上的 3.16 APK 取回图标五个密度与启动页位图并改回引用。

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

# —— 8. 品牌资产还原：overlay 把图标换成了矢量鲸鱼，用户要求保留 3.16 的蓝鱼女仆头像 ——
# 图标与启动页位图是从 3.16 APK 原样抽出来的，挂在独立静态站上（逐字节一致）。
# 早先直接拉 3.16 APK（8.7MB），但 GitHub runner 每次都在 8682852 字节处被链路截断：
# run-33 / run-34 的 IncompleteRead 六次重试全停在同一个偏移，不是偶发，是硬截断。
# 改成分文件取，单个最大 278KB，每个单独校验 size + sha256，坏哪个重试哪个。
BRAND_BASE = "https://bluewhale-brand-bluewhale-update-d8e0r9wc21f00b8.webapps.tcloudbase.com"
BRAND_ASSETS = {
    # 目标路径（相对 src）: (远端文件名, 字节数, sha256)
    "manager/src/main/res/mipmap-mdpi/ic_launcher_foreground_bluewhale.png":
        ("ic_launcher_foreground-mdpi.png", 17309,
         "55ffbf0b0d188e1a60b396a0b7a1b253ca599b6c8853ff1f76a4e746b5d89d14"),
    "manager/src/main/res/mipmap-hdpi/ic_launcher_foreground_bluewhale.png":
        ("ic_launcher_foreground-hdpi.png", 35769,
         "8caa2d7e47c6eb44fb72f7d8f825d61c94530a4990f10610de2b77d7b12fc471"),
    "manager/src/main/res/mipmap-xhdpi/ic_launcher_foreground_bluewhale.png":
        ("ic_launcher_foreground-xhdpi.png", 58521,
         "2718006d18c19ca2481b652d89bd739e9374d62679239b1298762a52f4370b58"),
    "manager/src/main/res/mipmap-xxhdpi/ic_launcher_foreground_bluewhale.png":
        ("ic_launcher_foreground-xxhdpi.png", 117077,
         "cdd71cb47cb4638fb60d8b09f08abff42f02e83d73084eec49f115916b152017"),
    "manager/src/main/res/mipmap-xxxhdpi/ic_launcher_foreground_bluewhale.png":
        ("ic_launcher_foreground-xxxhdpi.png", 189659,
         "ee7bb3c9675710470ac698fe76d57dbb9e9f1893667c8a6ab79d78080eb72208"),
    "manager/src/main/res/drawable-nodpi/ic_app_brand.png":
        ("ic_app_brand.png", 278497,
         "5adebcc7c31950aa9dc40c3583e3e2a245c61025ff06a0baeec14ba5be247337"),
}


def fetch_bytes(url: str, size: int, sha256: str, attempts: int = 5) -> bytes:
    """取单个小文件：按字节数与 sha256 校验，短读/脏包重试。"""
    import hashlib
    import time
    import urllib.request

    last: Exception | None = None
    for attempt in range(1, attempts + 1):
        try:
            request = urllib.request.Request(url, headers={"User-Agent": "bluewhale-ci"})
            with urllib.request.urlopen(request, timeout=60) as response:
                payload = response.read()
            if len(payload) != size:
                raise IOError(f"大小不符 {len(payload)} != {size}")
            digest = hashlib.sha256(payload).hexdigest()
            if digest != sha256:
                raise IOError(f"sha256 不符 {digest[:12]} != {sha256[:12]}")
            return payload
        except Exception as error:  # noqa: BLE001
            last = error
            print(f"{url.rsplit('/', 1)[-1]} 第 {attempt}/{attempts} 次下载失败: {error}",
                  file=sys.stderr)
            time.sleep(min(4 * attempt, 20))
    raise RuntimeError(f"下载失败（已试 {attempts} 次）{url}: {last}")


try:
    for rel, (name, size, sha) in BRAND_ASSETS.items():
        target = ROOT / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(fetch_bytes(f"{BRAND_BASE}/{name}", size, sha))
    print("还原蓝鱼图标与启动页位图: 6 个文件，与 3.16 逐字节一致")
    patch_text("manager/src/main/res/mipmap-anydpi/ic_launcher.xml", [
        ('<foreground android:drawable="@drawable/ic_launcher_foreground" />',
         '<foreground android:drawable="@mipmap/ic_launcher_foreground_bluewhale" />'),
    ])
    patch_text("manager/src/main/res/values/colors.xml", [
        ('<color name="ic_launcher_background">#FF08101F</color>',
         '<color name="ic_launcher_background">#FFFFFFFF</color>'),
        ('<color name="ic_splash_background">#FF774F6F</color>',
         '<color name="ic_splash_background">#FFFFFFFF</color>'),
    ])
    # 启动页：3.16 的 drawable/ic_launcher_splash 就是一个 bitmap(center, @drawable/ic_app_brand)，
    # 主题 windowSplashScreenAnimatedIcon 指向它、底色纯白。3.17 上游改成方块动画 + 品红底，
    # 只换资源不换主题等于没换（主题指向 maplesu_splash_brand），必须两处一起改回。
    splash = ROOT / "manager/src/main/res/drawable/ic_launcher_splash.xml"
    splash.write_text(
        '<?xml version="1.0" encoding="utf-8"?>\n'
        '<bitmap xmlns:android="http://schemas.android.com/apk/res/android"\n'
        '    android:gravity="center"\n'
        '    android:src="@drawable/ic_app_brand" />\n',
        encoding="utf-8",
    )
    # 主题有两份：values 与 values-night。只改白天那份，深色模式下启动页仍是上游方块动画
    # （3.16 的 Starting 主题没有 night 变体，白色蓝鱼图两种模式都一样），两份必须都改。
    for themes in ("manager/src/main/res/values/themes.xml",
                   "manager/src/main/res/values-night/themes.xml"):
        patch_text(themes, [
            ('<item name="windowSplashScreenBackground">@color/maple_window_background</item>',
             '<item name="windowSplashScreenBackground">@color/ic_splash_background</item>'),
            ('<item name="windowSplashScreenAnimatedIcon">@drawable/maplesu_splash_brand</item>',
             '<item name="windowSplashScreenAnimatedIcon">@drawable/ic_launcher_splash</item>'),
        ])
    print("还原启动页: ic_app_brand 位图 + 白底 + 主题指向")
except Exception as error:  # noqa: BLE001
    failures.append(f"品牌资产还原失败: {error}")

# —— 9. 蓝鱼品牌皮肤：深色底、去枫叶、去 MapleSU 可见文案 ——
# 3.17 只换了包名/图标，界面还是上游那套：浅色纸感、枫叶飘落、@MapleSU_Debug_Bot 横幅、
# “关于 MapleSU”、红色错误条。装上去像把源码直接搬过来。这里改默认外观与可见文案。
patch_text("manager/src/main/java/com/maplesu/core/data/repository/SettingsRepositoryImpl.kt", [
    ('get() = if (ThemeLock.ENABLED) ThemeLock.THEME_MODE else appearance.getInt("color_mode", 0)',
     'get() = if (ThemeLock.ENABLED) ThemeLock.THEME_MODE else appearance.getInt("color_mode", 2)'),
])
patch_text("manager/src/main/java/com/maplesu/core/ui/viewmodel/MainActivityViewModel.kt", [
    ('    init {\n        prefs.registerOnSharedPreferenceChangeListener(listener)',
     '    init {\n'
     '        // 蓝鱼品牌皮肤：已经装过 3.17 的用户也切到深色、关掉枫叶（只跑一次）\n'
     '        if (!prefs.getBoolean("bw_brand_skin_v1", false)) {\n'
     '            prefs.edit().putBoolean("bw_brand_skin_v1", true)\n'
     '                .putBoolean("snow_enabled", false).apply()\n'
     '            settingRepo.themeMode = 2\n'
     '            settingRepo.miuixMonet = false\n'
     '            _uiState.value = readUiState()\n'
     '        }\n'
     '        prefs.registerOnSharedPreferenceChangeListener(listener)'),
])
patch_text("manager/src/main/java/com/maplesu/core/ui/util/AppearancePrefsPolicy.kt", [
    ('        "snow_enabled" to enabled,', '        "snow_enabled" to false,'),
])
patch_text("manager/src/main/java/com/maplesu/core/ui/MainActivity.kt", [
    ('if ((skin.appliedScene && uiState.snowEnabled) ||\n                        (!skin.appliedScene && uiMode == UiMode.Miuix && uiState.introComic)) {',
     'if (uiState.snowEnabled) {'),
])
patch_text("manager/src/main/java/com/maplesu/core/ui/screen/home/HomeBetaBanner.kt", [
    ('internal const val MAPLESU_FEEDBACK_URL = "https://t.me/MapleSU_Debug_Bot"',
     'internal const val MAPLESU_FEEDBACK_URL = "https://github.com/wyyzinyg/bluewhale-maplesu"'),
])
patch_text("manager/src/main/java/com/maplesu/core/ui/screen/home/AboutMapleDialogMiuix.kt", [
    ('        Text(\n'
     '            text = aboutCommunityText(stringResource(R.string.about_maple_community), colorScheme.primary),\n'
     '            modifier = Modifier.fillMaxWidth()\n'
     '                .background(colorScheme.primary.copy(alpha = 0.08f), RoundedCornerShape(12.dp))\n'
     '                .padding(12.dp),\n'
     '            fontSize = 14.sp,\n'
     '            fontWeight = FontWeight.Medium,\n'
     '            color = colorScheme.onSurface,\n'
     '        )\n'
     '        CreditsMiuix()',
     '        CreditsMiuix()'),
    ('        AdvisorWallMiuix(Modifier.padding(top = 4.dp))\n', ''),
    ('        kind = BrandBannerKind.MAPLE,\n', '        kind = null,\n'),
])
patch_text("manager/src/main/java/com/maplesu/core/ui/screen/home/AboutMapleDialogMaterial.kt", [
    ('        Text(\n'
     '            text = aboutCommunityText(stringResource(R.string.about_maple_community), MaterialTheme.colorScheme.primary),\n'
     '            modifier = Modifier.fillMaxWidth()\n'
     '                .background(MaterialTheme.colorScheme.primary.copy(alpha = 0.08f), RoundedCornerShape(12.dp))\n'
     '                .padding(12.dp),\n'
     '            style = MaterialTheme.typography.bodyMedium,\n'
     '            fontWeight = FontWeight.Medium,\n'
     '        )\n'
     '        CreditsMaterial()',
     '        CreditsMaterial()'),
    ('        AdvisorWallMaterial(Modifier.padding(top = 4.dp))\n', ''),
    ('        kind = BrandBannerKind.MAPLE,\n', '        kind = null,\n'),
])
patch_text("manager/src/main/res/values/themes.xml", [
    ('<style name="Theme.KernelSU" parent="android:Theme.Material.Light.NoActionBar">',
     '<style name="Theme.KernelSU" parent="android:Theme.Material.NoActionBar">'),
    ('<item name="android:windowLightStatusBar">true</item>',
     '<item name="android:windowLightStatusBar">false</item>'),
    ('<item name="android:windowLightNavigationBar">true</item>',
     '<item name="android:windowLightNavigationBar">false</item>'),
])
patch_text("manager/src/main/res/values/colors.xml", [
    ('<color name="maple_window_background">#FFF7F7F7</color>',
     '<color name="maple_window_background">#FF070B14</color>'),
])
patch_text("manager/src/main/res/values-night/colors.xml", [
    ('<color name="maple_window_background">#FF000000</color>',
     '<color name="maple_window_background">#FF070B14</color>'),
])
patch_text("manager/build.gradle.kts", [
    ("        versionCode = 32731", "        versionCode = 32732"),
    ('        versionName = "3.17.0-bw"', '        versionName = "3.18.0-bw"'),
])

# 文案：横幅 / 关于 / 环境检查 / 超级用户 / 模块
patch_text("manager/src/main/res/values/maplesu_release_strings.xml", [
    ('<string name="home_public_beta_notice">公测版本非正式版本，含有不稳定实现，如遇问题请在 @MapleSU_Debug_Bot 反馈</string>',
     '<string name="home_public_beta_notice">蓝色大肥鱼 · 内测版｜遇到问题请在 GitHub 仓库反馈</string>'),
])
patch_text("manager/src/main/res/values/maplesu_about.xml", [
    ('<string name="about_maple_title">About MapleSU</string>',
     '<string name="about_maple_title">About BlueWhale</string>'),
    ('<string name="about_maple_entry_summary">Developers, open-source credits and license</string>',
     '<string name="about_maple_entry_summary">Version, open-source credits and license</string>'),
    ('<string name="about_maple_overview">Overview: an Android root manager with two work modes you can switch between.</string>',
     '<string name="about_maple_overview">Overview: BlueWhale is an Android root manager built on MapleSU; upstream credits and the GPL-3.0 license are kept.</string>'),
    ('<string name="about_maple_overview_plain">Overview: an Android root manager.</string>',
     '<string name="about_maple_overview_plain">Overview: an Android root manager built on MapleSU.</string>'),
    ('<string name="about_maple_developers">Developer: MapleAutumn.</string>',
     '<string name="about_maple_developers">Maintained by the BlueWhale team · Upstream: MapleSU (MapleAutumn)</string>'),
])
patch_text("manager/src/main/res/values-zh-rCN/maplesu_about.xml", [
    ('<string name="about_maple_title">关于 MapleSU</string>',
     '<string name="about_maple_title">关于蓝色大肥鱼</string>'),
    ('<string name="about_maple_entry_summary">开发者、开源致谢与许可</string>',
     '<string name="about_maple_entry_summary">版本、开源致谢与许可</string>'),
    ('<string name="about_maple_overview">简介：一款 Android Root 管理器，提供两种工作模式，按需切换。</string>',
     '<string name="about_maple_overview">简介：蓝色大肥鱼是基于 MapleSU 二次开发的 Android Root 管理器，保留上游署名与 GPL-3.0 许可。</string>'),
    ('<string name="about_maple_overview_plain">简介：一款 Android Root 管理器。</string>',
     '<string name="about_maple_overview_plain">简介：一款基于 MapleSU 的 Android Root 管理器。</string>'),
    ('<string name="about_maple_developers">开发者：MapleAutumn。</string>',
     '<string name="about_maple_developers">维护：蓝鱼团队 · 上游：MapleSU（MapleAutumn）</string>'),
])
patch_text("manager/src/main/res/values/home_environment_check.xml", [
    ('<string name="home_environment_check_failed">Environment check did not complete</string>',
     '<string name="home_environment_check_failed">No usable root environment detected</string>'),
    ('<string name="home_environment_check_timeout_summary">The environment probe timed out. Tap to retry or export diagnostic logs.</string>',
     '<string name="home_environment_check_timeout_summary">Probe timed out. Tap to retry; finish root setup first if the device is not rooted.</string>'),
    ('<string name="home_environment_check_failed_summary">The environment probe failed. Tap to retry or export diagnostic logs.</string>',
     '<string name="home_environment_check_failed_summary">Probe failed. Tap to retry or export diagnostic logs; root may not be set up yet.</string>'),
    ('<string name="home_environment_check_unconfirmed_summary">The runtime could not be confirmed. Tap to retry or export diagnostic logs.</string>',
     '<string name="home_environment_check_unconfirmed_summary">Runtime not confirmed yet. Tap to retry; this is expected before root is set up.</string>'),
])
patch_text("manager/src/main/res/values-zh-rCN/home_environment_check.xml", [
    ('<string name="home_environment_check_failed">环境检查未完成</string>',
     '<string name="home_environment_check_failed">未检测到可用的 root 环境</string>'),
    ('<string name="home_environment_check_timeout_summary">环境探测已超时。点击重试，或导出诊断日志。</string>',
     '<string name="home_environment_check_timeout_summary">探测超时了。点重试再探一次；还没 root 的话，先按主页路线完成环境准备。</string>'),
    ('<string name="home_environment_check_failed_summary">环境探测失败。点击重试，或导出诊断日志。</string>',
     '<string name="home_environment_check_failed_summary">探测没成功。点重试或导出诊断日志；还没 root 时这是正常现象。</string>'),
    ('<string name="home_environment_check_unconfirmed_summary">运行环境尚未确认。点击重试，或导出诊断日志。</string>',
     '<string name="home_environment_check_unconfirmed_summary">运行环境还没确认。点重试；没 root 时先空着是正常的。</string>'),
])
patch_text("manager/src/main/res/values/strings_workmode.xml", [
    ('<string name="work_mode_superuser_unresolved">The current mode is not confirmed yet, so the superuser list is unavailable.</string>',
     '<string name="work_mode_superuser_unresolved">No root environment yet, so the superuser list stays empty.</string>'),
])
patch_text("manager/src/main/res/values-zh-rCN/strings_workmode.xml", [
    ('<string name="work_mode_superuser_unresolved">还没有确认当前模式，超级用户列表暂不可用</string>',
     '<string name="work_mode_superuser_unresolved">还没有可用的 root 环境，超级用户列表先空着</string>'),
    ('<string name="work_mode_superuser_unavailable">当前模式下超级用户列表暂时不可用</string>',
     '<string name="work_mode_superuser_unavailable">当前模式下暂不提供超级用户列表</string>'),
])
patch_text("manager/src/main/res/values/maplesu_strings.xml", [
    ('<string name="module_load_failed">Failed to load modules. Please try again.</string>',
     '<string name="module_load_failed">Module service is not ready. Check root status and retry.</string>'),
])
patch_text("manager/src/main/res/values-zh-rCN/maplesu_strings.xml", [
    ('<string name="module_load_failed">加载模块失败，请重试</string>',
     '<string name="module_load_failed">模块服务还没就绪，确认 root 环境后点重试</string>'),
])
print("品牌皮肤已应用：深色默认 + 去枫叶 + 蓝鱼文案")

if failures:
    print("\n修补失败：", file=sys.stderr)
    for item in failures:
        print(" - " + item, file=sys.stderr)
    sys.exit(1)
print("构建期修补已全部应用。")
