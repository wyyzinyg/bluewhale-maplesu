# 构建结果

- run: 47  提交: 2583cc1e90295dc6fa899a49b692f6bc13c477ab
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
移除位图 drawable-hdpi
移除位图 drawable-mdpi
移除位图 drawable-xxxhdpi
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
+ echo '== java =='
== java ==
+ java -version
openjdk version "21.0.13" 2026-10-20 LTS
OpenJDK Runtime Environment Temurin-21.0.13+9 (build 21.0.13+9-LTS)
OpenJDK 64-Bit Server VM Temurin-21.0.13+9 (build 21.0.13+9-LTS, mixed mode, sharing)
+ SDK=/usr/local/lib/android/sdk
+ echo SDK=/usr/local/lib/android/sdk
SDK=/usr/local/lib/android/sdk
+ SM=/usr/local/lib/android/sdk/cmdline-tools/latest/bin/sdkmanager
+ '[' '!' -x /usr/local/lib/android/sdk/cmdline-tools/latest/bin/sdkmanager ']'
+ echo SM=/usr/local/lib/android/sdk/cmdline-tools/latest/bin/sdkmanager
SM=/usr/local/lib/android/sdk/cmdline-tools/latest/bin/sdkmanager
+ mkdir -p /usr/local/lib/android/sdk/licenses
+ printf '\n8933bad161af4178b1185d1a37fbf41ea5269c55\nd56f5187479451eabf01fb78af6dfcb131a6481e\n24333f8a63b6825ea9c5514f83c2829b004d1fee\n'
+ printf '\n84831b9409646a918e30573bab4c9c91346d8abd\n'
++ ls /usr/local/lib/android/sdk/licenses
+ echo $'licenses 已预写: android-sdk-license\nandroid-sdk-preview-license'
licenses 已预写: android-sdk-license
android-sdk-preview-license
+ for pkg in "platforms;android-37.0" "platforms;android-37" "build-tools;37.0.0" "platforms;android-36" "build-tools;36.0.0" "cmake;3.22.1" "ndk;26.1.10909125" "ndk;28.2.13676358" "ndk;29.0.14206865"
+ echo '--- install platforms;android-37.0'
--- install platforms;android-37.0
+ /usr/local/lib/android/sdk/cmdline-tools/latest/bin/sdkmanager 'platforms;android-37.0'
Loading package information...                                                  Loading local repository...                                                     [                                       ] 3% Loading local repository...        [                                       ] 3% Fetch remote repository...         [=                                      ] 3% Fetch remote repository...         [=                                      ] 4% Fetch remote repository...         [=                                      ] 5% Fetch remote repository...         [==                                     ] 5% Fetch remote repository...         [==                                     ] 6% Fetch remote repository...         [==                                     ] 7% Fetch remote repository...         [==                                     ] 7% Computing updates...               [===                                    ] 8% Computing updates...               [===                                    ] 10% Computing updates...              [=======================================] 100% Computing updates...             

+ for pkg in "platforms;android-37.0" "platforms;android-37" "build-tools;37.0.0" "platforms;android-36" "build-tools;36.0.0" "cmake;3.22.1" "ndk;26.1.10909125" "ndk;28.2.13676358" "ndk;29.0.14206865"
+ echo '--- install platforms;android-37'
--- install platforms;android-37
+ /usr/local/lib/android/sdk/cmdline-tools/latest/bin/sdkmanager 'platforms;android-37'
Loading package information...                                                  Loading local repository...                                                     [                                       ] 3% Loading local repository...        [                                       ] 3% Fetch remote repository...         [=                                      ] 3% Fetch remote repository...         [=                                      ] 4% Fetch remote repository...         [=                                      ] 5% Fetch remote repository...         [==                                     ] 5% Fetch remote repository...         [==                                     ] 6% Fetch remote repository...         [==                                     ] 7% Fetch remote repository...         [==                                     ] 7% Computing updates...               [===                                    ] 8% Computing updates...               [===                                    ] 10% Computing updates...                                                                                              Warning: Failed to find package 'platforms;android-37'
[===                                    ] 10% Computing updates...              + true
+ for pkg in "platforms;android-37.0" "platforms;android-37" "build-tools;37.0.0" "platforms;android-36" "build-tools;36.0.0" "cmake;3.22.1" "ndk;26.1.10909125" "ndk;28.2.13676358" "ndk;29.0.14206865"
+ echo '--- install build-tools;37.0.0'
--- install build-tools;37.0.0
+ /usr/local/lib/android/sdk/cmdline-tools/latest/bin/sdkmanager 'build-tools;37.0.0'
Loading package information...                                                  Loading local repository...                                                     [                                       ] 3% Loading local repository...        [                                       ] 3% Fetch remote repository...         [=                                      ] 3% Fetch remote repository...         [=                                      ] 4% Fetch remote repository...         [=                                      ] 5% Fetch remote repository...         [==                                     ] 5% Fetch remote repository...         [==                                     ] 6% Fetch remote repository...         [==                                     ] 7% Fetch remote repository...         [==                                     ] 7% Computing updates...               [===                                    ] 8% Computing updates...               [===                                    ] 10% Computing updates...              [=======================================] 100% Computing updates...             

