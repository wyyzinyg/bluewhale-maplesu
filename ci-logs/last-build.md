# 构建结果

- run: 29  提交: 72cb0f1d9a8cdd2185b6fe8beb6c570dc48126ec
- 作业结论: failure

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
改好 gradle.properties: 落 bluewhaleSkipUltraBridge

#### gradle 失败原因
2512:> Task :manager:mergeReleaseAssets FAILED
2608:FAILURE: Build failed with an exception.
2610:* What went wrong:
2611:Execution failed for task ':manager:mergeReleaseAssets' (registered by plugin 'com.android.internal.application').

#### CMake 错误日志
--- src/manager/build/jailbreakProviders/build/CMakeFiles/CMakeOutput.log
    arg [cmTC_8ff1a] ==> ignore
    arg [/usr/local/lib/android/sdk/ndk/28.2.13676358/toolchains/llvm/prebuilt/linux-x86_64/sysroot/usr/lib/aarch64-linux-android/31/crtbegin_dynamic.o] ==> obj [/usr/local/lib/android/sdk/ndk/28.2.13676358/toolchains/llvm/prebuilt/linux-x86_64/sysroot/usr/lib/aarch64-linux-android/31/crtbegin_dynamic.o]
    arg [-L/usr/local/lib/android/sdk/ndk/28.2.13676358/toolchains/llvm/prebuilt/linux-x86_64/lib/clang/19/lib/linux/aarch64] ==> dir [/usr/local/lib/android/sdk/ndk/28.2.13676358/toolchains/llvm/prebuilt/linux-x86_64/lib/clang/19/lib/linux/aarch64]
    arg [-L/usr/local/lib/android/sdk/ndk/28.2.13676358/toolchains/llvm/prebuilt/linux-x86_64/sysroot/usr/lib/aarch64-linux-android/31] ==> dir [/usr/local/lib/android/sdk/ndk/28.2.13676358/toolchains/llvm/prebuilt/linux-x86_64/sysroot/usr/lib/aarch64-linux-android/31]
    arg [-L/usr/local/lib/android/sdk/ndk/28.2.13676358/toolchains/llvm/prebuilt/linux-x86_64/sysroot/usr/lib/aarch64-linux-android] ==> dir [/usr/local/lib/android/sdk/ndk/28.2.13676358/toolchains/llvm/prebuilt/linux-x86_64/sysroot/usr/lib/aarch64-linux-android]
    arg [-L/usr/local/lib/android/sdk/ndk/28.2.13676358/toolchains/llvm/prebuilt/linux-x86_64/sysroot/usr/lib] ==> dir [/usr/local/lib/android/sdk/ndk/28.2.13676358/toolchains/llvm/prebuilt/linux-x86_64/sysroot/usr/lib]
    arg [--build-id=sha1] ==> ignore
    arg [--no-undefined-version] ==> ignore
    arg [--fatal-warnings] ==> ignore
    arg [--no-undefined] ==> ignore
    arg [CMakeFiles/cmTC_8ff1a.dir/CMakeCXXCompilerABI.cpp.o] ==> ignore
    arg [-Bstatic] ==> search static
    arg [-lc++] ==> lib [c++]
    arg [-Bdynamic] ==> search dynamic
    arg [-lm] ==> lib [m]
    arg [/usr/local/lib/android/sdk/ndk/28.2.13676358/toolchains/llvm/prebuilt/linux-x86_64/lib/clang/19/lib/linux/libclang_rt.builtins-aarch64-android.a] ==> lib [/usr/local/lib/android/sdk/ndk/28.2.13676358/toolchains/llvm/prebuilt/linux-x86_64/lib/clang/19/lib/linux/libclang_rt.builtins-aarch64-android.a]
    arg [-l:libunwind.a] ==> lib [-l:libunwind.a]
    arg [-ldl] ==> lib [dl]
    arg [-lc] ==> lib [c]
    arg [/usr/local/lib/android/sdk/ndk/28.2.13676358/toolchains/llvm/prebuilt/linux-x86_64/lib/clang/19/lib/linux/libclang_rt.builtins-aarch64-android.a] ==> lib [/usr/local/lib/android/sdk/ndk/28.2.13676358/toolchains/llvm/prebuilt/linux-x86_64/lib/clang/19/lib/linux/libclang_rt.builtins-aarch64-android.a]
    arg [-l:libunwind.a] ==> lib [-l:libunwind.a]
    arg [-ldl] ==> lib [dl]
    arg [/usr/local/lib/android/sdk/ndk/28.2.13676358/toolchains/llvm/prebuilt/linux-x86_64/sysroot/usr/lib/aarch64-linux-android/31/crtend_android.o] ==> obj [/usr/local/lib/android/sdk/ndk/28.2.13676358/toolchains/llvm/prebuilt/linux-x86_64/sysroot/usr/lib/aarch64-linux-android/31/crtend_android.o]
  remove lib [/usr/local/lib/android/sdk/ndk/28.2.13676358/toolchains/llvm/prebuilt/linux-x86_64/lib/clang/19/lib/linux/libclang_rt.builtins-aarch64-android.a]
  remove lib [/usr/local/lib/android/sdk/ndk/28.2.13676358/toolchains/llvm/prebuilt/linux-x86_64/lib/clang/19/lib/linux/libclang_rt.builtins-aarch64-android.a]
  collapse library dir [/usr/local/lib/android/sdk/ndk/28.2.13676358/toolchains/llvm/prebuilt/linux-x86_64/lib/clang/19/lib/linux/aarch64] ==> [/usr/local/lib/android/sdk/ndk/28.2.13676358/toolchains/llvm/prebuilt/linux-x86_64/lib/clang/19/lib/linux/aarch64]
  collapse library dir [/usr/local/lib/android/sdk/ndk/28.2.13676358/toolchains/llvm/prebuilt/linux-x86_64/sysroot/usr/lib/aarch64-linux-android/31] ==> [/usr/local/lib/android/sdk/ndk/28.2.13676358/toolchains/llvm/prebuilt/linux-x86_64/sysroot/usr/lib/aarch64-linux-android/31]
  collapse library dir [/usr/local/lib/android/sdk/ndk/28.2.13676358/toolchains/llvm/prebuilt/linux-x86_64/sysroot/usr/lib/aarch64-linux-android] ==> [/usr/local/lib/android/sdk/ndk/28.2.13676358/toolchains/llvm/prebuilt/linux-x86_64/sysroot/usr/lib/aarch64-linux-android]
  collapse library dir [/usr/local/lib/android/sdk/ndk/28.2.13676358/toolchains/llvm/prebuilt/linux-x86_64/sysroot/usr/lib] ==> [/usr/local/lib/android/sdk/ndk/28.2.13676358/toolchains/llvm/prebuilt/linux-x86_64/sysroot/usr/lib]
  implicit libs: [c++;m;-l:libunwind.a;dl;c;-l:libunwind.a;dl]
  implicit objs: [/usr/local/lib/android/sdk/ndk/28.2.13676358/toolchains/llvm/prebuilt/linux-x86_64/sysroot/usr/lib/aarch64-linux-android/31/crtbegin_dynamic.o;/usr/local/lib/android/sdk/ndk/28.2.13676358/toolchains/llvm/prebuilt/linux-x86_64/sysroot/usr/lib/aarch64-linux-android/31/crtend_android.o]
  implicit dirs: [/usr/local/lib/android/sdk/ndk/28.2.13676358/toolchains/llvm/prebuilt/linux-x86_64/lib/clang/19/lib/linux/aarch64;/usr/local/lib/android/sdk/ndk/28.2.13676358/toolchains/llvm/prebuilt/linux-x86_64/sysroot/usr/lib/aarch64-linux-android/31;/usr/local/lib/android/sdk/ndk/28.2.13676358/toolchains/llvm/prebuilt/linux-x86_64/sysroot/usr/lib/aarch64-linux-android;/usr/local/lib/android/sdk/ndk/28.2.13676358/toolchains/llvm/prebuilt/linux-x86_64/sysroot/usr/lib]
  implicit fwks: []


