# 构建结果

- run: 48  提交: 6513fe1a4bcbf78cd691b3425af43145e8b0ba53
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
Loading package information...                                                  Loading local repository...                                                     [                                       ] 3% Loading local repository...        [                                       ] 3% Fetch remote repository...         [=                                      ] 3% Fetch remote repository...         [=                                      ] 4% Fetch remote repository...         [=                                      ] 5% Fetch remote repository...         [==                                     ] 5% Fetch remote repository...         [==                                     ] 6% Fetch remote repository...         [==                                     ] 7% Fetch remote repository...         [==                                     ] 7% Computing updates...               [===                                    ] 8% Computing updates...               [===                                    ] 10% Computing updates...              [===                                    ] 10% Installing NDK (Side by side) 28.2[===                                    ] 10% Downloading android-ndk-r28c-linux[====                                   ] 10% Downloading android-ndk-r28c-linux[====                                   ] 11% Downloading android-ndk-r28c-linux[====                                   ] 12% Downloading android-ndk-r28c-linux[=====                                  ] 13% Downloading android-ndk-r28c-linux[=====                                  ] 14% Downloading android-ndk-r28c-linux[=====                                  ] 15% Downloading android-ndk-r28c-linux[======                                 ] 15% Downloading android-ndk-r28c-linux[======                                 ] 16% Downloading android-ndk-r28c-linux[======                                 ] 17% Downloading android-ndk-r28c-linux[=======                                ] 18% Downloading android-ndk-r28c-linux[=======                                ] 19% Downloading android-ndk-r28c-linux[=======                                ] 20% Downloading android-ndk-r28c-linux[========                               ] 20% Downloading android-ndk-r28c-linux[========                               ] 21% Downloading android-ndk-r28c-linux[========                               ] 22% Downloading android-ndk-r28c-linux[=========                              ] 23% Downloading android-ndk-r28c-linux[=========                              ] 24% Downloading android-ndk-r28c-linux[=========                              ] 25% Downloading android-ndk-r28c-linux[==========                             ] 25% Downloading android-ndk-r28c-linux[==========                             ] 26% Downloading android-ndk-r28c-linux[==========                             ] 27% Downloading android-ndk-r28c-linux[===========                            ] 28% Downloading android-ndk-r28c-linux[===========                            ] 29% Downloading android-ndk-r28c-linux[===========                            ] 30% Downloading android-ndk-r28c-linux[============                           ] 30% Downloading android-ndk-r28c-linux[============                           ] 31% Downloading android-ndk-r28c-linux[============                           ] 32% Downloading android-ndk-r28c-linux[============                           ] 33% Downloading android-ndk-r28c-linux[============                           ] 33% Unzipping...                      [============                           ] 33% Unzipping... android-ndk-r28c/    [============                           ] 33% Unzipping... android-ndk-r28c/READ[=============                          ] 33% Unzipping... android-ndk-r28c/READ[=============                          ] 33% Unzipping... android-ndk-r28c/meta[=============                          ] 33% Unzipping... android-ndk-r28c/shad[=============                          ] 33% Unzipping... android-ndk-r28c/ndk-[=============                          ] 33% Unzipping... android-ndk-r28c/wrap[=============                          ] 33% Unzipping... android-ndk-r28c/ndk-[=============                          ] 33% Unzipping... android-ndk-r28c/tool[=============                          ] 34% Unzipping... android-ndk-r28c/tool[=============                          ] 35% Unzipping... android-ndk-r28c/tool[==============                         ] 35% Unzipping... android-ndk-r28c/tool[==============                         ] 36% Unzipping... android-ndk-r28c/tool[==============                         ] 37% Unzipping... android-ndk-r28c/tool[===============                        ] 38% Unzipping... android-ndk-r28c/tool[===============                        ] 39% Unzipping... android-ndk-r28c/tool[===============                        ] 40% Unzipping... android-ndk-r28c/tool[================                       ] 40% Unzipping... android-ndk-r28c/tool[================                       ] 41% Unzipping... android-ndk-r28c/tool[================                       ] 42% Unzipping... android-ndk-r28c/tool[=================                      ] 43% Unzipping... android-ndk-r28c/tool[=================                      ] 44% Unzipping... android-ndk-r28c/tool[=================                      ] 45% Unzipping... android-ndk-r28c/tool[==================                     ] 45% Unzipping... android-ndk-r28c/tool[==================                     ] 46% Unzipping... android-ndk-r28c/tool[==================                     ] 47% Unzipping... android-ndk-r28c/tool[===================                    ] 48% Unzipping... android-ndk-r28c/tool[===================                    ] 49% Unzipping... android-ndk-r28c/tool[===================                    ] 50% Unzipping... android-ndk-r28c/tool[====================                   ] 50% Unzipping... android-ndk-r28c/tool[====================                   ] 51% Unzipping... android-ndk-r28c/tool[====================                   ] 52% Unzipping... android-ndk-r28c/tool[=====================                  ] 53% Unzipping... android-ndk-r28c/tool[=====================                  ] 54% Unzipping... android-ndk-r28c/tool[=====================                  ] 54% Unzipping... android-ndk-r28c/buil[=====================                  ] 54% Unzipping... android-ndk-r28c/sour[=====================                  ] 54% Unzipping... android-ndk-r28c/NOTI[=====================                  ] 54% Unzipping... android-ndk-r28c/ndk-[=====================                  ] 54% Unzipping... android-ndk-r28c/NOTI[=====================                  ] 54% Unzipping... android-ndk-r28c/pyth[=====================                  ] 54% Unzipping... android-ndk-r28c/preb[=====================                  ] 54% Unzipping... android-ndk-r28c/ndk-[=====================                  ] 54% Unzipping... android-ndk-r28c/sour[=====================                  ] 54% Unzipping... android-ndk-r28c/simp[=====================                  ] 55% Unzipping... android-ndk-r28c/simp[=====================                  ] 55% Unzipping... android-ndk-r28c/CHAN[=======================================] 100% Unzipping... android-ndk-r28c/CHA