+ for pkg in "platforms;android-37.0" "platforms;android-37" "build-tools;37.0.0" "platforms;android-36" "build-tools;36.0.0" "cmake;3.22.1" "ndk;26.1.10909125" "ndk;28.2.13676358" "ndk;29.0.14206865"
+ echo '--- install platforms;android-36'
--- install platforms;android-36
+ /usr/local/lib/android/sdk/cmdline-tools/latest/bin/sdkmanager 'platforms;android-36'
Loading package information...                                                  Loading local repository...                                                     [                                       ] 3% Loading local repository...        [                                       ] 3% Fetch remote repository...         [=                                      ] 3% Fetch remote repository...         [=                                      ] 4% Fetch remote repository...         [=                                      ] 5% Fetch remote repository...         [==                                     ] 5% Fetch remote repository...         [==                                     ] 6% Fetch remote repository...         [==                                     ] 7% Fetch remote repository...         [==                                     ] 7% Computing updates...               [===                                    ] 8% Computing updates...               [===                                    ] 10% Computing updates...              [=======================================] 100% Computing updates...             

+ for pkg in "platforms;android-37.0" "platforms;android-37" "build-tools;37.0.0" "platforms;android-36" "build-tools;36.0.0" "cmake;3.22.1" "ndk;26.1.10909125" "ndk;28.2.13676358" "ndk;29.0.14206865"
+ echo '--- install build-tools;36.0.0'
--- install build-tools;36.0.0
+ /usr/local/lib/android/sdk/cmdline-tools/latest/bin/sdkmanager 'build-tools;36.0.0'
Loading package information...                                                  Loading local repository...                                                     [                                       ] 3% Loading local repository...        [                                       ] 3% Fetch remote repository...         [=                                      ] 3% Fetch remote repository...         [=                                      ] 4% Fetch remote repository...         [=                                      ] 5% Fetch remote repository...         [==                                     ] 5% Fetch remote repository...         [==                                     ] 6% Fetch remote repository...         [==                                     ] 7% Fetch remote repository...         [==                                     ] 7% Computing updates...               [===                                    ] 8% Computing updates...               [===                                    ] 10% Computing updates...              [=======================================] 100% Computing updates...             

