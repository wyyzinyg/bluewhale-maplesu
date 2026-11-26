# 构建结果

- run: 27  提交: 9d0ea38f0357bf66bde4374157b9a86a80b499a6
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
改好 build.gradle.kts: runtime 只构建发布所需目标（跳过 ultra 探针）
改好 product.py: cached_jar 缺缓存时从 Maven 补拉

#### gradle 失败原因
2183:ld.lld: error: undefined symbol: kernel_module::maplesu_request_auth_state()
2192:ld.lld: error: undefined symbol: kernel_module::maplesu_request_set_auth_mode(kernel_module::RequestAuthMode)
2201:ld.lld: error: undefined symbol: kernel_module::CleanupReceiptScope::CleanupReceiptScope()
2210:ld.lld: error: undefined symbol: kernel_module::CleanupReceiptScope::~CleanupReceiptScope()
2219:ld.lld: error: undefined symbol: maplesu::sdk::install_maplesu_environment(char const*, maplesu::sdk::InstallMode, maplesu::sdk::InstallConfig const&)
2223:ld.lld: error: undefined symbol: maplesu::sdk::get_sdk_version()
2229:ld.lld: error: undefined hidden symbol: maplesu::storage::StorageScope::~StorageScope()
2238:ld.lld: error: undefined symbol: kernel_module::maplesu_request_owner_lifetime_capture(kernel_module::RequestOwnerLifetimeToken&)
2242:ld.lld: error: undefined symbol: kernel_module::maplesu_request_owner_close()
2251:ld.lld: error: undefined symbol: kernel_module::maplesu_request_helper_open()
2255:ld.lld: error: undefined symbol: kernel_module::maplesu_request_owner_deployment(kernel_module::RequestDeploymentNamespace&)
2261:ld.lld: error: undefined symbol: kernel_module::maplesu_request_owner_binding_matches(kernel_module::RequestOwnerBinding const&)
2267:ld.lld: error: undefined symbol: maplesu::sdk::uninstall_maplesu_environment(char const*)
2271:ld.lld: error: undefined hidden symbol: maplesu::storage::current_kernel_directory(std::__ndk1::basic_string<char, std::__ndk1::char_traits<char>, std::__ndk1::allocator<char>>&)
2275:ld.lld: error: undefined symbol: maplesu::sdk::get_maplesu_environment_state(char const*)
2279:ld.lld: error: undefined hidden symbol: maplesu::storage::StorageScope::StorageScope(maplesu::storage::StorageLocator const&, char const*)
2283:ld.lld: error: undefined symbol: maplesu::sdk::get_installed_maplesu_environment_version(char const*, maplesu::sdk::MapleSUSdkVersion&)
2287:ld.lld: error: undefined symbol: maplesu::sdk::get_root_status_report(char const*)
2291:ld.lld: error: undefined hidden symbol: maplesu::sdk::current_root_status_result()
2295:ld.lld: error: undefined symbol: maplesu::sdk::run_root_cmd(char const*, char const*, std::__ndk1::basic_string<char, std::__ndk1::char_traits<char>, std::__ndk1::allocator<char>>&)
2299:ld.lld: error: too many errors emitted, stopping now (use --error-limit=0 to see all errors)
2300:clang++: error: linker command failed with exit code 1 (use -v to see invocation)
2303:> Task :manager:buildMapleSuRuntime FAILED
2307:FAILURE: Build failed with an exception.
2309:* What went wrong:
2310:Execution failed for task ':manager:buildMapleSuRuntime' (registered in build file 'manager/build.gradle.kts').