+ for pkg in "platforms;android-37.0" "platforms;android-37" "build-tools;37.0.0" "platforms;android-36" "build-tools;36.0.0" "cmake;3.22.1" "ndk;26.1.10909125" "ndk;28.2.13676358" "ndk;29.0.14206865"
+ echo '--- install ndk;29.0.14206865'
--- install ndk;29.0.14206865
+ /usr/local/lib/android/sdk/cmdline-tools/latest/bin/sdkmanager 'ndk;29.0.14206865'
Loading package information...                                                  Loading local repository...                                                     [                                       ] 3% Loading local repository...        [                                       ] 3% Fetch remote repository...         [=                                      ] 3% Fetch remote repository...         [=                                      ] 4% Fetch remote repository...         [=                                      ] 5% Fetch remote repository...         [==                                     ] 5% Fetch remote repository...         [==                                     ] 6% Fetch remote repository...         [==                                     ] 7% Fetch remote repository...         [==                                     ] 7% Computing updates...               [===                                    ] 8% Computing updates...               [===                                    ] 10% Computing updates...              [=======================================] 100% Computing updates...             

+ echo '== platforms =='
== platforms ==
+ ls /usr/local/lib/android/sdk/platforms
android-34
android-34-ext10
android-34-ext11
android-34-ext12
android-34-ext8
android-35
android-35-ext14
android-35-ext15
android-36
android-36-ext18
android-36-ext19
android-36.1
android-37.0
android-37.1
android-37.2
android-37.2-beta1
android-37.2-beta2
android-37.2-beta3
+ echo '== ndk =='
== ndk ==
+ ls /usr/local/lib/android/sdk/ndk
26.1.10909125
27.3.13750724
28.2.13676358
29.0.14206865
30.0.16248370
+ test -d /usr/local/lib/android/sdk/ndk/26.1.10909125
+ test -d /usr/local/lib/android/sdk/ndk/28.2.13676358
+ echo ANDROID_HOME=/usr/local/lib/android/sdk
+ echo ANDROID_SDK_ROOT=/usr/local/lib/android/sdk
+ python3 -m pip install --upgrade pip
Defaulting to user installation because normal site-packages is not writeable
Requirement already satisfied: pip in /usr/lib/python3/dist-packages (25.1.1)
Collecting pip
  Downloading pip-26.3-py3-none-any.whl.metadata (4.6 kB)