+ for pkg in "platforms;android-37.0" "platforms;android-37" "build-tools;37.0.0" "platforms;android-36" "build-tools;36.0.0" "cmake;3.22.1" "ndk;26.1.10909125" "ndk;28.2.13676358" "ndk;29.0.14206865"
+ echo '--- install cmake;3.22.1'
--- install cmake;3.22.1
+ /usr/local/lib/android/sdk/cmdline-tools/latest/bin/sdkmanager 'cmake;3.22.1'
Loading package information...                                                  Loading local repository...                                                     [                                       ] 3% Loading local repository...        [                                       ] 3% Fetch remote repository...         [=                                      ] 3% Fetch remote repository...         [=                                      ] 4% Fetch remote repository...         [=                                      ] 5% Fetch remote repository...         [==                                     ] 5% Fetch remote repository...         [==                                     ] 6% Fetch remote repository...         [==                                     ] 7% Fetch remote repository...         [==                                     ] 7% Computing updates...               [===                                    ] 8% Computing updates...               [===                                    ] 10% Computing updates...              [===                                    ] 10% Installing CMake 3.22.1           [===                                    ] 10% Downloading cmake-3.22.1-linux.zip[====                                   ] 10% Downloading cmake-3.22.1-linux.zip[====                                   ] 11% Downloading cmake-3.22.1-linux.zip[====                                   ] 12% Downloading cmake-3.22.1-linux.zip[=====                                  ] 13% Downloading cmake-3.22.1-linux.zip[=====                                  ] 14% Downloading cmake-3.22.1-linux.zip[=====                                  ] 15% Downloading cmake-3.22.1-linux.zip[======                                 ] 15% Downloading cmake-3.22.1-linux.zip[======                                 ] 16% Downloading cmake-3.22.1-linux.zip[======                                 ] 17% Downloading cmake-3.22.1-linux.zip[=======                                ] 18% Downloading cmake-3.22.1-linux.zip[=======                                ] 19% Downloading cmake-3.22.1-linux.zip[=======                                ] 20% Downloading cmake-3.22.1-linux.zip[========                               ] 20% Downloading cmake-3.22.1-linux.zip[========                               ] 21% Downloading cmake-3.22.1-linux.zip[========                               ] 22% Downloading cmake-3.22.1-linux.zip[=========                              ] 23% Downloading cmake-3.22.1-linux.zip[=========                              ] 24% Downloading cmake-3.22.1-linux.zip[=========                              ] 25% Downloading cmake-3.22.1-linux.zip[==========                             ] 25% Downloading cmake-3.22.1-linux.zip[==========                             ] 26% Downloading cmake-3.22.1-linux.zip[==========                             ] 27% Downloading cmake-3.22.1-linux.zip[===========                            ] 28% Downloading cmake-3.22.1-linux.zip[===========                            ] 29% Downloading cmake-3.22.1-linux.zip[===========                            ] 30% Downloading cmake-3.22.1-linux.zip[============                           ] 30% Downloading cmake-3.22.1-linux.zip[============                           ] 31% Downloading cmake-3.22.1-linux.zip[============                           ] 32% Downloading cmake-3.22.1-linux.zip[============                           ] 33% Downloading cmake-3.22.1-linux.zip[============                           ] 33% Unzipping...                      [============                           ] 33% Unzipping... bin/cmake            [=============                          ] 33% Unzipping... bin/cmake            [=============                          ] 34% Unzipping... bin/cmake            [=============                          ] 35% Unzipping... bin/cmake            [==============                         ] 35% Unzipping... bin/cmake            [==============                         ] 36% Unzipping... bin/cmake            [==============                         ] 37% Unzipping... bin/cmake            [===============                        ] 38% Unzipping... bin/cmake            [===============                        ] 39% Unzipping... bin/cmake            [===============                        ] 39% Unzipping... bin/ctest            [===============                        ] 40% Unzipping... bin/ctest            [================                       ] 40% Unzipping... bin/ctest            [================                       ] 41% Unzipping... bin/ctest            [================                       ] 42% Unzipping... bin/ctest            [=================                      ] 43% Unzipping... bin/ctest            [=================                      ] 44% Unzipping... bin/ctest            [=================                      ] 45% Unzipping... bin/ctest            [==================                     ] 45% Unzipping... bin/ctest            [==================                     ] 46% Unzipping... bin/ctest            [==================                     ] 46% Unzipping... bin/cpack            [==================                     ] 47% Unzipping... bin/cpack            [===================                    ] 48% Unzipping... bin/cpack            [===================                    ] 49% Unzipping... bin/cpack            [===================                    ] 50% Unzipping... bin/cpack            [====================                   ] 50% Unzipping... bin/cpack            [====================                   ] 51% Unzipping... bin/cpack            [====================                   ] 52% Unzipping... bin/cpack            [====================                   ] 52% Unzipping... share/vim/vimfiles/in[====================                   ] 52% Unzipping... share/vim/vimfiles/sy[====================                   ] 52% Unzipping... share/aclocal/cmake.m[====================                   ] 52% Unzipping... share/emacs/site-lisp[====================                   ] 52% Unzipping... share/cmake-3.22/incl[====================                   ] 52% Unzipping... share/cmake-3.22/Help[=====================                  ] 53% Unzipping... share/cmake-3.22/Help[=====================                  ] 53% Unzipping... share/cmake-3.22/Temp[=====================                  ] 53% Unzipping... share/cmake-3.22/Modu[=====================                  ] 54% Unzipping... share/cmake-3.22/Modu[=====================                  ] 54% Unzipping... share/bash-completion[=====================                  ] 54% Unzipping... doc/cmake-3.22/Copyri[=====================                  ] 54% Unzipping... doc/cmake-3.22/cmzlib[=====================                  ] 54% Unzipping... doc/cmake-3.22/cmzstd[=====================                  ] 54% Unzipping... doc/cmake-3.22/cmnght[=====================                  ] 54% Unzipping... doc/cmake-3.22/cmsys/[=====================                  ] 54% Unzipping... doc/cmake-3.22/cmcurl[=====================                  ] 54% Unzipping... doc/cmake-3.22/cmlibr[=====================                  ] 54% Unzipping... doc/cmake-3.22/cmliba[=====================                  ] 54% Unzipping... doc/cmake-3.22/cmlibl[=====================                  ] 54% Unzipping... doc/cmake-3.22/cmlibu[=====================                  ] 54% Unzipping... doc/openssl-1.1.1l/LI[=====================                  ] 54% Unzipping... source.properties    [=====================                  ] 54% Unzipping... bin/ninja            [=====================                  ] 54% Unzipping... doc/ninja/LICENSE    [=====================                  ] 54% Unzipping... share/cmake-3.22/Modu[=====================                  ] 55% Unzipping... share/cmake-3.22/Modu[=======================================] 100% Unzipping... share/cmake-3.22/Mod