Checking whether the ASM compiler is Clang using "--version" matched "(clang version)":
Android (13624864, +pgo, +bolt, +lto, +mlgo, based on r530567e) clang version 19.0.1 (https://android.googlesource.com/toolchain/llvm-project 97a699bf4812a18fb657c2779f5296a4ab2694d2)
Target: x86_64-unknown-linux-gnu
Thread model: posix
InstalledDir: /usr/local/lib/android/sdk/ndk/28.2.13676358/toolchains/llvm/prebuilt/linux-x86_64/bin
--- src/manager/build/jailbreakProviders/build/CMakeFiles/CMakeError.log
Checking whether the ASM compiler is GNU using "--version" did not match "(GNU assembler)|(GCC)|(Free Software Foundation)":
Android (13624864, +pgo, +bolt, +lto, +mlgo, based on r530567e) clang version 19.0.1 (https://android.googlesource.com/toolchain/llvm-project 97a699bf4812a18fb657c2779f5296a4ab2694d2)
Target: x86_64-unknown-linux-gnu
Thread model: posix
InstalledDir: /usr/local/lib/android/sdk/ndk/28.2.13676358/toolchains/llvm/prebuilt/linux-x86_64/bin

```
#### provider 子构建日志（CMake/cargo 报错常只写在这里）
--- src/manager/build/jailbreakProviders/build.json
{"ok": null, "errors": null, "failure": null}
--- src/manager/build/jailbreakProviders/root/build.json
{"ok": null, "errors": null, "failure": null}
--- src/manager/build/jailbreakProviders/extractor/build.json
{"ok": null, "errors": null, "failure": null}
--- src/manager/build/jailbreakProviders/ir/build.json
{"ok": null, "errors": null, "failure": null}
===== src/manager/build/jailbreakProviders/build.log =====
   Compiling anstyle-parse v1.0.0
   Compiling num-traits v0.2.19
   Compiling petgraph v0.8.3
   Compiling regex v1.13.1
   Compiling prost-types v0.14.4
   Compiling serde_derive v1.0.229
   Compiling lzma-sys v0.1.20
   Compiling anstyle-query v1.1.5
   Compiling protoc-bin-vendored-linux-ppcle_64 v3.2.0
   Compiling portable-atomic v1.15.0
   Compiling protoc-bin-vendored-macos-x86_64 v3.2.0
   Compiling log v0.4.34
   Compiling protoc-bin-vendored-linux-s390_64 v3.2.0
   Compiling protoc-bin-vendored-win32 v3.2.0
   Compiling multimap v0.10.1
   Compiling protoc-bin-vendored-linux-x86_32 v3.2.0
   Compiling radium v0.7.0
   Compiling is_terminal_polyfill v1.70.2
   Compiling zmij v1.0.23
   Compiling protoc-bin-vendored-linux-x86_64 v3.2.0
   Compiling anstyle v1.0.14
   Compiling colorchoice v1.0.5
   Compiling protoc-bin-vendored-linux-aarch_64 v3.2.0
   Compiling zstd-safe v7.3.0
   Compiling protoc-bin-vendored-macos-aarch_64 v3.2.0
   Compiling protoc-bin-vendored v3.2.0
   Compiling anstream v1.0.0
   Compiling prost-build v0.14.4
   Compiling terminal_size v0.4.4
   Compiling brotli-decompressor v5.0.3
   Compiling crypto-common v0.2.2
   Compiling block-buffer v0.12.1
   Compiling strsim v0.11.1
   Compiling tap v1.0.1
   Compiling libbz2-rs-sys v0.2.5
   Compiling unicode-width v0.2.2
   Compiling thiserror v2.0.20
   Compiling serde_json v1.0.151
   Compiling clap_lex v1.1.1
   Compiling clap_builder v4.6.7
   Compiling bzip2 v0.6.1
   Compiling console v0.16.6
   Compiling rayon v1.12.0
   Compiling wyz v0.5.1
   Compiling digest v0.11.3
   Compiling brotli v8.0.4
   Compiling payload-extract v0.1.1 (/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/jailbreak-providers/ghostlock/extractor-native/vendor/payload-extract)
   Compiling clap_derive v4.6.7
   Compiling thiserror-impl v2.0.20
   Compiling aho-corasick v1.1.5
   Compiling cpufeatures v0.3.1
   Compiling funty v2.0.0
   Compiling adler2 v2.0.1
   Compiling simd-adler32 v0.3.10
   Compiling unit-prefix v0.5.2
   Compiling itoa v1.0.18
   Compiling typed-path v0.12.3
   Compiling indicatif v0.18.6
   Compiling zip v8.6.0
   Compiling bsdiff-android v0.0.2
   Compiling miniz_oxide v0.9.1
   Compiling bitvec v1.1.1
   Compiling clap v4.6.7
   Compiling sha2 v0.11.0
   Compiling yaxpeax-arch v0.3.2
   Compiling xz2 v0.1.7
   Compiling zstd v0.13.3
   Compiling memmap2 v0.9.11
   Compiling hex v0.4.3
   Compiling lz4_flex v0.14.0
   Compiling yaxpeax-arm v0.5.0
   Compiling flate2 v1.1.10
   Compiling ghostlock-extract v0.1.0 (/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/jailbreak-providers/ghostlock/extractor-native)
    Finished `release` profile [optimized] target(s) in 1m 01s
{
  "module": "/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/build/jailbreakProviders/ir/maplesu_ir.ko",
  "sha256": "68a48bd0ff1abb1e0f4ad50b11889ecbfcdb85b172e8a02af7586834924c8c70",
  "bytes": 15240,
  "contract": "/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/jailbreak-providers/ir-loader/contract.json",
  "facts": {
    "vermagic": "6.6.89-android15-8-g7e1f3c083cc6-abogki467167594-4k SMP preempt mod_unload modversions aarch64",
    "vermagicSuffix": " SMP preempt mod_unload modversions aarch64",
    "versionEntries": 1,
    "thisModuleName": "maplesu_ir",
    "initReloc": "init_module",
    "exitReloc": "cleanup_module",
    "specBytes": 4096,
    "imports": [],
    "kcfiInitTypeId": "0x36b1c5a6",
    "initSection": ".init.text",
    "initSize": 3588,
    "definedSymbols": [
      "$d.0",
      "$d.1",
      "$d.2",
      "$d.3",
      "$d.4",
      "$d.5",
      "$d.6",
      "$d.7",
      "$x.1",
      "$x.2",
      "$x.4",
      "__ir_spec",
      "__this_module",
      "cleanup_module",
      "init_module",
      "init_module.ctx",
      "ir_verify_patched",
      "maplesu_ir.c"
    ]
  }
}
canary: /home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/build/jailbreakProviders/ir/maplesu_ir-canary.ko
$ /usr/bin/python3 /home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/jailbreak-providers/root-loader/build_root_module.py --ndk-dir /usr/local/lib/android/sdk/ndk/28.2.13676358 --out-dir /home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/build/jailbreakProviders/root --contract /home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/jailbreak-providers/root-loader/contracts/6.6.89-android15-8-g7e1f3c083cc6-abogki467167594-4k.json --quiet
$ /usr/bin/python3 /home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/jailbreak-providers/root-loader/build_root_module.py --module maplesu_l3 --ndk-dir /usr/local/lib/android/sdk/ndk/28.2.13676358 --out-dir /home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/build/jailbreakProviders/l3 --contract /home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/jailbreak-providers/root-loader/contracts/6.6.89-android15-8-g7e1f3c083cc6-abogki467167594-4k.json --quiet
补拉 Maven 依赖 https://repo1.maven.org/maven2/org/jetbrains/kotlinx/kotlinx-serialization-json-jvm/1.11.0/kotlinx-serialization-json-jvm-1.11.0.jar
补拉 Maven 依赖 https://repo1.maven.org/maven2/org/jetbrains/kotlinx/kotlinx-serialization-core-jvm/1.11.0/kotlinx-serialization-core-jvm-1.11.0.jar
补拉 Maven 依赖 https://repo1.maven.org/maven2/org/jetbrains/kotlin/kotlin-compiler-embeddable/2.4.20/kotlin-compiler-embeddable-2.4.20.jar
补拉 Maven 依赖 https://repo1.maven.org/maven2/org/jetbrains/kotlinx/kotlinx-coroutines-core-jvm/1.11.0/kotlinx-coroutines-core-jvm-1.11.0.jar
===== src/manager/build/jailbreakProviders/l3/per-kmi/android17-6.18/build.log =====
$ /usr/bin/python3 /home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/jailbreak-providers/root-loader/build_root_module.py --module maplesu_l3 --ndk-dir /usr/local/lib/android/sdk/ndk/28.2.13676358 --out-dir /home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/build/jailbreakProviders/l3/per-kmi/android17-6.18/l3 --contract /home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/jailbreak-providers/root-loader/contracts/family-6.18.json --quiet
===== src/manager/build/jailbreakProviders/l3/per-kmi/android14-6.1/build.log =====
$ /usr/bin/python3 /home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/jailbreak-providers/root-loader/build_root_module.py --module maplesu_l3 --ndk-dir /usr/local/lib/android/sdk/ndk/28.2.13676358 --out-dir /home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/build/jailbreakProviders/l3/per-kmi/android14-6.1/l3 --contract /home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/jailbreak-providers/root-loader/contracts/family-6.1.json --quiet
#### 主构建日志尾
[90/97] Building CXX object CMakeFiles/maplesu_patch_core.dir/upstream/patch_compat_filldir.cpp.o
[91/97] Building CXX object CMakeFiles/maplesu_patch_core.dir/upstream/patch_do_execve.cpp.o
/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/patch-engine/upstream/patch_do_execve.cpp:1:12: warning: #pragma once in main file [-Wpragma-once-outside-header]
<U+FEFF>#pragma once
                ^
1 warning generated.
[92/97] Building CXX object CMakeFiles/maplesu_patch_core.dir/upstream/patch_filldir64.cpp.o
[93/97] Building CXX object CMakeFiles/maplesu-kernel-patch.dir/src/patch_main.cpp.o
[94/97] Building CXX object CMakeFiles/maplesu_patch_core.dir/src/patch_plan.cpp.o
[95/97] Building CXX object CMakeFiles/maplesu_patch_core.dir/upstream/patch_kernel_root.cpp.o
[96/97] Linking CXX static library libmaplesu_patch_core.a
[97/97] Linking CXX executable maplesu-kernel-patch

> Task :manager:configureMapleSuRuntime
-- The CXX compiler identification is Clang 17.0.2
-- The ASM compiler identification is Clang with GNU-like command-line
-- Found assembler: /usr/local/lib/android/sdk/ndk/26.1.10909125/toolchains/llvm/prebuilt/linux-x86_64/bin/clang
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /usr/local/lib/android/sdk/ndk/26.1.10909125/toolchains/llvm/prebuilt/linux-x86_64/bin/clang++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- The C compiler identification is Clang 17.0.2
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /usr/local/lib/android/sdk/ndk/26.1.10909125/toolchains/llvm/prebuilt/linux-x86_64/bin/clang - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Configuring done
-- Generating done
-- Build files have been written to: /home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/build/maplesuRuntime

> Task :manager:buildMapleSuRuntime
[1/11] Building CXX object CMakeFiles/maplesu_bootstrap.dir/src/block_partition_access.cpp.o
[2/11] Building CXX object CMakeFiles/maplesu_parasite.dir/src/parasite/parasite_loader.cpp.o
[3/11] Linking CXX shared library libmaplesu_parasite.so
[4/11] Building CXX object CMakeFiles/maplesu_bootstrap.dir/src/su_bootstrap.cpp.o
[5/11] Building CXX object CMakeFiles/maplesu-runtime.dir/src/su_session.cpp.o
[6/11] Building CXX object CMakeFiles/maplesu-runtime.dir/src/exec_main.cpp.o
[7/11] Building CXX object CMakeFiles/maplesu_bootstrap.dir/src/session_process.cpp.o
[8/11] Linking CXX shared library libmaplesu_bootstrap.so
[9/11] Linking CXX executable maplesu-runtime
[10/11] Building CXX object CMakeFiles/maplesu-su.dir/src/su_main.cpp.o
[11/11] Linking CXX executable maplesu-su

> Task :manager:buildModulePolicy
-- The C compiler identification is Clang 17.0.2
-- The CXX compiler identification is Clang 17.0.2
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /usr/local/lib/android/sdk/ndk/26.1.10909125/toolchains/llvm/prebuilt/linux-x86_64/bin/clang - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /usr/local/lib/android/sdk/ndk/26.1.10909125/toolchains/llvm/prebuilt/linux-x86_64/bin/clang++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Configuring done
-- Generating done
-- Build files have been written to: /home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/module-policy/build/arm64-v8a
[0/2] Re-checking globbed directories...
[1/69] Building C object CMakeFiles/maplesu_sepol.dir/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/.deps/selinux/libsepol/src/boolean_record.c.o
[2/69] Building C object CMakeFiles/maplesu_sepol.dir/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/.deps/selinux/libsepol/src/avrule_block.c.o
[3/69] Building C object CMakeFiles/maplesu_sepol.dir/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/.deps/selinux/libsepol/src/booleans.c.o
[4/69] Building C object CMakeFiles/maplesu_sepol.dir/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/.deps/selinux/libsepol/src/constraint.c.o
[5/69] Building C object CMakeFiles/maplesu_sepol.dir/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/.deps/selinux/libsepol/src/avtab.c.o
[6/69] Building C object CMakeFiles/maplesu_sepol.dir/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/.deps/selinux/libsepol/src/assertion.c.o
[7/69] Building C object CMakeFiles/maplesu_sepol.dir/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/.deps/selinux/libsepol/src/context_record.c.o
[8/69] Building C object CMakeFiles/maplesu_sepol.dir/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/.deps/selinux/libsepol/src/context.c.o
[9/69] Building C object CMakeFiles/maplesu_sepol.dir/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/.deps/selinux/libsepol/src/debug.c.o
[10/69] Building C object CMakeFiles/maplesu_sepol.dir/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/.deps/selinux/libsepol/src/conditional.c.o
[11/69] Building C object CMakeFiles/maplesu_sepol.dir/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/.deps/selinux/libsepol/src/handle.c.o
[12/69] Building C object CMakeFiles/maplesu_sepol.dir/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/.deps/selinux/libsepol/src/hashtab.c.o
[13/69] Building C object CMakeFiles/maplesu_sepol.dir/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/.deps/selinux/libsepol/src/ebitmap.c.o
[14/69] Building C object CMakeFiles/maplesu_sepol.dir/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/.deps/selinux/libsepol/src/ibendport_record.c.o
[15/69] Building C object CMakeFiles/maplesu_sepol.dir/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/.deps/selinux/libsepol/src/hierarchy.c.o
[16/69] Building C object CMakeFiles/maplesu_sepol.dir/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/.deps/selinux/libsepol/src/ibendports.c.o
[17/69] Building C object CMakeFiles/maplesu_sepol.dir/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/.deps/selinux/libsepol/src/ibpkey_record.c.o
[18/69] Building C object CMakeFiles/maplesu_sepol.dir/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/.deps/selinux/libsepol/src/iface_record.c.o
[19/69] Building C object CMakeFiles/maplesu_sepol.dir/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/.deps/selinux/libsepol/src/ibpkeys.c.o
[20/69] Building C object CMakeFiles/maplesu_sepol.dir/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/.deps/selinux/libsepol/src/interfaces.c.o
[21/69] Building C object CMakeFiles/maplesu_sepol.dir/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/.deps/selinux/libsepol/src/kernel_to_common.c.o
[22/69] Building C object CMakeFiles/maplesu_sepol.dir/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/.deps/selinux/libsepol/src/expand.c.o
[23/69] Building C object CMakeFiles/maplesu_sepol.dir/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/.deps/selinux/libsepol/src/kernel_to_conf.c.o
[24/69] Building C object CMakeFiles/maplesu_sepol.dir/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/.deps/selinux/libsepol/src/kernel_to_cil.c.o
[25/69] Building C object CMakeFiles/maplesu_sepol.dir/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/.deps/selinux/libsepol/src/link.c.o
[26/69] Building C object CMakeFiles/maplesu_sepol.dir/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/.deps/selinux/libsepol/src/mls.c.o
[27/69] Building C object CMakeFiles/maplesu_sepol.dir/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/.deps/selinux/libsepol/src/node_record.c.o
[28/69] Building C object CMakeFiles/maplesu_sepol.dir/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/.deps/selinux/libsepol/src/nodes.c.o
[29/69] Building C object CMakeFiles/maplesu_sepol.dir/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/.deps/selinux/libsepol/src/module.c.o
[30/69] Building C object CMakeFiles/maplesu_sepol.dir/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/.deps/selinux/libsepol/src/polcaps.c.o
[31/69] Building C object CMakeFiles/maplesu_sepol.dir/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/.deps/selinux/libsepol/src/policydb_convert.c.o
[32/69] Building C object CMakeFiles/maplesu_sepol.dir/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/.deps/selinux/libsepol/src/policydb_public.c.o
[33/69] Building C object CMakeFiles/maplesu_sepol.dir/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/.deps/selinux/libsepol/src/optimize.c.o
[34/69] Building C object CMakeFiles/maplesu_sepol.dir/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/.deps/selinux/libsepol/src/port_record.c.o
[35/69] Building C object CMakeFiles/maplesu_sepol.dir/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/.deps/selinux/libsepol/src/ports.c.o
[36/69] Building C object CMakeFiles/maplesu_sepol.dir/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/.deps/selinux/libsepol/src/policydb_validate.c.o
[37/69] Building C object CMakeFiles/maplesu_sepol.dir/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/.deps/selinux/libsepol/src/sidtab.c.o
[38/69] Building C object CMakeFiles/maplesu_sepol.dir/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/.deps/selinux/libsepol/src/symtab.c.o
[39/69] Building C object CMakeFiles/maplesu_sepol.dir/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/.deps/selinux/libsepol/src/policydb.c.o
[40/69] Building C object CMakeFiles/maplesu_sepol.dir/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/.deps/selinux/libsepol/src/module_to_cil.c.o
[41/69] Building C object CMakeFiles/maplesu_sepol.dir/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/.deps/selinux/libsepol/src/user_record.c.o
[42/69] Building C object CMakeFiles/maplesu_sepol.dir/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/.deps/selinux/libsepol/src/services.c.o
[43/69] Building C object CMakeFiles/maplesu_sepol.dir/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/.deps/selinux/libsepol/src/users.c.o
[44/69] Building C object CMakeFiles/maplesu_sepol.dir/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/.deps/selinux/libsepol/src/util.c.o
[45/69] Building CXX object CMakeFiles/maplesu-policy.dir/src/ksu_manager_fd.cpp.o
[46/69] Building C object CMakeFiles/maplesu_sepol.dir/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/.deps/selinux/libsepol/src/write.c.o
[47/69] Linking C static library libmaplesu_sepol.a
[48/69] Building CXX object CMakeFiles/maplesu-policy.dir/src/jailbreak_selinux_hide.cpp.o
[49/69] Building CXX object CMakeFiles/maplesu-policy.dir/src/boot_sdk_control.cpp.o
[50/69] Building CXX object CMakeFiles/maplesu-policy.dir/derived/sepolicy.cpp.o
[51/69] Building CXX object CMakeFiles/maplesu-policy.dir/src/boot_sdk_layout.cpp.o
[52/69] Building CXX object CMakeFiles/maplesu-policy.dir/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/runtime/ultra/policy/module_policy_config.cpp.o
[53/69] Building CXX object CMakeFiles/maplesu-policy.dir/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/runtime/ultra/policy/jailbreak_status_layout.cpp.o
[54/69] Building CXX object CMakeFiles/maplesu-policy.dir/src/policy_hook_loader.cpp.o
[55/69] Building CXX object CMakeFiles/maplesu-policy.dir/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/runtime/ultra/policy/kernel_layout.cpp.o
[56/69] Building CXX object CMakeFiles/maplesu-policy.dir/src/main.cpp.o
[57/69] Building CXX object CMakeFiles/maplesu-policy.dir/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/runtime/ultra/policy/kernel_payload_metadata.cpp.o
[58/69] Building CXX object CMakeFiles/maplesu-policy.dir/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/runtime/ultra/policy/kernel_payload.cpp.o
[59/69] Building CXX object CMakeFiles/maplesu-policy.dir/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/runtime/ultra/policy/kernel_payload_hook.cpp.o
[60/69] Building CXX object CMakeFiles/maplesu-policy.dir/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/runtime/ultra/policy/kernel_payload_loader.cpp.o
[61/69] Building CXX object CMakeFiles/maplesu-module-policy-config-tests.dir/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/runtime/ultra/policy/module_policy_config.cpp.o
[62/69] Building CXX object CMakeFiles/maplesu-policy-tests.dir/derived/sepolicy.cpp.o
[63/69] Building CXX object CMakeFiles/maplesu-policy-tests.dir/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/runtime/ultra/policy/module_policy_config.cpp.o
[64/69] Building CXX object CMakeFiles/maplesu-module-policy-config-tests.dir/tests/module_policy_config_tests.cpp.o
[65/69] Linking CXX executable maplesu-module-policy-config-tests
[66/69] Building CXX object CMakeFiles/maplesu-policy-tests.dir/tests/policy_tests.cpp.o
[67/69] Linking CXX executable maplesu-policy-tests
[68/69] Building CXX object CMakeFiles/maplesu-policy.dir/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/runtime/ultra/policy/hook-bundles/policy-bundles.cpp.o
[69/69] Linking CXX executable maplesu-policy
{"abi": "arm64-v8a", "selinux_commit": "be1b39a657fee7faacfae548b75cb53302043a01", "magisk_commit": "e8a58776f1d7bdf852072ad0baa6eceb9a1e4aac", "binary": "/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/module-policy/build/arm64-v8a/maplesu-policy", "sha256": "b63430f3ceb9db7902e7aeef7030f7016f9d5106f814f3586eda16845876d26f", "bytes": 15280096, "tests_binary": "/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/module-policy/build/arm64-v8a/maplesu-policy-tests", "tests_sha256": "ddc0bbd0c58542ca566ab0c7ae58df8346b1d6c503451374c7b23e5d4d1a657c", "temporaryHookBackend": {"enabled": true, "controlAbi": 2, "bundleSourceSha256": "6e36c28fd4705e9ee9719b26c28b52c78e2fdd8f63c5c8a4bc4560a725f5ebf1"}}

> Task :manager:buildModuleTools
 Downloading crates ...
  Downloaded unicode-ident v1.0.27
  Downloaded either v1.19.0
  Downloaded prost v0.13.5
  Downloaded prost-derive v0.13.5
  Downloaded memmap2 v0.9.12
  Downloaded syn v3.0.9
  Downloaded libc v0.2.191
   Compiling proc-macro2 v1.0.107
   Compiling unicode-ident v1.0.27
   Compiling quote v1.0.47
   Compiling anyhow v1.0.104
   Compiling either v1.19.0
   Compiling libc v0.2.191
   Compiling itertools v0.14.0
   Compiling utf8parse v0.2.2
   Compiling anstyle-parse v1.0.0
   Compiling anstyle v1.0.14
   Compiling syn v2.0.119
   Compiling bytes v1.12.1
   Compiling anstyle-query v1.1.5
   Compiling colorchoice v1.0.5
   Compiling is_terminal_polyfill v1.70.2
   Compiling anstream v1.0.0
   Compiling syn v3.0.9
   Compiling clap_lex v1.1.1
   Compiling strsim v0.11.1
   Compiling heck v0.5.0
   Compiling memmap2 v0.9.12
   Compiling clap_builder v4.6.7
   Compiling log v0.4.34
   Compiling prost-derive v0.13.5
   Compiling clap_derive v4.6.7
   Compiling prost v0.13.5
   Compiling prop-rs v0.2.0 (/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/third_party/ksu_props/src/crates/prop-rs)
   Compiling prop-rs-android v0.2.0 (/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/third_party/ksu_props/src/crates/prop-rs-android)
   Compiling clap v4.6.7
   Compiling maplesu-module-tools v0.2.0 (/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/module-tools)
    Finished `release` profile [optimized] target(s) in 12.61s
{
  "host": "maplesu-tools",
  "abi": "arm64-v8a",
  "tools": {
    "resetprop": "link"
  },
  "pinnedCheckout": {
    "path": "third_party/ksu_props/src",
    "commit": "ddb6ee7294467f7f25bad2118e9e24eee104144b",
    "filesVerified": 34,
    "sourceManifest": "82c4b8b3b491e230725bfd10a026aac1fa79d602357aecfec8afc8b9352391aa",
    "cargoLock": "09729c863b6c257854480921817fc98278e54d93b639a74391a47796496f2a0f"
  },
  "reuse": {
    "includedFrom": "third_party/ksu_props/src/tools/resetprop/src/resetprop_main.rs",
    "includedSha256": "4b133d446030f337adf797914bfd179365486995bae598b1ffacf7cc0168466b",
    "hostEntry": "module-tools/src/main.rs",
    "hostEntrySha256": "772ddf3900f61cf94ff66b324a0c6521134800185d1074cd71799aa96123c64f",
    "hostModule": "module-tools/src/module_sync.rs",
    "hostModuleSha256": "73c7a6b496eb6ecd37685a2c404bad439c954b4cf483e5c0554f69179d3b0766"
  },
  "cargoLock": "a036d5b6779c0ac6ed636779420733cdab759525e4778debc64625c0bce97511",
  "artifact": {
    "unstrippedSha256": "11251374204a3fbbef441d16ce75888b12ac719cfe4a7fd056c7709c2d6f631c",
    "sha256": "3ce001732d9ac209e199a7107657161a88233b6147c9c77231cbfe6f847fedfa",
    "size": 1162760,
    "elfClass": true,
    "machine": true,
    "type": true,
    "interpreter": "/system/bin/linker64",
    "needed": [
      "libc.so",
      "libdl.so"
    ]
  },
  "strippedPath": "manager/build/moduleTools/native/maplesu-tools"
}

> Task :manager:packageMapleSuRuntime
> Task :manager:preBuild UP-TO-DATE
> Task :manager:preReleaseBuild UP-TO-DATE
> Task :manager:mergeReleaseJniLibFolders
> Task :manager:mergeReleaseNativeLibs
> Task :manager:checkReleaseDuplicateClasses
> Task :manager:stripReleaseDebugSymbols
> Task :manager:generateReleaseBuildConfig
> Task :manager:protobufDummy UP-TO-DATE
> Task :manager:extractReleaseNativeSymbolTables
> Task :manager:extractIncludeReleaseProto
> Task :manager:extractProto
> Task :manager:extractReleaseProto
> Task :manager:mergeReleaseNativeDebugMetadata
> Task :manager:compileReleaseAidl
> Task :manager:generateReleaseProto
> Task :manager:generateReleaseResValues
> Task :manager:extractReleaseSupportedLocales
> Task :manager:mapReleaseSourceSetPaths
> Task :manager:generateReleaseResources
> Task :manager:generateReleaseLocaleConfig
> Task :manager:processReleaseNavigationResources
> Task :manager:packageReleaseResources
> Task :manager:javaPreCompileRelease FROM-CACHE
> Task :manager:parseReleaseLocalResources
> Task :manager:mergeReleaseArtProfile
> Task :manager:generateReleaseRFile
> Task :manager:checkReleaseAarMetadata
> Task :manager:compileReleaseNavigationResources
> Task :manager:createReleaseCompatibleScreenManifests
> Task :manager:extractDeepLinksRelease
> Task :manager:processReleaseMainManifest
> Task :manager:processReleaseManifest
> Task :manager:extractProguardFiles
> Task :manager:mergeReleaseStartupProfile
> Task :manager:generateReleaseAssets UP-TO-DATE

> Task :manager:packagePolicyHooks
  [kcfi] every prefix already equals this image's compare sites
{
  "passed": true,
  "scope": "image-derived sidecar ELF/CFI build only; not installed or activated",
  "kernelRelease": "6.1.25-android14-11-o-gf12b379cb280",
  "buildId": "b9991b90faeb15a9305fd19c707e70b9c301058a",
  "controlAbi": 2,
  "imageSha256": "71c55accaab6932e073f46ed1877923c5edd165f7236813ee33aab92c7d3bc46",
  "facts": {
    "MSU_PH_PAGE_BYTES": 4096,
    "MSU_PH_KPROBE_SIZE": 128,
    "MSU_PH_KP_ADDR": 40,
    "MSU_PH_KP_NAME": 48,
    "MSU_PH_KP_PRE": 64,
    "MSU_PH_REGS_PC": 256,
    "MSU_PH_PROC_OPS_SIZE": 96,
    "MSU_PH_PROC_IOCTL": 64,
    "MSU_PH_EXECMEM_MODULE_TEXT": 0
  },
  "callbacks": {
    "msu_policy_pre": "0xa6be5dd9",
    "msu_policy_ioctl": "0xe01408cd"
  },
  "module": {
    "path": "/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/build/policyHookBackend/0/maplesu_policy_hook.ko",
    "sha256": "d0c7967e6a1cc43fbf71d344677a203673ff8e83abf2aee1e0fd4a45f596e68f",
    "bytes": 38568
  },
  "deviceAccess": false,
  "installed": false,
  "fullPolicyHidingAcceptance": false
}

> Task :manager:mergeReleaseResources

> Task :manager:packagePolicyHooks
  [kcfi] every prefix already equals this image's compare sites
{
  "passed": true,
  "scope": "image-derived sidecar ELF/CFI build only; not installed or activated",
  "kernelRelease": "6.6.89-android15-8-g7e1f3c083cc6-abogki467167594-4k",
  "buildId": "dd2cf7af96b056206a703b1de7bbe4bc5fd43e0d",
  "controlAbi": 2,
  "imageSha256": "346d51ea1f63413ffa5d99c5c426806291af3573f0a1d66a7621c388e835880e",
  "facts": {
    "MSU_PH_PAGE_BYTES": 4096,
    "MSU_PH_KPROBE_SIZE": 128,
    "MSU_PH_KP_ADDR": 40,
    "MSU_PH_KP_NAME": 48,
    "MSU_PH_KP_PRE": 64,
    "MSU_PH_REGS_PC": 256,
    "MSU_PH_PROC_OPS_SIZE": 96,
    "MSU_PH_PROC_IOCTL": 64,
    "MSU_PH_EXECMEM_MODULE_TEXT": 0
  },
  "callbacks": {
    "msu_policy_pre": "0xa6be5dd9",
    "msu_policy_ioctl": "0xe01408cd"
  },
  "module": {
    "path": "/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/build/policyHookBackend/1/maplesu_policy_hook.ko",
    "sha256": "f793e8b06910498e522602dd5ac65110bc273005c8e4240db1cf49afec6a9153",
    "bytes": 39032
  },
  "deviceAccess": false,
  "installed": false,
  "fullPolicyHidingAcceptance": false
}
  [kcfi] init_module     0x36b1c5a6 -> 0x6fbb3035 (image compare site)
  [kcfi] cleanup_module  0xa540670c -> 0xe5c47d60 (image compare site)
  [kcfi] msu_policy_pre  0xa6be5dd9 -> 0xc073bc77 (image compare site)
  [kcfi] msu_policy_ioctl 0xe01408cd -> 0x2af6cdbb (image compare site)
{
  "passed": true,
  "scope": "image-derived sidecar ELF/CFI build only; not installed or activated",
  "kernelRelease": "6.12.58-android16-6-g376529f3e739-ab15072794-4k",
  "buildId": "2c5cbae8a262025cafc6a8318c7e8e2677b44990",
  "controlAbi": 2,
  "imageSha256": "6679e3fbc59c802e22e35c4ef87eefe5c0e7d0e79e37e294ef58324d457e50fb",
  "facts": {
    "MSU_PH_PAGE_BYTES": 4096,
    "MSU_PH_KPROBE_SIZE": 128,
    "MSU_PH_KP_ADDR": 40,
    "MSU_PH_KP_NAME": 48,
    "MSU_PH_KP_PRE": 64,
    "MSU_PH_REGS_PC": 256,
    "MSU_PH_PROC_OPS_SIZE": 96,
    "MSU_PH_PROC_IOCTL": 64,
    "MSU_PH_EXECMEM_MODULE_TEXT": 0
  },
  "callbacks": {
    "msu_policy_pre": "0xc073bc77",
    "msu_policy_ioctl": "0x2af6cdbb"
  },
  "module": {
    "path": "/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/build/policyHookBackend/2/maplesu_policy_hook.ko",
    "sha256": "5e4527bca2dee3962d2a5405bfdca6c843fae5403ae1cc0f36222c79d700e6b2",
    "bytes": 39080
  },
  "deviceAccess": false,
  "installed": false,
  "fullPolicyHidingAcceptance": false
}
{
  "schemaVersion": 1,
  "controlAbi": 2,
  "generatedAt": "2026-11-26T09:59:14.996958+00:00",
  "images": [
    {
      "asset": "maplesu/policy-hook/b9991b90faeb15a9305fd19c707e70b9c301058a.ko",
      "sha256": "d0c7967e6a1cc43fbf71d344677a203673ff8e83abf2aee1e0fd4a45f596e68f",
      "bytes": 38568,
      "buildId": "b9991b90faeb15a9305fd19c707e70b9c301058a",
      "kernelRelease": "6.1.25-android14-11-o-gf12b379cb280",
      "pageSize": 4096
    },
    {
      "asset": "maplesu/policy-hook/dd2cf7af96b056206a703b1de7bbe4bc5fd43e0d.ko",
      "sha256": "f793e8b06910498e522602dd5ac65110bc273005c8e4240db1cf49afec6a9153",
      "bytes": 39032,
      "buildId": "dd2cf7af96b056206a703b1de7bbe4bc5fd43e0d",
      "kernelRelease": "6.6.89-android15-8-g7e1f3c083cc6-abogki467167594-4k",
      "pageSize": 4096
    },
    {
      "asset": "maplesu/policy-hook/2c5cbae8a262025cafc6a8318c7e8e2677b44990.ko",
      "sha256": "5e4527bca2dee3962d2a5405bfdca6c843fae5403ae1cc0f36222c79d700e6b2",
      "bytes": 39080,
      "buildId": "2c5cbae8a262025cafc6a8318c7e8e2677b44990",
      "kernelRelease": "6.12.58-android16-6-g376529f3e739-ab15072794-4k",
      "pageSize": 4096
    }
  ]
}

> Task :manager:mergeReleaseAssets FAILED
> Task :manager:processReleaseManifestForPackage
> Task :manager:compileReleaseKotlin
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/src/main/java/com/maplesu/core/theme/ThemeDocument.kt:52:17 'when' expression over a subject of type 'Any?' is not exhaustive. Add a 'null' or 'else' branch.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/src/main/java/com/maplesu/core/theme/ThemeStore.kt:154:54 Unnecessary safe call on a non-null receiver of type 'JSONObject'.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/src/main/java/com/maplesu/core/ui/component/material/SegmentedSettingsItems.kt:62:17 'fun Slider(value: Float, onValueChange: (Float) -> Unit, modifier: Modifier = ..., enabled: Boolean = ..., valueRange: ClosedFloatingPointRange<Float> = ..., steps: Int = ..., onValueChangeFinished: (() -> Unit)? = ..., colors: SliderColors = ..., interactionSource: MutableInteractionSource = ...): Unit' is deprecated. Use the Slider overload that accepts SliderState, onValueChange, and onValueChangeFinished instead.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/src/main/java/com/maplesu/core/ui/screen/host/HiddenFlowComponents.kt:135:58 'fun InputField(query: String, onQueryChange: (String) -> Unit, onSearch: (String) -> Unit, expanded: Boolean, onExpandedChange: (Boolean) -> Unit, modifier: Modifier = ..., enabled: Boolean = ..., placeholder: ComposableFunction0<Unit>? = ..., leadingIcon: ComposableFunction0<Unit>? = ..., trailingIcon: ComposableFunction0<Unit>? = ..., colors: TextFieldColors = ..., interactionSource: MutableInteractionSource? = ...): Unit' is deprecated. Use SearchBarDefaults.InputField with TextFieldState and SearchBarState.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/src/main/java/com/maplesu/core/ui/screen/install/InstallSteps.kt:246:21 'fun ListItem(headlineContent: ComposableFunction0<Unit>, modifier: Modifier = ..., overlineContent: ComposableFunction0<Unit>? = ..., supportingContent: ComposableFunction0<Unit>? = ..., leadingContent: ComposableFunction0<Unit>? = ..., trailingContent: ComposableFunction0<Unit>? = ..., colors: ListItemColors = ..., tonalElevation: Dp = ..., shadowElevation: Dp = ...): Unit' is deprecated. Use the overload where `headlineContent` is now a trailing `content` lambda.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/src/main/java/com/maplesu/core/ui/screen/settings/ThemeComponents.kt:189:59 'fun Slider(value: Float, onValueChange: (Float) -> Unit, modifier: Modifier = ..., enabled: Boolean = ..., valueRange: ClosedFloatingPointRange<Float> = ..., steps: Int = ..., onValueChangeFinished: (() -> Unit)? = ..., colors: SliderColors = ..., interactionSource: MutableInteractionSource = ...): Unit' is deprecated. Use the Slider overload that accepts SliderState, onValueChange, and onValueChangeFinished instead.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/src/main/java/com/maplesu/core/ui/util/KsuCli.kt:694:87 Unnecessary safe call on a non-null receiver of type 'JSONObject'.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/src/main/java/com/maplesu/core/ui/util/KsuCli.kt:1660:21 Unnecessary safe call on a non-null receiver of type 'InstallerSnapshot'.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/src/main/java/com/maplesu/core/ui/viewmodel/HomeViewModel.kt:286:77 Unnecessary safe call on a non-null receiver of type 'Throwable'.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/src/main/java/com/maplesu/core/ui/webui/ModuleWebOrigin.kt:6:37 Non-public primary constructor is exposed via the generated 'copy()' method of the 'data' class.

The generated 'copy()' will change its visibility in future releases.

To suppress the warning do one of the following:
- Annotate the data class with the '@ConsistentCopyVisibility' annotation.
- Use the '-Xconsistent-data-class-copy-visibility' compiler flag.
- Annotate the data class with the '@ExposedCopyVisibility' annotation 
  (Discouraged, but can be used to keep binary compatibility).

To learn more, see the documentation of the '@ConsistentCopyVisibility' and '@ExposedCopyVisibility' annotations.

This will become an error in language version 2.5. See https://youtrack.jetbrains.com/issue/KT-11914.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/src/main/java/dev/maplesu/manager/installer/InstallerServiceClient.kt:466:32 Unnecessary safe call on a non-null receiver of type 'ClientResult'.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/src/main/java/dev/maplesu/manager/installer/InstallerServiceClient.kt:467:29 Unnecessary safe call on a non-null receiver of type 'ClientResult'.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/src/main/java/dev/maplesu/manager/installer/NativeInstallTransaction.kt:197:68 Java type mismatch: inferred type is 'String?', but 'String' was expected.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/src/main/java/dev/maplesu/manager/installer/StockRestoreTargets.kt:133:17 Condition is always 'true'.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/src/main/java/dev/maplesu/manager/jailbreak/GhostlockHandover.kt:98:29 Unnecessary non-null assertion (!!) on a non-null receiver of type 'String'.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/src/main/java/dev/maplesu/manager/jailbreak/GhostlockHandover.kt:100:49 Unnecessary non-null assertion (!!) on a non-null receiver of type 'String'.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/src/main/java/dev/maplesu/manager/jailbreak/IrImages.kt:428:44 'static field CPU_ABI: String!' is deprecated. Deprecated in Java.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/src/main/java/dev/maplesu/manager/jailbreak/JailbreakLogActions.kt:124:26 'fun rememberModalBottomSheetState(skipPartiallyExpanded: Boolean = ..., confirmValueChange: (SheetValue) -> Boolean = ...): SheetState' is deprecated. Use rememberBottomSheetState with Hidden initial value.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/src/main/java/dev/maplesu/manager/market/MapleMarketRepository.kt:207:48 The corresponding parameter in the supertype 'Callback' is named 'e'. This may cause problems when calling this function with named arguments.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/src/main/java/dev/maplesu/manager/modules/LiteScriptModuleBackend.kt:1402:17 Only safe (?.) or non-null asserted (!!.) calls are allowed on a nullable receiver of type 'File?'.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/src/main/java/dev/maplesu/manager/modules/MapleSuModuleBackend.kt:709:30 Only safe (?.) or non-null asserted (!!.) calls are allowed on a nullable receiver of type 'File?'.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/src/main/java/dev/maplesu/manager/modules/compat/UltraModuleInstallTransaction.kt:339:29 Unnecessary safe call on a non-null receiver of type 'JSONObject'.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/src/main/java/dev/maplesu/manager/modules/compat/UltraModuleInstallTransaction.kt:339:77 Unnecessary safe call on a non-null receiver of type 'JSONObject'.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/src/main/java/dev/maplesu/manager/runtime/MapleSuSupervisedProcess.kt:49:40 Return in function with expression body and without explicit return type. Use block body '{...}' or add an explicit return type. This will become an error in language version 2.5. See https://youtrack.jetbrains.com/issue/KTLC-288.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/src/main/java/dev/maplesu/manager/runtime/MapleSuSupervisedProcess.kt:51:52 Return in function with expression body and without explicit return type. Use block body '{...}' or add an explicit return type. This will become an error in language version 2.5. See https://youtrack.jetbrains.com/issue/KTLC-288.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/src/main/java/dev/maplesu/manager/runtime/MapleSuSupervisedProcess.kt:58:22 Return in function with expression body and without explicit return type. Use block body '{...}' or add an explicit return type. This will become an error in language version 2.5. See https://youtrack.jetbrains.com/issue/KTLC-288.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/src/main/java/dev/maplesu/manager/runtime/NativeSessionProcess.kt:100:25 Return in function with expression body and without explicit return type. Use block body '{...}' or add an explicit return type. This will become an error in language version 2.5. See https://youtrack.jetbrains.com/issue/KTLC-288.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/src/main/java/dev/maplesu/manager/runtime/NativeSuDirectory.kt:195:25 Condition is always 'false'.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/src/main/java/dev/maplesu/manager/runtime/NativeSuDirectory.kt:292:21 Condition is always 'false'.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/src/main/java/dev/maplesu/manager/runtime/NativeSuDirectoryProvider.kt:542:54 Unnecessary safe call on a non-null receiver of type 'Bundle'.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/src/main/java/dev/maplesu/manager/runtime/NativeSuDirectoryProvider.kt:850:25 Unnecessary safe call on a non-null receiver of type 'JailbreakStatus'.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/src/main/java/dev/maplesu/manager/runtime/RuntimeDeployment.kt:425:13 Condition is always 'true'.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/src/main/java/dev/maplesu/manager/runtime/SuPathWiring.kt:193:69 Java type mismatch: inferred type is 'String?', but 'String' was expected.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/src/main/java/dev/maplesu/manager/runtime/ultra/ManagerOwnerRootResult.kt:28:58 'when' expression over a subject of type 'Any?' is not exhaustive. Add a 'null' or 'else' branch.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/src/main/java/dev/maplesu/manager/runtime/ultra/RootStatusReport.kt:8:59 'when' expression over a subject of type 'Any?' is not exhaustive. Add a 'null' or 'else' branch.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/src/main/java/dev/maplesu/manager/runtime/ultra/UltraAuthorizationResult.kt:32:13 'when' expression over a subject of type 'Any?' is not exhaustive. Add a 'null' or 'else' branch.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/src/main/java/dev/maplesu/manager/runtime/ultra/UltraEnvironmentIdentity.kt:413:70 'when' expression over a subject of type 'Any?' is not exhaustive. Add a 'null' or 'else' branch.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/src/main/java/dev/maplesu/manager/runtime/ultra/UltraEnvironmentInstaller.kt:449:57 'val id: Long' is deprecated. Deprecated in Java.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/src/main/java/dev/maplesu/manager/runtime/ultra/UltraEnvironmentProbe.kt:264:13 Condition is always 'true'.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/src/main/java/dev/maplesu/manager/runtime/ultra/UltraIdentityBroker.kt:99:52 Unnecessary safe call on a non-null receiver of type 'AuthorizationSnapshot'.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/src/main/java/dev/maplesu/manager/runtime/ultra/UltraReceipt.kt:75:24 'when' expression over a subject of type 'Any?' is not exhaustive. Add a 'null' or 'else' branch.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/src/main/java/dev/maplesu/manager/runtime/ultra/UltraRuntimeClient.kt:458:53 Unnecessary non-null assertion (!!) on a non-null receiver of type 'JSONObject'.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/src/main/java/dev/maplesu/manager/runtime/ultra/UltraRuntimeClient.kt:460:59 Unnecessary non-null assertion (!!) on a non-null receiver of type 'JSONObject'.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/src/main/java/dev/maplesu/manager/runtime/ultra/UltraRuntimeClient.kt:556:59 'when' expression over a subject of type 'Any?' is not exhaustive. Add a 'null' or 'else' branch.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/src/main/java/dev/maplesu/manager/runtime/ultra/UltraRuntimeClient.kt:592:21 Unnecessary safe call on a non-null receiver of type 'JSONObject'.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/src/main/java/dev/maplesu/manager/ultrakernel/UltraInitBootAssets.kt:68:45 Only safe (?.) or non-null asserted (!!.) calls are allowed on a nullable receiver of type 'File?'.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/src/main/java/dev/maplesu/manager/ultrakernel/UltraInitBootTargetResolver.kt:277:20 Only safe (?.) or non-null asserted (!!.) calls are allowed on a nullable receiver of type 'File?'.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/src/main/java/dev/maplesu/manager/ultrakernel/UltraInitBootTargetResolver.kt:303:42 Only safe (?.) or non-null asserted (!!.) calls are allowed on a nullable receiver of type 'File?'.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/src/main/java/dev/maplesu/manager/ultrakernel/UltraInitBootTargetResolver.kt:390:24 Only safe (?.) or non-null asserted (!!.) calls are allowed on a nullable receiver of type 'File?'.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/src/main/java/dev/maplesu/manager/ultrakernel/UltraInitBootTargetResolver.kt:420:20 Only safe (?.) or non-null asserted (!!.) calls are allowed on a nullable receiver of type 'File?'.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/src/main/java/dev/maplesu/manager/ultrakernel/UltraInitBootTargetResolver.kt:447:20 Only safe (?.) or non-null asserted (!!.) calls are allowed on a nullable receiver of type 'File?'.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/src/main/java/dev/maplesu/manager/ultrakernel/UltraInitBootTargetResolver.kt:510:20 Only safe (?.) or non-null asserted (!!.) calls are allowed on a nullable receiver of type 'File?'.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/src/main/java/dev/maplesu/manager/ultrakernel/UltraKernelBuilder.kt:593:24 Redundant creation of Json format. Creating instances for each use can be slow.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/src/main/java/dev/maplesu/manager/ultrakernel/UltraKernelRecipe.kt:644:38 Redundant call of conversion method.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/src/main/java/dev/maplesu/manager/ultrakernel/UltraKernelResidentAbi.kt:191:113 Unnecessary non-null assertion (!!) on a non-null receiver of type 'String'.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/src/main/java/dev/maplesu/manager/ultrakernel/UltraKernelResidentAbi.kt:916:67 Unnecessary non-null assertion (!!) on a non-null receiver of type 'Boolean'.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/src/main/java/dev/maplesu/manager/ultrakernel/UltraKernelShellcode.kt:1023:36 Unnecessary non-null assertion (!!) on a non-null receiver of type 'Int'.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/src/main/java/dev/maplesu/manager/ultrakernel/UltraKernelShellcode.kt:1103:71 Unnecessary non-null assertion (!!) on a non-null receiver of type 'UltraKernelStructOffsets.ObjectValue'.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/src/main/java/dev/maplesu/manager/ultrakernel/UltraKernelShellcode.kt:2312:71 Cast is redundant.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/src/main/java/dev/maplesu/manager/ultrakernel/UltraKernelShellcode.kt:2313:72 Cast is redundant.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/src/main/java/dev/maplesu/manager/ultrakernel/UltraKernelShellcode.kt:2316:41 Cast is redundant.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/src/main/java/dev/maplesu/manager/ultrakernel/UltraKernelShellcode.kt:2316:86 Cast is redundant.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/src/main/java/dev/maplesu/manager/workmode/detect/ModeDetector.kt:137:66 Unnecessary non-null assertion (!!) on a non-null receiver of type 'RootChannelKind'.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/src/main/java/dev/maplesu/manager/workmode/migration/HostMigrationFacade.kt:66:33 Cast is redundant.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/src/main/java/dev/maplesu/manager/workmode/migration/MigrationDetector.kt:109:37 Unnecessary safe call on a non-null receiver of type 'FileFact'.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/src/main/java/dev/maplesu/manager/workmode/recovery/RecoveryDecision.kt:203:28 Condition is always 'true'.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/src/main/java/dev/maplesu/manager/workmode/service/ModeSwitchProgress.kt:92:17 Only safe (?.) or non-null asserted (!!.) calls are allowed on a nullable receiver of type 'File?'.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/src/main/java/dev/maplesu/manager/workmode/service/RootShellControlPlane.kt:117:33 Only safe (?.) or non-null asserted (!!.) calls are allowed on a nullable receiver of type 'File?'.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/src/main/java/dev/maplesu/manager/workmode/snapshot/ControlPlaneModeSwitchSnapshots.kt:168:17 'when' is exhaustive so 'else' is redundant here.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/src/main/java/dev/maplesu/manager/workmode/storage/FileMoveExecutor.kt:168:37 Only safe (?.) or non-null asserted (!!.) calls are allowed on a nullable receiver of type 'File?'.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/src/main/java/dev/maplesu/manager/workmode/storage/FileMoveExecutor.kt:170:45 Java type mismatch: inferred type is 'File?', but 'File' was expected.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/src/main/java/dev/maplesu/manager/workmode/superuser/LiteImplantBackup.kt:60:46 Java type mismatch: inferred type is 'String?', but 'String' was expected.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/src/main/java/dev/maplesu/manager/workmode/superuser/LiteImplantBackup.kt:61:48 Java type mismatch: inferred type is 'String?', but 'String' was expected.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/src/main/java/dev/maplesu/manager/workmode/superuser/LiteImplantBackup.kt:62:47 Java type mismatch: inferred type is 'String?', but 'String' was expected.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/src/main/java/dev/maplesu/manager/workmode/ui/LiteHiddenViewModel.kt:445:43 Unnecessary safe call on a non-null receiver of type 'HiddenDeactivateResult'.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/src/main/java/dev/maplesu/manager/workmode/ui/RecoveryMaterial.kt:77:31 Unnecessary safe call on a non-null receiver of type 'RecoveryDecision'.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/src/main/java/dev/maplesu/manager/workmode/ui/RecoveryMiuix.kt:82:31 Unnecessary safe call on a non-null receiver of type 'RecoveryDecision'.
w: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/src/main/java/dev/maplesu/manager/workmode/ui/WorkModeSheetMaterial.kt:110:22 'fun rememberModalBottomSheetState(skipPartiallyExpanded: Boolean = ..., confirmValueChange: (SheetValue) -> Boolean = ...): SheetState' is deprecated. Use rememberBottomSheetState with Hidden initial value.

[Incubating] Problems report is available at: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/build/reports/problems/problems-report.html

FAILURE: Build failed with an exception.

* What went wrong:
Execution failed for task ':manager:mergeReleaseAssets' (registered by plugin 'com.android.internal.application').
> ULTRA_CLAIM_FRESH_GENERATION_REQUIRED

* Try:
> Run with --stacktrace option to get the stack trace.
> Run with --info or --debug option to get more log output.
> Run with --scan to get full insights from a Build Scan (powered by Develocity).
> Get more help at https://help.gradle.org.

Deprecated Gradle features were used in this build, making it incompatible with Gradle 10.

You can use '--warning-mode all' to show the individual deprecation warnings and determine if they come from your own scripts or plugins.

For more on this, please refer to https://docs.gradle.org/9.8.1/userguide/command_line_interface.html#sec:command_line_warnings in the Gradle documentation.

BUILD FAILED in 8m 56s
88 actionable tasks: 87 executed, 1 from cache
```
