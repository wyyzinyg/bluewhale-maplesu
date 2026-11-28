#!/usr/bin/env python3
"""32748 (3.22.9-bw): the root card stops stacking four rows.

User screenshot 19:25 on 32747 and request "make it look like SukiSU Nova":

  The card carried a badge, a headline row, a jailbreak button floating in the
  middle and a second arrow row underneath — four competing targets in one
  card, and the button inside the headline row sat on top of the row's own
  click target.

This patch replaces the whole RootAccessCardMiuix block (same slice anchors
32742 used, so it does not depend on the text inside) with the SukiSU shape:

  badge (未激活 / 检查中)      -> status word (未检测到 Root, 24sp)
  one line of explanation     -> two side-by-side buttons 【安装】【越狱】

The install button keeps the old behaviour (patch-boot install page), the
jailbreak button keeps opening the no-root panel.

Also: SELinux status read via android.os.SELinux.isSELinuxEnforced() first —
the old probe only read /sys/fs/selinux/enforce, which untrusted_app cannot
open on stock kernels, so the home screen said 未知 on a perfectly enforcing
device.

Bumps 32747/3.22.8-bw -> 32748/3.22.9-bw.
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else "src")

HOME = "manager/src/main/java/com/maplesu/core/ui/screen/home/HomeMiuix.kt"
READER = "manager/src/main/java/dev/maplesu/manager/installer/InstallerPartitionReader.kt"
GRADLE = "manager/build.gradle.kts"

OLD_MARK = "@Composable\nprivate fun RootAccessCardMiuix("
END_MARK = "\n@Composable\nprivate fun About7kCard("

NEW_CARD = '''@Composable
private fun RootAccessCardMiuix(
    onNoRootClick: () -> Unit,
    onPatchBootClick: () -> Unit,
    checking: Boolean = false,
    modifier: Modifier = Modifier,
    flat: Boolean = false,
) {
    HomeCard(flat = flat, modifier = modifier) {
        Column(
            modifier = Modifier
                .fillMaxWidth()
                .padding(start = 16.dp, end = 16.dp, top = 14.dp, bottom = 16.dp),
        ) {
            Row(verticalAlignment = Alignment.CenterVertically) {
                Column(modifier = Modifier.weight(1f)) {
                    Text(
                        text = stringResource(R.string.home_root_access_title),
                        fontSize = 16.sp,
                        fontWeight = FontWeight.Medium,
                        color = colorScheme.onBackground,
                    )
                    Spacer(Modifier.height(2.dp))
                    Text(
                        text = stringResource(R.string.home_root_access_summary),
                        fontSize = 13.sp,
                        color = colorScheme.onSurfaceVariantSummary,
                    )
                }
                Spacer(Modifier.width(12.dp))
                StatusTag(
                    label = if (checking) "检查中" else stringResource(R.string.home_root_access_status),
                    contentColor = colorScheme.onPrimary,
                    backgroundColor = colorScheme.primary,
                )
            }
            Spacer(Modifier.height(18.dp))
            // 3.22.9-bw：一行大字说结论，不再把四层信息堆在一张卡里。
            Text(
                text = if (checking) "正在检查 root 环境…" else "未检测到 Root",
                fontSize = 24.sp,
                fontWeight = FontWeight.SemiBold,
                color = colorScheme.onBackground,
            )
            Spacer(Modifier.height(6.dp))
            Text(
                text = if (checking) "探测结束后这里会给出安装或越狱入口"
                        else "选一条路径：装系统环境，或用本地通道提权",
                fontSize = 12.sp,
                color = colorScheme.onSurfaceVariantSummary,
            )
            Spacer(Modifier.height(16.dp))
            Row(verticalAlignment = Alignment.CenterVertically) {
                TextButton(
                    text = "安装",
                    onClick = onPatchBootClick,
                    colors = ButtonDefaults.textButtonColors(
                        color = colorScheme.primary,
                        textColor = colorScheme.onPrimary,
                    ),
                )
                Spacer(Modifier.width(10.dp))
                TextButton(
                    text = "越狱",
                    onClick = onNoRootClick,
                    colors = ButtonDefaults.textButtonColors(
                        color = Color(0xFF2563EB),
                        textColor = Color.White,
                    ),
                )
            }
        }
    }
}
'''

OLD_SELINUX = '''    private fun selinuxStatus(): String =
        when (runCatching { File("/sys/fs/selinux/enforce").readText().trim() }.getOrNull()) {
            "1" -> "Enforcing"
            "0" -> "Permissive"
            null -> "Unknown"
            else -> "Unknown"
        }'''

NEW_SELINUX = '''    private fun selinuxStatus(): String = runCatching {
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


def _rebuild_card(root: Path) -> None:
    p = root / HOME
    if not p.is_file():
        print("SKIP card: HomeMiuix.kt missing")
        return
    text = p.read_text(encoding="utf-8")
    if "3.22.9-bw：一行大字说结论" in text:
        print("SKIP card: already rebuilt")
        return
    start = text.find(OLD_MARK)
    if start < 0:
        print("SKIP card: RootAccessCardMiuix not found")
        return
    end = text.find(END_MARK, start)
    if end < 0:
        print("SKIP card: end anchor not found")
        return
    text = text[:start] + NEW_CARD + text[end:]
    p.write_text(text, encoding="utf-8")
    print("patched: RootAccessCardMiuix -> SukiSU shape (badge + headline + two buttons)")


def _fix_selinux(root: Path) -> None:
    p = root / READER
    if not p.is_file():
        print("SKIP selinux: InstallerPartitionReader.kt missing")
        return
    text = p.read_text(encoding="utf-8")
    if "android.os.SELinux.isSELinuxEnforced()" in text:
        print("SKIP selinux: already using SELinux API")
        return
    if OLD_SELINUX not in text:
        print("SKIP selinux: probe anchor missing")
        return
    text = text.replace(OLD_SELINUX, NEW_SELINUX, 1)
    p.write_text(text, encoding="utf-8")
    print("patched: selinuxStatus via android.os.SELinux + file fallback")


def bump_version(root: Path) -> None:
    path = root / GRADLE
    if not path.is_file():
        print("SKIP bump: missing %s" % GRADLE)
        return
    text = path.read_text(encoding="utf-8")
    pairs = (("versionCode = 32747", "versionCode = 32748"),
             ('versionName = "3.22.8-bw"', 'versionName = "3.22.9-bw"'))
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
        print("bumped manager version -> 32748/3.22.9-bw")


def patch_32748_home3(root: Path) -> None:
    _rebuild_card(root)
    _fix_selinux(root)
    bump_version(root)


if __name__ == "__main__":
    patch_32748_home3(ROOT.resolve())
