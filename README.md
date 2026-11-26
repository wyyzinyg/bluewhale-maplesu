# 蓝色大肥鱼 · MapleSU 基座

以 [MapleSU](https://github.com/FengQiuFQ/MapleSU) 源码为底子重建的蓝鱼管理器，保留蓝鱼自己的品牌与深蓝风格。

| 项 | 值 |
| --- | --- |
| 包名 | `com.blue.whale.mask`（与 3.16.0-bw 同包名同签名，可原地升级） |
| 版本 | `3.17.0-bw` / `32731` |
| 应用名 | 蓝色大肥鱼 |
| 主色 / 图标底 | `#2856D8` / `#08101F`，前景为蓝鱼矢量鲸鱼 |
| 界面 | Material + Miuix 双模 |

## 为什么用 overlay 而不是整仓复制

上游仓库 703 MB（含七套内核 Image、预编译 .so、CMake/Cargo 原生工程）。整个塞进来会让 diff 不可读，也违反上游自己的发布策略。所以本仓库只放：

- `overlay/apply_bluewhale.py` —— 品牌化补丁，逐条断言命中，改不动就报错退出
- `overlay/ic_launcher_foreground.xml` —— 蓝鱼矢量图标
- `.github/workflows/build.yml` —— 拉上游 → 打补丁 → 编 release

上游一更新，重跑一次 CI 就能跟上，而不是合并一个 703 MB 的分叉。

## 构建

本地：

```bash
curl -sSL -o /tmp/ms.tar.gz https://codeload.github.com/FengQiuFQ/MapleSU/tar.gz/refs/heads/main
mkdir -p src && tar xzf /tmp/ms.tar.gz -C src --strip-components=1
python3 overlay/apply_bluewhale.py src
cd src && ./gradlew --dependency-verification=off -PbluewhaleSkipSdkVerify=true :manager:assembleRelease
```

或者在 Actions 里跑 `build-bluewhale`（推荐：本机 4 G 内存编不动这个体量的 App，Kotlin 阶段会被内存上限杀掉）。

产物是**未签名**的 release APK，本地用 `bluewhale-release.p12` 签完再装机：

```bash
zipalign -f -p 4 app-release-unsigned.apk aligned.apk
apksigner sign --ks bluewhale-release.p12 --ks-key-alias bluewhale \
  --out 蓝色大肥鱼_3.17.0-bw_32731.apk aligned.apk
```

## 上游公开快照的两个缺口

1. `:manager:verifyUltraSdkIdentity` 引用 `.tmp/p1-source-r9-build/report/build-report.json`，公开导出里没有这个文件，自检必失败。补丁用 `-PbluewhaleSkipSdkVerify=true` 开关跳过，不删检查本身。
2. `gradle/verification-metadata.xml` 对 `protoc:4.36.1` 的校验值和实际下载到的产物对不上，构建时用 `--dependency-verification=off`。

## 许可

上游 MapleSU 为 GPL-3.0-or-later，KernelSU 内核部分 GPL-2.0-only，越狱 providers 各保留原许可（Shark v2.2.2 = GPL-3.0）。本仓库作为衍生物同样以 GPL-3.0-or-later 发布。

## 路线

- [x] 以 MapleSU 为基座重建，保留蓝鱼身份与深蓝风格
- [ ] 首页三态（未安装 / 临时 root / 永久 root）+ 冷启动不闪「未安装」
- [ ] 越狱对话框接入蓝鱼自己的三条 root 路线
- [ ] 用 root-loader 的方法重做蓝鱼极简内核模块（导入符号压到 4 个）
