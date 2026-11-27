#!/usr/bin/env python3
"""32740: dual home entries (no-root + patch boot image) and native package fixes."""
from pathlib import Path


def patch_home_patch_entry(root: Path) -> None:
    rel = "manager/src/main/java/com/maplesu/core/ui/screen/home/HomeMiuix.kt"
    path = root / rel
    text = path.read_text(encoding="utf-8")
    if "RootAccessCardMiuix" in text:
        print(f"skip: {rel} already combined")
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
                                RootAccessCardMiuix(
                                    onNoRootClick = actions.onJailbreakClick,
                                    onPatchBootClick = actions.onInstallClick,
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
            onClick = onNoRootClick,
        )
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

"""
    if marker not in text:
        raise SystemExit("FATAL: About7kCard marker not found")
    text = text.replace(marker, func + marker, 1)
    path.write_text(text, encoding="utf-8")
    print(f"patched {rel}: combined root entry card")


def patch_patch_entry_strings(root: Path) -> None:
    resources = [
        ("manager/src/main/res/values/strings.xml", [
            ("home_patch_boot_entry_title", "Patch boot image"),
            ("home_patch_boot_entry_summary", "BootLoader unlocked: patch boot / init_boot and flash"),
            ("home_root_access_title", "Root access"),
            ("home_root_access_summary", "Choose how to get root on this device"),
            ("home_root_access_status", "Inactive"),
        ]),
        ("manager/src/main/res/values-zh-rCN/strings.xml", [
            ("home_patch_boot_entry_title", "修补 Boot 镜像"),
            ("home_patch_boot_entry_summary", "已解锁 BootLoader：修补 boot / init_boot 镜像后刷入"),
            ("home_root_access_title", "Root 权限"),
            ("home_root_access_summary", "选择适合这台设备的获取方式"),
            ("home_root_access_status", "未激活"),
        ]),
    ]
    for rel, strings in resources:
        path = root / rel
        text = path.read_text(encoding="utf-8")
        for name, value in strings:
            if f'<string name="{name}">' in text:
                continue
            if "</resources>" not in text:
                raise SystemExit(f"FATAL: {rel}: resources end not found")
            text = text.replace(
                "</resources>",
                f'    <string name="{name}">{value}</string>\n</resources>',
                1,
            )
        path.write_text(text, encoding="utf-8")
        print(f"patched {rel}: combined root entry strings")


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
    print("32739-r3: combined home root entry + native package applied")