#### CMake 错误日志
--- src/manager/build/jailbreakProviders/build/CMakeFiles/CMakeOutput.log
    arg [cmTC_80b32] ==> ignore
    arg [/usr/local/lib/android/sdk/ndk/28.2.13676358/toolchains/llvm/prebuilt/linux-x86_64/sysroot/usr/lib/aarch64-linux-android/31/crtbegin_dynamic.o] ==> obj [/usr/local/lib/android/sdk/ndk/28.2.13676358/toolchains/llvm/prebuilt/linux-x86_64/sysroot/usr/lib/aarch64-linux-android/31/crtbegin_dynamic.o]
    arg [-L/usr/local/lib/android/sdk/ndk/28.2.13676358/toolchains/llvm/prebuilt/linux-x86_64/lib/clang/19/lib/linux/aarch64] ==> dir [/usr/local/lib/android/sdk/ndk/28.2.13676358/toolchains/llvm/prebuilt/linux-x86_64/lib/clang/19/lib/linux/aarch64]
    arg [-L/usr/local/lib/android/sdk/ndk/28.2.13676358/toolchains/llvm/prebuilt/linux-x86_64/sysroot/usr/lib/aarch64-linux-android/31] ==> dir [/usr/local/lib/android/sdk/ndk/28.2.13676358/toolchains/llvm/prebuilt/linux-x86_64/sysroot/usr/lib/aarch64-linux-android/31]
    arg [-L/usr/local/lib/android/sdk/ndk/28.2.13676358/toolchains/llvm/prebuilt/linux-x86_64/sysroot/usr/lib/aarch64-linux-android] ==> dir [/usr/local/lib/android/sdk/ndk/28.2.13676358/toolchains/llvm/prebuilt/linux-x86_64/sysroot/usr/lib/aarch64-linux-android]
    arg [-L/usr/local/lib/android/sdk/ndk/28.2.13676358/toolchains/llvm/prebuilt/linux-x86_64/sysroot/usr/lib] ==> dir [/usr/local/lib/android/sdk/ndk/28.2.13676358/toolchains/llvm/prebuilt/linux-x86_64/sysroot/usr/lib]
    arg [--build-id=sha1] ==> ignore
    arg [--no-undefined-version] ==> ignore
    arg [--fatal-warnings] ==> ignore
    arg [--no-undefined] ==> ignore
    arg [CMakeFiles/cmTC_80b32.dir/CMakeCXXCompilerABI.cpp.o] ==> ignore
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
   Compiling alloc-stdlib v0.2.4
   Compiling tempfile v3.27.0
   Compiling anstyle-parse v1.0.0
   Compiling regex v1.13.1
   Compiling prost-types v0.14.4
   Compiling serde_derive v1.0.229
   Compiling lzma-sys v0.1.20
   Compiling multimap v0.10.1
   Compiling protoc-bin-vendored-linux-x86_32 v3.2.0
   Compiling radium v0.7.0
   Compiling zmij v1.0.23
   Compiling is_terminal_polyfill v1.70.2
   Compiling protoc-bin-vendored-linux-x86_64 v3.2.0
   Compiling zstd-safe v7.3.0
   Compiling protoc-bin-vendored-linux-aarch_64 v3.2.0
   Compiling anstyle v1.0.14
   Compiling colorchoice v1.0.5
   Compiling protoc-bin-vendored-macos-aarch_64 v3.2.0
   Compiling protoc-bin-vendored-linux-ppcle_64 v3.2.0
   Compiling portable-atomic v1.15.0
   Compiling protoc-bin-vendored-macos-x86_64 v3.2.0
   Compiling anstyle-query v1.1.5
   Compiling log v0.4.34
   Compiling protoc-bin-vendored-linux-s390_64 v3.2.0
   Compiling protoc-bin-vendored-win32 v3.2.0
   Compiling prost-build v0.14.4
   Compiling protoc-bin-vendored v3.2.0
   Compiling anstream v1.0.0
   Compiling terminal_size v0.4.4
   Compiling brotli-decompressor v5.0.3
   Compiling crypto-common v0.2.2
   Compiling block-buffer v0.12.1
   Compiling unicode-width v0.2.2
   Compiling thiserror v2.0.20
   Compiling serde_json v1.0.151
   Compiling clap_lex v1.1.1
   Compiling tap v1.0.1
   Compiling strsim v0.11.1
   Compiling libbz2-rs-sys v0.2.5
   Compiling bzip2 v0.6.1
   Compiling clap_builder v4.6.7
   Compiling wyz v0.5.1
   Compiling console v0.16.6
   Compiling rayon v1.12.0
   Compiling digest v0.11.3
   Compiling brotli v8.0.4
   Compiling payload-extract v0.1.1 (/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/jailbreak-providers/ghostlock/extractor-native/vendor/payload-extract)
   Compiling aho-corasick v1.1.5
   Compiling clap_derive v4.6.7
   Compiling thiserror-impl v2.0.20
   Compiling cpufeatures v0.3.1
   Compiling adler2 v2.0.1
   Compiling unit-prefix v0.5.2
   Compiling itoa v1.0.18
   Compiling typed-path v0.12.3
   Compiling simd-adler32 v0.3.10
   Compiling funty v2.0.0
   Compiling miniz_oxide v0.9.1
   Compiling bitvec v1.1.1
   Compiling zip v8.6.0
   Compiling indicatif v0.18.6
   Compiling clap v4.6.7
   Compiling sha2 v0.11.0
   Compiling zstd v0.13.3
   Compiling xz2 v0.1.7
   Compiling bsdiff-android v0.0.2
   Compiling yaxpeax-arch v0.3.2
   Compiling memmap2 v0.9.11
   Compiling lz4_flex v0.14.0
   Compiling hex v0.4.3
   Compiling yaxpeax-arm v0.5.0
   Compiling flate2 v1.1.10
   Compiling ghostlock-extract v0.1.0 (/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/jailbreak-providers/ghostlock/extractor-native)
    Finished `release` profile [optimized] target(s) in 51.24s
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
          "decodedSha256": "e2096ce9903a7ab804f15faefeeb955730259bde9f96d0fbd53de7efcef190ca",
          "decodedBytes": 88136
        }
      },
      {
        "id": "plant-61258-690108013dcc",
        "engine": "plant",
        "releases": [
          "6.12.58-android16-6-g690108013dcc-abogki576129896-4k"
        ],
        "variant": "CVE-2026-98260-6.12.58",
        "kmi": "android16-6.12",
        "kernelUapi": 6,
        "pageSize": "4k",
        "models": [
          "vivo",
          "iQOO"
        ],
        "payloadKey": "plant-61258-690108013dcc",
        "kernelRelease": "6.12.58-android16-6-g690108013dcc-abogki576129896-4k",
        "runner": "plant-61258",
        "runnerFile": {
          "asset": "maplesu-93260/plant/plant-61258",
          "sha256": "e2096ce9903a7ab804f15faefeeb955730259bde9f96d0fbd53de7efcef190ca",
          "bytes": 88136,
          "gzip": false,
          "decodedSha256": "e2096ce9903a7ab804f15faefeeb955730259bde9f96d0fbd53de7efcef190ca",
          "decodedBytes": 88136
        }
      },
      {
        "id": "plant-61223-41f4cb1fa7c7",
        "engine": "plant",
        "releases": [
          "6.12.23-android16-5-g41f4cb1fa7c7-abogki465038634-4k"
        ],
        "variant": "CVE-2026-98260-vivo-6.12.23",
        "kmi": "android16-6.12",
        "kernelUapi": 6,
        "pageSize": "4k",
        "models": [
          "vivo V2505A",
          "iQOO"
        ],
        "payloadKey": "plant-61223-41f4cb1fa7c7",
        "kernelRelease": "6.12.23-android16-5-g41f4cb1fa7c7-abogki465038634-4k",
        "runner": "plant-61223",
        "runnerFile": {
          "asset": "maplesu-93260/plant/plant-61223",
          "sha256": "f492283c410e7a421cee83a043eee770d727b83d921c1eb6d5670500f0ef4b18",
          "bytes": 47208,
          "gzip": false,
          "decodedSha256": "f492283c410e7a421cee83a043eee770d727b83d921c1eb6d5670500f0ef4b18",
          "decodedBytes": 47208
        }
      },
      {
        "id": "plant-66118-9bc34d5b0c79",
        "engine": "plant",
        "releases": [
          "6.6.118-android15-8-g9bc34d5b0c79-abogki537459655-4k"
        ],
        "variant": "CVE-2026-98260-6.6.118",
        "kmi": "android15-6.6",
        "kernelUapi": 6,
        "pageSize": "4k",
        "models": [
          "PLQ110",
          "OnePlus Ace6",
          "PKR110",
          "OnePlus Ace5 Pro",
          "PKJ110",
          "OPPO Find X8 Ultra",
          "RMX6699",
          "Realme GT8",
          "PLE110",
          "OPPO K13 Turbo Pro"
        ],
        "payloadKey": "plant-66118-9bc34d5b0c79",
        "kernelRelease": "6.6.118-android15-8-g9bc34d5b0c79-abogki537459655-4k",
        "runner": "plant-66118",
        "runnerFile": {
          "asset": "maplesu-93260/plant/plant-66118",
          "sha256": "4f12224e267aa5de874445de54a1416a0e487e9436937a0e69b9f43bd13368b8",
          "bytes": 47544,
          "gzip": false,
          "decodedSha256": "4f12224e267aa5de874445de54a1416a0e487e9436937a0e69b9f43bd13368b8",
          "decodedBytes": 47544
        }
      },
      {
        "id": "plant-66118-c4127a25dcf3",
        "engine": "plant",
        "releases": [
          "6.6.118-android15-8-gc4127a25dcf3-ab15863337-4k"
        ],
        "variant": "CVE-2026-98260-6.6.118",
        "kmi": "android15-6.6",
        "kernelUapi": 6,
        "pageSize": "4k",
        "models": [
          "OPD2413",
          "OnePlus Pad2 Pro",
          "PKH110",
          "OPPO Find N5",
          "OPD2409",
          "OPPO Pad4 Pro"
        ],
        "payloadKey": "plant-66118-c4127a25dcf3",
        "kernelRelease": "6.6.118-android15-8-gc4127a25dcf3-ab15863337-4k",
        "runner": "plant-66118",
        "runnerFile": {
          "asset": "maplesu-93260/plant/plant-66118",
          "sha256": "4f12224e267aa5de874445de54a1416a0e487e9436937a0e69b9f43bd13368b8",
          "bytes": 47544,
          "gzip": false,
          "decodedSha256": "4f12224e267aa5de874445de54a1416a0e487e9436937a0e69b9f43bd13368b8",
          "decodedBytes": 47544
        }
      },
      {
        "id": "plant-66127-d489d4ad2a70",
        "engine": "plant",
        "releases": [
          "6.6.127-android15-8-gd489d4ad2a70-abogki567717946-4k"
        ],
        "variant": "CVE-2026-98260-vivo-6.6.127",
        "kmi": "android15-6.6",
        "kernelUapi": 6,
        "pageSize": "4k",
        "models": [
          "vivo PD2454",
          "iQOO"
        ],
        "payloadKey": "plant-66127-d489d4ad2a70",
        "kernelRelease": "6.6.127-android15-8-gd489d4ad2a70-abogki567717946-4k",
        "runner": "plant-66127",
        "runnerFile": {
          "asset": "maplesu-93260/plant/plant-66127",
          "sha256": "d28abdd10c24a317f2f9ccb273f907a375c13a52b321a914f7fd7deeb15ad319",
          "bytes": 85208,
          "gzip": false,
          "decodedSha256": "d28abdd10c24a317f2f9ccb273f907a375c13a52b321a914f7fd7deeb15ad319",
          "decodedBytes": 85208
        }
      }
    ],
    "files": [
      {
        "device": "louise",
        "asset": "maplesu-93260/payload/cred_bootstrap",
        "sha256": "6b890e5f44c8f0918e0e6a84ada952c6492f0744284b4873c258f7d71ff40cef",
        "bytes": 91488,
        "gzip": false,
        "decodedSha256": "6b890e5f44c8f0918e0e6a84ada952c6492f0744284b4873c258f7d71ff40cef",
        "decodedBytes": 91488
      },
      {
        "device": "louise_cmd.sh",
        "asset": "maplesu-93260/payload/root_dispatcher.sh",
        "sha256": "77d320b92d95798459c00e30b9805eea5574475518ae4dfebbb7806a83032e59",
        "bytes": 2019,
        "gzip": false,
        "decodedSha256": "77d320b92d95798459c00e30b9805eea5574475518ae4dfebbb7806a83032e59",
        "decodedBytes": 2019
      },
      {
        "device": "probe",
        "asset": "maplesu-93260/payload/kprobe_trigger.bin",
        "sha256": "468685e883d9712e89b116e7b1efc34728e52b43259946239fbfaee78813d4dc",
        "bytes": 257427,
        "gzip": true,
        "decodedSha256": "1b7da65023ee4a5015ae120624696d98fc9c962f6bae1cbc9a5294657e6fb40d",
        "decodedBytes": 1059616
      },
      {
        "device": "PD2546-symbols.json",
        "asset": "maplesu-93260/payload/kallsyms_6.12.58.bin",
        "sha256": "ac8f75a03c79ef5017925c35fd9847df38461168cd25373a46eb69511c6000b3",
        "bytes": 1416457,
        "gzip": true,
        "decodedSha256": "8f7238a1e5bf288534b3316806d2c7b7fd1a566778f17041dfb48f3c97e282be",
        "decodedBytes": 15394695
      }
    ],
    "declared": []
  }
}

