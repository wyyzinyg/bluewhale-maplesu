"""32744 (3.22.5-bw): one "诊断日志" entry = diagnostics report + send log.

User decision 2026-11-28 15:20:
  "把诊断报告合并到发送日志里做成一个入口，名称就叫诊断日志；补全诊断日志你想知道的东西"

Changes:
  1. Diagnostics card title -> 诊断日志 (zh) / Diagnostics log (en).
  2. Card carries two actions: save report (Download) and send log (existing
     SendLogDialog / SendLogBottomSheet), wired through a new defaulted
     onSendLog parameter so home/settings call sites keep compiling.
  3. Settings Miuix/Material pass the send-log callback (settings is where the
     dialog lives).
  4. Report gains the fields needed for this device's half-active DirtyFrag:
     /data/adb/modules detail, /data/adb/ksu, /dev/dfm6 stat, key ro.* props,
     plus an explicit nextStep line.
  5. Bump 32743/3.22.4-bw -> 32744/3.22.5-bw.
"""

from pathlib import Path

UI_REL = "manager/src/main/java/com/maplesu/core/ui/screen/home/RootDiagnosticsUi.kt"
KT_REL = "manager/src/main/java/com/maplesu/core/ui/screen/home/RootDiagnostics.kt"
MIUIX_SET_REL = "manager/src/main/java/com/maplesu/core/ui/screen/settings/SettingsMiuix.kt"
MAT_SET_REL = "manager/src/main/java/com/maplesu/core/ui/screen/settings/SettingsMaterial.kt"
ZH_XML = "manager/src/main/res/values-zh-rCN/root_diagnostics.xml"
EN_XML = "manager/src/main/res/values/root_diagnostics.xml"

OLD_SECTION_SIG = '''internal fun RootDiagnosticsSection(
    state: HomeUiState,
    onRetry: () -> Unit,
    flat: Boolean = false,
) {
'''
NEW_SECTION_SIG = '''internal fun RootDiagnosticsSection(
    state: HomeUiState,
    onRetry: () -> Unit,
    onSendLog: () -> Unit = {},
    flat: Boolean = false,
) {
'''

OLD_MIUIX_CALL = '''        UiMode.Miuix -> RootDiagnosticsCardMiuix(
            flat = flat,
            onClick = { showSheet = true },
            onRecheck = { startCollect("card-recheck", rerunRootCheck = true, openSheet = true) },
            onCopy = { copyReport() },
        )
'''
NEW_MIUIX_CALL = '''        UiMode.Miuix -> RootDiagnosticsCardMiuix(
            flat = flat,
            onClick = { showSheet = true },
            onRecheck = { startCollect("card-recheck", rerunRootCheck = true, openSheet = true) },
            onCopy = { copyReport() },
            onSendLog = onSendLog,
        )
'''

OLD_MATERIAL_CALL = '''        UiMode.Material -> RootDiagnosticsCardMaterial(
            flat = flat,
            onClick = { showSheet = true },
            onRecheck = { startCollect("card-recheck", rerunRootCheck = true, openSheet = true) },
            onCopy = { copyReport() },
        )
'''
NEW_MATERIAL_CALL = '''        UiMode.Material -> RootDiagnosticsCardMaterial(
            flat = flat,
            onClick = { showSheet = true },
            onRecheck = { startCollect("card-recheck", rerunRootCheck = true, openSheet = true) },
            onCopy = { copyReport() },
            onSendLog = onSendLog,
        )
'''

OLD_MIUIX_SIG = '''private fun RootDiagnosticsCardMiuix(
    flat: Boolean,
    onClick: () -> Unit,
    onRecheck: () -> Unit,
    onCopy: () -> Unit,
) {
'''
NEW_MIUIX_SIG = '''private fun RootDiagnosticsCardMiuix(
    flat: Boolean,
    onClick: () -> Unit,
    onRecheck: () -> Unit,
    onCopy: () -> Unit,
    onSendLog: () -> Unit = {},
) {
'''

