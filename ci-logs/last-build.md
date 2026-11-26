# 构建结果

- run: 10  提交: 8eb9dd3d4ba2e0816689d968c5b26b094514aefd
- 作业结论: failure

```
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

蓝鱼品牌化补丁已全部应用。
+ echo '== java =='
== java ==
+ java -version
openjdk version "21.0.13.1" 2026-11-17 LTS
OpenJDK Runtime Environment Temurin-21.0.13.1+2 (build 21.0.13.1+2-LTS)
OpenJDK 64-Bit Server VM Temurin-21.0.13.1+2 (build 21.0.13.1+2-LTS, mixed mode, sharing)
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
+ for pkg in "platforms;android-37.0" "platforms;android-37" "build-tools;37.0.0" "platforms;android-36" "build-tools;36.0.0" "cmake;3.22.1" "ndk;28.2.13676358" "ndk;29.0.14206865"
+ echo '--- install platforms;android-37.0'
--- install platforms;android-37.0
+ /usr/local/lib/android/sdk/cmdline-tools/latest/bin/sdkmanager 'platforms;android-37.0'
Loading package information...                                                  Loading local repository...                                                     [                                       ] 3% Loading local repository...        [                                       ] 3% Fetch remote repository...         [=                                      ] 3% Fetch remote repository...         [=                                      ] 4% Fetch remote repository...         [=                                      ] 5% Fetch remote repository...         [==                                     ] 5% Fetch remote repository...         [==                                     ] 6% Fetch remote repository...         [==                                     ] 7% Fetch remote repository...         [==                                     ] 7% Computing updates...               [===                                    ] 8% Computing updates...               [===                                    ] 10% Computing updates...              [=======================================] 100% Computing updates...             

+ for pkg in "platforms;android-37.0" "platforms;android-37" "build-tools;37.0.0" "platforms;android-36" "build-tools;36.0.0" "cmake;3.22.1" "ndk;28.2.13676358" "ndk;29.0.14206865"
+ echo '--- install platforms;android-37'
--- install platforms;android-37
+ /usr/local/lib/android/sdk/cmdline-tools/latest/bin/sdkmanager 'platforms;android-37'
Loading package information...                                                  Loading local repository...                                                     [                                       ] 3% Loading local repository...        [                                       ] 3% Fetch remote repository...         [=                                      ] 3% Fetch remote repository...         [=                                      ] 4% Fetch remote repository...         [=                                      ] 5% Fetch remote repository...         [==                                     ] 5% Fetch remote repository...         [==                                     ] 6% Fetch remote repository...         [==                                     ] 7% Fetch remote repository...         [==                                     ] 7% Computing updates...               [===                                    ] 8% Computing updates...               [===                                    ] 10% Computing updates...                                                                                              Warning: Failed to find package 'platforms;android-37'
[===                                    ] 10% Computing updates...              + true
+ for pkg in "platforms;android-37.0" "platforms;android-37" "build-tools;37.0.0" "platforms;android-36" "build-tools;36.0.0" "cmake;3.22.1" "ndk;28.2.13676358" "ndk;29.0.14206865"
+ echo '--- install build-tools;37.0.0'
--- install build-tools;37.0.0
+ /usr/local/lib/android/sdk/cmdline-tools/latest/bin/sdkmanager 'build-tools;37.0.0'
Loading package information...                                                  Loading local repository...                                                     [                                       ] 3% Loading local repository...        [                                       ] 3% Fetch remote repository...         [=                                      ] 3% Fetch remote repository...         [=                                      ] 4% Fetch remote repository...         [=                                      ] 5% Fetch remote repository...         [==                                     ] 5% Fetch remote repository...         [==                                     ] 6% Fetch remote repository...         [==                                     ] 7% Fetch remote repository...         [==                                     ] 7% Computing updates...               [===                                    ] 8% Computing updates...               [===                                    ] 10% Computing updates...              [=======================================] 100% Computing updates...             

+ for pkg in "platforms;android-37.0" "platforms;android-37" "build-tools;37.0.0" "platforms;android-36" "build-tools;36.0.0" "cmake;3.22.1" "ndk;28.2.13676358" "ndk;29.0.14206865"
+ echo '--- install platforms;android-36'
--- install platforms;android-36
+ /usr/local/lib/android/sdk/cmdline-tools/latest/bin/sdkmanager 'platforms;android-36'
Loading package information...                                                  Loading local repository...                                                     [                                       ] 3% Loading local repository...        [                                       ] 3% Fetch remote repository...         [=                                      ] 3% Fetch remote repository...         [=                                      ] 4% Fetch remote repository...         [=                                      ] 5% Fetch remote repository...         [==                                     ] 5% Fetch remote repository...         [==                                     ] 6% Fetch remote repository...         [==                                     ] 7% Fetch remote repository...         [==                                     ] 7% Computing updates...               [===                                    ] 8% Computing updates...               [===                                    ] 10% Computing updates...              [=======================================] 100% Computing updates...             

+ for pkg in "platforms;android-37.0" "platforms;android-37" "build-tools;37.0.0" "platforms;android-36" "build-tools;36.0.0" "cmake;3.22.1" "ndk;28.2.13676358" "ndk;29.0.14206865"
+ echo '--- install build-tools;36.0.0'
--- install build-tools;36.0.0
+ /usr/local/lib/android/sdk/cmdline-tools/latest/bin/sdkmanager 'build-tools;36.0.0'
Loading package information...                                                  Loading local repository...                                                     [                                       ] 3% Loading local repository...        [                                       ] 3% Fetch remote repository...         [=                                      ] 3% Fetch remote repository...         [=                                      ] 4% Fetch remote repository...         [=                                      ] 5% Fetch remote repository...         [==                                     ] 5% Fetch remote repository...         [==                                     ] 6% Fetch remote repository...         [==                                     ] 7% Fetch remote repository...         [==                                     ] 7% Computing updates...               [===                                    ] 8% Computing updates...               [===                                    ] 10% Computing updates...              [=======================================] 100% Computing updates...             

+ for pkg in "platforms;android-37.0" "platforms;android-37" "build-tools;37.0.0" "platforms;android-36" "build-tools;36.0.0" "cmake;3.22.1" "ndk;28.2.13676358" "ndk;29.0.14206865"
+ echo '--- install cmake;3.22.1'
--- install cmake;3.22.1
+ /usr/local/lib/android/sdk/cmdline-tools/latest/bin/sdkmanager 'cmake;3.22.1'
Loading package information...                                                  Loading local repository...                                                     [                                       ] 3% Loading local repository...        [                                       ] 3% Fetch remote repository...         [=                                      ] 3% Fetch remote repository...         [=                                      ] 4% Fetch remote repository...         [=                                      ] 5% Fetch remote repository...         [==                                     ] 5% Fetch remote repository...         [==                                     ] 6% Fetch remote repository...         [==                                     ] 7% Fetch remote repository...         [==                                     ] 7% Computing updates...               [===                                    ] 8% Computing updates...               [===                                    ] 10% Computing updates...              [===                                    ] 10% Installing CMake 3.22.1           [===                                    ] 10% Downloading cmake-3.22.1-linux.zip[====                                   ] 10% Downloading cmake-3.22.1-linux.zip[====                                   ] 11% Downloading cmake-3.22.1-linux.zip[====                                   ] 12% Downloading cmake-3.22.1-linux.zip[=====                                  ] 13% Downloading cmake-3.22.1-linux.zip[=====                                  ] 14% Downloading cmake-3.22.1-linux.zip[=====                                  ] 15% Downloading cmake-3.22.1-linux.zip[======                                 ] 15% Downloading cmake-3.22.1-linux.zip[======                                 ] 16% Downloading cmake-3.22.1-linux.zip[======                                 ] 17% Downloading cmake-3.22.1-linux.zip[=======                                ] 18% Downloading cmake-3.22.1-linux.zip[=======                                ] 19% Downloading cmake-3.22.1-linux.zip[=======                                ] 20% Downloading cmake-3.22.1-linux.zip[========                               ] 20% Downloading cmake-3.22.1-linux.zip[========                               ] 21% Downloading cmake-3.22.1-linux.zip[========                               ] 22% Downloading cmake-3.22.1-linux.zip[=========                              ] 23% Downloading cmake-3.22.1-linux.zip[=========                              ] 24% Downloading cmake-3.22.1-linux.zip[=========                              ] 25% Downloading cmake-3.22.1-linux.zip[==========                             ] 25% Downloading cmake-3.22.1-linux.zip[==========                             ] 26% Downloading cmake-3.22.1-linux.zip[==========                             ] 27% Downloading cmake-3.22.1-linux.zip[===========                            ] 28% Downloading cmake-3.22.1-linux.zip[===========                            ] 29% Downloading cmake-3.22.1-linux.zip[===========                            ] 30% Downloading cmake-3.22.1-linux.zip[============                           ] 30% Downloading cmake-3.22.1-linux.zip[============                           ] 31% Downloading cmake-3.22.1-linux.zip[============                           ] 32% Downloading cmake-3.22.1-linux.zip[============                           ] 33% Downloading cmake-3.22.1-linux.zip[============                           ] 33% Unzipping...                      [============                           ] 33% Unzipping... bin/cmake            [=============                          ] 33% Unzipping... bin/cmake            [=============                          ] 34% Unzipping... bin/cmake            [=============                          ] 35% Unzipping... bin/cmake            [==============                         ] 35% Unzipping... bin/cmake            [==============                         ] 36% Unzipping... bin/cmake            [==============                         ] 37% Unzipping... bin/cmake            [===============                        ] 38% Unzipping... bin/cmake            [===============                        ] 39% Unzipping... bin/cmake            [===============                        ] 39% Unzipping... bin/ctest            [===============                        ] 40% Unzipping... bin/ctest            [================                       ] 40% Unzipping... bin/ctest            [================                       ] 41% Unzipping... bin/ctest            [================                       ] 42% Unzipping... bin/ctest            [=================                      ] 43% Unzipping... bin/ctest            [=================                      ] 44% Unzipping... bin/ctest            [=================                      ] 45% Unzipping... bin/ctest            [==================                     ] 45% Unzipping... bin/ctest            [==================                     ] 46% Unzipping... bin/ctest            [==================                     ] 46% Unzipping... bin/cpack            [==================                     ] 47% Unzipping... bin/cpack            [===================                    ] 48% Unzipping... bin/cpack            [===================                    ] 49% Unzipping... bin/cpack            [===================                    ] 50% Unzipping... bin/cpack            [====================                   ] 50% Unzipping... bin/cpack            [====================                   ] 51% Unzipping... bin/cpack            [====================                   ] 52% Unzipping... bin/cpack            [====================                   ] 52% Unzipping... share/vim/vimfiles/in[====================                   ] 52% Unzipping... share/vim/vimfiles/sy[====================                   ] 52% Unzipping... share/aclocal/cmake.m[====================                   ] 52% Unzipping... share/emacs/site-lisp[====================                   ] 52% Unzipping... share/cmake-3.22/incl[====================                   ] 52% Unzipping... share/cmake-3.22/Help[=====================                  ] 53% Unzipping... share/cmake-3.22/Help[=====================                  ] 53% Unzipping... share/cmake-3.22/Temp[=====================                  ] 53% Unzipping... share/cmake-3.22/Modu[=====================                  ] 54% Unzipping... share/cmake-3.22/Modu[=====================                  ] 54% Unzipping... share/bash-completion[=====================                  ] 54% Unzipping... doc/cmake-3.22/Copyri[=====================                  ] 54% Unzipping... doc/cmake-3.22/cmzlib[=====================                  ] 54% Unzipping... doc/cmake-3.22/cmzstd[=====================                  ] 54% Unzipping... doc/cmake-3.22/cmnght[=====================                  ] 54% Unzipping... doc/cmake-3.22/cmsys/[=====================                  ] 54% Unzipping... doc/cmake-3.22/cmcurl[=====================                  ] 54% Unzipping... doc/cmake-3.22/cmlibr[=====================                  ] 54% Unzipping... doc/cmake-3.22/cmliba[=====================                  ] 54% Unzipping... doc/cmake-3.22/cmlibl[=====================                  ] 54% Unzipping... doc/cmake-3.22/cmlibu[=====================                  ] 54% Unzipping... doc/openssl-1.1.1l/LI[=====================                  ] 54% Unzipping... source.properties    [=====================                  ] 54% Unzipping... bin/ninja            [=====================                  ] 54% Unzipping... doc/ninja/LICENSE    [=====================                  ] 54% Unzipping... share/cmake-3.22/Modu[=====================                  ] 55% Unzipping... share/cmake-3.22/Modu[=======================================] 100% Unzipping... share/cmake-3.22/Mod

+ for pkg in "platforms;android-37.0" "platforms;android-37" "build-tools;37.0.0" "platforms;android-36" "build-tools;36.0.0" "cmake;3.22.1" "ndk;28.2.13676358" "ndk;29.0.14206865"
+ echo '--- install ndk;28.2.13676358'
--- install ndk;28.2.13676358
+ /usr/local/lib/android/sdk/cmdline-tools/latest/bin/sdkmanager 'ndk;28.2.13676358'
Loading package information...                                                  Loading local repository...                                                     [                                       ] 3% Loading local repository...        [                                       ] 3% Fetch remote repository...         [=                                      ] 3% Fetch remote repository...         [=                                      ] 4% Fetch remote repository...         [=                                      ] 5% Fetch remote repository...         [==                                     ] 5% Fetch remote repository...         [==                                     ] 6% Fetch remote repository...         [==                                     ] 7% Fetch remote repository...         [==                                     ] 7% Computing updates...               [===                                    ] 8% Computing updates...               [===                                    ] 10% Computing updates...              [===                                    ] 10% Installing NDK (Side by side) 28.2[===                                    ] 10% Downloading android-ndk-r28c-linux[====                                   ] 10% Downloading android-ndk-r28c-linux[====                                   ] 11% Downloading android-ndk-r28c-linux[====                                   ] 12% Downloading android-ndk-r28c-linux[=====                                  ] 13% Downloading android-ndk-r28c-linux[=====                                  ] 14% Downloading android-ndk-r28c-linux[=====                                  ] 15% Downloading android-ndk-r28c-linux[======                                 ] 15% Downloading android-ndk-r28c-linux[======                                 ] 16% Downloading android-ndk-r28c-linux[======                                 ] 17% Downloading android-ndk-r28c-linux[=======                                ] 18% Downloading android-ndk-r28c-linux[=======                                ] 19% Downloading android-ndk-r28c-linux[=======                                ] 20% Downloading android-ndk-r28c-linux[========                               ] 20% Downloading android-ndk-r28c-linux[========                               ] 21% Downloading android-ndk-r28c-linux[========                               ] 22% Downloading android-ndk-r28c-linux[=========                              ] 23% Downloading android-ndk-r28c-linux[=========                              ] 24% Downloading android-ndk-r28c-linux[=========                              ] 25% Downloading android-ndk-r28c-linux[==========                             ] 25% Downloading android-ndk-r28c-linux[==========                             ] 26% Downloading android-ndk-r28c-linux[==========                             ] 27% Downloading android-ndk-r28c-linux[===========                            ] 28% Downloading android-ndk-r28c-linux[===========                            ] 29% Downloading android-ndk-r28c-linux[===========                            ] 30% Downloading android-ndk-r28c-linux[============                           ] 30% Downloading android-ndk-r28c-linux[============                           ] 31% Downloading android-ndk-r28c-linux[============                           ] 32% Downloading android-ndk-r28c-linux[============                           ] 33% Downloading android-ndk-r28c-linux[============                           ] 33% Unzipping...                      [============                           ] 33% Unzipping... android-ndk-r28c/    [============                           ] 33% Unzipping... android-ndk-r28c/READ[=============                          ] 33% Unzipping... android-ndk-r28c/READ[=============                          ] 33% Unzipping... android-ndk-r28c/meta[=============                          ] 33% Unzipping... android-ndk-r28c/shad[=============                          ] 33% Unzipping... android-ndk-r28c/ndk-[=============                          ] 33% Unzipping... android-ndk-r28c/wrap[=============                          ] 33% Unzipping... android-ndk-r28c/ndk-[=============                          ] 33% Unzipping... android-ndk-r28c/tool[=============                          ] 34% Unzipping... android-ndk-r28c/tool[=============                          ] 35% Unzipping... android-ndk-r28c/tool[==============                         ] 35% Unzipping... android-ndk-r28c/tool[==============                         ] 36% Unzipping... android-ndk-r28c/tool[==============                         ] 37% Unzipping... android-ndk-r28c/tool[===============                        ] 38% Unzipping... android-ndk-r28c/tool[===============                        ] 39% Unzipping... android-ndk-r28c/tool[===============                        ] 40% Unzipping... android-ndk-r28c/tool[================                       ] 40% Unzipping... android-ndk-r28c/tool[================                       ] 41% Unzipping... android-ndk-r28c/tool[================                       ] 42% Unzipping... android-ndk-r28c/tool[=================                      ] 43% Unzipping... android-ndk-r28c/tool[=================                      ] 44% Unzipping... android-ndk-r28c/tool[=================                      ] 45% Unzipping... android-ndk-r28c/tool[==================                     ] 45% Unzipping... android-ndk-r28c/tool[==================                     ] 46% Unzipping... android-ndk-r28c/tool[==================                     ] 47% Unzipping... android-ndk-r28c/tool[===================                    ] 48% Unzipping... android-ndk-r28c/tool[===================                    ] 49% Unzipping... android-ndk-r28c/tool[===================                    ] 50% Unzipping... android-ndk-r28c/tool[====================                   ] 50% Unzipping... android-ndk-r28c/tool[====================                   ] 51% Unzipping... android-ndk-r28c/tool[====================                   ] 52% Unzipping... android-ndk-r28c/tool[=====================                  ] 53% Unzipping... android-ndk-r28c/tool[=====================                  ] 54% Unzipping... android-ndk-r28c/tool[=====================                  ] 54% Unzipping... android-ndk-r28c/buil[=====================                  ] 54% Unzipping... android-ndk-r28c/sour[=====================                  ] 54% Unzipping... android-ndk-r28c/NOTI[=====================                  ] 54% Unzipping... android-ndk-r28c/ndk-[=====================                  ] 54% Unzipping... android-ndk-r28c/NOTI[=====================                  ] 54% Unzipping... android-ndk-r28c/pyth[=====================                  ] 54% Unzipping... android-ndk-r28c/preb[=====================                  ] 54% Unzipping... android-ndk-r28c/ndk-[=====================                  ] 54% Unzipping... android-ndk-r28c/sour[=====================                  ] 54% Unzipping... android-ndk-r28c/simp[=====================                  ] 55% Unzipping... android-ndk-r28c/simp[=====================                  ] 55% Unzipping... android-ndk-r28c/CHAN[=======================================] 100% Unzipping... android-ndk-r28c/CHA

+ for pkg in "platforms;android-37.0" "platforms;android-37" "build-tools;37.0.0" "platforms;android-36" "build-tools;36.0.0" "cmake;3.22.1" "ndk;28.2.13676358" "ndk;29.0.14206865"
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
27.3.13750724
28.2.13676358
29.0.14206865
30.0.16248370
+ test -d /usr/local/lib/android/sdk/ndk/28.2.13676358
+ echo ANDROID_HOME=/usr/local/lib/android/sdk
+ echo ANDROID_SDK_ROOT=/usr/local/lib/android/sdk
+ python3 -m pip install --upgrade pip
Defaulting to user installation because normal site-packages is not writeable
Requirement already satisfied: pip in /usr/lib/python3/dist-packages (25.1.1)
Collecting pip
  Downloading pip-26.3-py3-none-any.whl.metadata (4.6 kB)
Downloading pip-26.3-py3-none-any.whl (2.0 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.0/2.0 MB 61.4 MB/s eta 0:00:00
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
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 16.4/16.4 MB 179.5 MB/s  0:00:00
Installing collected packages: pyelftools, unicorn

Successfully installed pyelftools-0.32 unicorn-2.1.4
+ rustup toolchain install stable --profile minimal
info: syncing channel updates for stable-x86_64-unknown-linux-gnu

  stable-x86_64-unknown-linux-gnu unchanged - rustc 1.100.0 (0ef1bc386 2026-11-09)

+ export PATH=/home/runner/.cargo/bin:/opt/hostedtoolcache/Java_Temurin-Hotspot_jdk/21.0.13-2/x64/bin:/snap/bin:/home/runner/.local/bin:/opt/pipx_bin:/home/runner/.cargo/bin:/home/runner/.config/composer/vendor/bin:/usr/local/.ghcup/bin:/home/runner/.dotnet/tools:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
+ PATH=/home/runner/.cargo/bin:/opt/hostedtoolcache/Java_Temurin-Hotspot_jdk/21.0.13-2/x64/bin:/snap/bin:/home/runner/.local/bin:/opt/pipx_bin:/home/runner/.cargo/bin:/home/runner/.config/composer/vendor/bin:/usr/local/.ghcup/bin:/home/runner/.dotnet/tools:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
+ rustc --version
rustc 1.100.0 (0ef1bc386 2026-11-09)
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

> Configure project :libsu-service
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/third_party/libsu-service/build.gradle.kts:22:39: 'fun RegisteringDomainObjectDelegateProviderWithAction<out TaskContainer, Task>.provideDelegate(receiver: Any?, property: KProperty<*>): ExistingDomainObjectDelegate<TaskProvider<Task>>' is deprecated. Use 'val task = tasks.register(name) { }' instead. See the Gradle 9.6 upgrading guide.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/third_party/libsu-service/build.gradle.kts:22:39: 'fun <T : Any, C : NamedDomainObjectContainer<T>> C.registering(action: T.() -> Unit): RegisteringDomainObjectDelegateProviderWithAction<out C, T>' is deprecated. Use 'val element = register(name) { }' instead. See the Gradle 9.6 upgrading guide.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/third_party/libsu-service/build.gradle.kts:22:39: 'fun <T> ExistingDomainObjectDelegate<out T>.getValue(receiver: Any?, property: KProperty<*>): T' is deprecated. Use the named() API instead. See the Gradle 9.6 upgrading guide.

> Configure project :manager
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/build.gradle.kts:208:29: 'fun srcDir(srcDir: Any): Any' is deprecated. Use `directories` mutable set instead.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/build.gradle.kts:209:29: 'fun srcDir(srcDir: Any): Any' is deprecated. Use `directories` mutable set instead.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/build.gradle.kts:216:31: 'fun srcDir(srcDir: Any): Any' is deprecated. Use `directories` mutable set instead.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/build.gradle.kts:220:31: 'fun srcDir(srcDir: Any): Any' is deprecated. Use `directories` mutable set instead.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/build.gradle.kts:222:29: 'fun srcDir(srcDir: Any): Any' is deprecated. Use `directories` mutable set instead.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/build.gradle.kts:223:31: 'fun srcDir(srcDir: Any): Any' is deprecated. Use `directories` mutable set instead.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/build.gradle.kts:228:31: 'fun srcDir(srcDir: Any): Any' is deprecated. Use `directories` mutable set instead.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/build.gradle.kts:229:31: 'fun srcDir(srcDir: Any): Any' is deprecated. Use `directories` mutable set instead.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/build.gradle.kts:841:39: 'fun setSrcDirs(srcDirs: Iterable<*>): Any' is deprecated. Use `directories` mutable set instead.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/build.gradle.kts:1114:37: 'fun <U : Task> RegisteringDomainObjectDelegateProviderWithTypeAndAction<out TaskContainer, U>.provideDelegate(receiver: Any?, property: KProperty<*>): ExistingDomainObjectDelegate<TaskProvider<U>>' is deprecated. Use 'val task = tasks.register<Type>(name) { }' instead. See the Gradle 9.6 upgrading guide.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/build.gradle.kts:1114:37: 'fun <T : Any, C : PolymorphicDomainObjectContainer<T>, U : T> C.registering(type: KClass<U>, action: U.() -> Unit): RegisteringDomainObjectDelegateProviderWithTypeAndAction<out C, U>' is deprecated. Use 'val element = register<Type>(name) { }' instead. See the Gradle 9.6 upgrading guide.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/build.gradle.kts:1114:37: 'fun <T> ExistingDomainObjectDelegate<out T>.getValue(receiver: Any?, property: KProperty<*>): T' is deprecated. Use the named() API instead. See the Gradle 9.6 upgrading guide.

> Task :libsu-service:verifyOfficialTrampoline
> Task :libsu-service:preBuild
> Task :libsu-service:preReleaseBuild
> Task :libsu-service:mergeReleaseJniLibFolders

> Task :manager:checkProviderTracelessInvariants
TRACELESS INVARIANTS OK checks=26 points=19

> Task :libsu-service:mergeReleaseNativeLibs NO-SOURCE
> Task :libsu-service:copyReleaseJniLibsProjectOnly
> Task :libsu-service:compileReleaseAidl
> Task :libsu-service:generateReleaseResources
> Task :libsu-service:packageReleaseResources
> Task :libsu-service:processReleaseNavigationResources
> Task :installer-core:compileJava
> Task :installer-core:processResources NO-SOURCE
> Task :installer-core:classes
> Task :installer-core:jar
> Task :image-core:compileJava
> Task :image-core:processResources
> Task :image-core:classes
> Task :image-core:jar
> Task :libsu-service:javaPreCompileRelease
> Task :libsu-service:extractReleaseSupportedLocales
> Task :libsu-service:prepareReleaseArtProfile
> Task :libsu-service:mapReleaseSourceSetPaths
> Task :libsu-service:parseReleaseLocalResources
> Task :libsu-service:compileReleaseLibraryResources
> Task :libsu-service:writeReleaseAarMetadata
> Task :libsu-service:extractDeepLinksRelease
> Task :libsu-service:generateReleaseAssets UP-TO-DATE
> Task :libsu-service:generateReleaseRFile
> Task :libsu-service:mergeReleaseAssets
> Task :libsu-service:compileReleaseKotlin NO-SOURCE
> Task :libsu-service:processReleaseManifest

> Task :libsu-service:compileReleaseJavaWithJavac
Java compiler version 21 has deprecated support for compiling with source/target version 8.
Try one of the following options:
    1. [Recommended] Use Java toolchain with a lower language version
    2. Set a higher source/target version
    3. Use a lower version of the JDK running the build (if you're not using Java toolchain)
For more details on how to configure these settings, see https://developer.android.com/build/jdks.
To suppress this warning, set android.javaCompile.suppressSourceTargetDeprecationWarning=true in gradle.properties.
Add android.sync.suppressAgpWarnings=JAVA_COMPILE_DEPRECATED_SOURCE_TARGET to the gradle.properties file to suppress this warning.
warning: [options] source value 8 is obsolete and will be removed in a future release
warning: [options] target value 8 is obsolete and will be removed in a future release
warning: [options] To suppress warnings about obsolete options, use -Xlint:-options.
Note: Some input files use or override a deprecated API.
Note: Recompile with -Xlint:deprecation for details.
3 warnings

> Task :libsu-service:mergeReleaseGeneratedProguardFiles
> Task :libsu-service:exportReleaseConsumerProguardFiles
> Task :libsu-service:processReleaseJavaRes NO-SOURCE
> Task :libsu-service:extractProguardFiles
> Task :libsu-service:bundleLibRuntimeToJarRelease
> Task :libsu-service:bundleLibCompileToJarRelease
> Task :libsu-service:createFullJarRelease
> Task :libsu-service:generateReleaseLintVitalModel
> Task :libsu-service:prepareLintJarForPublish
> Task :libsu-service:generateReleaseLintModel
> Task :libsu-service:extractDeepLinksForAarRelease
> Task :libsu-service:checkReleaseAarMetadata
> Task :libsu-service:extractReleaseAnnotations
> Task :libsu-service:mergeReleaseConsumerProguardFiles
> Task :libsu-service:writeReleaseLintModelMetadata
> Task :libsu-service:mergeReleaseJavaResource
> Task :libsu-service:syncReleaseLibJars
> Task :libsu-service:bundleReleaseLocalLintAar

> Task :manager:buildJailbreakProviders
MAPLESU: per-KMI modules for android15-6.6, android15-6.6, android12-5.10, android13-5.15, android14-6.1, android16-6.12, android17-6.18
Traceback (most recent call last):
  File "/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/jailbreak-providers/build.py", line 627, in <module>
    process = subprocess.run(command, stdout=log, stderr=subprocess.STDOUT)
  File "/usr/lib/python3.14/subprocess.py", line 555, in run
    with Popen(*popenargs, **kwargs) as process:
         ~~~~~^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.14/subprocess.py", line 1039, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
    ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                        pass_fds, cwd, env,
                        ^^^^^^^^^^^^^^^^^^^
    ...<5 lines>...
                        gid, gids, uid, umask,
                        ^^^^^^^^^^^^^^^^^^^^^^
                        start_new_session, process_group)
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.14/subprocess.py", line 1875, in _execute_child
    self._posix_spawn(args, executable, env, restore_signals, close_fds,
    ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                      p2cread, p2cwrite,
                      ^^^^^^^^^^^^^^^^^^
                      c2pread, c2pwrite,
                      ^^^^^^^^^^^^^^^^^^
                      errread, errwrite)
                      ^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.14/subprocess.py", line 1819, in _posix_spawn
    self.pid = os.posix_spawn(executable, args, env, **kwargs)
               ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: '/usr/local/lib/android/sdk/cmake/3.22.1/bin/cmake.exe'

> Task :manager:buildJailbreakProviders FAILED
> Task :libsu-service:lintVitalAnalyzeRelease

[Incubating] Problems report is available at: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/build/reports/problems/problems-report.html

FAILURE: Build failed with an exception.

* What went wrong:
Execution failed for task ':manager:buildJailbreakProviders' (registered in build file 'manager/build.gradle.kts').
> Process 'command '/usr/bin/python3'' finished with non-zero exit value 1

* Try:
> Run with --stacktrace option to get the stack trace.
> Run with --info or --debug option to get more log output.
> Run with --scan to get full insights from a Build Scan (powered by Develocity).
> Get more help at https://help.gradle.org.

Deprecated Gradle features were used in this build, making it incompatible with Gradle 10.

You can use '--warning-mode all' to show the individual deprecation warnings and determine if they come from your own scripts or plugins.

For more on this, please refer to https://docs.gradle.org/9.8.1/userguide/command_line_interface.html#sec:command_line_warnings in the Gradle documentation.

BUILD FAILED in 1m 4s
44 actionable tasks: 44 executed
```
