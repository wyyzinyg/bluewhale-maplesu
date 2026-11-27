#!/usr/bin/env python3
"""32740: dual home entries (no-root + patch boot image) and native package fixes."""
from pathlib import Path


def patch_home_patch_entry(root: Path) -> None:
    rel = "manager/src/main/java/com/maplesu/core/ui/screen/home/HomeMiuix.kt"
    path = root / rel
    text = path.read_text(encoding="utf-8")
    if "PatchBootEntryCardMiuix" in text:
        print(f"skip: {rel} already patched")
        return
    old = """                        if (showNoRootEntry) {
                            Column(modifier = sideInset) {
                                NoRootEntryCardMiuix(
                                    onClick = actions.onJailbreakClick,
                                    modifier = Modifier.fillMaxWidth(),
                                    flat = flatHome,
                                )
                            }
                        }
"""
    new = """                        if (showNoRootEntry) {
                            Column(modifier = sideInset) {
                                NoRootEntryCardMiuix(
                                    onClick = actions.onJailbreakClick,
                                    modifier = Modifier.fillMaxWidth(),
                                    flat = flatHome,
                                )
                                Spacer(Modifier.height(12.dp))
                                PatchBootEntryCardMiuix(
                                    onClick = actions.onInstallClick,
                                    modifier = Modifier.fillMaxWidth(),
                                    flat = flatHome,
                                )
                            }
                        }
"""
    if old not in text:
        raise SystemExit("FATAL: no-root entry marker not found")
    text = text.replace(old, new, 1)
    marker = """@Composable
private fun About7kCard("""
    func = """@Composable
private fun PatchBootEntryCardMiuix(
    onClick: () -> Unit,
    modifier: Modifier = Modifier,
    flat: Boolean = false,
) {
    HomeCard(flat = flat, modifier = modifier) {
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
            onClick = onClick,
        )
    }
}

"""
    if marker not in text:
        raise SystemExit("FATAL: About7kCard marker not found")
    text = text.replace(marker, func + marker, 1)
    path.write_text(text, encoding="utf-8")
    print(f"patched {rel}: patch-boot entry beside no-root")


def patch_patch_entry_strings(root: Path) -> None:
    for rel, title, summary in [
        ("manager/src/main/res/values/strings.xml", "Patch boot image", "BootLoader unlocked: pick a boot or init_boot image to patch and flash"),
        ("manager/src/main/res/values-zh-rCN/strings.xml", "修补 Boot 镜像", "已解锁 BootLoader：选择 boot / init_boot 镜像修补并刷入"),
    ]:
        path = root / rel
        text = path.read_text(encoding="utf-8")
        if "home_patch_boot_entry_title" in text:
            print(f"skip: {rel} already patched")
            continue
        strings = (
            '    <string name="home_patch_boot_entry_title">' + title + "</string>\n"
            '    <string name="home_patch_boot_entry_summary">' + summary + "</string>\n"
        )
        if "</resources>" not in text:
            raise SystemExit(f"FATAL: {rel}: resources end not found")
        text = text.replace("</resources>", strings + "</resources>", 1)
        path.write_text(text, encoding="utf-8")
        print(f"patched {rel}: patch-boot entry strings")


def patch_native_package(root: Path) -> None:
    files = [
        "jailbreak-providers/dirtyfrag/adapter/bootstrap.c",
        "jailbreak-providers/android/src/main/java/dev/maplesu/manager/jailbreak/DirtyfragAttempt.java",
    ]
    for rel in files:
        path = root / rel
        if not path.is_file():
            print(f"skip missing: {rel}")
            continue
        text = path.read_text(encoding="utf-8")
        if rel.endswith(".java"):
            # Java 包名 dev.maplesu.manager.jailbreak 必须保持，只改字符串常量/路径。
            if '"dev.maplesu.manager"' not in text:
                print(f"skip: {rel} already new package")
                continue
            text = text.replace('"dev.maplesu.manager"', '"com.blue.whale.mask"')
        else:
            if "dev.maplesu.manager" not in text:
                print(f"skip: {rel} already new package")
                continue
            text = text.replace("dev.maplesu.manager", "com.blue.whale.mask")
        path.write_text(text, encoding="utf-8")
        print(f"patched {rel}: native package -> com.blue.whale.mask")


def patch_32740(root: Path) -> None:
    patch_home_patch_entry(root)
    patch_patch_entry_strings(root)
    patch_native_package(root)
    print("32739-r2: dual home entries + native package applied")