> Task :manager:configureMapleSuPatch
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
-- Build files have been written to: /home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/manager/build/maplesuPatch

> Task :manager:buildMapleSuPatch
[1/97] Building CXX object CMakeFiles/maplesu_patch_core.dir/upstream/3rdparty/asmjit2-src/src/asmjit/arm/a64func.cpp.o
[2/97] Building CXX object CMakeFiles/maplesu_patch_core.dir/upstream/3rdparty/asmjit2-src/src/asmjit/arm/a64formatter.cpp.o
[3/97] Building CXX object CMakeFiles/maplesu_patch_core.dir/upstream/3rdparty/asmjit2-src/src/asmjit/arm/a64compiler.cpp.o
[4/97] Building CXX object CMakeFiles/maplesu_patch_core.dir/upstream/3rdparty/asmjit2-src/src/asmjit/arm/a64builder.cpp.o
[5/97] Building CXX object CMakeFiles/maplesu_patch_core.dir/upstream/3rdparty/asmjit2-src/src/asmjit/arm/a64emithelper.cpp.o
[6/97] Building CXX object CMakeFiles/maplesu_patch_core.dir/upstream/3rdparty/asmjit2-src/src/asmjit/arm/a64instapi.cpp.o
[7/97] Building CXX object CMakeFiles/maplesu_patch_core.dir/upstream/3rdparty/asmjit2-src/src/asmjit/arm/a64operand.cpp.o
[8/97] Building CXX object CMakeFiles/maplesu_patch_core.dir/upstream/3rdparty/asmjit2-src/src/asmjit/arm/a64instdb.cpp.o
[9/97] Building CXX object CMakeFiles/maplesu_patch_core.dir/upstream/3rdparty/asmjit2-src/src/asmjit/core/archtraits.cpp.o
[10/97] Building CXX object CMakeFiles/maplesu_patch_core.dir/upstream/3rdparty/asmjit2-src/src/asmjit/arm/armformatter.cpp.o
[11/97] Building CXX object CMakeFiles/maplesu_patch_core.dir/upstream/3rdparty/asmjit2-src/src/asmjit/core/assembler.cpp.o
[12/97] Building CXX object CMakeFiles/maplesu_patch_core.dir/upstream/3rdparty/asmjit2-src/src/asmjit/core/codewriter.cpp.o
[13/97] Building CXX object CMakeFiles/maplesu_patch_core.dir/upstream/3rdparty/asmjit2-src/src/asmjit/core/constpool.cpp.o
[14/97] Building CXX object CMakeFiles/maplesu_patch_core.dir/upstream/3rdparty/asmjit2-src/src/asmjit/core/builder.cpp.o
[15/97] Building CXX object CMakeFiles/maplesu_patch_core.dir/upstream/3rdparty/asmjit2-src/src/asmjit/core/cpuinfo.cpp.o
[16/97] Building CXX object CMakeFiles/maplesu_patch_core.dir/upstream/3rdparty/asmjit2-src/src/asmjit/core/codeholder.cpp.o
[17/97] Building CXX object CMakeFiles/maplesu_patch_core.dir/upstream/3rdparty/asmjit2-src/src/asmjit/arm/a64rapass.cpp.o
[18/97] Building CXX object CMakeFiles/maplesu_patch_core.dir/upstream/3rdparty/asmjit2-src/src/asmjit/arm/a64assembler.cpp.o
[19/97] Building CXX object CMakeFiles/maplesu_patch_core.dir/upstream/3rdparty/asmjit2-src/src/asmjit/core/compiler.cpp.o
[20/97] Building CXX object CMakeFiles/maplesu_patch_core.dir/upstream/3rdparty/asmjit2-src/src/asmjit/core/emitter.cpp.o
[21/97] Building CXX object CMakeFiles/maplesu_patch_core.dir/upstream/3rdparty/asmjit2-src/src/asmjit/core/emithelper.cpp.o
[22/97] Building CXX object CMakeFiles/maplesu_patch_core.dir/upstream/3rdparty/asmjit2-src/src/asmjit/core/environment.cpp.o
[23/97] Building CXX object CMakeFiles/maplesu_patch_core.dir/upstream/3rdparty/asmjit2-src/src/asmjit/core/emitterutils.cpp.o
[24/97] Building CXX object CMakeFiles/maplesu_patch_core.dir/upstream/3rdparty/asmjit2-src/src/asmjit/core/errorhandler.cpp.o
[25/97] Building CXX object CMakeFiles/maplesu_patch_core.dir/upstream/3rdparty/asmjit2-src/src/asmjit/core/globals.cpp.o
[26/97] Building CXX object CMakeFiles/maplesu_patch_core.dir/upstream/3rdparty/asmjit2-src/src/asmjit/core/formatter.cpp.o
[27/97] Building CXX object CMakeFiles/maplesu_patch_core.dir/upstream/3rdparty/asmjit2-src/src/asmjit/core/inst.cpp.o
[28/97] Building CXX object CMakeFiles/maplesu_patch_core.dir/upstream/3rdparty/asmjit2-src/src/asmjit/core/func.cpp.o
[29/97] Building CXX object CMakeFiles/maplesu_patch_core.dir/upstream/3rdparty/asmjit2-src/src/asmjit/core/funcargscontext.cpp.o
[30/97] Building CXX object CMakeFiles/maplesu_patch_core.dir/upstream/3rdparty/asmjit2-src/src/asmjit/core/instdb.cpp.o
[31/97] Building CXX object CMakeFiles/maplesu_patch_core.dir/upstream/3rdparty/asmjit2-src/src/asmjit/core/logger.cpp.o
[32/97] Building CXX object CMakeFiles/maplesu_patch_core.dir/upstream/3rdparty/asmjit2-src/src/asmjit/core/osutils.cpp.o
[33/97] Building CXX object CMakeFiles/maplesu_patch_core.dir/upstream/3rdparty/asmjit2-src/src/asmjit/core/operand.cpp.o
[34/97] Building CXX object CMakeFiles/maplesu_patch_core.dir/upstream/3rdparty/asmjit2-src/src/asmjit/core/jitruntime.cpp.o
[35/97] Building CXX object CMakeFiles/maplesu_patch_core.dir/upstream/3rdparty/asmjit2-src/src/asmjit/core/support.cpp.o
[36/97] Building CXX object CMakeFiles/maplesu_patch_core.dir/upstream/3rdparty/asmjit2-src/src/asmjit/core/jitallocator.cpp.o
[37/97] Building CXX object CMakeFiles/maplesu_patch_core.dir/upstream/3rdparty/asmjit2-src/src/asmjit/core/target.cpp.o
[38/97] Building CXX object CMakeFiles/maplesu_patch_core.dir/upstream/3rdparty/asmjit2-src/src/asmjit/core/string.cpp.o
[39/97] Building CXX object CMakeFiles/maplesu_patch_core.dir/upstream/3rdparty/asmjit2-src/src/asmjit/core/rastack.cpp.o
[40/97] Building CXX object CMakeFiles/maplesu_patch_core.dir/upstream/3rdparty/asmjit2-src/src/asmjit/core/ralocal.cpp.o
[41/97] Building CXX object CMakeFiles/maplesu_patch_core.dir/upstream/3rdparty/asmjit2-src/src/asmjit/core/virtmem.cpp.o
[42/97] Building CXX object CMakeFiles/maplesu_patch_core.dir/upstream/3rdparty/asmjit2-src/src/asmjit/core/type.cpp.o
[43/97] Building CXX object CMakeFiles/maplesu_patch_core.dir/upstream/3rdparty/asmjit2-src/src/asmjit/core/zonehash.cpp.o
[44/97] Building CXX object CMakeFiles/maplesu_patch_core.dir/upstream/3rdparty/asmjit2-src/src/asmjit/core/zone.cpp.o
[45/97] Building CXX object CMakeFiles/maplesu_patch_core.dir/upstream/3rdparty/asmjit2-src/src/asmjit/core/zonetree.cpp.o
[46/97] Building CXX object CMakeFiles/maplesu_patch_core.dir/upstream/3rdparty/asmjit2-src/src/asmjit/core/zonestack.cpp.o
[47/97] Building CXX object CMakeFiles/maplesu_patch_core.dir/upstream/3rdparty/asmjit2-src/src/asmjit/core/zonelist.cpp.o
[48/97] Building CXX object CMakeFiles/maplesu_patch_core.dir/upstream/3rdparty/asmjit2-src/src/asmjit/core/zonevector.cpp.o
[49/97] Building CXX object CMakeFiles/maplesu_patch_core.dir/upstream/3rdparty/asmjit2-src/src/asmjit/x86/x86builder.cpp.o
[50/97] Building CXX object CMakeFiles/maplesu_patch_core.dir/upstream/3rdparty/asmjit2-src/src/asmjit/core/rapass.cpp.o
[51/97] Building CXX object CMakeFiles/maplesu_patch_core.dir/upstream/3rdparty/asmjit2-src/src/asmjit/x86/x86func.cpp.o
[52/97] Building CXX object CMakeFiles/maplesu_patch_core.dir/upstream/3rdparty/asmjit2-src/src/asmjit/x86/x86compiler.cpp.o
[53/97] Building CXX object CMakeFiles/maplesu_patch_core.dir/upstream/3rdparty/asmjit2-src/src/asmjit/x86/x86formatter.cpp.o
[54/97] Building CXX object CMakeFiles/maplesu_patch_core.dir/upstream/3rdparty/asmjit2-src/src/asmjit/x86/x86emithelper.cpp.o
[55/97] Building C object CMakeFiles/maplesu_patch_core.dir/upstream/3rdparty/capstone-5.0.7/src/arch/AArch64/AArch64BaseInfo.c.o
[56/97] Building CXX object CMakeFiles/maplesu_patch_core.dir/upstream/3rdparty/asmjit2-src/src/asmjit/x86/x86operand.cpp.o
[57/97] Building CXX object CMakeFiles/maplesu_patch_core.dir/upstream/3rdparty/asmjit2-src/src/asmjit/x86/x86instapi.cpp.o
[58/97] Building C object CMakeFiles/maplesu_patch_core.dir/upstream/3rdparty/capstone-5.0.7/src/arch/AArch64/AArch64Mapping.c.o
[59/97] Building C object CMakeFiles/maplesu_patch_core.dir/upstream/3rdparty/capstone-5.0.7/src/arch/AArch64/AArch64Module.c.o
[60/97] Building C object CMakeFiles/maplesu_patch_core.dir/upstream/3rdparty/capstone-5.0.7/src/Mapping.c.o
[61/97] Building CXX object CMakeFiles/maplesu_patch_core.dir/upstream/3rdparty/asmjit2-src/src/asmjit/x86/x86assembler.cpp.o
[62/97] Building C object CMakeFiles/maplesu_patch_core.dir/upstream/3rdparty/capstone-5.0.7/src/MCInst.c.o
[63/97] Building C object CMakeFiles/maplesu_patch_core.dir/upstream/3rdparty/capstone-5.0.7/src/MCInstrDesc.c.o
[64/97] Building C object CMakeFiles/maplesu_patch_core.dir/upstream/3rdparty/capstone-5.0.7/src/MCRegisterInfo.c.o
[65/97] Building C object CMakeFiles/maplesu_patch_core.dir/upstream/3rdparty/capstone-5.0.7/src/SStream.c.o
[66/97] Building C object CMakeFiles/maplesu_patch_core.dir/upstream/3rdparty/capstone-5.0.7/src/cs.c.o
[67/97] Building C object CMakeFiles/maplesu_patch_core.dir/upstream/3rdparty/capstone-5.0.7/src/utils.c.o
[68/97] Building CXX object CMakeFiles/maplesu_patch_core.dir/upstream/3rdparty/asmjit2-src/src/asmjit/x86/x86instdb.cpp.o
[69/97] Building CXX object CMakeFiles/maplesu_patch_core.dir/upstream/3rdparty/cJSON/cJSON.cpp.o
[70/97] Building C object CMakeFiles/maplesu_patch_core.dir/upstream/3rdparty/capstone-5.0.7/src/arch/AArch64/AArch64InstPrinter.c.o
[71/97] Building CXX object CMakeFiles/maplesu_patch_core.dir/upstream/3rdparty/asmjit2-src/src/asmjit/x86/x86rapass.cpp.o
[72/97] Building CXX object CMakeFiles/maplesu_patch_core.dir/upstream/analyze/init_cred_searcher.cpp.o
[73/97] Building C object CMakeFiles/maplesu_patch_core.dir/upstream/3rdparty/capstone-5.0.7/src/arch/AArch64/AArch64Disassembler.c.o
[74/97] Building CXX object CMakeFiles/maplesu_patch_core.dir/upstream/analyze/kallsyms_lookup_name.cpp.o
[75/97] Building CXX object CMakeFiles/maplesu_patch_core.dir/upstream/analyze/kallsyms_lookup_name_6_12_0.cpp.o
[76/97] Building CXX object CMakeFiles/maplesu_patch_core.dir/upstream/analyze/kallsyms_lookup_name_4_6_0.cpp.o
[77/97] Building CXX object CMakeFiles/maplesu_patch_core.dir/upstream/analyze/kallsyms_lookup_name_6_1_0.cpp.o
[78/97] Building CXX object CMakeFiles/maplesu_patch_core.dir/upstream/analyze/kallsyms_lookup_name_6_1_42.cpp.o
[79/97] Building CXX object CMakeFiles/maplesu_patch_core.dir/upstream/analyze/kallsyms_lookup_name_6_4_0.cpp.o
[80/97] Building CXX object CMakeFiles/maplesu_patch_core.dir/upstream/analyze/kernel_symbol_finder.cpp.o
[81/97] Building CXX object CMakeFiles/maplesu_patch_core.dir/upstream/analyze/kernel_version_parser.cpp.o
[82/97] Building CXX object CMakeFiles/maplesu_patch_core.dir/upstream/analyze/kernel_symbol_proxy.cpp.o
[83/97] Building CXX object CMakeFiles/maplesu_patch_core.dir/upstream/analyze/kallsyms_lookup_name_6_1_60.cpp.o
[84/97] Building CXX object CMakeFiles/maplesu_patch_core.dir/upstream/analyze/symbol_analyze.cpp.o
[85/97] Building CXX object CMakeFiles/maplesu_patch_core.dir/upstream/patch_base.cpp.o
[86/97] Building CXX object CMakeFiles/maplesu_patch_core.dir/upstream/patch_audit_log_start.cpp.o
[87/97] Building CXX object CMakeFiles/maplesu_patch_core.dir/src/patch_safety.cpp.o
[88/97] Building CXX object CMakeFiles/maplesu_patch_core.dir/upstream/patch_avc_denied.cpp.o
[89/97] Building CXX object CMakeFiles/maplesu_patch_core.dir/upstream/patch_compat_filldir.cpp.o
[90/97] Building CXX object CMakeFiles/maplesu_patch_core.dir/upstream/patch_current_avc_check.cpp.o
[91/97] Building CXX object CMakeFiles/maplesu_patch_core.dir/upstream/patch_do_execve.cpp.o
/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/patch-engine/upstream/patch_do_execve.cpp:1:12: warning: #pragma once in main file [-Wpragma-once-outside-header]
<U+FEFF>#pragma once
                ^
