# 构建结果

- run: 26  提交: a28464bc2894cd16181f04847aa4d220d6153f14
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
2008:> Task :manager:configureMapleSuPatch FAILED
2022:FAILURE: Build failed with an exception.
2024:* What went wrong:
2025:Execution failed for task ':manager:configureMapleSuPatch' (registered in build file 'manager/build.gradle.kts').

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
   Compiling tempfile v3.27.0
   Compiling alloc-stdlib v0.2.4
   Compiling regex v1.13.1
   Compiling prost-types v0.14.4
   Compiling serde_derive v1.0.229
   Compiling lzma-sys v0.1.20
   Compiling anstyle-query v1.1.5
   Compiling zmij v1.0.23
   Compiling radium v0.7.0
   Compiling protoc-bin-vendored-linux-x86_64 v3.2.0
   Compiling zstd-safe v7.3.0
   Compiling protoc-bin-vendored-linux-aarch_64 v3.2.0
   Compiling protoc-bin-vendored-macos-aarch_64 v3.2.0
   Compiling protoc-bin-vendored-linux-ppcle_64 v3.2.0
   Compiling portable-atomic v1.15.0
   Compiling is_terminal_polyfill v1.70.2
   Compiling protoc-bin-vendored-macos-x86_64 v3.2.0
   Compiling log v0.4.34
   Compiling protoc-bin-vendored-linux-s390_64 v3.2.0
   Compiling anstyle v1.0.14
   Compiling protoc-bin-vendored-win32 v3.2.0
   Compiling colorchoice v1.0.5
   Compiling multimap v0.10.1
   Compiling protoc-bin-vendored-linux-x86_32 v3.2.0
   Compiling prost-build v0.14.4
   Compiling protoc-bin-vendored v3.2.0
   Compiling anstream v1.0.0
   Compiling brotli-decompressor v5.0.3
   Compiling terminal_size v0.4.4
   Compiling block-buffer v0.12.1
   Compiling crypto-common v0.2.2
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
   Compiling unit-prefix v0.5.2
   Compiling itoa v1.0.18
   Compiling typed-path v0.12.3
   Compiling simd-adler32 v0.3.10
   Compiling adler2 v2.0.1
   Compiling funty v2.0.0
   Compiling xz2 v0.1.7
   Compiling bitvec v1.1.1
   Compiling zip v8.6.0
   Compiling miniz_oxide v0.9.1
   Compiling indicatif v0.18.6
   Compiling clap v4.6.7
   Compiling sha2 v0.11.0
   Compiling bsdiff-android v0.0.2
   Compiling zstd v0.13.3
   Compiling yaxpeax-arch v0.3.2
   Compiling memmap2 v0.9.11
   Compiling lz4_flex v0.14.0
   Compiling hex v0.4.3
   Compiling yaxpeax-arm v0.5.0
   Compiling flate2 v1.1.10
   Compiling ghostlock-extract v0.1.0 (/home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/jailbreak-providers/ghostlock/extractor-native)
    Finished `release` profile [optimized] target(s) in 41.55s
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
        ]
      },
      {
        "id": "plant-61821-f957accaf563",
        "engine": "plant",
        "releases": [
          "6.18.21-android17-5-gf957accaf563-ab15926176-4k"
        ],
        "variant": "CVE-2026-98260-6.18",
        "kmi": "android17-6.18",
        "kernelUapi": 6,
        "pageSize": "4k",
        "models": [
          "PYB110",
          "OnePlus 16"
        ],
        "payloadKey": "plant-61821-f957accaf563",
        "kernelRelease": "6.18.21-android17-5-gf957accaf563-ab15926176-4k",
        "runner": "plant-61821",
        "runnerFile": {
          "asset": "maplesu-93260/plant/plant-61821",
          "sha256": "e8c2530af2f4cd02d37d043d08ce3246f1aa0909e2814448b8beeab4a99ce460",
          "bytes": 48184,
          "gzip": false,
          "decodedSha256": "e8c2530af2f4cd02d37d043d08ce3246f1aa0909e2814448b8beeab4a99ce460",
          "decodedBytes": 48184
        }
      },
      {
        "id": "plant-61821-7fcbffcad3e1",
        "engine": "plant",
        "releases": [
          "6.18.21-android17-5-g7fcbffcad3e1-ab16353812-4k"
        ],
        "variant": "CVE-2026-98260-6.18",
        "kmi": "android17-6.18",
        "kernelUapi": 6,
        "pageSize": "4k",
        "models": [
          "PYB110",
          "OnePlus 16"
        ],
        "payloadKey": "plant-61821-7fcbffcad3e1",
        "kernelRelease": "6.18.21-android17-5-g7fcbffcad3e1-ab16353812-4k",
        "runner": "plant-61821",
        "runnerFile": {
          "asset": "maplesu-93260/plant/plant-61821",
          "sha256": "e8c2530af2f4cd02d37d043d08ce3246f1aa0909e2814448b8beeab4a99ce460",
          "bytes": 48184,
          "gzip": false,
          "decodedSha256": "e8c2530af2f4cd02d37d043d08ce3246f1aa0909e2814448b8beeab4a99ce460",
          "decodedBytes": 48184
        }
      },
      {
        "id": "plant-61269-242e1a07f878",
        "engine": "plant",
        "releases": [
          "6.12.69-android16-6-g242e1a07f878-ab15865446-4k"
        ],
        "variant": "CVE-2026-98260-6.12.69",
        "kmi": "android16-6.12",
        "kernelUapi": 6,
        "pageSize": "4k",
        "models": [
          "PLK110",
          "OnePlus 15",
          "PLZ110",
          "OnePlus 15T",
          "PMS110",
          "OnePlus Ace7 Pro",
          "PYF110",
          "OnePlus Ace7",
          "PLR110",
          "OnePlus Ace6T",
          "PMB110",
          "OnePlus Ace6 Ultra",
          "OPD2513",
          "OnePlus Pad3 Pro",
          "OPD2515",
          "OPPO Pad Mini",
          "OPD2511",
          "OPPO Pad 5 Pro",
          "PMA110",
          "OPPO Find X9 Ultra",
          "PLG110",
          "OPPO Find X9 Pro",
          "PLJ110",
          "OPPO Find X9",
          "PME110EX",
          "OPPO Find X9s Pro",
          "PMX110",
          "OPPO Find X10",
          "RMX5200",
          "Realme GT8 Pro",
          "RMX8899",
          "Realme Neo8"
        ],
        "payloadKey": "plant-61269-242e1a07f878",
        "kernelRelease": "6.12.69-android16-6-g242e1a07f878-ab15865446-4k",
        "runner": "plant-61269",
        "runnerFile": {
          "asset": "maplesu-93260/plant/plant-61269",
          "sha256": "440388e7bd4c8cb34437117eec361079216d66eb591abbc9da25ce7fd7ebe901",
          "bytes": 47216,
          "gzip": false,
          "decodedSha256": "440388e7bd4c8cb34437117eec361079216d66eb591abbc9da25ce7fd7ebe901",
          "decodedBytes": 47216
        }
      },
      {
        "id": "plant-61269-5fd39602326e",
        "engine": "plant",
        "releases": [
          "6.12.69-android16-6-g5fd39602326e-ab16372235-4k"
        ],
        "variant": "CVE-2026-98260-6.12.69",
        "kmi": "android16-6.12",
        "kernelUapi": 6,
        "pageSize": "4k",
        "models": [
          "PLK110",
          "OnePlus 15",
          "PLZ110",
          "OnePlus 15T",
          "PMS110",
          "OnePlus Ace7 Pro",
          "PYF110",
          "OnePlus Ace7",
          "PLR110",
          "OnePlus Ace6T",
          "PMB110",
          "OnePlus Ace6 Ultra",
          "OPD2513",
          "OnePlus Pad3 Pro",
          "OPD2515",
          "OPPO Pad Mini",
          "OPD2511",
          "OPPO Pad 5 Pro",
          "PMA110",
          "OPPO Find X9 Ultra",
          "PLG110",
          "OPPO Find X9 Pro",
          "PLJ110",
          "OPPO Find X9",
          "PME110EX",
          "OPPO Find X9s Pro",
          "PMX110",
          "OPPO Find X10",
          "RMX5200",
          "Realme GT8 Pro",
          "RMX8899",
          "Realme Neo8"
        ],
        "payloadKey": "plant-61269-5fd39602326e",
        "kernelRelease": "6.12.69-android16-6-g5fd39602326e-ab16372235-4k",
        "runner": "plant-61269",
        "runnerFile": {
          "asset": "maplesu-93260/plant/plant-61269",
          "sha256": "440388e7bd4c8cb34437117eec361079216d66eb591abbc9da25ce7fd7ebe901",
          "bytes": 47216,
          "gzip": false,
          "decodedSha256": "440388e7bd4c8cb34437117eec361079216d66eb591abbc9da25ce7fd7ebe901",
          "decodedBytes": 47216
        }
      },
      {
        "id": "plant-61238-844001fb8721",
        "engine": "plant",
        "releases": [
          "6.12.38-android16-5-g844001fb8721-ab14552068-4k"
        ],
        "variant": "CVE-2026-98260-6.12.38",
        "kmi": "android16-6.12",
        "kernelUapi": 6,
        "pageSize": "4k",
        "models": [
          "PLR110",
          "OnePlus Ace6T",
          "RMX8899",
          "Realme Neo8"
        ],
        "payloadKey": "plant-61238-844001fb8721",
        "kernelRelease": "6.12.38-android16-5-g844001fb8721-ab14552068-4k",
        "runner": "plant-61238",
        "runnerFile": {
          "asset": "maplesu-93260/plant/plant-61238",
          "sha256": "010b1c4426456e215616609bff263e8f5965fe109d3fe1ab4f95dbb351b7f271",
          "bytes": 46920,
          "gzip": false,
          "decodedSha256": "010b1c4426456e215616609bff263e8f5965fe109d3fe1ab4f95dbb351b7f271",
          "decodedBytes": 46920
        }
      },
      {
        "id": "plant-61258-7704a1ae279b",
        "engine": "plant",
        "releases": [
          "6.12.58-android16-6-g7704a1ae279b-ab15213644-4k"
        ],
        "variant": "CVE-2026-98260-6.12.58",
        "kmi": "android16-6.12",
        "kernelUapi": 6,
        "pageSize": "4k",
        "models": [
          "OPD2513",
          "OnePlus Pad3 Pro",
          "OPD2515",
          "OPPO Pad Mini"
        ],
        "payloadKey": "plant-61258-7704a1ae279b",
        "kernelRelease": "6.12.58-android16-6-g7704a1ae279b-ab15213644-4k",
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
        "id": "plant-61258-0a092cc0037a",
        "engine": "plant",
        "releases": [
          "6.12.58-android16-6-g0a092cc0037a-abogki521987229-4k"
        ],
        "variant": "CVE-2026-98260-6.12.58",
        "kmi": "android16-6.12",
        "kernelUapi": 6,
        "pageSize": "4k",
        "models": [
          "vivo",
          "iQOO"
        ],
        "payloadKey": "plant-61258-0a092cc0037a",
        "kernelRelease": "6.12.58-android16-6-g0a092cc0037a-abogki521987229-4k",
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

> Task :manager:configureMapleSuPatch FAILED
CMake Error at /usr/local/lib/android/sdk/cmake/3.22.1/share/cmake-3.22/Modules/CMakeDetermineSystem.cmake:130 (message):
  Could not find toolchain file:
  /usr/local/lib/android/sdk/ndk/26.1.10909125/build/cmake/android.toolchain.cmake
Call Stack (most recent call first):
  CMakeLists.txt:2 (project)


CMake Error: CMAKE_C_COMPILER not set, after EnableLanguage
CMake Error: CMAKE_CXX_COMPILER not set, after EnableLanguage
-- Configuring incomplete, errors occurred!

[Incubating] Problems report is available at: file:///home/runner/work/bluewhale-maplesu/bluewhale-maplesu/src/build/reports/problems/problems-report.html

FAILURE: Build failed with an exception.

* What went wrong:
Execution failed for task ':manager:configureMapleSuPatch' (registered in build file 'manager/build.gradle.kts').
> Process 'command '/usr/local/lib/android/sdk/cmake/3.22.1/bin/cmake'' finished with non-zero exit value 1

* Try:
> Run with --stacktrace option to get the stack trace.
> Run with --info or --debug option to get more log output.
> Run with --scan to get full insights from a Build Scan (powered by Develocity).
> Get more help at https://help.gradle.org.

Deprecated Gradle features were used in this build, making it incompatible with Gradle 10.

You can use '--warning-mode all' to show the individual deprecation warnings and determine if they come from your own scripts or plugins.

For more on this, please refer to https://docs.gradle.org/9.8.1/userguide/command_line_interface.html#sec:command_line_warnings in the Gradle documentation.

BUILD FAILED in 2m 52s
46 actionable tasks: 46 executed
```
