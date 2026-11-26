#!/usr/bin/env python3
"""蓝鱼 3.20.1 收口（32737）：内核认主 + 首页两处 UI 修复

对应 3.20.x 方案第 4 节「验证通过后的正式 3.20.1」。三块改动：

A. 构建期包名（「late-load 成功却没有 root」的硬根因）
   ko / ksud 是按包名匹配管理器的，而 manifest.json、Kbuild、ksud/build.rs 三处默认值
   还是上游的 dev.maplesu.manager，于是内核只认旧包名。这里把三处默认值统一成
   com.blue.whale.mask（.pr 变体同步加 .pr 后缀），build_ksud.sh / build_lkm.sh
   本来就读 manifest.json 的 packageName、也支持 KSU_PACKAGE_NAME 覆盖，不用改。

B. late-load 的拉起目标
   ksud 重启管理器写死的是 me.weishu.kernelsu.ui.MainActivity（KernelSU 的类名），
   本 App 是 com.maplesu.core.ui.MainActivity。改成后者。（注意：包名对齐后
   late_load 会走 MapleSU handover 分支直接 return，不会强停管理器——这是上限，
   不是 bug；这一项修的是 PR / 其他包名变体下的拉起。）

C. 首页两处 UI（只动 Miuix 默认首页）
   1. 内测横幅再往下沉一层：从 InfoCard 之前移到 About7kCard 之后（首屏彻底不见）。
   2. 未激活设备上加一张独立的「无 Root 模式」入口卡：位置在环境检查结果之后、
      状态卡之前，点击打开现有的无 Root 选择弹窗（复用 HomeActions.onJailbreakClick，
      不新增对话框、不新增权限）。
      可见判据在 HomePager 里算（与其它管理器专属入口共用隐身互斥判据），
      卡片本身只负责画。

用法（跑在 patch_bluewhale_320.py 之后）：
    python3 overlay/patch_bluewhale_321.py <上游源码根目录>

幂等：版本已是 32737 就只自检、不重复改。任一锚点命中数不为 1 直接非零退出。
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "src").resolve()
failures: list[str] = []
notices: list[str] = []
changed: list[str] = []

VERSION_CODE = "32737"
VERSION_NAME = "3.20.1-bw"
PREV_CODE = "32736"
PREV_NAME = "3.20.0-bw"
OLD_PKG = "dev.maplesu.manager"
NEW_PKG = "com.blue.whale.mask"

HOME_MIUIX = "manager/src/main/java/com/maplesu/core/ui/screen/home/HomeMiuix.kt"
HOME_SCREEN = "manager/src/main/java/com/maplesu/core/ui/screen/home/HomeScreen.kt"
GRADLE = "manager/build.gradle.kts"


def read_raw(rel: str) -> str | None:
    path = ROOT / rel
    if not path.is_file():
        failures.append(f"缺文件: {rel}")
        return None
    with open(path, "r", encoding="utf-8", newline="") as handle:
        return handle.read()


def read(rel: str) -> str | None:
    raw = read_raw(rel)
    return None if raw is None else raw.replace("\r\n", "\n")


def write(rel: str, text: str, like: str | None = None) -> None:
    if like is not None and "\r\n" in like:
        text = text.replace("\r\n", "\n").replace("\n", "\r\n")
    with open(ROOT / rel, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    if rel not in changed:
        changed.append(rel)


def replace_once(rel: str, old: str, new: str, note: str) -> None:
    raw = read_raw(rel)
    if raw is None:
        return
    text = raw.replace("\r\n", "\n")
    hits = text.count(old)
    if hits != 1:
        failures.append(f"{rel}: {note} —— 期望 1 处，实际 {hits} 处")
        return
    write(rel, text.replace(old, new), like=raw)
    print(f"改好 {rel}: {note}")


gradle_raw = read_raw(GRADLE)
gradle_text = None if gradle_raw is None else gradle_raw.replace("\r\n", "\n")
already = gradle_text is not None and f"versionCode = {VERSION_CODE}" in gradle_text

# —— A. 构建期包名 ——
# verify_payload.py §5d 的三重校验要求三处同值：manifest.identity.managerPackage、
# applied/kernel/Kbuild 的 KSU_MANAGER_PACKAGE、applied/userspace/ksud/build.rs 的
# cargo:rustc-env=KSU_PACKAGE_NAME。少改一处，构建会直接卡在 verify_payload。
MANIFEST = "third_party/kernelsu/manifest.json"
KBUILD = "third_party/kernelsu/applied/kernel/Kbuild"
BUILD_RS = "third_party/kernelsu/applied/userspace/ksud/build.rs"

if already:
    notices.append("包名已对齐，跳过")
else:
    # manifest 里共有 6 处带点的旧包名（身份两处 + sources 两处 + checks 两处 + 摘要一处），
    # 另外还有一行是指纹补丁的 JNI 符号摘要（Java_dev_maplesu_manager_*），那行不能动。
    MANIFEST_EDITS = [
        # 身份：packageName 与 managerPackage 必须同值（verify_payload §5d 逐字比对）
        ('"packageName": "dev.maplesu.manager",', f'"packageName": "{NEW_PKG}",', 1),
        ('"managerPackage": "dev.maplesu.manager",', f'"managerPackage": "{NEW_PKG}",', 1),
        # sources：来源记录，跟着真实 Kbuild / build.rs 走
        ('"kernel/Kbuild: KSU_MANAGER_PACKAGE ?= dev.maplesu.manager",',
         f'"kernel/Kbuild: KSU_MANAGER_PACKAGE ?= {NEW_PKG}",', 1),
        ('"userspace/ksud/build.rs: cargo:rustc-env=KSU_PACKAGE_NAME=dev.maplesu.manager",',
         f'"userspace/ksud/build.rs: cargo:rustc-env=KSU_PACKAGE_NAME={NEW_PKG}",', 1),
        # checks：补丁自检里写的“期望字符串”，不改就会自己判自己不通过
        ('"KSU_MANAGER_PACKAGE ?= dev.maplesu.manager"', f'"KSU_MANAGER_PACKAGE ?= {NEW_PKG}"', 1),
        ('"cargo:rustc-env=KSU_PACKAGE_NAME=dev.maplesu.manager"',
         f'"cargo:rustc-env=KSU_PACKAGE_NAME={NEW_PKG}"', 1),
        # 摘要字段（纯文档）
        ('KSU_PACKAGE_NAME=dev.maplesu.manager / KSU_MANAGER_MIN_GEN=2',
         f'KSU_PACKAGE_NAME={NEW_PKG} / KSU_MANAGER_MIN_GEN=2', 1),
    ]
    raw = read_raw(MANIFEST)
    if raw is not None:
        text = raw.replace("\r\n", "\n")
        ok = True
        for old, new_value, expect in MANIFEST_EDITS:
            hits = text.count(old)
            if hits != expect:
                failures.append(f"{MANIFEST}: 锚点命中 {hits} 处（期望 {expect}）→ {old[:56]!r}")
                ok = False
                continue
            text = text.replace(old, new_value)
        if ok:
            write(MANIFEST, text, like=raw)
            print(f"改好 {MANIFEST}: 身份 / sources / checks / 摘要 共 {len(MANIFEST_EDITS)} 处包名")

    # Kbuild：认主宏（三重校验）与 .pr 变体。
    replace_once(KBUILD, f"KSU_MANAGER_PACKAGE ?= {OLD_PKG}\n",
                 f"KSU_MANAGER_PACKAGE ?= {NEW_PKG}\n",
                 "KSU_MANAGER_PACKAGE 默认值")
    replace_once(KBUILD, f"KSU_PACKAGE_NAME ?= {OLD_PKG}.pr\n",
                 f"KSU_PACKAGE_NAME ?= {NEW_PKG}.pr\n",
                 "KSU_PACKAGE_NAME 的 .pr 变体")

    # ksud 的兜底默认值（cargo 构建期写进 KSU_PACKAGE_NAME 环境）。
    replace_once(BUILD_RS, f'println!("cargo:rustc-env=KSU_PACKAGE_NAME={OLD_PKG}");',
                 f'println!("cargo:rustc-env=KSU_PACKAGE_NAME={NEW_PKG}");',
                 "ksud 的包名兜底默认值")

# —— B. late-load 拉起目标 ——
replace_once("third_party/kernelsu/applied/userspace/ksud/src/late_load.rs",
             '&format!("{package_name}/me.weishu.kernelsu.ui.MainActivity"),',
             '&format!("{package_name}/com.maplesu.core.ui.MainActivity"),',
             "late-load 重启管理器的 Activity") if not already else notices.append("已改过 late-load 拉起目标")

# 版本
if gradle_text is not None:
    if already:
        notices.append(f"版本已是 {VERSION_CODE}/{VERSION_NAME}")
    else:
        for old, new in ((f"versionCode = {PREV_CODE}", f"versionCode = {VERSION_CODE}"),
                         (f'versionName = "{PREV_NAME}"', f'versionName = "{VERSION_NAME}"')):
            if gradle_text.count(old) != 1:
                failures.append(f"{GRADLE}: 版本锚点 {old!r} 不唯一")
                continue
            gradle_text = gradle_text.replace(old, new)
        if not any("版本锚点" in item for item in failures):
            write(GRADLE, gradle_text, like=gradle_raw)
            print(f"版本 → {VERSION_NAME} / {VERSION_CODE}")

# —— C1. 横幅再下沉一层（InfoCard 之前 → About7kCard 之后） ——
BANNER = "                        HomeBetaBanner(onClick = actions.onFeedbackClick)\n"
INFO_HEAD = (
    "                        Column(\n"
    "                            modifier = sideInset,\n"
    "                            verticalArrangement = Arrangement.spacedBy(12.dp),\n"
    "                        ) {\n"
    "                        HomeBetaBanner(onClick = actions.onFeedbackClick)\n"
    "                        InfoCard("
)
ABOUT_TAIL = ("                        About7kCard(showModes = aboutShowsModes,"
              " modifier = Modifier.fillMaxWidth(), flat = flatHome)\n")

if already:
    notices.append("首页横幅已下沉，跳过")
else:
    miuix_raw = read_raw(HOME_MIUIX)
    miuix = None if miuix_raw is None else miuix_raw.replace("\r\n", "\n")
    if miuix is None:
        pass
    elif miuix.count(INFO_HEAD) != 1:
        failures.append(f"{HOME_MIUIX}: InfoCard 分组块（含横幅）命中 {miuix.count(INFO_HEAD)} 处")
    elif miuix.count(ABOUT_TAIL) != 1:
        failures.append(f"{HOME_MIUIX}: About7kCard 行命中 {miuix.count(ABOUT_TAIL)} 处")
    else:
        moved = miuix.replace(INFO_HEAD, INFO_HEAD.replace(BANNER, "", 1), 1)
        moved = moved.replace(ABOUT_TAIL, ABOUT_TAIL + BANNER, 1)
        write(HOME_MIUIX, moved, like=miuix_raw)
        print(f"改好 {HOME_MIUIX}: 内测横幅移到 About7kCard 之后（首屏不再出现）")

# —— C2. 无 Root 入口卡 ——
ENTRY_PARAM_OLD = (
    "    // Ultra 环境版本与更新提示；非 Ultra / 隐藏时为 null。\n"
    "    ultraEnvironment: UltraEnvironmentUpdatePanel? = null,\n"
    ") {\n"
)
ENTRY_PARAM_NEW = (
    "    // Ultra 环境版本与更新提示；非 Ultra / 隐藏时为 null。\n"
    "    ultraEnvironment: UltraEnvironmentUpdatePanel? = null,\n"
    "    // 3.20.1：未激活设备上的「无 Root 模式」独立入口。\n"
    "    // 判据在 HomePager 里算（含隐身互斥），首页只负责画；默认 false 即保持原行为。\n"
    "    showNoRootEntry: Boolean = false,\n"
    ") {\n"
)

ENTRY_ANCHOR = "                        // 绿色状态卡:跟其它卡片一样吃 12dp 边距(卡宽 = 屏宽 − 24dp)。"
ENTRY_BLOCK = (
    "                        // 3.20.1：环境检查结果之后给「无 Root 模式」独立入口。\n"
    "                        // 只在未激活、非 late-load、非隐身时出现（判据在 HomePager 算）。\n"
    "                        // 点击复用现有的无 Root 选择弹窗，不新增对话框、不新增权限。\n"
    "                        if (showNoRootEntry) {\n"
    "                            Column(modifier = sideInset) {\n"
    "                                NoRootEntryCardMiuix(\n"
    "                                    onClick = actions.onJailbreakClick,\n"
    "                                    modifier = Modifier.fillMaxWidth(),\n"
    "                                    flat = flatHome,\n"
    "                                )\n"
    "                            }\n"
    "                        }\n"
)

CARD_FN_OLD = "@Composable\nprivate fun About7kCard("
CARD_FN_NEW = '''@Composable
private fun NoRootEntryCardMiuix(
    onClick: () -> Unit,
    modifier: Modifier = Modifier,
    flat: Boolean = false,
) {
    HomeCard(flat = flat, modifier = modifier) {
        ArrowPreference(
            title = stringResource(R.string.home_no_root_entry_title),
            summary = stringResource(R.string.home_no_root_entry_summary),
            startAction = {
                Icon(
                    imageVector = Icons.Filled.Security,
                    contentDescription = stringResource(R.string.home_no_root_entry_title),
                    modifier = Modifier.padding(end = 6.dp),
                    tint = colorScheme.onBackground,
                )
            },
            onClick = onClick,
        )
    }
}

@Composable
private fun About7kCard('''

if already:
    notices.append("无 Root 入口卡已加，跳过")
else:
    miuix_raw = read_raw(HOME_MIUIX)
    miuix = None if miuix_raw is None else miuix_raw.replace("\r\n", "\n")
    if miuix is not None:
        ok = True
        if miuix.count(ENTRY_PARAM_OLD) != 1:
            failures.append(f"{HOME_MIUIX}: HomePagerMiuix 参数尾部命中 {miuix.count(ENTRY_PARAM_OLD)} 处")
            ok = False
        if miuix.count(ENTRY_ANCHOR) != 1:
            failures.append(f"{HOME_MIUIX}: 状态卡注释锚点命中 {miuix.count(ENTRY_ANCHOR)} 处")
            ok = False
        if miuix.count(CARD_FN_OLD) != 1:
            failures.append(f"{HOME_MIUIX}: About7kCard 定义锚点命中 {miuix.count(CARD_FN_OLD)} 处")
            ok = False
        if ok:
            miuix = miuix.replace(ENTRY_PARAM_OLD, ENTRY_PARAM_NEW, 1)
            miuix = miuix.replace(ENTRY_ANCHOR, ENTRY_BLOCK + ENTRY_ANCHOR, 1)
            miuix = miuix.replace(CARD_FN_OLD, CARD_FN_NEW, 1)
            write(HOME_MIUIX, miuix, like=miuix_raw)
            print(f"改好 {HOME_MIUIX}: 加「无 Root 模式」入口卡与参数")

# —— C3. HomePager：算可见性并传下去 ——
SCREEN_OLD = (
    "    val statusState = remember(displayState, ultraVisible) {\n"
    "        displayState.copy(ultraBrandVisible = ultraVisible)\n"
    "    }\n"
)
SCREEN_NEW = SCREEN_OLD + (
    "    // 3.20.1：「无 Root 模式」独立入口的判据。\n"
    "    // 与其它管理器专属入口共用 suppressEntries（隐身 / 隐藏确认窗口一律不画），\n"
    "    // 再加三条：未激活、非 late-load、判定未落定（litePending）时不抢先画。\n"
    "    val showNoRootEntry = !suppressEntries &&\n"
    "        !statusState.isManager &&\n"
    "        !statusState.isLateLoadMode &&\n"
    "        !statusState.litePending &&\n"
    "        !statusState.hiddenConfirming\n"
)

CALL_OLD = (
    "        UiMode.Miuix -> HomePagerMiuix(\n"
    "            state = statusState,\n"
    "            ultra = ultra,\n"
    "            aboutShowsModes = aboutShowsModes,\n"
    "            ultraEnvironment = ultraEnvironment.takeIf { ultraVisible },\n"
    "            actions = actions,\n"
    "            bottomInnerPadding = bottomInnerPadding,\n"
    "            workModeEntry = workModeEntry,\n"
    "            onOpenWorkMode = onOpenWorkMode,\n"
    "            workModeSwitch = workModeSwitch,\n"
    "        )\n"
)
CALL_NEW = CALL_OLD.replace(
    "            workModeSwitch = workModeSwitch,\n        )",
    "            workModeSwitch = workModeSwitch,\n            showNoRootEntry = showNoRootEntry,\n        )",
)

if already:
    notices.append("HomePager 判据已加，跳过")
else:
    scr_raw = read_raw(HOME_SCREEN)
    scr = None if scr_raw is None else scr_raw.replace("\r\n", "\n")
    if scr is not None:
        ok = True
        if scr.count(SCREEN_OLD) != 1:
            failures.append(f"{HOME_SCREEN}: statusState 块命中 {scr.count(SCREEN_OLD)} 处")
            ok = False
        if scr.count(CALL_OLD) != 1:
            failures.append(f"{HOME_SCREEN}: Miuix 调用块命中 {scr.count(CALL_OLD)} 处")
            ok = False
        if ok:
            scr = scr.replace(SCREEN_OLD, SCREEN_NEW, 1).replace(CALL_OLD, CALL_NEW, 1)
            write(HOME_SCREEN, scr, like=scr_raw)
            print(f"改好 {HOME_SCREEN}: 计算并传入无 Root 入口可见性")

# —— C4. 新增两条文案 ——
STRINGS = {
    "values": ("No-root mode",
               "Gain temporary root through Shizuku or an external activation tool."),
    "values-zh-rCN": ("无 Root 模式", "用 Shizuku 或外部激活工具获取临时 root 权限。"),
    "values-zh-rHK": ("無 Root 模式", "用 Shizuku 或外部啟用工具取得臨時 root 權限。"),
}

if already:
    notices.append("文案已加，跳过")
else:
    for locale, (title, summary) in STRINGS.items():
        rel = f"manager/src/main/res/{locale}/strings.xml"
        raw = read_raw(rel)
        if raw is None:
            continue
        if "home_no_root_entry_title" in raw:
            notices.append(f"{locale}: 文案已存在，跳过")
            continue
        text = raw.replace("\r\n", "\n")
        if text.count("</resources>") != 1:
            failures.append(f"{rel}: </resources> 命中 {text.count('</resources>')} 处")
            continue
        block = (
            "    <!-- 3.20.1：未激活设备首页的「无 Root 模式」入口卡 -->\n"
            f'    <string name="home_no_root_entry_title">{title}</string>\n'
            f'    <string name="home_no_root_entry_summary">{summary}</string>\n'
            "</resources>"
        )
        write(rel, text.replace("</resources>", block, 1), like=raw)
        print(f"改好 {rel}: 加 home_no_root_entry_*")

# —— 自检 ——
# 自检：逐条复刻 verify_payload.py §5d 的断言，构建前就能知道会不会挂。
manifest = read(MANIFEST)
kbuild = read(KBUILD)
build_rs = read(BUILD_RS)
if manifest is not None:
    if f'"managerPackage": "{NEW_PKG}"' not in manifest:
        failures.append("manifest: identity.managerPackage 未落到新包名")
    if f'"packageName": "{NEW_PKG}"' not in manifest:
        failures.append("manifest: identity.packageName 不是新包名（应该由 3.17.0 补丁改过）")
    leftover = [line.strip()[:80] for line in manifest.splitlines()
                if OLD_PKG in line and "Java_dev_maplesu_manager" not in line]
    if leftover:
        failures.append(f"manifest: 还有 {len(leftover)} 行旧包名 → {leftover[:3]}")
if kbuild is not None and f"KSU_MANAGER_PACKAGE ?= {NEW_PKG}" not in kbuild:
    failures.append("Kbuild: KSU_MANAGER_PACKAGE 未落到新包名（verify_payload 会挂）")
if build_rs is not None and f"cargo:rustc-env=KSU_PACKAGE_NAME={NEW_PKG}" not in build_rs:
    failures.append("build.rs: 默认包名未落到新包名（verify_payload 会挂）")
late = read("third_party/kernelsu/applied/userspace/ksud/src/late_load.rs")
if late is not None and "me.weishu.kernelsu.ui.MainActivity" in late:
    failures.append("late_load.rs: 仍指向 KernelSU 的 MainActivity")
if read(GRADLE) is not None and f"versionCode = {VERSION_CODE}" not in read(GRADLE):
    failures.append(f"{GRADLE}: 版本未落到 {VERSION_CODE}")

if failures:
    print("\n3.20.1 补丁失败：", file=sys.stderr)
    for item in failures:
        print(" - " + item, file=sys.stderr)
    sys.exit(1)

print()
for item in notices:
    print("注意: " + item)
print(f"3.20.1 补丁已应用：改动 {len(changed)} 个文件。")
for rel in changed:
    print("  · " + rel)