+ for pkg in "platforms;android-37.0" "platforms;android-37" "build-tools;37.0.0" "platforms;android-36" "build-tools;36.0.0" "cmake;3.22.1" "ndk;26.1.10909125" "ndk;28.2.13676358" "ndk;29.0.14206865"
+ echo '--- install ndk;26.1.10909125'
--- install ndk;26.1.10909125
+ /usr/local/lib/android/sdk/cmdline-tools/latest/bin/sdkmanager 'ndk;26.1.10909125'
Loading package information...                                                  Loading local repository...                                                     [                                       ] 3% Loading local repository...        [                                       ] 3% Fetch remote repository...         [=                                      ] 3% Fetch remote repository...         [=                                      ] 4% Fetch remote repository...         [=                                      ] 5% Fetch remote repository...         [==                                     ] 5% Fetch remote repository...         [==                                     ] 6% Fetch remote repository...         [==                                     ] 7% Fetch remote repository...         [==                                     ] 7% Computing updates...               [===                                    ] 8% Computing updates...               [===                                    ] 10% Computing updates...              [===                                    ] 10% Installing NDK (Side by side) 26.1[===                                    ] 10% Downloading android-ndk-r26b-linux[====                                   ] 10% Downloading android-ndk-r26b-linux[====                                   ] 11% Downloading android-ndk-r26b-linux[====                                   ] 12% Downloading android-ndk-r26b-linux[=====                                  ] 13% Downloading android-ndk-r26b-linux[=====                                  ] 14% Downloading android-ndk-r26b-linux[=====                                  ] 15% Downloading android-ndk-r26b-linux[======                                 ] 15% Downloading android-ndk-r26b-linux[======                                 ] 16% Downloading android-ndk-r26b-linux[======                                 ] 17% Downloading android-ndk-r26b-linux[=======                                ] 18% Downloading android-ndk-r26b-linux[=======                                ] 19% Downloading android-ndk-r26b-linux[=======                                ] 20% Downloading android-ndk-r26b-linux[========                               ] 20% Downloading android-ndk-r26b-linux[========                               ] 21% Downloading android-ndk-r26b-linux[========                               ] 22% Downloading android-ndk-r26b-linux[=========                              ] 23% Downloading android-ndk-r26b-linux[=========                              ] 24% Downloading android-ndk-r26b-linux[=========                              ] 25% Downloading android-ndk-r26b-linux[==========                             ] 25% Downloading android-ndk-r26b-linux[==========                             ] 26% Downloading android-ndk-r26b-linux[==========                             ] 27% Downloading android-ndk-r26b-linux[===========                            ] 28% Downloading android-ndk-r26b-linux[===========                            ] 29% Downloading android-ndk-r26b-linux[===========                            ] 30% Downloading android-ndk-r26b-linux[============                           ] 30% Downloading android-ndk-r26b-linux[============                           ] 31% Downloading android-ndk-r26b-linux[============                           ] 32% Downloading android-ndk-r26b-linux[============                           ] 33% Downloading android-ndk-r26b-linux[============                           ] 33% Unzipping...                      [============                           ] 33% Unzipping... android-ndk-r26b/    [============                           ] 33% Unzipping... android-ndk-r26b/CHAN[=============                          ] 33% Unzipping... android-ndk-r26b/CHAN[=============                          ] 33% Unzipping... android-ndk-r26b/wrap[=============                          ] 33% Unzipping... android-ndk-r26b/preb[=============                          ] 33% Unzipping... android-ndk-r26b/buil[=============                          ] 33% Unzipping... android-ndk-r26b/NOTI[=============                          ] 33% Unzipping... android-ndk-r26b/ndk-[=============                          ] 33% Unzipping... android-ndk-r26b/NOTI[=============                          ] 33% Unzipping... android-ndk-r26b/meta[=============                          ] 33% Unzipping... android-ndk-r26b/ndk-[=============                          ] 33% Unzipping... android-ndk-r26b/pyth[=============                          ] 33% Unzipping... android-ndk-r26b/sour[=============                          ] 33% Unzipping... android-ndk-r26b/simp[=============                          ] 33% Unzipping... android-ndk-r26b/ndk-[=============                          ] 33% Unzipping... android-ndk-r26b/READ[=============                          ] 33% Unzipping... android-ndk-r26b/tool[=============                          ] 34% Unzipping... android-ndk-r26b/tool[=============                          ] 35% Unzipping... android-ndk-r26b/tool[==============                         ] 35% Unzipping... android-ndk-r26b/tool[==============                         ] 36% Unzipping... android-ndk-r26b/tool[==============                         ] 37% Unzipping... android-ndk-r26b/tool[===============                        ] 38% Unzipping... android-ndk-r26b/tool[===============                        ] 39% Unzipping... android-ndk-r26b/tool[===============                        ] 40% Unzipping... android-ndk-r26b/tool[================                       ] 40% Unzipping... android-ndk-r26b/tool[================                       ] 41% Unzipping... android-ndk-r26b/tool[================                       ] 42% Unzipping... android-ndk-r26b/tool[=================                      ] 43% Unzipping... android-ndk-r26b/tool[=================                      ] 44% Unzipping... android-ndk-r26b/tool[=================                      ] 45% Unzipping... android-ndk-r26b/tool[==================                     ] 45% Unzipping... android-ndk-r26b/tool[==================                     ] 46% Unzipping... android-ndk-r26b/tool[==================                     ] 47% Unzipping... android-ndk-r26b/tool[===================                    ] 48% Unzipping... android-ndk-r26b/tool[===================                    ] 49% Unzipping... android-ndk-r26b/tool[===================                    ] 50% Unzipping... android-ndk-r26b/tool[====================                   ] 50% Unzipping... android-ndk-r26b/tool[====================                   ] 51% Unzipping... android-ndk-r26b/tool[====================                   ] 52% Unzipping... android-ndk-r26b/tool[=====================                  ] 53% Unzipping... android-ndk-r26b/tool[=====================                  ] 54% Unzipping... android-ndk-r26b/tool[=====================                  ] 55% Unzipping... android-ndk-r26b/tool[=====================                  ] 55% Unzipping... android-ndk-r26b/ndk-[=====================                  ] 55% Unzipping... android-ndk-r26b/shad[=======================================] 100% Unzipping... android-ndk-r26b/sha

