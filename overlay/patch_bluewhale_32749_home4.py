#!/usr/bin/env python3
"""32749 (3.22.10-bw): fix the two things 3.22.9-bw got wrong.

1. `android.os.SELinux` is a @hide class. Referencing it directly fails the
   Kotlin compile with `Unresolved reference 'SELinux'` on
   InstallerPartitionReader.kt:172 — that is exactly what killed 32748.
   Replace the direct call with a reflective lookup; if the hidden-API filter
   refuses it, fall back to /sys/fs/selinux/enforce and finally to the
   /proc/self/attr/current domain, which is readable from an app process.

2. The home screen still had a second card under the Root card — the
   "未安装 / 无 Root 模式" entry plus its "修补 Boot 镜像" row. After 3.22.9-bw
   moved both actions into the Root card's button row, that block is a
   duplicate: drop it (brace-matched, so indentation drift cannot save it).

Bumps 32748/3.22.9-bw -> 32749/3.22.10-bw.
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else "src")

READER = "manager/src/main/java/dev/maplesu/manager/installer/InstallerPartitionReader.kt"
HOME = "manager/src/main/java/com/maplesu/core/ui/screen/home/HomeMiuix.kt"
GRADLE = "manager/build.gradle.kts"

OLD_SELINUX = '''    private fun selinuxStatus(): String = runCatching {
        // 3.22.9-bw：公开 API 先读；untrusted_app 打不开 /sys/fs/selinux/enforce 时
        // 以前只能写 Unknown，而设备其实是 Enforcing。
        if (android.os.SELinux.isSELinuxEnforced()) "Enforcing" else "Permissive"
    }.getOrElse {
        when (runCatching { File("/sys/fs/selinux/enforce").readText().trim() }.getOrNull()) {
            "1" -> "Enforcing"
            "0" -> "Permissive"
            else -> "Unknown"
        }
    }'''

NEW_SELINUX = '''    private fun selinuxStatus(): String = runCatching {
        // 3.22.10-bw：android.os.SELinux 是 @hide 类，直接引用编不过（32748 就死在这里）。
        // 反射取一次；被 hidden-api 拦截时退回文件，再退回自身域的判断。
        val cls = Class.forName("android.os.SELinux")
        val enforced = cls.getMethod("isSELinuxEnforced").invoke(null)
        if (enforced == true) "Enforcing" else "Permissive"
    }.getOrElse {
        when (runCatching { File("/sys/fs/selinux/enforce").readText().trim() }.getOrNull()) {
            "1" -> "Enforcing"
            "0" -> "Permissive"
            else -> when {
                runCatching { File("/proc/self/attr/current").readText() }
                    .getOrNull()?.contains("u:r:") == true -> "Enforcing"
                else -> "Unknown"
            }
        }
    }'''

DUP_MARK = "if (showNoRootEntry) {"


def _p(root: Path, rel: str) -> Path:
    return root / rel


def fix_selinux(root: Path) -> None:
    p = _p(root, READER)
    if not p.is_file():
        print("SKIP selinux: Reader missing")
        return
    text = p.read_text(encoding="utf-8")
    if "android.os.SELinux.isSELinuxEnforced()" not in text:
        if 'Class.forName("android.os.SELinux")' in text:
            print("SKIP selinux: already reflective")
        else:
            print("SKIP selinux: anchor missing")
        return
    if OLD_SELINUX not in text:
        print("SKIP selinux: block text drifted")
        return
    text = text.replace(OLD_SELINUX, NEW_SELINUX, 1)
    p.write_text(text, encoding="utf-8")
    print("patched: SELinux via reflection (no @hide reference)")


def drop_dup_card(root: Path) -> None:
    p = _p(root, HOME)
    if not p.is_file():
        print("SKIP dup: HomeMiuix missing")
        return
    text = p.read_text(encoding="utf-8")
    idx = text.find(DUP_MARK)
    if idx < 0:
        print("SKIP dup: block already gone")
        return
    # 从 DUP_MARK 的 `{` 开始做括号配平（跳过字符串里的括号）
    start = text.find("{", idx)
    depth = 0
    i = start
    in_str = False
    while i < len(text):
        ch = text[i]
        if in_str:
            if ch == "\\":
                i += 2
                continue
            if ch == '"':
                in_str = False
        else:
            if ch == '"':
                in_str = True
            elif ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
                if depth == 0:
                    break
        i += 1
    if depth != 0:
        print("SKIP dup: unbalanced braces")
        return
    end = i + 1
    # 吃掉后面的换行与行内缩进
    while end < len(text) and text[end] in "\n\r \t":
        end += 1
    text = text[:idx] + "// 3.22.10-bw：入口已并入 Root 卡按钮行，这张重复卡删除。\n" + text[end:]
    p.write_text(text, encoding="utf-8")
    print("patched: removed duplicate no-root entry card")


def bump_version(root: Path) -> None:
    path = _p(root, GRADLE)
    if not path.is_file():
        print("SKIP bump: missing %s" % GRADLE)
        return
    text = path.read_text(encoding="utf-8")
    pairs = (("versionCode = 32748", "versionCode = 32749"),
             ('versionName = "3.22.9-bw"', 'versionName = "3.22.10-bw"'))
    hit = 0
    for old, new in pairs:
        if new in text:
            hit += 1
            continue
        if old not in text:
            print("WARN bump: '%s' not found (dry tree may be stale)" % old)
            continue
        text = text.replace(old, new, 1)
        hit += 1
    path.write_text(text, encoding="utf-8")
    if hit:
        print("bumped manager version -> 32749/3.22.10-bw")


def patch_32749_home4(root: Path) -> None:
    fix_selinux(root)
    drop_dup_card(root)
    bump_version(root)


if __name__ == "__main__":
    patch_32749_home4(ROOT.resolve())