Downloading pip-26.3-py3-none-any.whl (2.0 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.0/2.0 MB 157.7 MB/s eta 0:00:00
Installing collected packages: pip
Successfully installed pip-26.3
+ python3 -m pip install pyelftools==0.32 unicorn==2.1.4
Defaulting to user installation because normal site-packages is not writeable
Collecting pyelftools==0.32
  Downloading pyelftools-0.32-py3-none-any.whl.metadata (372 bytes)
Collecting unicorn==2.1.4
  Downloading unicorn-2.1.4-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.2 kB)
Downloading pyelftools-0.32-py3-none-any.whl (188 kB)
Downloading unicorn-2.1.4-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (16.4 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 16.4/16.4 MB 209.6 MB/s  0:00:00
Installing collected packages: pyelftools, unicorn

Successfully installed pyelftools-0.32 unicorn-2.1.4
+ export PATH=/home/runner/.cargo/bin:/opt/hostedtoolcache/Java_Temurin-Hotspot_jdk/21.0.13-9/x64/bin:/snap/bin:/home/runner/.local/bin:/opt/pipx_bin:/home/runner/.cargo/bin:/home/runner/.config/composer/vendor/bin:/usr/local/.ghcup/bin:/home/runner/.dotnet/tools:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
+ PATH=/home/runner/.cargo/bin:/opt/hostedtoolcache/Java_Temurin-Hotspot_jdk/21.0.13-9/x64/bin:/snap/bin:/home/runner/.local/bin:/opt/pipx_bin:/home/runner/.cargo/bin:/home/runner/.config/composer/vendor/bin:/usr/local/.ghcup/bin:/home/runner/.dotnet/tools:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
+ rustup toolchain install stable --profile minimal
info: syncing channel updates for stable-x86_64-unknown-linux-gnu

  stable-x86_64-unknown-linux-gnu unchanged - rustc 1.100.0 (0ef1bc386 2026-11-09)

+ rustc --version
rustc 1.100.0 (0ef1bc386 2026-11-09)
+ rustup target add aarch64-linux-android --toolchain stable
info: downloading component rust-std
+ EXTRACTOR=/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/jailbreak-providers/ghostlock/extractor-native/Cargo.toml
+ '[' -f /home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/jailbreak-providers/ghostlock/extractor-native/Cargo.toml ']'
+ cargo fetch --manifest-path /home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/jailbreak-providers/ghostlock/extractor-native/Cargo.toml
    Updating crates.io index
 Downloading crates ...
  Downloaded funty v2.0.0
  Downloaded yaxpeax-arch v0.3.2
  Downloaded serde_derive v1.0.229
  Downloaded unicode-ident v1.0.25
  Downloaded serde_core v1.0.229
  Downloaded thiserror v2.0.20
  Downloaded yaxpeax-arm v0.5.0
  Downloaded syn v3.0.6
  Downloaded percent-encoding v2.3.2
  Downloaded unit-prefix v0.5.2
  Downloaded getrandom v0.4.3
  Downloaded aho-corasick v1.1.5
  Downloaded jobserver v0.1.35
  Downloaded wasm-bindgen v0.2.128
  Downloaded wasm-bindgen-macro v0.2.128
  Downloaded thiserror-impl v2.0.20
  Downloaded quinn-udp v0.5.15
  Downloaded console v0.16.6
  Downloaded anstyle-parse v1.0.0
  Downloaded itoa v1.0.18
  Downloaded prost v0.14.4
  Downloaded itertools v0.14.0
  Downloaded either v1.18.0
  Downloaded shlex v2.0.1
  Downloaded wasm-bindgen-macro-support v0.2.128
  Downloaded rustversion v1.0.23
  Downloaded once_cell v1.21.4
  Downloaded indicatif v0.18.6
  Downloaded portable-atomic v1.15.0
  Downloaded clap_builder v4.6.7
  Downloaded libbz2-rs-sys v0.2.5
  Downloaded wyz v0.5.1
  Downloaded clap_lex v1.1.1
  Downloaded zmij v1.0.23
  Downloaded bzip2 v0.6.1
  Downloaded bsdiff-android v0.0.2
  Downloaded alloc-no-stdlib v2.0.4
  Downloaded equivalent v1.0.2
  Downloaded alloc-stdlib v0.2.4
  Downloaded radium v0.7.0
  Downloaded prost-derive v0.14.4
  Downloaded strsim v0.11.1
  Downloaded is_terminal_polyfill v1.70.2
  Downloaded anstyle-query v1.1.5
  Downloaded clap v4.6.7
  Downloaded simd-adler32 v0.3.10
  Downloaded flate2 v1.1.10
  Downloaded rand_core v0.10.1
  Downloaded futures-task v0.3.34
  Downloaded miniz_oxide v0.9.1
  Downloaded adler2 v2.0.1
  Downloaded utf8_iter v1.0.4
  Downloaded displaydoc v0.2.7
  Downloaded cfg_aliases v0.2.2
  Downloaded colorchoice v1.0.5
  Downloaded zstd v0.13.3
  Downloaded wasm-bindgen-shared v0.2.128
  Downloaded smallvec v1.16.1
  Downloaded zerofrom v0.1.8
  Downloaded brotli-decompressor v5.0.3
  Downloaded tap v1.0.1
  Downloaded wasm-bindgen-futures v0.4.78
  Downloaded cfg-if v1.0.5
  Downloaded futures-sink v0.3.34
  Downloaded futures-macro v0.3.34
  Downloaded try-lock v0.2.5
  Downloaded quote v1.0.47
  Downloaded slab v0.4.12
  Downloaded futures-io v0.3.34
  Downloaded futures-core v0.3.34
  Downloaded windows-link v0.2.1
  Downloaded tokio-macros v2.7.2
  Downloaded errno v0.3.14
  Downloaded fastrand v2.5.0
  Downloaded block-buffer v0.12.1
  Downloaded cpufeatures v0.3.1
  Downloaded form_urlencoded v1.2.2
  Downloaded tower-layer v0.3.3
  Downloaded untrusted v0.9.0
  Downloaded lru-slab v0.1.3
  Downloaded ipnet v2.12.2
  Downloaded want v0.3.1
  Downloaded atomic-waker v1.1.2
  Downloaded heck v0.5.0
  Downloaded proc-macro2 v1.0.107
  Downloaded autocfg v1.5.1
  Downloaded anyhow v1.0.104
  Downloaded zstd-safe v7.3.0
  Downloaded pkg-config v0.3.34
  Downloaded pin-project-lite v0.2.17
  Downloaded futures-channel v0.3.34
  Downloaded find-msvc-tools v0.1.12
  Downloaded crc32fast v1.5.2
  Downloaded xz2 v0.1.7
  Downloaded wasi v0.11.1+wasi-snapshot-preview1
  Downloaded tempfile v3.27.0
  Downloaded sha2 v0.11.0
  Downloaded digest v0.11.3
  Downloaded crypto-common v0.2.2
  Downloaded hybrid-array v0.4.15
  Downloaded rustls-pki-types v1.15.1
  Downloaded zeroize v1.9.0
  Downloaded web-time v1.1.0
  Downloaded wasm-streams v0.4.2
  Downloaded yoke-derive v0.8.3
  Downloaded writeable v0.6.4
  Downloaded http-body v1.1.0
  Downloaded tokio-rustls v0.26.5
  Downloaded httparse v1.10.1
  Downloaded hyper-rustls v0.27.9
  Downloaded crossbeam-utils v0.8.23
  Downloaded crossbeam-deque v0.8.8
  Downloaded prost-build v0.14.4
  Downloaded memmap2 v0.9.11
  Downloaded num-traits v0.2.19
  Downloaded socket2 v0.6.5
  Downloaded bitflags v2.13.2
  Downloaded subtle v2.6.1
  Downloaded serde_urlencoded v0.7.1
  Downloaded rustc-hash v2.1.3
  Downloaded rand_pcg v0.10.2
  Downloaded chacha20 v0.10.2
  Downloaded log v0.4.34
  Downloaded http-body-util v0.1.5
  Downloaded crossbeam-epoch v0.9.21
  Downloaded protoc-bin-vendored v3.2.0
  Downloaded multimap v0.10.1
  Downloaded twox-hash v2.1.4
  Downloaded hex v0.4.3
  Downloaded terminal_size v0.4.4
  Downloaded anstyle v1.0.14
  Downloaded anstream v1.0.0
  Downloaded utf8parse v0.2.2
  Downloaded anstyle-wincon v3.0.11
  Downloaded once_cell_polyfill v1.70.2
  Downloaded zlib-rs v0.6.8
  Downloaded bytes v1.12.1
  Downloaded cc v1.4.6
  Downloaded r-efi v6.0.0
  Downloaded zip v8.6.0
  Downloaded idna_adapter v1.2.2
  Downloaded zerovec-derive v0.11.6
  Downloaded zerofrom-derive v0.1.8
  Downloaded yoke v0.8.3
  Downloaded stable_deref_trait v1.2.1
  Downloaded tinystr v0.8.4
  Downloaded potential_utf v0.1.6
  Downloaded tower-service v0.3.3
  Downloaded sync_wrapper v1.0.2
  Downloaded windows-targets v0.52.6
  Downloaded getrandom v0.2.17
  Downloaded rayon-core v1.13.0
  Downloaded foldhash v0.1.5
  Downloaded fixedbitset v0.5.7
  Downloaded unicode-width v0.2.2
  Downloaded serde v1.0.229
  Downloaded bumpalo v3.20.3
  Downloaded indexmap v2.14.2
  Downloaded mio v1.2.3
  Downloaded url v2.5.8
  Downloaded synstructure v0.14.0
  Downloaded litemap v0.8.3
  Downloaded base64 v0.22.1
  Downloaded futures v0.3.34
  Downloaded clap_derive v4.6.7
  Downloaded memchr v2.8.3
  Downloaded typed-path v0.12.3
  Downloaded typenum v1.20.1
  Downloaded icu_provider v2.3.1
  Downloaded ryu v1.0.23
  Downloaded tinyvec v1.13.3
  Downloaded hyper-util v0.1.20
  Downloaded prost-types v0.14.4
  Downloaded prettyplease v0.2.37
  Downloaded lz4_flex v0.14.0
  Downloaded encode_unicode v1.0.0
  Downloaded js-sys v0.3.105
  Downloaded idna v1.1.0
  Downloaded icu_normalizer_data v2.3.0
  Downloaded tracing-core v0.1.36
  Downloaded serde_json v1.0.151
  Downloaded hashbrown v0.17.1
  Downloaded reqwest v0.12.28
  Downloaded zerotrie v0.2.5
  Downloaded icu_locale_core v2.3.0
  Downloaded http v1.5.0
  Downloaded rustls-webpki v0.103.15
  Downloaded quinn v0.11.12
  Downloaded rand v0.10.2
  Downloaded regex v1.13.1
  Downloaded futures-util v0.3.34
  Downloaded icu_properties v2.3.0
  Downloaded zerovec v0.11.8
  Downloaded icu_collections v2.3.0
  Downloaded tower-http v0.6.11
  Downloaded tower v0.5.3
  Downloaded rayon v1.12.0
  Downloaded bitvec v1.1.1
  Downloaded webpki-roots v1.0.9
  Downloaded tokio-util v0.7.19
  Downloaded hyper v1.11.1
  Downloaded hashbrown v0.15.5
  Downloaded icu_properties_data v2.3.0
  Downloaded quinn-proto v0.11.18
  Downloaded syn v2.0.119
  Downloaded regex-syntax v0.8.11
  Downloaded rustix v1.1.5
  Downloaded rustls v0.23.45
  Downloaded windows_x86_64_gnullvm v0.52.6
  Downloaded windows_aarch64_gnullvm v0.52.6
  Downloaded bzip2-sys v0.1.13+1.0.8
  Downloaded tracing v0.1.44
  Downloaded windows_i686_gnullvm v0.52.6
  Downloaded icu_normalizer v2.3.0
  Downloaded brotli v8.0.4
  Downloaded regex-automata v0.4.18
  Downloaded web-sys v0.3.105
  Downloaded zstd-sys v2.1.0+zstd.1.5.7
  Downloaded lzma-sys v0.1.20
  Downloaded petgraph v0.8.3
  Downloaded libc v0.2.189
  Downloaded windows_x86_64_gnu v0.52.6
  Downloaded windows_aarch64_msvc v0.52.6
  Downloaded windows_x86_64_msvc v0.52.6
  Downloaded windows_i686_gnu v0.52.6
  Downloaded tokio v1.53.1
  Downloaded windows_i686_msvc v0.52.6
  Downloaded ring v0.17.14
  Downloaded windows-sys v0.52.0
  Downloaded protoc-bin-vendored-macos-aarch_64 v3.2.0
  Downloaded windows-sys v0.61.2
  Downloaded protoc-bin-vendored-macos-x86_64 v3.2.0
  Downloaded linux-raw-sys v0.12.1
  Downloaded protoc-bin-vendored-linux-x86_64 v3.2.0
  Downloaded protoc-bin-vendored-win32 v3.2.0
  Downloaded protoc-bin-vendored-linux-aarch_64 v3.2.0
  Downloaded protoc-bin-vendored-linux-ppcle_64 v3.2.0
  Downloaded protoc-bin-vendored-linux-x86_32 v3.2.0
  Downloaded protoc-bin-vendored-linux-s390_64 v3.2.0
+ ls /home/runner/.cargo/registry
CACHEDIR.TAG
cache
index
src
+ python3 --version
Python 3.14.4
+ cd src
++ command -v python3
+ ./gradlew --no-daemon --max-workers=4 --dependency-verification=off -PbluewhaleSkipSdkVerify=true -PmaplesuPython=/usr/bin/python3 -PmaplesuUltraviderNdk=/usr/local/lib/android/sdk/ndk/28.2.13676358 '-Dorg.gradle.jvmargs=-Xmx6g -XX:MaxMetaspaceSize=1g' :manager:assembleRelease
Fetching distribution.
Downloading https://services.gradle.org/distributions/gradle-9.8.1-bin.zip
..............10%..............20%...............30%..............40%...............50%..............60%...............70%..............80%...............90%..............100%

Welcome to Gradle 9.8.1!

Here are the highlights of this release:
 - Java 27 support
 - Maven mirror settings reuse
 - Linked problem locations in build output

For more details see https://docs.gradle.org/9.8.1/release-notes.html

To honour the JVM settings for this build a single-use Daemon process will be forked. For more on this, please refer to https://docs.gradle.org/9.8.1/userguide/gradle_daemon.html#sec:disabling_the_daemon in the Gradle documentation.
Daemon will be stopped at the end of the build 
```
