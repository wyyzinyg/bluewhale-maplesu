"""32745 (3.22.6-bw): finish the home screen and make the log say why.

Four things, all of them visible to the user right now:

1. The standalone "环境提示" warning card is still on screen after 3.22.4-bw
   (user screenshot 15:31). 3.22.4-bw deleted one copy by exact indentation
   match; this patch drops the whole `if (state.showEnvironmentRefreshWarning)`
   block by brace matching on BOTH skins, so indentation drift cannot save it.
   The card's own text still pointed at a「重新检测」button that has not existed
   since 3.22.3-bw, so those four environment strings lose that tail sentence.

2. First second after launch the home page shows ONLY "正在检查环境" — the
   Root entry (tap-to-patch + 越狱) is hidden behind
   `!statusState.environmentChecking`. The probe can take 20s, so the button
   the user wants is unreachable exactly when he wants it. Show the card while
   checking, with its headline reading 正在检查 root 环境….

3. Report gains section F: the runtime evidence that actually decides
   whether the jailbreak failed in the kernel or in the sandbox —
   `avc: denied` lines, `blocked by seccomp`, hook evidence files,
   /sys/module leftovers, pstore panic lines. Without these the report can
   only say "KSU not ready", which is what it said for 24 hours.

Bumps 32744/3.22.5-bw -> 32745/3.22.6-bw.
"""

from pathlib import Path
import re

HOME_REL = "manager/src/main/java/com/maplesu/core/ui/screen/home/HomeMiuix.kt"
HOME_MATERIAL_REL = "manager/src/main/java/com/maplesu/core/ui/screen/home/HomeMaterial.kt"
SCREEN_REL = "manager/src/main/java/com/maplesu/core/ui/screen/home/HomeScreen.kt"
DIAG_REL = "manager/src/main/java/com/maplesu/core/ui/screen/home/RootDiagnostics.kt"

WARN_MARK = "if (state.showEnvironmentRefreshWarning) {"

RED_ZH = " 外部工具提权完成后，先强制停止并重开本应用，或点「重新检测」。"
RED_EN = " After an external tool finishes elevation, force-stop and reopen this app, or tap Re-check."

CARD_ANCHOR = '''private fun RootAccessCardMiuix(
    onNoRootClick: () -> Unit,
    onPatchBootClick: () -> Unit,
'''
CARD_ANCHOR_NEW = '''private fun RootAccessCardMiuix(
    onNoRootClick: () -> Unit,
    onPatchBootClick: () -> Unit,
    checking: Boolean = false,
'''

HEADLINE_OLD = '''                Text(
                    text = "未检测到可用的 root 环境",'''
HEADLINE_NEW = '''                Text(
                    text = if (checking) "正在检查 root 环境…" else "未检测到可用的 root 环境",'''

CALL_OLD = '''RootAccessCardMiuix(
                            onNoRootClick ='''
CALL_NEW = '''RootAccessCardMiuix(
                            checking = state.environmentChecking,
                            onNoRootClick ='''

CHECK_DEP = "        !statusState.environmentChecking &&\n"

DIAG_ANCHOR = '''    if (snapshot.error != null) {
        appendLine()
        appendLine("collectionError=${snapshot.error}")
    }
}'''
DIAG_SECTION = '''
    appendLine()
    appendLine("F. Runtime evidence (why the last attempt died)")
    appendLine("logcatAvc=" + logcatGrep("avc: denied", 12))
    appendLine("logcatSeccomp=" + logcatGrep("blocked by seccomp", 6))
    appendLine("logcatKsu=" + logcatGrep("KernelSU:", 8))
    appendLine("hookEvidence=" + hookEvidence())
    appendLine("sysModules=" + sysModules())
    appendLine("pstore=" + pstorePanic())
'''