1 warning generated.
[92/97] Building CXX object CMakeFiles/maplesu_patch_core.dir/upstream/patch_filldir64.cpp.o
[93/97] Building CXX object CMakeFiles/maplesu_patch_core.dir/src/patch_plan.cpp.o
[94/97] Building CXX object CMakeFiles/maplesu-kernel-patch.dir/src/patch_main.cpp.o
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
[1/25] Building CXX object CMakeFiles/maplesu_bootstrap.dir/src/block_partition_access.cpp.o
[2/25] Building CXX object CMakeFiles/maplesu_parasite.dir/src/parasite/parasite_loader.cpp.o
[3/25] Linking CXX shared library libmaplesu_parasite.so
[4/25] Building CXX object CMakeFiles/maplesu_bootstrap.dir/src/su_bootstrap.cpp.o
[5/25] Building CXX object CMakeFiles/maplesu-runtime.dir/src/exec_main.cpp.o
[6/25] Building CXX object CMakeFiles/maplesu-runtime.dir/src/su_session.cpp.o
[7/25] Building CXX object CMakeFiles/maplesu_bootstrap.dir/src/session_process.cpp.o
[8/25] Linking CXX shared library libmaplesu_bootstrap.so
[9/25] Building CXX object CMakeFiles/maplesu_ultra_bridge.dir/ultra/bridge/module_environment_capture.cpp.o
[10/25] Building CXX object CMakeFiles/maplesu_ultra_bridge.dir/ultra/bridge/installed_helper_readback.cpp.o
[11/25] Linking CXX executable maplesu-runtime
[12/25] Building CXX object CMakeFiles/maplesu_ultra_bridge.dir/ultra/policy/backend_publish.cpp.o
[13/25] Building CXX object CMakeFiles/maplesu_ultra_bridge.dir/ultra/policy/module_policy_management.cpp.o
[14/25] Building CXX object CMakeFiles/maplesu_ultra_bridge.dir/ultra/policy/module_policy_config.cpp.o
[15/25] Building CXX object CMakeFiles/maplesu-su.dir/src/su_main.cpp.o
[16/25] Building CXX object CMakeFiles/maplesu_ultra_bridge.dir/ultra/bridge/sdk_call_scope.cpp.o
[17/25] Building ASM object CMakeFiles/maplesu_ultra_bridge.dir/ultra/bridge/sdk_syscall.S.o
[18/25] Linking CXX executable maplesu-su
[19/25] Building CXX object CMakeFiles/maplesu_ultra_bridge.dir/ultra/bridge/manager_owner_root_probe.cpp.o
[20/25] Building CXX object CMakeFiles/maplesu_ultra_bridge.dir/ultra/bridge/uninstall_callback_watchdog.cpp.o
[21/25] Building CXX object CMakeFiles/maplesu_ultra_bridge.dir/ultra/upgrade/executable_publish.cpp.o
[22/25] Building CXX object CMakeFiles/maplesu_ultra_bridge.dir/ultra/third_party/cJSON/cJSON.cpp.o
[23/25] Building CXX object CMakeFiles/maplesu_ultra_bridge.dir/ultra/bridge/webui_lifecycle.cpp.o
[24/25] Building CXX object CMakeFiles/maplesu_ultra_bridge.dir/ultra/bridge/native_lib_ultra.cpp.o
[25/25] Linking CXX shared library libmaplesu_ultra_bridge.so
FAILED: libmaplesu_ultra_bridge.so 
: && /usr/local/lib/android/sdk/ndk/26.1.10909125/toolchains/llvm/prebuilt/linux-x86_64/bin/clang++ --target=aarch64-none-linux-android31 --sysroot=/usr/local/lib/android/sdk/ndk/26.1.10909125/toolchains/llvm/prebuilt/linux-x86_64/sysroot -fPIC -g -DANDROID -fdata-sections -ffunction-sections -funwind-tables -fstack-protector-strong -no-canonical-prefixes -D_FORTIFY_SOURCE=2 -Wformat -Werror=format-security   -O3 -DNDEBUG  -static-libstdc++ -Wl,--build-id=sha1 -Wl,--no-undefined-version -Wl,--fatal-warnings -Wl,--no-undefined -Qunused-arguments  -Wl,--gc-sections   -Wl,--wrap=maplesu_module_uninstall_callback -Wl,--wrap=__set_current_module_root_key_hd04aBTnbSZlTRP7S4mQpIeVvr2ssGjW -Wl,--wrap=__get_current_module_root_key_hd04aBTnbSZlTRP7S4mQpIeVvr2ssGjW -Wl,--wrap=syscall -Wl,--wrap=fork -Wl,--wrap=pipe2 -Wl,--wrap=close -Wl,--wrap=waitpid -Wl,--no-undefined -Wl,--gc-sections -Wl,-z,relro,-z,now -Wl,--undefined=_ZN11kernel_root29parasite_precheck_app_with_cbEPKcS1_PFvS1_NS_15AppDynlibStatusEE -Wl,--undefined=_ZN11kernel_root20parasite_implant_appEPKcS1_S1_ -Wl,--undefined=_ZN11kernel_root23parasite_implant_su_envEPKcS1_S1_S1_ -Wl,-z,max-page-size=16384,-z,common-page-size=16384 -shared -Wl,-soname,libmaplesu_ultra_bridge.so -o libmaplesu_ultra_bridge.so CMakeFiles/maplesu_ultra_bridge.dir/ultra/bridge/native_lib_ultra.cpp.o CMakeFiles/maplesu_ultra_bridge.dir/ultra/bridge/module_environment_capture.cpp.o CMakeFiles/maplesu_ultra_bridge.dir/ultra/policy/module_policy_config.cpp.o CMakeFiles/maplesu_ultra_bridge.dir/ultra/policy/module_policy_management.cpp.o CMakeFiles/maplesu_ultra_bridge.dir/ultra/policy/backend_publish.cpp.o CMakeFiles/maplesu_ultra_bridge.dir/ultra/upgrade/executable_publish.cpp.o CMakeFiles/maplesu_ultra_bridge.dir/ultra/bridge/sdk_call_scope.cpp.o CMakeFiles/maplesu_ultra_bridge.dir/ultra/bridge/manager_owner_root_probe.cpp.o CMakeFiles/maplesu_ultra_bridge.dir/ultra/bridge/installed_helper_readback.cpp.o CMakeFiles/maplesu_ultra_bridge.dir/ultra/bridge/sdk_syscall.S.o CMakeFiles/maplesu_ultra_bridge.dir/ultra/bridge/uninstall_callback_watchdog.cpp.o CMakeFiles/maplesu_ultra_bridge.dir/ultra/bridge/webui_lifecycle.cpp.o CMakeFiles/maplesu_ultra_bridge.dir/ultra/third_party/cJSON/cJSON.cpp.o  /home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/runtime/maplesu-sdk/lib/arm64-v8a/libkernel_module_kit_static.a  -lz  -llog  -ldl  -latomic -lm && :
ld.lld: error: undefined symbol: kernel_module::maplesu_request_auth_state()
>>> referenced by manager_owner_identity.h:12 (/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/runtime/ultra/bridge/manager_owner_identity.h:12)
>>>               CMakeFiles/maplesu_ultra_bridge.dir/ultra/bridge/native_lib_ultra.cpp.o:(Java_dev_maplesu_manager_runtime_ultra_bridge_NativeBridge_installEnvironment)
>>> referenced by maplesu_storage_worker_private.h:16 (/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/runtime/ultra/bridge/../../maplesu-sdk/sdk/include/maplesu_storage_worker_private.h:16)
>>>               CMakeFiles/maplesu_ultra_bridge.dir/ultra/bridge/module_environment_capture.cpp.o:(maplesu::storage::WorkerScope::WorkerScope(char const*))
>>> referenced by maplesu_storage_worker_private.h:26 (/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/runtime/ultra/bridge/../../maplesu-sdk/sdk/include/maplesu_storage_worker_private.h:26)
>>>               CMakeFiles/maplesu_ultra_bridge.dir/ultra/bridge/module_environment_capture.cpp.o:(maplesu::storage::WorkerScope::root())
>>> referenced 41 more times

