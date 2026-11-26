# 构建结果

- run: 15  提交: 46e55a5f26269305d4c946ca2ed0c02c4823f954
- 作业结论: failure

```
#### provider 子构建日志（CMake/cargo 报错常只写在这里）
===== src/manager/build/jailbreakProviders/build.log =====
   Compiling protoc-bin-vendored-linux-ppcle_64 v3.2.0
   Compiling portable-atomic v1.15.0
   Compiling protoc-bin-vendored-macos-x86_64 v3.2.0
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
   Compiling libbz2-rs-sys v0.2.5
   Compiling strsim v0.11.1
   Compiling unicode-width v0.2.2
   Compiling thiserror v2.0.20
   Compiling serde_json v1.0.151
   Compiling tap v1.0.1
   Compiling clap_lex v1.1.1
   Compiling wyz v0.5.1
   Compiling clap_builder v4.6.7
   Compiling console v0.16.6
   Compiling bzip2 v0.6.1
   Compiling rayon v1.12.0
   Compiling digest v0.11.3
   Compiling brotli v8.0.4
   Compiling payload-extract v0.1.1 (/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/jailbreak-providers/ghostlock/extractor-native/vendor/payload-extract)
   Compiling clap_derive v4.6.7
   Compiling aho-corasick v1.1.5
   Compiling thiserror-impl v2.0.20
   Compiling cpufeatures v0.3.1
   Compiling simd-adler32 v0.3.10
   Compiling unit-prefix v0.5.2
   Compiling itoa v1.0.18
   Compiling typed-path v0.12.3
   Compiling adler2 v2.0.1
   Compiling funty v2.0.0
   Compiling miniz_oxide v0.9.1
   Compiling zip v8.6.0
   Compiling bitvec v1.1.1
   Compiling indicatif v0.18.6
   Compiling clap v4.6.7
   Compiling bsdiff-android v0.0.2
   Compiling sha2 v0.11.0
   Compiling zstd v0.13.3
   Compiling xz2 v0.1.7
   Compiling yaxpeax-arch v0.3.2
   Compiling memmap2 v0.9.11
   Compiling lz4_flex v0.14.0
   Compiling hex v0.4.3
   Compiling yaxpeax-arm v0.5.0
   Compiling flate2 v1.1.10
   Compiling ghostlock-extract v0.1.0 (/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/jailbreak-providers/ghostlock/extractor-native)
    Finished `release` profile [optimized] target(s) in 1m 02s
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
Traceback (most recent call last):
  File "/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/jailbreak-providers/root-loader/build_root_module.py", line 7588, in <module>
    sys.exit(main())
             ~~~~^^
  File "/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/jailbreak-providers/root-loader/build_root_module.py", line 7113, in main
    return run_l3(args)
  File "/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/jailbreak-providers/root-loader/build_root_module.py", line 6813, in run_l3
    l3_facts = derive_l3_facts(image, symbols, contract)
  File "/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/jailbreak-providers/root-loader/build_root_module.py", line 2543, in derive_l3_facts
    bridge = derive_l3_policy_bridge(image, symbols, contract["kprobe"]["size"])
  File "/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/jailbreak-providers/root-loader/build_root_module.py", line 2498, in derive_l3_policy_bridge
    return policy_build.derive(inputs, image, symbols, probe_size)
           ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/jailbreak-providers/root-loader/policy_hook_build.py", line 67, in derive
    if hashlib.sha256((b.PROJECT_ROOT / name).read_bytes()).hexdigest() != digest:
                      ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^
  File "/usr/lib/python3.14/pathlib/__init__.py", line 778, in read_bytes
    with self.open(mode='rb', buffering=0) as f:
         ~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.14/pathlib/__init__.py", line 772, in open
    return io.open(self, mode, buffering, encoding, errors, newline)
           ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: '/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/runtime/pro/policy/kernel/abi_anchors.c'
#### 主构建日志尾
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
  Downloaded unicode-ident v1.0.25
  Downloaded quote v1.0.47
  Downloaded thiserror v2.0.20
  Downloaded yaxpeax-arm v0.5.0
  Downloaded yaxpeax-arch v0.3.2
  Downloaded serde_derive v1.0.229
  Downloaded syn v3.0.6
  Downloaded serde_json v1.0.151
  Downloaded autocfg v1.5.1
  Downloaded wyz v0.5.1
  Downloaded zmij v1.0.23
  Downloaded tap v1.0.1
  Downloaded prost-derive v0.14.4
  Downloaded cfg-if v1.0.5
  Downloaded radium v0.7.0
  Downloaded terminal_size v0.4.4
  Downloaded proc-macro2 v1.0.107
  Downloaded serde v1.0.229
  Downloaded bitvec v1.1.1
  Downloaded prost v0.14.4
  Downloaded anyhow v1.0.104
  Downloaded wasm-bindgen v0.2.128
  Downloaded wasm-bindgen-macro-support v0.2.128
  Downloaded rustversion v1.0.23
  Downloaded zerofrom v0.1.8
  Downloaded once_cell_polyfill v1.70.2
  Downloaded bsdiff-android v0.0.2
  Downloaded alloc-stdlib v0.2.4
  Downloaded memchr v2.8.3
  Downloaded percent-encoding v2.3.2
  Downloaded utf8_iter v1.0.4
  Downloaded windows-targets v0.52.6
  Downloaded rand_pcg v0.10.2
  Downloaded cfg_aliases v0.2.2
  Downloaded hex v0.4.3
  Downloaded anstyle v1.0.14
  Downloaded tinystr v0.8.4
  Downloaded zstd v0.13.3
  Downloaded equivalent v1.0.2
  Downloaded sync_wrapper v1.0.2
  Downloaded untrusted v0.9.0
  Downloaded simd-adler32 v0.3.10
  Downloaded futures-task v0.3.34
  Downloaded futures-macro v0.3.34
  Downloaded tokio-macros v2.7.2
  Downloaded itoa v1.0.18
  Downloaded either v1.18.0
  Downloaded shlex v2.0.1
  Downloaded r-efi v6.0.0
  Downloaded bzip2 v0.6.1
  Downloaded crypto-common v0.2.2
  Downloaded funty v2.0.0
  Downloaded cc v1.4.6
  Downloaded getrandom v0.4.3
  Downloaded wasm-bindgen-macro v0.2.128
  Downloaded sha2 v0.11.0
  Downloaded once_cell v1.21.4
  Downloaded block-buffer v0.12.1
  Downloaded bytes v1.12.1
  Downloaded rand_core v0.10.1
  Downloaded wasm-bindgen-shared v0.2.128
  Downloaded socket2 v0.6.5
  Downloaded tempfile v3.27.0
  Downloaded ipnet v2.12.2
  Downloaded jobserver v0.1.35
  Downloaded pkg-config v0.3.34
  Downloaded bumpalo v3.20.3
  Downloaded try-lock v0.2.5
  Downloaded is_terminal_polyfill v1.70.2
  Downloaded colorchoice v1.0.5
  Downloaded anstyle-wincon v3.0.11
  Downloaded zstd-safe v7.3.0
  Downloaded pin-project-lite v0.2.17
  Downloaded futures-sink v0.3.34
  Downloaded futures-core v0.3.34
  Downloaded fastrand v2.5.0
  Downloaded cpufeatures v0.3.1
  Downloaded yoke v0.8.3
  Downloaded getrandom v0.2.17
  Downloaded console v0.16.6
  Downloaded clap_derive v4.6.7
  Downloaded xz2 v0.1.7
  Downloaded errno v0.3.14
  Downloaded web-time v1.1.0
  Downloaded windows-link v0.2.1
  Downloaded wasi v0.11.1+wasi-snapshot-preview1
  Downloaded wasm-bindgen-futures v0.4.78
  Downloaded want v0.3.1
  Downloaded anstyle-query v1.1.5
  Downloaded serde_core v1.0.229
  Downloaded futures-io v0.3.34
  Downloaded rustls-pki-types v1.15.1
  Downloaded zeroize v1.9.0
  Downloaded url v2.5.8
  Downloaded yoke-derive v0.8.3
  Downloaded form_urlencoded v1.2.2
  Downloaded tower-layer v0.3.3
  Downloaded lru-slab v0.1.3
  Downloaded hyper-rustls v0.27.9
  Downloaded http-body-util v0.1.5
  Downloaded protoc-bin-vendored v3.2.0
  Downloaded foldhash v0.1.5
  Downloaded heck v0.5.0
  Downloaded clap_lex v1.1.1
  Downloaded utf8parse v0.2.2
  Downloaded alloc-no-stdlib v2.0.4
  Downloaded thiserror-impl v2.0.20
  Downloaded slab v0.4.12
  Downloaded find-msvc-tools v0.1.12
  Downloaded crc32fast v1.5.2
  Downloaded zerofrom-derive v0.1.8
  Downloaded potential_utf v0.1.6
  Downloaded tower-service v0.3.3
  Downloaded serde_urlencoded v0.7.1
  Downloaded rustc-hash v2.1.3
  Downloaded chacha20 v0.10.2
  Downloaded httparse v1.10.1
  Downloaded atomic-waker v1.1.2
  Downloaded rayon-core v1.13.0
  Downloaded crossbeam-utils v0.8.23
  Downloaded crossbeam-deque v0.8.8
  Downloaded crossbeam-epoch v0.9.21
  Downloaded unit-prefix v0.5.2
  Downloaded strsim v0.11.1
  Downloaded anstyle-parse v1.0.0
  Downloaded adler2 v2.0.1
  Downloaded num-traits v0.2.19
  Downloaded regex v1.13.1
  Downloaded regex-syntax v0.8.11
  Downloaded futures-channel v0.3.34
  Downloaded digest v0.11.3
  Downloaded hybrid-array v0.4.15
  Downloaded wasm-streams v0.4.2
  Downloaded idna_adapter v1.2.2
  Downloaded stable_deref_trait v1.2.1
  Downloaded icu_provider v2.3.1
  Downloaded subtle v2.6.1
  Downloaded log v0.4.34
  Downloaded prost-types v0.14.4
  Downloaded multimap v0.10.1
  Downloaded memmap2 v0.9.11
  Downloaded lz4_flex v0.14.0
  Downloaded zstd-sys v2.1.0+zstd.1.5.7
  Downloaded js-sys v0.3.105
  Downloaded indexmap v2.14.2
  Downloaded bitflags v2.13.2
  Downloaded smallvec v1.16.1
  Downloaded zerovec-derive v0.11.6
  Downloaded writeable v0.6.4
  Downloaded tracing-core v0.1.36
  Downloaded quinn-udp v0.5.15
  Downloaded base64 v0.22.1
  Downloaded fixedbitset v0.5.7
  Downloaded indicatif v0.18.6
  Downloaded anstream v1.0.0
  Downloaded aho-corasick v1.1.5
  Downloaded typenum v1.20.1
  Downloaded displaydoc v0.2.7
  Downloaded http-body v1.1.0
  Downloaded tokio-rustls v0.26.5
  Downloaded mio v1.2.3
  Downloaded reqwest v0.12.28
  Downloaded synstructure v0.14.0
  Downloaded icu_normalizer_data v2.3.0
  Downloaded flate2 v1.1.10
  Downloaded syn v2.0.119
  Downloaded typed-path v0.12.3
  Downloaded litemap v0.8.3
  Downloaded prost-build v0.14.4
  Downloaded twox-hash v2.1.4
  Downloaded itertools v0.14.0
  Downloaded futures-util v0.3.34
  Downloaded zip v8.6.0
  Downloaded zerotrie v0.2.5
  Downloaded hyper-util v0.1.20
  Downloaded libbz2-rs-sys v0.2.5
  Downloaded hashbrown v0.17.1
  Downloaded quinn v0.11.12
  Downloaded tinyvec v1.13.3
  Downloaded hyper v1.11.1
  Downloaded rayon v1.12.0
  Downloaded encode_unicode v1.0.0
  Downloaded futures v0.3.34
  Downloaded miniz_oxide v0.9.1
  Downloaded icu_properties v2.3.0
  Downloaded icu_locale_core v2.3.0
  Downloaded icu_collections v2.3.0
  Downloaded ryu v1.0.23
  Downloaded clap v4.6.7
  Downloaded webpki-roots v1.0.9
  Downloaded rustls-webpki v0.103.15
  Downloaded tower v0.5.3
  Downloaded http v1.5.0
  Downloaded prettyplease v0.2.37
  Downloaded tower-http v0.6.11
  Downloaded tokio-util v0.7.19
  Downloaded rand v0.10.2
  Downloaded zerovec v0.11.8
  Downloaded hashbrown v0.15.5
  Downloaded idna v1.1.0
  Downloaded icu_properties_data v2.3.0
  Downloaded clap_builder v4.6.7
  Downloaded portable-atomic v1.15.0
  Downloaded brotli-decompressor v5.0.3
  Downloaded zlib-rs v0.6.8
  Downloaded quinn-proto v0.11.18
  Downloaded unicode-width v0.2.2
  Downloaded rustix v1.1.5
  Downloaded rustls v0.23.45
  Downloaded windows_aarch64_gnullvm v0.52.6
  Downloaded windows_x86_64_gnullvm v0.52.6
  Downloaded regex-automata v0.4.18
  Downloaded tracing v0.1.44
  Downloaded windows_i686_gnullvm v0.52.6
  Downloaded web-sys v0.3.105
  Downloaded icu_normalizer v2.3.0
  Downloaded lzma-sys v0.1.20
  Downloaded bzip2-sys v0.1.13+1.0.8
  Downloaded libc v0.2.189
  Downloaded tokio v1.53.1
  Downloaded brotli v8.0.4
  Downloaded petgraph v0.8.3
  Downloaded windows_x86_64_gnu v0.52.6
  Downloaded windows_x86_64_msvc v0.52.6
  Downloaded windows_i686_gnu v0.52.6
  Downloaded windows_aarch64_msvc v0.52.6
  Downloaded windows_i686_msvc v0.52.6
  Downloaded ring v0.17.14
  Downloaded protoc-bin-vendored-macos-aarch_64 v3.2.0
  Downloaded windows-sys v0.61.2
  Downloaded windows-sys v0.52.0
  Downloaded linux-raw-sys v0.12.1
  Downloaded protoc-bin-vendored-macos-x86_64 v3.2.0
  Downloaded protoc-bin-vendored-linux-aarch_64 v3.2.0
  Downloaded protoc-bin-vendored-win32 v3.2.0
  Downloaded protoc-bin-vendored-linux-x86_64 v3.2.0
  Downloaded protoc-bin-vendored-linux-ppcle_64 v3.2.0
  Downloaded protoc-bin-vendored-linux-s390_64 v3.2.0
  Downloaded protoc-bin-vendored-linux-x86_32 v3.2.0
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
> Task :libsu-service:mergeReleaseNativeLibs NO-SOURCE
> Task :libsu-service:copyReleaseJniLibsProjectOnly

> Task :manager:checkProviderTracelessInvariants
TRACELESS INVARIANTS OK checks=26 points=19

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
> Task :libsu-service:generateReleaseRFile
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
> Task :libsu-service:generateReleaseAssets UP-TO-DATE
> Task :libsu-service:bundleLibRuntimeToJarRelease
> Task :libsu-service:mergeReleaseAssets
> Task :libsu-service:bundleLibCompileToJarRelease
> Task :libsu-service:createFullJarRelease
> Task :libsu-service:extractProguardFiles
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
> Task :libsu-service:lintVitalAnalyzeRelease
> Task :manager:buildJailbreakProviders
MAPLESU: per-KMI modules for android15-6.6, android15-6.6, android12-5.10, android13-5.15, android14-6.1, android16-6.12, android17-6.18
{"exitCode": 3, "inputsStable": true, "deviceExecuted": false, "managerPackaged": false, "targets": ["maplesu-root-consumer", "maplesu-ghostlock-adapter", "maplesu-dirtyfrag-native", "maplesu-dirtyfrag-bootstrap"]}

> Task :manager:buildJailbreakProviders FAILED

[Incubating] Problems report is available at: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/build/reports/problems/problems-report.html

FAILURE: Build failed with an exception.

* What went wrong:
Execution failed for task ':manager:buildJailbreakProviders' (registered in build file 'manager/build.gradle.kts').
> Process 'command '/usr/bin/python3'' finished with non-zero exit value 3

* Try:
> Run with --stacktrace option to get the stack trace.
> Run with --info or --debug option to get more log output.
> Run with --scan to get full insights from a Build Scan (powered by Develocity).
> Get more help at https://help.gradle.org.

Deprecated Gradle features were used in this build, making it incompatible with Gradle 10.

You can use '--warning-mode all' to show the individual deprecation warnings and determine if they come from your own scripts or plugins.

For more on this, please refer to https://docs.gradle.org/9.8.1/userguide/command_line_interface.html#sec:command_line_warnings in the Gradle documentation.

BUILD FAILED in 2m 41s
44 actionable tasks: 44 executed
```
