"""32743 (3.22.4-bw): finish what 32742 left on screen.

User screenshot 2026-11-28 14:29 (after installing 32742):
  1. Home still shows a standalone notice card "运行环境还没确认。点重试…或点「重新检测」"
     — the "重新检测" button was removed in 32742, so that card now points at a
     ghost action. Remove the whole showEnvironmentRefreshWarning card.
  2. Settings still lists "发送日志" next to the new Root 诊断 card. Merge it:
     drop the send-log row (Miuix + Material); the diagnostics card already
     saves a report.

Bumps manager version 32742/3.22.3-bw -> 32743/3.22.4-bw.
"""

from pathlib import Path

HOME_REL = "manager/src/main/java/com/maplesu/core/ui/screen/home/HomeMiuix.kt"
MIUIX_REL = "manager/src/main/java/com/maplesu/core/ui/screen/settings/SettingsMiuix.kt"
MATERIAL_REL = "manager/src/main/java/com/maplesu/core/ui/screen/settings/SettingsMaterial.kt"

OLD_WARN = '''                        if (state.showEnvironmentRefreshWarning) {
                            val summary = stringResource(when (state.environmentFailure) {
                                HomeEnvironmentFailure.TIMED_OUT -> R.string.home_environment_check_timeout_summary
                                HomeEnvironmentFailure.UNCONFIRMED -> R.string.home_environment_check_unconfirmed_summary
                                HomeEnvironmentFailure.BUSY -> R.string.home_environment_check_busy_summary
                                else -> R.string.home_environment_check_failed_summary
                            })
                            Column(modifier = sideInset) {
                                WarningCard(
                                    message = stringResource(R.string.home_environment_refresh_warning, summary),
                                    level = WarningLevel.Notice,
                                    onClick = actions.onEnvironmentRetry,
                                )
                            }
                        }
'''

NEW_WARN = '''                        // 3.22.4-bw：环境提示改由 Root 卡首行承载，删掉这条指向已移除「重新检测」的警告卡。
'''

OLD_MIUIX = '''                            if (modePolicy.shows(SettingsSection.LOG_AND_ABOUT)) {
                                ArrowRowMiuix(
                                    title = stringResource(R.string.send_log),
                                    summary = null,
                                    icon = Icons.Rounded.BugReport,
                                    onClick = { showSendLogDialog = true },
                                )
                                SendLogDialog(
                                    show = showSendLogDialog,
                                    onDismissRequest = { showSendLogDialog = false },
                                    loadingDialog = loadingDialog,
                                )
'''

NEW_MIUIX = '''                            if (modePolicy.shows(SettingsSection.LOG_AND_ABOUT)) {
                                // 3.22.4-bw：发送日志并入 Root 诊断卡（保存报告），这里只留关于。
'''

OLD_MATERIAL = '''                        if (modePolicy.shows(SettingsSection.LOG_AND_ABOUT)) {
                            add {
                                ArrowRowMaterial(
                                    title = stringResource(R.string.send_log),
                                    summary = null,
                                    icon = Icons.Filled.BugReport,
                                    onClick = { showBottomSheet = true },
                                )
                            }
'''

NEW_MATERIAL = '''                        if (modePolicy.shows(SettingsSection.LOG_AND_ABOUT)) {
                            // 3.22.4-bw：发送日志并入 Root 诊断卡（保存报告），这里只留关于。
'''


def _sub_once(text: str, old: str, new: str, tag: str) -> str:
    if new.strip() in text and old not in text:
        print("skip: %s already done" % tag)
        return text
    if old not in text:
        print("skip: %s anchor missing" % tag)
        return text
    print("patched: %s" % tag)
    return text.replace(old, new, 1)


def _patch_home(root: Path) -> None:
    p = root / HOME_REL
    if not p.is_file():
        print("skip: HomeMiuix.kt missing")
        return
    text = p.read_text(encoding="utf-8")
    text = _sub_once(text, OLD_WARN, NEW_WARN, "home environment notice card")
    p.write_text(text, encoding="utf-8")


def _patch_miuix(root: Path) -> None:
    p = root / MIUIX_REL
    if not p.is_file():
        print("skip: SettingsMiuix.kt missing")
        return
    text = p.read_text(encoding="utf-8")
    text = _sub_once(text, OLD_MIUIX, NEW_MIUIX, "settings send-log (miuix)")
    p.write_text(text, encoding="utf-8")


def _patch_material(root: Path) -> None:
    p = root / MATERIAL_REL
    if not p.is_file():
        print("skip: SettingsMaterial.kt missing")
        return
    text = p.read_text(encoding="utf-8")
    text = _sub_once(text, OLD_MATERIAL, NEW_MATERIAL, "settings send-log (material)")
    p.write_text(text, encoding="utf-8")


def _bump_version(root: Path) -> None:
    gradle = root / "manager/build.gradle.kts"
    if not gradle.is_file():
        print("skip: manager/build.gradle.kts missing")
        return
    text = gradle.read_text(encoding="utf-8")
    changed = False
    for old, new in (("versionCode = 32742", "versionCode = 32743"),
                     ('versionName = "3.22.3-bw"', 'versionName = "3.22.4-bw"')):
        if old in text:
            text = text.replace(old, new, 1)
            changed = True
    if changed:
        gradle.write_text(text, encoding="utf-8")
        print("bumped manager version -> 32743/3.22.4-bw")
    else:
        print("skip: version already bumped")


def patch_32743_clean(root: Path) -> None:
    _patch_home(root)
    _patch_miuix(root)
    _patch_material(root)
    _bump_version(root)


if __name__ == "__main__":
    import sys

    patch_32743_clean(Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve())