ld.lld: error: undefined symbol: kernel_module::maplesu_request_set_auth_mode(kernel_module::RequestAuthMode)
>>> referenced by manager_owner_identity.h:19 (/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/runtime/ultra/bridge/manager_owner_identity.h:19)
>>>               CMakeFiles/maplesu_ultra_bridge.dir/ultra/bridge/native_lib_ultra.cpp.o:(Java_dev_maplesu_manager_runtime_ultra_bridge_NativeBridge_installEnvironment)
>>> referenced by manager_owner_identity.h:30 (/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/runtime/ultra/bridge/manager_owner_identity.h:30)
>>>               CMakeFiles/maplesu_ultra_bridge.dir/ultra/bridge/native_lib_ultra.cpp.o:(Java_dev_maplesu_manager_runtime_ultra_bridge_NativeBridge_installEnvironment)
>>> referenced by module_environment_capture.cpp:36 (/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/runtime/ultra/bridge/module_environment_capture.cpp:36)
>>>               CMakeFiles/maplesu_ultra_bridge.dir/ultra/bridge/module_environment_capture.cpp.o:(maplesu::capture_module_environment(char const*, std::__ndk1::vector<std::__ndk1::basic_string<char, std::__ndk1::char_traits<char>, std::__ndk1::allocator<char>>, std::__ndk1::allocator<std::__ndk1::basic_string<char, std::__ndk1::char_traits<char>, std::__ndk1::allocator<char>>>>&))
>>> referenced 156 more times