+ for pkg in "platforms;android-37.0" "platforms;android-37" "build-tools;37.0.0" "platforms;android-36" "build-tools;36.0.0" "cmake;3.22.1" "ndk;26.1.10909125" "ndk;28.2.13676358" "ndk;29.0.14206865"
+ echo '--- install ndk;28.2.13676358'
--- install ndk;28.2.13676358
+ /usr/local/lib/android/sdk/cmdline-tools/latest/bin/sdkmanager 'ndk;28.2.13676358'
Loading package information...                                                  Loading local repository...                                                     [                                       ] 3% Loading local repository...        [                                       ] 3% Fetch remote repository...         [=                                      ] 3% Fetch remote repository...         [=                                      ] 4% Fetch remote repository...         [=                                      ] 5% Fetch remote repository...         [==                                     ] 5% Fetch remote repository...         [==                                     ] 6% Fetch remote repository...         [==                                     ] 7% Fetch remote repository...         [==                                     ] 7% Computing updates...               [===                                    ] 8% Computing updates...               [===                                    ] 10% Computing updates...              [===                                    ] 10% Installing NDK (Side by side) 28.2[===                                    ] 10% Downloading android-ndk-r28c-linux[====                                   ] 10% Downloading android-ndk-r28c-linux[====                                   ] 11% Downloading android-ndk-r28c-linux[====                                   ] 12% Downloading android-ndk-r28c-linux[=====                                  ] 13% Downloading android-ndk-r28c-linux[=====                                  ] 14% Downloading android-ndk-r28c-linux[=====                                  ] 15% Downloading android-ndk-r28c-linux[======                                 ] 15% Downloading android-ndk-r28c-linux[======                                 ] 16% Downloading android-ndk-r28c-linux[======                                 ] 17% Downloading android-ndk-r28c-linux[=======                                ] 18% Downloading android-ndk-r28c-linux[=======                                ] 19% Downloading android-ndk-r28c-linux[=======                                ] 20% Downloading android-ndk-r28c-linux[========                               ] 20% Downloading android-ndk-r28c-linux[========                               ] 21% Downloading android-ndk-r28c-linux[========                               ] 22% Downloading android-ndk-r28c-linux[=========                              ] 23% Downloading android-ndk-r28c-linux[=========                              ] 24% Downloading android-ndk-r28c-linux[=========                              ] 25% Downloading android-ndk-r28c-linux[==========                             ] 25% Downloading android-ndk-r28c-linux[==========                             ] 26% Downloading android-ndk-r28c-linux[==========                             ] 27% Downloading android-ndk-r28c-linux[===========                            ] 28% Downloading android-ndk-r28c-linux[===========                            ] 29% Downloading android-ndk-r28c-linux[===========                            ] 30% Downloading android-ndk-r28c-linux[============                           ] 30% Downloading android-ndk-r28c-linux[============                           ] 31% Downloading android-ndk-r28c-linux[============                           ] 32% Downloading android-ndk-r28c-linux[============                           ] 33% Downloading android-ndk-r28c-linux[============                           ] 33% Unzipping...                      [============                           ] 33% Unzipping... android-ndk-r28c/    [============                           ] 33% Unzipping... android-ndk-r28c/READ[=============                          ] 33% Unzipping... android-ndk-r28c/READ[=============                          ] 33% Unzipping... android-ndk-r28c/meta[=============                          ] 33% Unzipping... android-ndk-r28c/shad[=============                          ] 33% Unzipping... android-ndk-r28c/ndk-[=============                          ] 33% Unzipping... android-ndk-r28c/wrap[=============                          ] 33% Unzipping... android-ndk-r28c/ndk-[=============                          ] 33% Unzipping... android-ndk-r28c/tool[=============                          ] 34% Unzipping... android-ndk-r28c/tool[=============                          ] 35% Unzipping... android-ndk-r28c/tool[==============                         ] 35% Unzipping... android-ndk-r28c/tool[==============                         ] 36% Unzipping... android-ndk-r28c/tool[==============                         ] 37% Unzipping... android-ndk-r28c/tool```
