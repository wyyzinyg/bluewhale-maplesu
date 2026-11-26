#!/usr/bin/env python3
"""蓝鱼 3.20.0 收口（32736）：首页信息架构重排 + 无 Root 口径 + Tiana 备用镜像位

按 3.20.0 方案实现三件事，只做方案里写明的改动，不顺手扩功能：

  1. 首页信息架构重排（只动 Miuix 默认首页，Material 保持原样）
     把 `HomeBetaBanner(...)` 从列表顶部移到 `InfoCard` 之前。改完之后顺序是
     状态卡 → 工作模式 → 安装/环境卡 → 警告卡 → 内测横幅 → 设备信息 → 关于，
     首次进入不再先看到黄色内测横幅。

  2. 无 Root 口径
     逐条改 `res/values*/` 里 <string> 的**正文**（不动资源名）：
     越狱/越獄 → 无 Root/無 Root，"越狱模式" → "无 Root 模式"，
     "开始越狱" → "开始无 Root 激活"，"自动越狱" → "自动激活"，
     "越狱日志" → "无 Root 日志"；英文 Jailbreak → No-root（"Jailbreak mode" 等按短语改）。
     只改文案：Shizuku / Ghostlock / 内核逻辑、权限声明、资源名一律不碰。

  3. Tiana 备用镜像的落点
     Tiana 文件存储的直链带 `_fs_scope` 鉴权，匿名 curl 是 403，不能写进 update.json。
     所以这里只在更新通道里留一个**空的** `TIANA_UPDATE_URL` 常量：
     留空 ⇒ 该镜像整条跳过，CloudBase 主站 + GitHub raw 兜底不受影响；
     等 Tiana Web 上有了匿名可读的 update.json，把地址填进这个常量即可，
     不需要再改 fetch 逻辑，也不需要动 update.json 的格式。

用法：
    python3 overlay/patch_bluewhale_320.py <上游源码根目录>

幂等：已应用过（版本已是 32736）就只做自检、不重复改，退出码仍为 0。
每个锚点必须唯一命中；命中不了直接失败退出，宁可不打补丁，也不要出一个半改的包。
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "src").resolve()
failures: list[str] = []
notices: list[str] = []
changed_files: list[str] = []

VERSION_CODE = "32736"
VERSION_NAME = "3.20.0-bw"
PREV_CODE = "32735"
PREV_NAME = "3.19.0-bw"


def read_raw(rel: str) -> str | None:
    """按原样读（newline=""）：CRLF 原样保留，改完再按原样写回，diff 才只剩真正改动的行。"""
    path = ROOT / rel
    if not path.is_file():
        failures.append(f"缺文件: {rel}")
        return None
    with open(path, "r", encoding="utf-8", newline="") as handle:
        return handle.read()


def read(rel: str) -> str | None:
    """读成 LF 归一后的文本（结构类替换用它，锚点里就只用写 \\n）。"""
    raw = read_raw(rel)
    return None if raw is None else raw.replace("\r\n", "\n")


def write(rel: str, text: str, like: str | None = None) -> None:
    """写回；若原文件是 CRLF（like 里带 \\r\\n），把行尾还原成 CRLF。"""
    if like is not None and "\r\n" in like:
        text = text.replace("\r\n", "\n").replace("\n", "\r\n")
    with open(ROOT / rel, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    if rel not in changed_files:
        changed_files.append(rel)


def replace_once(rel: str, old: str, new: str, note: str) -> None:
    """把 old 换成 new；old 必须恰好出现一次，否则记失败。"""
    raw = read_raw(rel)
    if raw is None:
        return
    text = raw.replace("\r\n", "\n")
    hits = text.count(old)
    if hits != 1:
        failures.append(f"{rel}: 期望 1 处，实际 {hits} 处 → {old.strip()[:60]!r}")
        return
    write(rel, text.replace(old, new), like=raw)
    print(f"改好 {rel}: {note}")


# —— 0. 幂等：先看版本，已经在 32736 就只自检 ——
gradle_rel = "manager/build.gradle.kts"
gradle_raw = read_raw(gradle_rel)
gradle_text = None if gradle_raw is None else gradle_raw.replace("\r\n", "\n")
already = gradle_text is not None and f"versionCode = {VERSION_CODE}" in gradle_text

# —— 1. 版本 ——
if gradle_text is not None:
    if already:
        notices.append(f"版本已是 {VERSION_CODE}/{VERSION_NAME}，跳过改动")
    else:
        for old, new in ((f"versionCode = {PREV_CODE}", f"versionCode = {VERSION_CODE}"),
                         (f'versionName = "{PREV_NAME}"', f'versionName = "{VERSION_NAME}"')):
            hits = gradle_text.count(old)
            if hits != 1:
                failures.append(f"{gradle_rel}: 版本锚点 {old!r} 命中 {hits} 处")
                continue
            gradle_text = gradle_text.replace(old, new)
        if not failures:
            write(gradle_rel, gradle_text, like=gradle_raw)
            print(f"版本 → {VERSION_NAME} / {VERSION_CODE}")

# —— 2. 首页重排（Miuix） ——
# 已应用过就整段跳过：横幅已被移走，再找原锚点会命中 0 处（这不是上游变了，是补丁已经生效）。
MIUIX = "manager/src/main/java/com/maplesu/core/ui/screen/home/HomeMiuix.kt"
BANNER = "                        HomeBetaBanner(onClick = actions.onFeedbackClick)\n"
INFO_BLOCK = (
    "                        Column(\n"
    "                            modifier = sideInset,\n"
    "                            verticalArrangement = Arrangement.spacedBy(12.dp),\n"
    "                        ) {\n"
    "                        InfoCard("
)
miuix_raw = None if already else read_raw(MIUIX)
miuix = None if miuix_raw is None else miuix_raw.replace("\r\n", "\n")
if miuix is not None:
    if BANNER not in miuix:
        if INFO_BLOCK in miuix and "HomeBetaBanner" in miuix:
            notices.append("内测横幅已不在顶部，视为已重排")
        else:
            failures.append(f"{MIUIX}: 找不到内测横幅行（上游可能改过布局）")
    elif miuix.count(BANNER) != 1:
        failures.append(f"{MIUIX}: 内测横幅行命中 {miuix.count(BANNER)} 处")
    elif miuix.count(INFO_BLOCK) != 1:
        failures.append(f"{MIUIX}: InfoCard 分组块命中 {miuix.count(INFO_BLOCK)} 处")
    else:
        moved = miuix.replace(BANNER, "", 1)
        moved = moved.replace(INFO_BLOCK, INFO_BLOCK.replace("                        InfoCard(",
                                                             BANNER + "                        InfoCard("), 1)
        write(MIUIX, moved, like=miuix_raw)
        print(f"改好 {MIUIX}: 内测横幅移到 InfoCard 之前（状态卡前置）")

# —— 3. 无 Root 口径 ——
# 先长短语、后单词，避免“越狱模式”被先拆成“无 Root 模式”以外的碎片。
ZH_RULES = [
    ("重新越狱选择", "重新激活并选择"),
    ("再次越狱选择", "再次启用并选择"),
    ("开始越狱", "开始无 Root 激活"),
    ("重新越狱", "重新激活"),
    ("再次越狱", "再次激活"),
    ("自动越狱", "自动激活"),
    ("本次越狱", "本次激活"),
    ("下次越狱生效", "下次激活生效"),
    ("越狱模式", "无 Root 模式"),
    ("越狱日志", "无 Root 日志"),
    ("越狱工作环境", "无 Root 工作环境"),
    ("全设备越狱提权", "全设备无 Root 提权"),
    ("越狱可能失败", "无 Root 激活可能失败"),
    ("收起窗口后越狱会继续运行", "收起窗口后无 Root 激活会继续运行"),
    ("确认越狱成功后", "确认激活成功后"),
    ("处理越狱引入的", "处理无 Root 激活引入的"),
    ("选择越狱方式", "选择激活方式"),
    ("隐藏越狱 SELinux 修改", "隐藏无 Root 激活的 SELinux 修改"),
    ("越狱", "无 Root"),
]
ZH_TW_RULES = [
    ("再次越獄選擇", "再次啟用並選擇"),
    ("開始越獄", "開始無 Root 啟用"),
    ("重新越獄", "重新啟用"),
    ("再次越獄", "再次啟用"),
    ("自動越獄", "自動啟用"),
    ("本次越獄", "本次啟用"),
    ("越獄模式", "無 Root 模式"),
    ("越獄日誌", "無 Root 日誌"),
    ("越獄可能失敗", "無 Root 啟用可能失敗"),
    ("越獄", "無 Root"),
]
EN_RULES = [
    ("during jailbreak mode", "during no-root mode"),
    ("Start a jailbreak", "Start an activation"),
    ("Start a Jailbreak", "Start an activation"),
    ("Jailbreak mode active", "No-root mode active"),
    ("Jailbreak mode", "No-root mode"),
    ("Jailbreak logs", "No-root logs"),
    ("Jailbreak environment", "No-root environment"),
    ("Jailbreak may have failed", "No-root activation may have failed"),
    ("confirmed jailbreak sessions", "confirmed activation sessions"),
    ("from the jailbreak", "from the activation"),
    ("Supports jailbreak privilege escalation", "Supports no-root privilege escalation"),
    ("This jailbreak has no original status snapshot", "This no-root session has no original status snapshot"),
    ("Fully reboot and jailbreak with the current version", "Fully reboot and activate again with the current version"),
    ("Saved for the next jailbreak", "Saved for the next activation"),
    ("jailbreak again", "activate again"),
    ("re-jailbreak", "re-activate"),
    ("Jailbreak", "No-root"),
    ("jailbreak", "no-root"),
]

STRING_RE = re.compile(r"(<string\b[^>]*>)(.*?)(</string>)", re.S)
TAG_RE = re.compile(r"<string\b[^>]*\bname=\"([^\"]+)\"")


def rules_for(values_dir: str) -> list[tuple[str, str]]:
    if values_dir in ("values-zh-rTW", "values-zh-rHK", "values-zh-rMO"):
        return ZH_TW_RULES
    if values_dir.startswith("values-zh"):
        return ZH_RULES
    return EN_RULES


def rewrite_body(body: str, rules: list[tuple[str, str]]) -> str:
    # 独立成句的 “越狱”/“Jailbreak” 是首页入口与预检标题，按方案叫「无 Root 模式」。
    bare = body.strip()
    for standalone, replacement in (("越狱", "无 Root 模式"), ("越獄", "無 Root 模式"),
                                    ("Jailbreak", "No-root mode")):
        if bare == standalone:
            lead = body[: len(body) - len(body.lstrip())]
            trail = body[len(body.rstrip()):]
            return lead + replacement + trail
    for old, new in rules:
        body = body.replace(old, new)
    # 中文与 “无 Root” 之间补一个空格，读起来不挤（"开始无Root" → "开始无 Root"）。
    body = re.sub(r"(?<=[\u4e00-\u9fff])无 Root", "无 Root", body)
    return body


def sweep_strings() -> None:
    res = ROOT / "manager/src/main/res"
    if not res.is_dir():
        failures.append("缺目录: manager/src/main/res")
        return
    touched = 0
    for values in sorted(res.glob("values*")):
        if not values.is_dir():
            continue
        rules = rules_for(values.name)
        for xml in sorted(values.glob("*.xml")):
            with open(xml, "r", encoding="utf-8", newline="") as handle:
                raw = handle.read()

            def repl(match: re.Match[str]) -> str:
                head, body, tail = match.group(1), match.group(2), match.group(3)
                new = rewrite_body(body, rules)
                return head + new + tail if new != body else match.group(0)

            new_raw = STRING_RE.sub(repl, raw)
            if new_raw != raw:
                with open(xml, "w", encoding="utf-8", newline="") as handle:
                    handle.write(new_raw)
                rel = str(xml.relative_to(ROOT))
                if rel not in changed_files:
                    changed_files.append(rel)
                touched += 1
    print(f"无 Root 口径：改写 {touched} 个资源文件")


sweep_strings()

# —— 4. Tiana 备用镜像位 ——
UPDATE_KT = "manager/src/main/java/com/maplesu/core/ui/util/ManagerUpdate.kt"
OLD_FALLBACKS = (
    "private val MANAGER_UPDATE_FALLBACKS = listOf(\n"
    '    "https://bluewhale-brand-bluewhale-update-d8e0r9wc21f00b8.webapps.tcloudbase.com/update.json",\n'
    '    "https://raw.githubusercontent.com/wyyzinyg/bluewhale-maplesu/main/release/update.json",\n'
    ")\n"
)
NEW_FALLBACKS = (
    "/**\n"
    " * Tiana 备用镜像（3.20.0）。\n"
    " *\n"
    " * Tiana 文件存储的直链带 `_fs_scope` 鉴权参数，匿名请求返回 403，不能直接写进 update.json；\n"
    " * 这里只接受 Tiana Web 上匿名可读的 update.json。留空表示该镜像整条跳过，\n"
    " * 主站（CloudBase）与 GitHub raw 兜底的顺序和语义都不变。\n"
    " *\n"
    " * 发布侧把地址填进下面这个常量即可，无需再改 fetch 逻辑，也无需改 update.json 的字段。\n"
    " */\n"
    'internal const val TIANA_UPDATE_URL = ""\n'
    "\n"
    "private val MANAGER_UPDATE_FALLBACKS = listOf(\n"
    '    "https://bluewhale-brand-bluewhale-update-d8e0r9wc21f00b8.webapps.tcloudbase.com/update.json",\n'
    '    "https://raw.githubusercontent.com/wyyzinyg/bluewhale-maplesu/main/release/update.json",\n'
    ") + listOfNotNull(TIANA_UPDATE_URL.takeIf { it.isNotBlank() })\n"
)
if already:
    notices.append("更新通道已有 Tiana 镜像位，跳过")
else:
    replace_once(UPDATE_KT, OLD_FALLBACKS, NEW_FALLBACKS,
                 "更新通道加 Tiana 备用镜像位（默认留空=跳过）")

# —— 5. 自检 ——
res = ROOT / "manager/src/main/res"
leftovers: list[str] = []
if res.is_dir():
    for xml in sorted(res.glob("values*/*.xml")):
        if "values-zh" in str(xml.parent) or xml.parent.name == "values":
            with open(xml, "r", encoding="utf-8", newline="") as handle:
                text = handle.read()
            for body in STRING_RE.finditer(text):
                if re.search(r"越狱|越獄|\bJailbreak\b", body.group(2)):
                    leftovers.append(f"{xml.relative_to(ROOT)}:{TAG_RE.search(body.group(1)).group(1)}")
if leftovers:
    failures.append(f"仍有 {len(leftovers)} 条越狱/Jailbreak 文案：" + ", ".join(leftovers[:5]))

if gradle_text is not None and f"versionCode = {VERSION_CODE}" not in read(gradle_rel):
    failures.append(f"{gradle_rel}: 版本未落到 {VERSION_CODE}")

update_text = read(UPDATE_KT)
if update_text is not None and "TIANA_UPDATE_URL" not in update_text:
    failures.append(f"{UPDATE_KT}: 缺 TIANA_UPDATE_URL 常量")

if failures:
    print("\n3.20.0 补丁失败：", file=sys.stderr)
    for item in failures:
        print(" - " + item, file=sys.stderr)
    sys.exit(1)

print()
if notices:
    for item in notices:
        print("注意: " + item)
print(f"3.20.0 补丁已应用：改动 {len(changed_files)} 个文件。")
for rel in changed_files[:20]:
    print("  · " + rel)
if len(changed_files) > 20:
    print(f"  · …… 其余 {len(changed_files) - 20} 个")