ld.lld: error: undefined symbol: kernel_module::CleanupReceiptScope::CleanupReceiptScope()
>>> referenced by manager_owner_identity.h:29 (/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/runtime/ultra/bridge/manager_owner_identity.h:29)
>>>               CMakeFiles/maplesu_ultra_bridge.dir/ultra/bridge/native_lib_ultra.cpp.o:(Java_dev_maplesu_manager_runtime_ultra_bridge_NativeBridge_installEnvironment)
>>> referenced by manager_owner_identity.h:29 (/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/runtime/ultra/bridge/manager_owner_identity.h:29)
>>>               CMakeFiles/maplesu_ultra_bridge.dir/ultra/bridge/native_lib_ultra.cpp.o:(Java_dev_maplesu_manager_runtime_ultra_bridge_NativeBridge_installEnvironment)
>>> referenced by manager_owner_identity.h:29 (/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/runtime/ultra/bridge/manager_owner_identity.h:29)
>>>               CMakeFiles/maplesu_ultra_bridge.dir/ultra/bridge/native_lib_ultra.cpp.o:(Java_dev_maplesu_manager_runtime_ultra_bridge_NativeBridge_installEnvironment)
>>> referenced 117 more times

ld.lld: error: undefined symbol: kernel_module::CleanupReceiptScope::~CleanupReceiptScope()
>>> referenced by manager_owner_identity.h:31 (/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/runtime/ultra/bridge/manager_owner_identity.h:31)
>>>               CMakeFiles/maplesu_ultra_bridge.dir/ultra/bridge/native_lib_ultra.cpp.o:(Java_dev_maplesu_manager_runtime_ultra_bridge_NativeBridge_installEnvironment)
>>> referenced by manager_owner_identity.h:31 (/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/runtime/ultra/bridge/manager_owner_identity.h:31)
>>>               CMakeFiles/maplesu_ultra_bridge.dir/ultra/bridge/native_lib_ultra.cpp.o:(Java_dev_maplesu_manager_runtime_ultra_bridge_NativeBridge_installEnvironment)
>>> referenced by manager_owner_identity.h:31 (/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/runtime/ultra/bridge/manager_owner_identity.h:31)
>>>               CMakeFiles/maplesu_ultra_bridge.dir/ultra/bridge/native_lib_ultra.cpp.o:(Java_dev_maplesu_manager_runtime_ultra_bridge_NativeBridge_installEnvironment)
>>> referenced 198 more times