OLD_MATERIAL_SIG = '''private fun RootDiagnosticsCardMaterial(
    flat: Boolean,
    onClick: () -> Unit,
    onRecheck: () -> Unit,
    onCopy: () -> Unit,
) {
'''
NEW_MATERIAL_SIG = '''private fun RootDiagnosticsCardMaterial(
    flat: Boolean,
    onClick: () -> Unit,
    onRecheck: () -> Unit,
    onCopy: () -> Unit,
    onSendLog: () -> Unit = {},
) {
'''

OLD_MIUIX_ROW = '''            Row(horizontalArrangement = Arrangement.spacedBy(4.dp)) {
                MiuixTextButton(
                    text = stringResource(R.string.root_diagnostics_copy),
                    onClick = onCopy,
                    colors = MiuixButtonDefaults.textButtonColorsPrimary(),
                    modifier = Modifier.testTag("root_diagnostics_copy"),
                )
            }
'''
NEW_MIUIX_ROW = '''            Row(horizontalArrangement = Arrangement.spacedBy(4.dp)) {
                MiuixTextButton(
                    text = stringResource(R.string.root_diagnostics_copy),
                    onClick = onCopy,
                    colors = MiuixButtonDefaults.textButtonColorsPrimary(),
                    modifier = Modifier.testTag("root_diagnostics_copy"),
                )
                MiuixTextButton(
                    text = stringResource(R.string.root_diagnostics_sendlog),
                    onClick = onSendLog,
                    colors = MiuixButtonDefaults.textButtonColorsPrimary(),
                    modifier = Modifier.testTag("root_diagnostics_sendlog"),
                )
            }
'''

OLD_MATERIAL_ROW = '''            Row(horizontalArrangement = Arrangement.spacedBy(4.dp)) {
                MaterialTextButton(
                    onClick = onCopy,
                    modifier = Modifier.testTag("root_diagnostics_copy"),
                ) { MaterialText(stringResource(R.string.root_diagnostics_copy)) }
            }
'''
NEW_MATERIAL_ROW = '''            Row(horizontalArrangement = Arrangement.spacedBy(4.dp)) {
                MaterialTextButton(
                    onClick = onCopy,
                    modifier = Modifier.testTag("root_diagnostics_copy"),
                ) { MaterialText(stringResource(R.string.root_diagnostics_copy)) }
                MaterialTextButton(
                    onClick = onSendLog,
                    modifier = Modifier.testTag("root_diagnostics_sendlog"),
                ) { MaterialText(stringResource(R.string.root_diagnostics_sendlog)) }
            }
'''

OLD_SET_MIUIX = '''                if (!appearanceOnly && diagnosticsState != null) {
                    item(key = "root-diagnostics") {
                        RootDiagnosticsSection(
                            state = diagnosticsState,
                            onRetry = onDiagnosticsRetry,
                            flat = LocalFlatUi.current,
                        )
                        Spacer(Modifier.height(12.dp))
                    }
                }
'''
NEW_SET_MIUIX = '''                if (!appearanceOnly && diagnosticsState != null) {
                    item(key = "root-diagnostics") {
                        RootDiagnosticsSection(
                            state = diagnosticsState,
                            onRetry = onDiagnosticsRetry,
                            onSendLog = { showSendLogDialog = true },
                            flat = LocalFlatUi.current,
                        )
                        Spacer(Modifier.height(12.dp))
                        SendLogDialog(
                            show = showSendLogDialog,
                            onDismissRequest = { showSendLogDialog = false },
                            loadingDialog = loadingDialog,
                        )
                    }
                }
'''

OLD_SET_MATERIAL = '''                if (diagnosticsState != null) {
                    Column(modifier = GroupPadding) {
                        RootDiagnosticsSection(
                            state = diagnosticsState,
                            onRetry = onDiagnosticsRetry,
                        )
'''
NEW_SET_MATERIAL = '''                if (diagnosticsState != null) {
                    Column(modifier = GroupPadding) {
                        RootDiagnosticsSection(
                            state = diagnosticsState,
                            onRetry = onDiagnosticsRetry,
                            onSendLog = { showBottomSheet = true },
                        )
'''

