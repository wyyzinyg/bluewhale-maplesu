# 蓝鱼主流 Root 管理器参考与能力落地

本清单用于固定参考来源，不代表把这些项目的界面、包名或后端替换进蓝鱼。Fork 保留各项目原有许可证、提交历史和归属；蓝鱼只吸收与本机后端兼容、能用测试或设备回执证明的能力。

## 固定参考源码

| 项目 | 上游固定提交 | 蓝鱼账号 Fork |
| --- | --- | --- |
| Magisk | `a212cd92b74174f87c720ff849461a90943b382f` (`master`) | `wyyzinyg/Magisk` |
| KernelSU | `eeb3bbf8359434f5596b8a7875b54ac4e5fc5495` (`main`) | `wyyzinyg/KernelSU` |
| KernelSU Next | `9af7088e9fde3fbc6588dc15e137d059af3e22c8` (`dev`) | `wyyzinyg/KernelSU-Next` |
| SukiSU Ultra | `1439545f12bffe0263690ba862139b70ee5f20cf` (`main`) | Fork 异步生成，必须回读后才可标记完成 |
| APatch | `7d77b0b5e9c7b50ce025f8abbdc238940c01a7a8` (`main`) | `wyyzinyg/APatch` |
| MMRL | `6c2b778867f7f66ee2d208ee82887aa2cf9bb0bb` (`master`) | `wyyzinyg/MMRL` |
| MapleSU | `ff3aa44850ea22717fa811a17831155a85f43445` | 蓝鱼现有固定上游，不重复 Fork |

## 能力对照结论

- Magisk / KernelSU 系列成熟的授权策略、命名空间、App Profile、挂载隔离、模块与 WebUI 思路，MapleSU 基线已经有对应实现。蓝鱼保留并审计现有实现，不新增同名重复页面。
- MMRL 的模块浏览与管理体验对应蓝鱼现有模块仓库、模块详情及安装事务；本轮不重写模块系统。
- APatch 的 SuperKey/APD、KernelSU Next 与 SukiSU 的 SUSFS 等能力依赖各自内核或守护进程。当前蓝鱼没有对应后端回执时，不提供假开关、不显示伪造的“已启用”。
- 现有授权模板已支持剪贴板导入导出；现有 SU 日志已支持按模式读取、搜索、筛选和清理。审计发现的实际缺口是：日志无法形成带筛选上下文、完整性摘要和回读验证的用户证据文件。

## 32738 实际新增

`SulogEvidenceArchive` 和 SU 日志页两套 UI 的导出按钮实现以下闭环：

1. 用户通过系统文件选择器主动选择 ZIP 保存位置，不申请额外存储权限。
2. `source.log` 保存当前文件已读取的有界原始快照；`filtered.log` 保存当前搜索和类型筛选后的可见记录，两者不混淆。
3. `metadata.json` 记录格式版本、应用版本、来源文件名、筛选条件、搜索文本、记录数和读取上限。
4. `SHA256SUMS.txt` 对两个日志载荷分别计算 SHA-256；导出结果另计算整包 SHA-256。
5. 写入后从同一 SAF URI 读回，逐字节比对，再验证 ZIP 条目集合、条数和逐文件摘要；任一项失败都不提示成功。
6. JVM 测试覆盖正常往返、中文内容、空筛选结果、载荷篡改、异常 ZIP 路径及不合法计数。

## 验证边界

快速工作流只证明 JVM 测试和 Release 编译；完整 native 工作流另外证明六 KMI、L3 和包名硬门禁。任何静态或 CI 通过都不冒充真机 `uid=0`、late-load、boot-patch、覆盖安装或重启后 Root 通过。正式签名与真机验收完成前，线上更新清单继续保持原版本。