DIAG_HELPERS = '''
// 3.22.6-bw：F 段证据采集。全部是只读探针；任一失败只写 error，不抛异常。
private fun logcatGrep(needle: String, limit: Int): String = runCatching {
    val p = ProcessBuilder("logcat", "-d", "-v", "brief")
        .redirectErrorStream(true)
        .start()
    val text = p.inputStream.bufferedReader().use { it.readText() }
    p.waitFor()
    val hits = text.lineSequence().filter { it.contains(needle, ignoreCase = true) }
        .toList().takeLast(limit).map { it.trim() }
    if (hits.isEmpty()) "none" else hits.joinToString(" ~ ")
}.getOrDefault("error")

private fun hookEvidence(): String = runCatching {
    val dirs = listOf(
        "/data/user_de/0/com.blue.whale.mask",
        "/data/user/0/com.blue.whale.mask",
    ).map { java.io.File(it) }
    val names = listOf(
        "maplesu-hook.json",
        "maplesu-hook-attest.json",
        "maplesu-hook-unload.json",
        "maplesu-hook-daemon.json",
        "maplesu-handover.json",
        "maplesu-hook-env.log",
        "maplesu-teardown.log",
    )
    val found = names.filter { n -> dirs.any { java.io.File(it, n).exists() } }
    if (found.isEmpty()) "none" else found.joinToString(",")
}.getOrDefault("error")

private fun sysModules(): String = runCatching {
    val out = java.io.File("/sys/module").listFiles()
        ?.map { it.name }
        ?.filter { it.contains("dfroot") || it.contains("ksu") || it.contains("maplesu") }
        ?: emptyList()
    if (out.isEmpty()) "none" else out.joinToString(",")
}.getOrDefault("error")

private fun pstorePanic(): String = runCatching {
    val dir = java.io.File("/sys/fs/pstore")
    val files = dir.listFiles() ?: return@runCatching "unreachable"
    val first = files.firstOrNull() ?: return@runCatching "empty"
    val text = first.readText()
    val hits = text.lineSequence()
        .filter {
            it.contains("Kernel panic") ||
                it.contains("Unable to handle kernel") ||
                it.contains("BUG: unable to handle") ||
                it.contains("Internal error")
        }
        .take(6).map { it.trim() }.toList()
    if (hits.isEmpty()) "clean(" + first.name + ")" else hits.joinToString(" ~ ")
}.getOrDefault("error")
'''


def _drop_block(text: str, marker: str, tag: str) -> str:
    if marker not in text:
        print("skip: %s (no marker)" % tag)
        return text
    if text.count(marker) > 1:
        print("note: %s occurs %d times; dropping all" % (tag, text.count(marker)))
    while marker in text:
        i = text.find(marker)
        brace = text.find("{", i)
        if brace < 0:
            print("skip: %s (no brace)" % tag)
            return text
        depth = 0
        j = brace
        while j < len(text):
            c = text[j]
            if c == "{":
                depth += 1
            elif c == "}":
                depth -= 1
                if depth == 0:
                    break
            j += 1
        start = text.rfind("\n", 0, i) + 1
        end = j + 1
        text = text[:start] + text[end:]
        print("dropped: %s (%d chars)" % (tag, end - start))
    return text


def _sub_once(text: str, old: str, new: str, tag: str) -> str:
    if new in text and old not in text:
        print("skip: %s already done" % tag)
        return text
    if old not in text:
        print("skip: %s anchor missing" % tag)
        return text
    print("patched: %s" % tag)
    return text.replace(old, new, 1)


def _write(root: Path, rel: str, text: str) -> None:
    p = root / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8")


def _patch_home(root: Path) -> None:
    p = root / HOME_REL
    if not p.is_file():
        print("skip: HomeMiuix.kt missing")
        return
    text = p.read_text(encoding="utf-8")
    text = _drop_block(text, WARN_MARK, "HomeMiuix environment notice card")
    p.write_text(text, encoding="utf-8")


def _patch_home_material(root: Path) -> None:
    p = root / HOME_MATERIAL_REL
    if not p.is_file():
        print("skip: HomeMaterial.kt missing")
        return
    text = p.read_text(encoding="utf-8")
    text = _drop_block(text, WARN_MARK, "HomeMaterial environment notice card")
    p.write_text(text, encoding="utf-8")


def _patch_screen(root: Path) -> None:
    p = root / SCREEN_REL
    if not p.is_file():
        print("skip: HomeScreen.kt missing")
        return
    text = p.read_text(encoding="utf-8")
    if CHECK_DEP in text:
        text = text.replace(CHECK_DEP, "", 1)
        print("patched: entry visible while checking")
    else:
        print("skip: entry checking dependency already gone")
    p.write_text(text, encoding="utf-8")


def _patch_strings(root: Path, rel: str, tail: str) -> None:
    p = root / rel
    if not p.is_file():
        print("skip: %s missing" % rel)
        return
    text = p.read_text(encoding="utf-8")
    if tail not in text:
        print("skip: %s already clean" % rel)
        return
    text = text.replace(tail, "", 1) if text.count(tail) == 1 else text.replace(tail, "")
    p.write_text(text, encoding="utf-8")
    print("patched: %s (removed dead re-check tail)" % rel)