KERNEL_ANCHOR = '    appendLine("kernel=" + runCatching { File("/proc/version").readText().trim() }.getOrDefault("error"))\n'
EXTRA_LINES = '''    appendLine("adb/modules=" + runCatching {
        File("/data/adb/modules").list()?.sorted()?.joinToString(",") { id ->
            val dir = File("/data/adb/modules", id)
            val state = when {
                File(dir, "remove").exists() -> "remove"
                File(dir, "disable").exists() -> "disabled"
                else -> "on"
            }
            "$id($state)"
        } ?: "none"
    }.getOrDefault("error"))
    appendLine("data/adb/ksu=" + runCatching { File("/data/adb/ksu").exists() }.getOrDefault(false))
    appendLine("/dev/dfm6 stat=" + runCatching {
        val f = File("/dev/dfm6")
        "exists=${f.exists()} readable=${f.canRead()} writable=${f.canWrite()} len=${f.length()}"
    }.getOrDefault("error"))
    appendLine("props=" + listOf("ro.build.type", "ro.debuggable", "ro.secure", "ro.build.version.sdk", "ro.product.cpu.abi")
        .joinToString(" ") { "$it=${systemProp(it)}" })
'''

CONCL_ANCHOR = '''    appendLine("D. Conclusion")
    appendLine(snapshot.conclusion)
'''
CONCL_EXTRA = '''    appendLine("nextStep=" + when {
        snapshot.adbKsud.exists || snapshot.userDeKsud.exists ->
            "ksud 已落盘；若 homepage 仍无 root，查 SU 守护启动（SELinux/权限）"
        snapshot.dfm6 ->
            "DirtyFrag 半激活：内核节点在、ksud 缺失；重启后重试越狱，或改用修补 Boot 镜像"
        else ->
            "无 root 通道；修补 Boot 镜像是最稳路径"
    })
'''

PROP_FN_ANCHOR = "\nprivate fun seccompText(state: HomeUiState): String {\n"
PROP_FN = '''
private fun systemProp(key: String): String = runCatching {
    val cls = Class.forName("android.os.SystemProperties")
    val get = cls.getMethod("get", String::class.java)
    (get.invoke(null, key) as? String)?.ifBlank { "?" } ?: "?"
}.getOrDefault("error")
'''


def _sub(text: str, old: str, new: str, tag: str) -> str:
    if new in text:
        print("skip: %s already applied" % tag)
        return text
    if old not in text:
        print("skip: %s anchor missing" % tag)
        return text
    print("patched: %s" % tag)
    return text.replace(old, new, 1)


def _ui(root: Path) -> None:
    p = root / UI_REL
    if not p.is_file():
        print("skip: RootDiagnosticsUi.kt missing")
        return
    t = p.read_text(encoding="utf-8")
    t = _sub(t, OLD_SECTION_SIG, NEW_SECTION_SIG, "section onSendLog")
    t = _sub(t, OLD_MIUIX_CALL, NEW_MIUIX_CALL, "miuix card call")
    t = _sub(t, OLD_MATERIAL_CALL, NEW_MATERIAL_CALL, "material card call")
    t = _sub(t, OLD_MIUIX_SIG, NEW_MIUIX_SIG, "miuix card sig")
    t = _sub(t, OLD_MATERIAL_SIG, NEW_MATERIAL_SIG, "material card sig")
    t = _sub(t, OLD_MIUIX_ROW, NEW_MIUIX_ROW, "miuix send-log button")
    t = _sub(t, OLD_MATERIAL_ROW, NEW_MATERIAL_ROW, "material send-log button")
    p.write_text(t, encoding="utf-8")


