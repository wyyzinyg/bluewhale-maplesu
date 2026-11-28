#!/usr/bin/env python3
"""32750 (3.22.11-bw): 蓝鱼不再自带提权，把所有"自我越狱"入口摘干净。

决定（2026-11-28，用户）：越狱不再自己做，root 由外部提权工具（月虹类）提供，
BluefishSU 只做 root 到手之后的管理面。于是界面上任何"蓝鱼会帮你提权"的暗示
都必须消失——留着最坏的结果是用户点一圈失败，以为这 App 是坏的。

1. HomeMiuix.kt 的 RootAccessCardMiuix：删掉【越狱】那个 TextButton（onNoRootClick
   那条），文案不再承诺"本地通道"。
2. HomeScreen.kt：整块移除 JailbreakSelectionDialog 的调用。那个三选一弹窗
   （DirtyFrag / Ghostlock / BluefishSU 98260）从此没有任何可达路径。

Bumps 32749/3.22.10-bw -> 32750/3.22.11-bw.
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else "src")

HOME_MIUIX = "manager/src/main/java/com/maplesu/core/ui/screen/home/HomeMiuix.kt"
HOME_SCREEN = "manager/src/main/java/com/maplesu/core/ui/screen/home/HomeScreen.kt"
GRADLE = "manager/build.gradle.kts"

OLD_JB_BUTTON = '''                Spacer(Modifier.width(10.dp))
                TextButton(
                    text = "越狱",
                    onClick = onNoRootClick,
                    colors = ButtonDefaults.textButtonColors(
                        color = Color(0xFF2563EB),
                        textColor = Color.White,
                    ),
                )'''

NEW_JB_BUTTON = '''                // 3.22.11-bw：蓝鱼不再自带提权，越狱按钮移除。
                // root 由外部提权工具提供，这里只留「安装」这条路。'''

OLD_HINT = '''                text = if (checking) "探测结束后这里会给出安装或越狱入口"
                        else "选一条路径：装系统环境，或用本地通道提权",'''

NEW_HINT = '''                text = if (checking) "探测结束后这里会给出安装入口"
                        else "未检测到系统环境，点「安装」开始准备",'''

NOTE_JB_DIALOG = "    // 3.22.11-bw：蓝鱼不再自带提权，越狱选择弹窗整体移除（root 由外部工具提供）。"


def _drop_brace_block(text: str, marker: str, note: str, label: str) -> str:
    """从 marker 开始，按大括号配对删掉整块；找不到只告警，不抛异常。"""
    idx = text.find(marker)
    if idx < 0:
        print("WARN 32750: %s marker not found" % label)
        return text
    start = text.find("{", idx)
    if start < 0:
        print("WARN 32750: %s has no brace" % label)
        return text
    depth = 0
    i = start
    while i < len(text):
        ch = text[i]
        if ch == '"':
            i += 1
            while i < len(text) and text[i] != '"':
                if text[i] == "\\":
                    i += 1
                i += 1
        elif ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                end = i + 1
                cut = text[:idx] + note + "\n" + text[end:]
                print("patched: %s (%d chars removed)" % (label, end - idx))
                return cut
        i += 1
    print("WARN 32750: %s brace not balanced" % label)
    return text


def patch_home_miuix(root: Path) -> None:
    p = root / HOME_MIUIX
    if not p.is_file():
        print("SKIP 32750: missing %s" % HOME_MIUIX)
        return
    text = p.read_text(encoding="utf-8")
    changed = False

    if OLD_JB_BUTTON in text:
        text = text.replace(OLD_JB_BUTTON, NEW_JB_BUTTON, 1)
        print("patched: removed jailbreak button")
        changed = True
    else:
        print("WARN 32750: jailbreak button anchor not found (tree may be stale)")

    if OLD_HINT in text:
        text = text.replace(OLD_HINT, NEW_HINT, 1)
        print("patched: rewrote root card hint strings")
        changed = True
    else:
        print("WARN 32750: hint anchor not found")

    if changed:
        p.write_text(text, encoding="utf-8")


def patch_home_screen(root: Path) -> None:
    p = root / HOME_SCREEN
    if not p.is_file():
        print("SKIP 32750: missing %s" % HOME_SCREEN)
        return
    text = p.read_text(encoding="utf-8")
    new_text = _drop_brace_block(text, "if (showJailbreakSelection) {", NOTE_JB_DIALOG, "jailbreak dialog block")
    if new_text != text:
        p.write_text(new_text, encoding="utf-8")


def bump_version(root: Path) -> None:
    p = root / GRADLE
    if not p.is_file():
        print("SKIP bump: missing %s" % GRADLE)
        return
    text = p.read_text(encoding="utf-8")
    pairs = (("versionCode = 32749", "versionCode = 32750"),
             ('versionName = "3.22.10-bw"', 'versionName = "3.22.11-bw"'))
    hit = 0
    for old, new in pairs:
        if old in text:
            text = text.replace(old, new, 1)
            hit += 1
        else:
            print("WARN bump: '%s' not found (dry tree may be stale)" % old)
    if hit:
        p.write_text(text, encoding="utf-8")
        print("bumped manager version -> 32750/3.22.11-bw")


def main() -> None:
    print("32750: bluefishsu stops shipping self-jailbreak")
    patch_home_miuix(ROOT)
    patch_home_screen(ROOT)
    bump_version(ROOT)


if __name__ == "__main__":
    main()