def _patch_diag(root: Path) -> None:
    p = root / DIAG_REL
    if not p.is_file():
        print("skip: RootDiagnostics.kt missing")
        return
    text = p.read_text(encoding="utf-8")
    if "F. Runtime evidence" in text:
        print("skip: runtime evidence already added")
        return
    if DIAG_ANCHOR not in text:
        print("skip: report tail anchor missing")
        return
    body_end = DIAG_ANCHOR[:-2] if DIAG_ANCHOR.endswith("\n}") else DIAG_ANCHOR
    text = text.replace(
        DIAG_ANCHOR,
        body_end + "\n" + DIAG_SECTION + "}\n",
        1,
    )
    text = text.rstrip("\n") + "\n" + DIAG_HELPERS + "\n"
    p.write_text(text, encoding="utf-8")
    print("patched: report section F (avc / seccomp / hook evidence / modules / pstore)")


def _bump(root: Path) -> None:
    g = root / "manager/build.gradle.kts"
    if not g.is_file():
        print("skip: manager/build.gradle.kts missing")
        return
    text = g.read_text(encoding="utf-8")
    changed = False
    for old, new in (("versionCode = 32744", "versionCode = 32745"),
                     ('versionName = "3.22.5-bw"', 'versionName = "3.22.6-bw"')):
        if old in text:
            text = text.replace(old, new, 1)
            changed = True
    if changed:
        g.write_text(text, encoding="utf-8")
        print("bumped manager version -> 32745/3.22.6-bw")
    else:
        print("skip: version already bumped")


_MATE = None
try:
    import patch_bluewhale_32742_home as _p42
    _MATE = getattr(_p42, "NEW_CARD", None)
except Exception as exc:  # pragma: no cover - chain always has 32740 first
    print("warn: 32740 mate unavailable: %r" % (exc,))
    _MATE = None


def _root_access_card_miuix() -> str:
    """3.22.3-bw shape of the card (32740 inject + 32742 replace), used as the
    mate for the checking->headline edit. Kept out of the main flow so the
    anchor can never be mistaken for the ordinary environment-notice block."""
    if _MATE:
        return _MATE
    return ""


def _patch_root_card_solo(root: Path) -> None:
    p = root / HOME_REL
    if not p.is_file():
        print("skip: HomeMiuix.kt missing (root card)")
        return
    text = p.read_text(encoding="utf-8")
    mate = _root_access_card_miuix()
    if mate and mate in text:
        text = text.replace(
            mate,
            mate.replace(CARD_ANCHOR, CARD_ANCHOR_NEW, 1)
                .replace(HEADLINE_OLD, HEADLINE_NEW, 1),
            1,
        )
        print("patched: root card checking param + headline")
    else:
        text = _sub_once(text, CARD_ANCHOR, CARD_ANCHOR_NEW, "root card checking param")
        text = _sub_once(text, HEADLINE_OLD, HEADLINE_NEW, "root card checking headline")
    text, n = re.subn(
        r"RootAccessCardMiuix\(\n(\s+)onNoRootClick =",
        r"RootAccessCardMiuix(\n\1checking = state.environmentChecking,\n\1onNoRootClick =",
        text,
        count=1,
    )
    print(("patched: root card call site" if n else "skip: root card call site anchor missing"))
    p.write_text(text, encoding="utf-8")


def patch_32745_clean(root: Path) -> None:
    if _root_access_card_miuix():
        _patch_root_card_solo(root)
    else:
        print("skip: root card mate missing")
    _patch_home(root)
    _patch_home_material(root)
    _patch_screen(root)
    for rel, tail in (
        ("manager/src/main/res/values-zh-rCN/home_environment_check.xml", RED_ZH),
        ("manager/src/main/res/values-zh-rCN/maplesu_litehidden.xml", RED_ZH),
        ("manager/src/main/res/values/home_environment_check.xml", RED_EN),
        ("manager/src/main/res/values/maplesu_litehidden.xml", RED_EN),
    ):
        _patch_strings(root, rel, tail)
    _patch_diag(root)
    _bump(root)


if __name__ == "__main__":
    import sys
    patch_32745_clean(Path(sys.argv[1] if len(sys.argv) > 1 else "."))
