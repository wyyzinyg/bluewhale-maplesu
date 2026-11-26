# 构建结果

- run: 46  提交: fa0b1a2755b0b2ff3e41e0afdc82b448dcc3efb1
- 作业结论: cancelled

#### 补丁摘要（是否真应用）
改好 manager/build.gradle.kts
改好 manager/build.gradle.kts
改好 manager/build.gradle.kts
改好 manager/src/main/res/values/maplesu_strings.xml
改好 manager/src/main/java/com/maplesu/core/data/repository/SettingsRepositoryImpl.kt
插入 BLUEWHALE_KEY_COLOR 常量
改好 manager/src/main/res/values/colors.xml
改好 manager/build.gradle.kts
修好 build.py: cmake 可执行名跨平台
修好 build.py: ninja 可执行名跨平台
修好 build.py: ir spec 路径反斜杠归一（带 basename 回退）
改好 build.gradle.kts: policy bundle 固定 ultra
改好 build.gradle.kts: bundle 同源校验随自检开关跳过
修好 prepare_host_dependencies.py: 插入 _retry_urlopen
修好 prepare_host_dependencies.py: 下载走重试
蓝鱼品牌化补丁已全部应用。
改好 build.gradle.kts: runtime 目标集按开关决定 bridge
改好 manager/build.gradle.kts: @get:InputFile abstract val ultraBridgeLibrary: 
改好 manager/build.gradle.kts: ultraBridgeLibrary.get().asFile.copyTo(jniDirect
改好 manager/build.gradle.kts: ultraBridgeLibrary.set(runtimeBuild.map { it.fil
改好 build.gradle.kts: bridge 不再作为硬性输出
改好 product.py: cached_jar 缺缓存时从 Maven 补拉
改好 build.gradle.kts: Ultra claim 门槛随跳过开关放行
改好 gradle.properties: 落 bluewhaleSkipUltraBridge
改好 manager/src/main/AndroidManifest.xml: android:authorities="dev.maplesu.manager.soter"
改好 manager/src/main/java/dev/maplesu/manager/soter/SoterTargetProvider.kt: const val AUTHORITY = "dev.maplesu.manager.soter
改好 manager/src/main/res/mipmap-anydpi/ic_launcher.xml: <foreground android:drawable="@drawable/ic_launc
改好 manager/src/main/res/values/colors.xml: <color name="ic_launcher_background">#FF08101F</
改好 manager/src/main/res/values/colors.xml: <color name="ic_splash_background">#FF774F6F</co
改好 manager/src/main/res/values/themes.xml: <item name="windowSplashScreenBackground">@color
改好 manager/src/main/res/values/themes.xml: <item name="windowSplashScreenAnimatedIcon">@dra
改好 manager/src/main/res/values-night/themes.xml: <item name="windowSplashScreenBackground">@color
改好 manager/src/main/res/values-night/themes.xml: <item name="windowSplashScreenAnimatedIcon">@dra
改好 manager/src/main/java/com/maplesu/core/data/repository/SettingsRepositoryImpl.kt: get() = if (ThemeLock.ENABLED) ThemeLock.THEME_M
改好 manager/src/main/java/com/maplesu/core/ui/viewmodel/MainActivityViewModel.kt: init {
改好 manager/src/main/java/com/maplesu/core/ui/util/AppearancePrefsPolicy.kt: "snow_enabled" to enabled,
改好 manager/src/main/java/com/maplesu/core/ui/MainActivity.kt: if ((skin.appliedScene && uiState.snowEnabled) |
改好 manager/src/main/java/com/maplesu/core/ui/screen/home/HomeBetaBanner.kt: internal const val MAPLESU_FEEDBACK_URL = "https
改好 manager/src/main/java/com/maplesu/core/ui/screen/home/AboutMapleDialogMiuix.kt: Text(
改好 manager/src/main/java/com/maplesu/core/ui/screen/home/AboutMapleDialogMiuix.kt: AdvisorWallMiuix(Modifier.padding(top = 4.dp))

#### gradle 失败原因

#### CMake 错误日志

```
#### provider 子构建日志（CMake/cargo 报错常只写在这里）
#### 主构建日志尾
上游体积: 703M
改好 manager/build.gradle.kts
改好 manager/build.gradle.kts
改好 manager/build.gradle.kts
改好 manager/src/main/res/values/maplesu_strings.xml
改好 manager/src/main/java/com/maplesu/core/data/repository/SettingsRepositoryImpl.kt
插入 BLUEWHALE_KEY_COLOR 常量
改好 manager/src/main/res/values/colors.xml
移除位图 drawable-xxhdpi
移除位图 drawable-mdpi
移除位图 drawable-xxxhdpi
移除位图 drawable-hdpi
移除位图 drawable-xhdpi
放入矢量图标
改好 manager/build.gradle.kts
修好 build.py: cmake 可执行名跨平台
修好 build.py: ninja 可执行名跨平台
修好 build.py: ir spec 路径反斜杠归一（带 basename 回退）
改好 build.gradle.kts: policy bundle 固定 ultra
改好 build.gradle.kts: bundle 同源校验随自检开关跳过
policy bundle 自检：18 个源，缺 0，漂 0
修好 prepare_host_dependencies.py: 插入 _retry_urlopen
修好 prepare_host_dependencies.py: 下载走重试

蓝鱼品牌化补丁已全部应用。
改好 build.gradle.kts: runtime 目标集按开关决定 bridge
改好 manager/build.gradle.kts: @get:InputFile abstract val ultraBridgeLibrary: 
改好 manager/build.gradle.kts: ultraBridgeLibrary.get().asFile.copyTo(jniDirect
改好 manager/build.gradle.kts: ultraBridgeLibrary.set(runtimeBuild.map { it.fil
改好 build.gradle.kts: bridge 不再作为硬性输出
改好 product.py: cached_jar 缺缓存时从 Maven 补拉
改好 build.gradle.kts: Ultra claim 门槛随跳过开关放行
改好 gradle.properties: 落 bluewhaleSkipUltraBridge
改好 manager/src/main/AndroidManifest.xml: android:authorities="dev.maplesu.manager.soter"
改好 manager/src/main/java/dev/maplesu/manager/soter/SoterTargetProvider.kt: const val AUTHORITY = "dev.maplesu.manager.soter
还原蓝鱼图标与启动页位图: 6 个文件，与 3.16 逐字节一致
改好 manager/src/main/res/mipmap-anydpi/ic_launcher.xml: <foreground android:drawable="@drawable/ic_launc
改好 manager/src/main/res/values/colors.xml: <color name="ic_launcher_background">#FF08101F</
改好 manager/src/main/res/values/colors.xml: <color name="ic_splash_background">#FF774F6F</co
改好 manager/src/main/res/values/themes.xml: <item name="windowSplashScreenBackground">@color
改好 manager/src/main/res/values/themes.xml: <item name="windowSplashScreenAnimatedIcon">@dra
改好 manager/src/main/res/values-night/themes.xml: <item name="windowSplashScreenBackground">@color
改好 manager/src/main/res/values-night/themes.xml: <item name="windowSplashScreenAnimatedIcon">@dra
还原启动页: ic_app_brand 位图 + 白底 + 主题指向
改好 manager/src/main/java/com/maplesu/core/data/repository/SettingsRepositoryImpl.kt: get() = if (ThemeLock.ENABLED) ThemeLock.THEME_M
改好 manager/src/main/java/com/maplesu/core/ui/viewmodel/MainActivityViewModel.kt: init {
        prefs.registerOnSharedPreferenceC
改好 manager/src/main/java/com/maplesu/core/ui/util/AppearancePrefsPolicy.kt: "snow_enabled" to enabled,
改好 manager/src/main/java/com/maplesu/core/ui/MainActivity.kt: if ((skin.appliedScene && uiState.snowEnabled) |
改好 manager/src/main/java/com/maplesu/core/ui/screen/home/HomeBetaBanner.kt: internal const val MAPLESU_FEEDBACK_URL = "https
改好 manager/src/main/java/com/maplesu/core/ui/screen/home/AboutMapleDialogMiuix.kt: Text(
            text = aboutCommunityText(stri
改好 manager/src/main/java/com/maplesu/core/ui/screen/home/AboutMapleDialogMiuix.kt: AdvisorWallMiuix(Modifier.padding(top = 4.dp))
改好 manager/src/main/java/com/maplesu/core/ui/screen/home/AboutMapleDialogMiuix.kt: kind = BrandBannerKind.MAPLE,
改好 manager/src/main/java/com/maplesu/core/ui/screen/home/AboutMapleDialogMaterial.kt: Text(
            text = aboutCommunityText(stri
改好 manager/src/main/java/com/maplesu/core/ui/screen/home/AboutMapleDialogMaterial.kt: AdvisorWallMaterial(Modifier.padding(top = 4.dp)
改好 manager/src/main/java/com/maplesu/core/ui/screen/home/AboutMapleDialogMaterial.kt: kind = BrandBannerKind.MAPLE,
改好 manager/src/main/res/values/themes.xml: <style name="Theme.KernelSU" parent="android:The
改好 manager/src/main/res/values/themes.xml: <item name="android:windowLightStatusBar">true</
改好 manager/src/main/res/values/themes.xml: <item name="android:windowLightNavigationBar">tr
改好 manager/src/main/res/values/colors.xml: <color name="maple_window_background">#FFF7F7F7<
改好 manager/src/main/res/values-night/colors.xml: <color name="maple_window_background">#FF000000<
改好 manager/build.gradle.kts: versionCode = 32731
改好 manager/build.gradle.kts: versionName = "3.17.0-bw"
改好 manager/src/main/res/values/maplesu_release_strings.xml: <string name="home_public_beta_notice">公测版本非正式版本
改好 manager/src/main/res/values/maplesu_about.xml: <string name="about_maple_title">About MapleSU</
改好 manager/src/main/res/values/maplesu_about.xml: <string name="about_maple_entry_summary">Develop
改好 manager/src/main/res/values/maplesu_about.xml: <string name="about_maple_overview">Overview: an
改好 manager/src/main/res/values/maplesu_about.xml: <string name="about_maple_overview_plain">Overvi
改好 manager/src/main/res/values/maplesu_about.xml: <string name="about_maple_developers">Developer:
改好 manager/src/main/res/values-zh-rCN/maplesu_about.xml: <string name="about_maple_title">关于 MapleSU</str
改好 manager/src/main/res/values-zh-rCN/maplesu_about.xml: <string name="about_maple_entry_summary">开发者、开源致
改好 manager/src/main/res/values-zh-rCN/maplesu_about.xml: <string name="about_maple_overview">简介：一款 Androi
改好 manager/src/main/res/values-zh-rCN/maplesu_about.xml: <string name="about_maple_overview_plain">简介：一款 
改好 manager/src/main/res/values-zh-rCN/maplesu_about.xml: <string name="about_maple_developers">开发者：MapleA
改好 manager/src/main/res/values/home_environment_check.xml: <string name="home_environment_check_failed">Env
改好 manager/src/main/res/values/home_environment_check.xml: <string name="home_environment_check_timeout_sum
改好 manager/src/main/res/values/home_environment_check.xml: <string name="home_environment_check_failed_summ
改好 manager/src/main/res/values/home_environment_check.xml: <string name="home_environment_check_unconfirmed
改好 manager/src/main/res/values-zh-rCN/home_environment_check.xml: <string name="home_environment_check_failed">环境检
改好 manager/src/main/res/values-zh-rCN/home_environment_check.xml: <string name="home_environment_check_timeout_sum
改好 manager/src/main/res/values-zh-rCN/home_environment_check.xml: <string name="home_environment_check_failed_summ
改好 manager/src/main/res/values-zh-rCN/home_environment_check.xml: <string name="home_environment_check_unconfirmed
改好 manager/src/main/res/values/strings_workmode.xml: <string name="work_mode_superuser_unresolved">Th
改好 manager/src/main/res/values-zh-rCN/strings_workmode.xml: <string name="work_mode_superuser_unresolved">还没
改好 manager/src/main/res/values-zh-rCN/strings_workmode.xml: <string name="work_mode_superuser_unavailable">当
改好 manager/src/main/res/values/maplesu_strings.xml: <string name="module_load_failed">Failed to load
改好 manager/src/main/res/values-zh-rCN/maplesu_strings.xml: <string name="module_load_failed">加载模块失败，请重试</st
品牌皮肤已应用：深色默认 + 去枫叶 + 蓝鱼文案
构建期修补已全部应用。
改好 manager/src/main/java/com/maplesu/core/data/repository/SettingsRepositoryImpl.kt: appearance.getBoolean("snow_enabled", true)
改好 manager/src/main/java/com/maplesu/core/ui/viewmodel/MainActivityViewModel.kt: 2 处 AppearancePreferences.INTRO_COMIC, t
改好 manager/src/main/java/com/maplesu/core/ui/util/AppearancePrefsPolicy.kt: "snow_enabled" to false,
改好 manager/src/main/res/values-zh-rCN/strings_ui_d.xml: <string name="ui_d_appearance_summary">界面风格 
改好 manager/src/main/res/values-zh-rCN/strings_ui_d.xml: <string name="ui_d_fall_title">枫叶飘落</string>
改好 manager/src/main/res/values-zh-rCN/strings_ui_d.xml: <string name="ui_d_fall_summary">让枫叶轻轻飘落，可随时
改好 manager/src/main/res/values/strings_ui_d.xml: <string name="ui_d_appearance_summary">Style
改好 manager/src/main/res/values/strings_ui_d.xml: <string name="ui_d_fall_title">Falling maple
改好 manager/src/main/res/values/strings_ui_d.xml: <string name="ui_d_fall_summary">Gentle fall
改好 manager/src/main/res/values-zh-rCN/maplesu_strings.xml: <string name="maplesu_backend_version">Maple
改好 manager/src/main/res/values/maplesu_strings.xml: <string name="maplesu_backend_version">Maple
改好 manager/src/main/java/com/maplesu/core/ui/component/maple/BrandDialogMaterial.kt: internal fun BrandDialogMaterial(
    kind: 
改好 manager/src/main/java/com/maplesu/core/ui/component/maple/BrandDialogMaterial.kt: icon = { BrandBanner(kind = kind, accent = M
文案统一完成: 346 条
文案总清已应用，版本 3.18.1-bw (32733)。
删掉启动页上游人物位图: 5 个
改好 manager/src/main/java/com/maplesu/core/ui/MainActivity.kt: if (uiState.snowEnabled) {
改好 manager/src/main/java/com/maplesu/core/ui/MainActivity.kt: if (skin.appliedScene && uiState.trollRainEnab
删掉 manager/src/main/java/com/maplesu/core/ui/screen/settings/AppearanceSettingsBody.kt: AppearanceGroup(stringResource(R.string.theme_section_effect
改好 manager/src/main/java/com/maplesu/core/ui/viewmodel/MainActivityViewModel.kt: .putBoolean("snow_enabled", false).apply()
改好 manager/src/main/res/values-zh-rCN/strings_ui_d.xml: <string name="ui_d_appearance_summary">界面风格 · 
改好 manager/src/main/res/values/strings_ui_d.xml: <string name="ui_d_appearance_summary">Style ·
改好 manager/build.gradle.kts: versionCode = 32733
改好 manager/build.gradle.kts: versionName = "3.18.1-bw"
特效收口已应用，版本 3.18.2-bw (32734)。
皮肤收尾已应用。
```
