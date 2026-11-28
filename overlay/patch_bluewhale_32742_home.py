"""32742 (3.22.3-bw): home root entry becomes KSU-shaped.

User request 2026-11-28:
  - "未检测到可用的 root 环境" 整行点击 -> 进入「修补 Boot 镜像」安装页。
  - 该行右侧固定一个两字按钮「越狱」-> 打开无 Root 模式面板（DirtyFrag/Ghostlock/98260）。
  - 不再并列两个箭头入口（上一版合并卡的两行结构废掉）。
  - 版本 32741/3.22.2-bw -> 32742/3.22.3-bw。

Implemented by replacing RootAccessCardMiuix (injected by patch_bluewhale_32740)
with a header row + one tappable info row carrying the jailbreak button + the
patch-boot arrow row.
"""

from pathlib import Path

OLD_MARK = "@Composable\nprivate fun RootAccessCardMiuix("
END_MARK = "\n@Composable\nprivate fun About7kCard("

NEW_CARD = '''@Composable
private fun RootAccessCardMiuix(
    onNoRootClick: () -> Unit,
    onPatchBootClick: () -> Unit,
    modifier: Modifier = Modifier,
    flat: Boolean = false,
) {
    HomeCard(flat = flat, modifier = modifier) {
        Row(
            modifier = Modifier
                .fillMaxWidth()
                .padding(start = 16.dp, end = 16.dp, top = 14.dp, bottom = 4.dp),
            verticalAlignment = Alignment.CenterVertically,
        ) {
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
                label = stringResource(R.string.home_root_access_status),
                contentColor = colorScheme.onPrimary,
                backgroundColor = colorScheme.primary,
            )
        }
        // 3.22.3-bw: 整行点进「修补 Boot 镜像」，右侧只留两字按钮「越狱」。
        Row(
            modifier = Modifier
                .fillMaxWidth()
                .clickable(onClick = onPatchBootClick)
                .padding(start = 16.dp, end = 16.dp, top = 10.dp, bottom = 10.dp),
            verticalAlignment = Alignment.CenterVertically,
        ) {
            Column(modifier = Modifier.weight(1f)) {
                Text(
                    text = "未检测到可用的 root 环境",
                    fontSize = 15.sp,
                    fontWeight = FontWeight.Medium,
                    color = colorScheme.onBackground,
                )
                Spacer(Modifier.height(2.dp))
                Text(
                    text = "点这一行，按「修补 Boot 镜像」完成环境准备",
                    fontSize = 12.sp,
                    color = colorScheme.onSurfaceVariantSummary,
                )
            }
            Spacer(Modifier.width(8.dp))
            TextButton(
                text = "越狱",
                onClick = onNoRootClick,
                colors = ButtonDefaults.textButtonColors(
                    color = Color(0xFF2563EB),
                    textColor = Color.White,
                ),
            )
        }
        ArrowPreference(
            title = stringResource(R.string.home_patch_boot_entry_title),
            summary = stringResource(R.string.home_patch_boot_entry_summary),
            startAction = {
                Icon(
                    imageVector = Icons.Filled.Build,
                    contentDescription = stringResource(R.string.home_patch_boot_entry_title),
                    modifier = Modifier.padding(end = 6.dp),
                    tint = colorScheme.onBackground,
                )
            },
            onClick = onPatchBootClick,
        )
    }
}
'''


def _rebuild_card(root: Path) -> None:
    rel = "manager/src/main/java/com/maplesu/core/ui/screen/home/HomeMiuix.kt"
    path = root / rel
    if not path.is_file():
        print("skip: HomeMiuix.kt missing")
        return
    text = path.read_text(encoding="utf-8")
    if "3.22.3-bw: 整行点进" in text:
        print("skip: home card already rebuilt")
        return
    start = text.find(OLD_MARK)
    if start < 0:
        print("skip: RootAccessCardMiuix not present (r3 combined card missing)")
        return
    end = text.find(END_MARK, start)
    if end < 0:
        raise SystemExit("FATAL: About7kCard marker not found after card")
    text = text[:start] + NEW_CARD + text[end:]
    path.write_text(text, encoding="utf-8")
    print("patched HomeMiuix.kt: KSU-shaped root entry (tap-to-patch + 越狱)")


def _bump_version(root: Path) -> None:
    gradle = root / "manager/build.gradle.kts"
    if not gradle.is_file():
        print("skip: manager/build.gradle.kts missing")
        return
    text = gradle.read_text(encoding="utf-8")
    changed = False
    for old, new in (("versionCode = 32741", "versionCode = 32742"),
                     ('versionName = "3.22.2-bw"', 'versionName = "3.22.3-bw"')):
        if old in text:
            text = text.replace(old, new, 1)
            changed = True
    if changed:
        gradle.write_text(text, encoding="utf-8")
        print("bumped manager version -> 32742/3.22.3-bw")
    else:
        print("skip: version already bumped")


def patch_32742_home(root: Path) -> None:
    _rebuild_card(root)
    _bump_version(root)


if __name__ == "__main__":
    import sys

    patch_32742_home(Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve())