ld.lld: error: undefined symbol: maplesu::sdk::install_maplesu_environment(char const*, maplesu::sdk::InstallMode, maplesu::sdk::InstallConfig const&)
>>> referenced by native_lib_ultra.cpp:834 (/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/runtime/ultra/bridge/native_lib_ultra.cpp:834)
>>>               CMakeFiles/maplesu_ultra_bridge.dir/ultra/bridge/native_lib_ultra.cpp.o:(Java_dev_maplesu_manager_runtime_ultra_bridge_NativeBridge_installEnvironment)

ld.lld: error: undefined symbol: maplesu::sdk::get_sdk_version()
>>> referenced by module_environment_capture.cpp:43 (/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/runtime/ultra/bridge/module_environment_capture.cpp:43)
>>>               CMakeFiles/maplesu_ultra_bridge.dir/ultra/bridge/module_environment_capture.cpp.o:(maplesu::capture_module_environment(char const*, std::__ndk1::vector<std::__ndk1::basic_string<char, std::__ndk1::char_traits<char>, std::__ndk1::allocator<char>>, std::__ndk1::allocator<std::__ndk1::basic_string<char, std::__ndk1::char_traits<char>, std::__ndk1::allocator<char>>>>&))
>>> referenced by native_lib_ultra.cpp:938 (/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/runtime/ultra/bridge/native_lib_ultra.cpp:938)
>>>               CMakeFiles/maplesu_ultra_bridge.dir/ultra/bridge/native_lib_ultra.cpp.o:(Java_dev_maplesu_manager_runtime_ultra_bridge_NativeBridge_getSdkVersion)

ld.lld: error: undefined hidden symbol: maplesu::storage::StorageScope::~StorageScope()
>>> referenced by optional:274 (/usr/local/lib/android/sdk/ndk/26.1.10909125/toolchains/llvm/prebuilt/linux-x86_64/sysroot/usr/include/c++/v1/optional:274)
>>>               CMakeFiles/maplesu_ultra_bridge.dir/ultra/bridge/module_environment_capture.cpp.o:(maplesu::storage::WorkerScope::root())
>>> referenced by optional:274 (/usr/local/lib/android/sdk/ndk/26.1.10909125/toolchains/llvm/prebuilt/linux-x86_64/sysroot/usr/include/c++/v1/optional:274)
>>>               CMakeFiles/maplesu_ultra_bridge.dir/ultra/bridge/module_environment_capture.cpp.o:(maplesu::storage::WorkerScope::close_checked())
>>> referenced by optional:248 (/usr/local/lib/android/sdk/ndk/26.1.10909125/toolchains/llvm/prebuilt/linux-x86_64/sysroot/usr/include/c++/v1/optional:248)
>>>               CMakeFiles/maplesu_ultra_bridge.dir/ultra/bridge/module_environment_capture.cpp.o:(maplesu::storage::WorkerScope::~WorkerScope())
>>> referenced 8 more times

ld.lld: error: undefined symbol: kernel_module::maplesu_request_owner_lifetime_capture(kernel_module::RequestOwnerLifetimeToken&)
>>> referenced by maplesu_storage_worker_private.h:30 (/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/runtime/ultra/bridge/../../maplesu-sdk/sdk/include/maplesu_storage_worker_private.h:30)
>>>               CMakeFiles/maplesu_ultra_bridge.dir/ultra/bridge/module_environment_capture.cpp.o:(maplesu::storage::WorkerScope::root())

ld.lld: error: undefined symbol: kernel_module::maplesu_request_owner_close()
>>> referenced by maplesu_storage_worker_private.h:33 (/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/runtime/ultra/bridge/../../maplesu-sdk/sdk/include/maplesu_storage_worker_private.h:33)
>>>               CMakeFiles/maplesu_ultra_bridge.dir/ultra/bridge/module_environment_capture.cpp.o:(maplesu::storage::WorkerScope::root())
>>> referenced by maplesu_storage_worker_private.h:73 (/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/runtime/ultra/bridge/../../maplesu-sdk/sdk/include/maplesu_storage_worker_private.h:73)
>>>               CMakeFiles/maplesu_ultra_bridge.dir/ultra/bridge/module_environment_capture.cpp.o:(maplesu::storage::WorkerScope::close_checked())
>>> referenced by maplesu_storage_worker_private.h:73 (/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/runtime/ultra/bridge/../../maplesu-sdk/sdk/include/maplesu_storage_worker_private.h:73)
>>>               CMakeFiles/maplesu_ultra_bridge.dir/ultra/bridge/module_environment_capture.cpp.o:(maplesu::storage::WorkerScope::close())
>>> referenced 7 more times

ld.lld: error: undefined symbol: kernel_module::maplesu_request_helper_open()
>>> referenced by maplesu_storage_worker_private.h:35 (/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/runtime/ultra/bridge/../../maplesu-sdk/sdk/include/maplesu_storage_worker_private.h:35)
>>>               CMakeFiles/maplesu_ultra_bridge.dir/ultra/bridge/module_environment_capture.cpp.o:(maplesu::storage::WorkerScope::root())