def _kt(root: Path) -> None:
    p = root / KT_REL
    if not p.is_file():
        print("skip: RootDiagnostics.kt missing")
        return
    t = p.read_text(encoding="utf-8")
    t = _sub(t, PROP_FN_ANCHOR, PROP_FN + PROP_FN_ANCHOR, "systemProp helper")
    t = _sub(t, KERNEL_ANCHOR, KERNEL_ANCHOR + EXTRA_LINES, "extra report fields")
    t = _sub(t, CONCL_ANCHOR, CONCL_ANCHOR + CONCL_EXTRA, "nextStep line")
    p.write_text(t, encoding="utf-8")


def _settings(root: Path) -> None:
    p = root / MIUIX_SET_REL
    if p.is_file():
        t = p.read_text(encoding="utf-8")
        t = _sub(t, OLD_SET_MIUIX, NEW_SET_MIUIX, "settings miuix send-log wiring")
        p.write_text(t, encoding="utf-8")
    p = root / MAT_SET_REL
    if p.is_file():
        t = p.read_text(encoding="utf-8")
        t = _sub(t, OLD_SET_MATERIAL, NEW_SET_MATERIAL, "settings material send-log wiring")
        p.write_text(t, encoding="utf-8")


def _strings(root: Path) -> None:
    zh = root / ZH_XML
    if zh.is_file():
        t = zh.read_text(encoding="utf-8")
        t = _sub(t, '<string name="root_diagnostics_title">Root 诊断</string>',
                 '<string name="root_diagnostics_title">诊断日志</string>', "zh title")
        if "root_diagnostics_sendlog" not in t:
            t = t.replace(
                '    <string name="root_diagnostics_copy">',
                '    <string name="root_diagnostics_sendlog">发送日志</string>\n    <string name="root_diagnostics_copy">',
                1,
            )
            print("added zh sendlog string")
        t = _sub(t,
                 '<string name="root_diagnostics_red_hint">外部工具提权完成后，先强制停止并重开本应用，或点「重新检测」。</string>',
                 '<string name="root_diagnostics_red_hint">外部工具提权完成后，请强制停止并重开本应用。</string>',
                 "zh hint")
        zh.write_text(t, encoding="utf-8")
    en = root / EN_XML
    if en.is_file():
        t = en.read_text(encoding="utf-8")
        t = _sub(t, '<string name="root_diagnostics_title">Root diagnostics</string>',
                 '<string name="root_diagnostics_title">Diagnostics log</string>', "en title")
        if "root_diagnostics_sendlog" not in t:
            t = t.replace(
                '    <string name="root_diagnostics_copy">',
                '    <string name="root_diagnostics_sendlog">Send log</string>\n    <string name="root_diagnostics_copy">',
                1,
            )
            print("added en sendlog string")
        t = _sub(t,
                 '<string name="root_diagnostics_red_hint">After an external tool finishes elevation, force-stop and reopen this app, or tap Re-check.</string>',
                 '<string name="root_diagnostics_red_hint">After an external tool finishes elevation, force-stop and reopen this app.</string>',
                 "en hint")
        en.write_text(t, encoding="utf-8")


def _bump(root: Path) -> None:
    g = root / "manager/build.gradle.kts"
    if not g.is_file():
        print("skip: manager/build.gradle.kts missing")
        return
    t = g.read_text(encoding="utf-8")
    changed = False
    for old, new in (("versionCode = 32743", "versionCode = 32744"),
                     ('versionName = "3.22.4-bw"', 'versionName = "3.22.5-bw"')):
        if old in t:
            t = t.replace(old, new, 1)
            changed = True
    if changed:
        g.write_text(t, encoding="utf-8")
        print("bumped manager version -> 32744/3.22.5-bw")
    else:
        print("skip: version already bumped")


def patch_32744_diaglog(root: Path) -> None:
    _ui(root)
    _kt(root)
    _settings(root)
    _strings(root)
    _bump(root)


if __name__ == "__main__":
    import sys

    patch_32744_diaglog(Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve())
