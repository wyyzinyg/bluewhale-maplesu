# NOTICE

本仓库是 [MapleSU](https://github.com/FengQiuFQ/MapleSU) 的衍生物，仅包含品牌化补丁与构建配置，不包含上游源码本体。构构建时从上游自动拉取。

## 上游与第三方

| 项目 | 用途 | 许可 |
| --- | --- | --- |
| MapleSU（FengQiuFQ/MapleSU） | 管理器、Ultra runtime、root-loader | GPL-3.0-or-later |
| KernelSU | Normal 模式内核实现（kernelsu.ko / ksud） | 内核 GPL-2.0-only，其余 GPL-3.0-or-later |
| 7kimisu | MapleSU 管理器的直接派生基础 | 遵循上游 KSU 许可 |
| Shark v2.2.2（Yunnijian/Shark） | DirtyFrag 类提权 plant | GPL-3.0 |
| GhostLock | ghostlock 系列提供者 | 见上游 NOTICE |
| KernelPatch / SKRoot | Ultra 模式参考实现 | 见上游 NOTICE |
| libsu | su 调用库 | Apache-2.0 |
| Magisk / libsepol | 模块策略与 sepolicy 工具链 | GPL-3.0 / Apache-2.0 |

## 分发要求

1. 本仓库及其构建产物按 GPL-3.0-or-later 分发，需随附完整对应源码。
2. 越狱 plant 不得链接进 APK，必须以独立可执行文件分发，并保留上游 NOTICE 与源文件摘要（参见上游 `jailbreak-providers/shark/manifest.json` 的做法）。
3. 不得移除上游版权声明与致谢（MapleAutumn、FinaSU、KernelSU、7kimisu、KernelPatch、SKRoot）。

## 本项目新增部分

`overlay/apply_bluewhale.py`、`overlay/ic_launcher_foreground.xml`、`.github/workflows/build.yml` 与蓝鱼品牌资产，同样以 GPL-3.0-or-later 发布。