ld.lld: error: undefined symbol: kernel_module::maplesu_request_owner_deployment(kernel_module::RequestDeploymentNamespace&)
>>> referenced by maplesu_storage_worker_private.h:43 (/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/runtime/ultra/bridge/../../maplesu-sdk/sdk/include/maplesu_storage_worker_private.h:43)
>>>               CMakeFiles/maplesu_ultra_bridge.dir/ultra/bridge/module_environment_capture.cpp.o:(maplesu::storage::WorkerScope::root())
>>> referenced by installed_helper_readback.cpp:345 (/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/runtime/ultra/bridge/installed_helper_readback.cpp:345)
>>>               CMakeFiles/maplesu_ultra_bridge.dir/ultra/bridge/installed_helper_readback.cpp.o:(maplesu::(anonymous namespace)::child_run(int, int, char const*, char const*, unsigned long, timespec const&))

ld.lld: error: undefined symbol: kernel_module::maplesu_request_owner_binding_matches(kernel_module::RequestOwnerBinding const&)
>>> referenced by maplesu_storage_worker_private.h:45 (/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/runtime/ultra/bridge/../../maplesu-sdk/sdk/include/maplesu_storage_worker_private.h:45)
>>>               CMakeFiles/maplesu_ultra_bridge.dir/ultra/bridge/module_environment_capture.cpp.o:(maplesu::storage::WorkerScope::root())
>>> referenced by installed_helper_readback.cpp:353 (/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/runtime/ultra/bridge/installed_helper_readback.cpp:353)
>>>               CMakeFiles/maplesu_ultra_bridge.dir/ultra/bridge/installed_helper_readback.cpp.o:(maplesu::(anonymous namespace)::child_run(int, int, char const*, char const*, unsigned long, timespec const&))

ld.lld: error: undefined symbol: maplesu::sdk::uninstall_maplesu_environment(char const*)
>>> referenced by native_lib_ultra.cpp:858 (/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/runtime/ultra/bridge/native_lib_ultra.cpp:858)
>>>               CMakeFiles/maplesu_ultra_bridge.dir/ultra/bridge/native_lib_ultra.cpp.o:(Java_dev_maplesu_manager_runtime_ultra_bridge_NativeBridge_uninstallEnvironment)

ld.lld: error: undefined hidden symbol: maplesu::storage::current_kernel_directory(std::__ndk1::basic_string<char, std::__ndk1::char_traits<char>, std::__ndk1::allocator<char>>&)
>>> referenced by maplesu_module_environment_private.h:88 (/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/runtime/ultra/bridge/../../maplesu-sdk/sdk/include/maplesu_module_environment_private.h:88)
>>>               CMakeFiles/maplesu_ultra_bridge.dir/ultra/bridge/module_environment_capture.cpp.o:(maplesu::module_environment::capture(unsigned int, unsigned int, unsigned int, char* const*, maplesu::module_environment::Environment&))

ld.lld: error: undefined symbol: maplesu::sdk::get_maplesu_environment_state(char const*)
>>> referenced by native_lib_ultra.cpp:878 (/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/runtime/ultra/bridge/native_lib_ultra.cpp:878)
>>>               CMakeFiles/maplesu_ultra_bridge.dir/ultra/bridge/native_lib_ultra.cpp.o:(Java_dev_maplesu_manager_runtime_ultra_bridge_NativeBridge_getEnvironmentState)

ld.lld: error: undefined hidden symbol: maplesu::storage::StorageScope::StorageScope(maplesu::storage::StorageLocator const&, char const*)
>>> referenced by construct_at.h:38 (/usr/local/lib/android/sdk/ndk/26.1.10909125/toolchains/llvm/prebuilt/linux-x86_64/sysroot/usr/include/c++/v1/__memory/construct_at.h:38)
>>>               CMakeFiles/maplesu_ultra_bridge.dir/ultra/bridge/module_environment_capture.cpp.o:(maplesu::storage::StorageScope& std::__ndk1::optional<maplesu::storage::StorageScope>::emplace[abi:v170000]<maplesu::storage::StorageLocator&, char const*, void>(maplesu::storage::StorageLocator&, char const*&&))

ld.lld: error: undefined symbol: maplesu::sdk::get_installed_maplesu_environment_version(char const*, maplesu::sdk::MapleSUSdkVersion&)
>>> referenced by native_lib_ultra.cpp:921 (/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/runtime/ultra/bridge/native_lib_ultra.cpp:921)
>>>               CMakeFiles/maplesu_ultra_bridge.dir/ultra/bridge/native_lib_ultra.cpp.o:(Java_dev_maplesu_manager_runtime_ultra_bridge_NativeBridge_getInstalledEnvironmentVersion)

ld.lld: error: undefined symbol: maplesu::sdk::get_root_status_report(char const*)
>>> referenced by native_lib_ultra.cpp:1170 (/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/runtime/ultra/bridge/native_lib_ultra.cpp:1170)
>>>               CMakeFiles/maplesu_ultra_bridge.dir/ultra/bridge/native_lib_ultra.cpp.o:(Java_dev_maplesu_manager_runtime_ultra_bridge_NativeBridge_testRoot)

ld.lld: error: undefined hidden symbol: maplesu::sdk::current_root_status_result()
>>> referenced by native_lib_ultra.cpp:1171 (/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/runtime/ultra/bridge/native_lib_ultra.cpp:1171)
>>>               CMakeFiles/maplesu_ultra_bridge.dir/ultra/bridge/native_lib_ultra.cpp.o:(Java_dev_maplesu_manager_runtime_ultra_bridge_NativeBridge_testRoot)

ld.lld: error: undefined symbol: maplesu::sdk::run_root_cmd(char const*, char const*, std::__ndk1::basic_string<char, std::__ndk1::char_traits<char>, std::__ndk1::allocator<char>>&)
>>> referenced by native_lib_ultra.cpp:1208 (/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/runtime/ultra/bridge/native_lib_ultra.cpp:1208)
>>>               CMakeFiles/maplesu_ultra_bridge.dir/ultra/bridge/native_lib_ultra.cpp.o:(Java_dev_maplesu_manager_runtime_ultra_bridge_NativeBridge_runRootCmd)

ld.lld: error: too many errors emitted, stopping now (use --error-limit=0 to see all errors)
clang++: error: linker command failed with exit code 1 (use -v to see invocation)
ninja: build stopped: subcommand failed.

> Task :manager:buildMapleSuRuntime FAILED

[Incubating] Problems report is available at: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/build/reports/problems/problems-report.html

FAILURE: Build failed with an exception.

* What went wrong:
Execution failed for task ':manager:buildMapleSuRuntime' (registered in build file 'manager/build.gradle.kts').
> Process 'command '/usr/local/lib/android/sdk/cmake/3.22.1/bin/cmake'' finished with non-zero exit value 1

* Try:
> Run with --stacktrace option to get the stack trace.
> Run with --info or --debug option to get more log output.
> Run with --scan to get full insights from a Build Scan (powered by Develocity).
> Get more help at https://help.gradle.org.

Deprecated Gradle features were used in this build, making it incompatible with Gradle 10.

You can use '--warning-mode all' to show the individual deprecation warnings and determine if they come from your own scripts or plugins.

For more on this, please refer to https://docs.gradle.org/9.8.1/userguide/command_line_interface.html#sec:command_line_warnings in the Gradle documentation.

BUILD FAILED in 4m 11s
49 actionable tasks: 49 executed
```
