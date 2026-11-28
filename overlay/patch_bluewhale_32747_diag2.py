#!/usr/bin/env python3
"""32747 (3.22.8-bw): make the report name the provider's last step, and stop
the home probe from re-running itself.

Two gaps left after 3.22.7-bw:

1. The report still ends at "MAPLESU_KSU_NOT_READY". Section F reads the
   system logcat, but the provider (crash_dump64 side) writes its story into
   files this app never quotes: files/jailbreak/attempts/<id>/request.json,
   caller-outcome.json, status.json, progress.jsonl, native-stage.log.
   Section G quotes the newest attempt directory, plus the lite credential
   file names the startup policy used to decide "installed".

2. Every cold start ran the root probe 3-4 times (18:01:36/37/39/43 on a real
   device). ROOT_RETRY_ATTEMPTS was 2 and shouldRetryRoot fired because
   liteInstalled came back true from stale credential evidence even though
   there is no root channel. One retry is enough for a real transient miss;
   four launches is noise the user sees as "正在检查" flicker.

Bumps 32746/3.22.7-bw -> 32747/3.22.8-bw.
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else "src")

DIAG = "manager/src/main/java/com/maplesu/core/ui/screen/home/RootDiagnostics.kt"
POLICY = "manager/src/main/java/dev/maplesu/manager/litehidden/LiteStartupStatusPolicy.kt"
GRADLE = "manager/build.gradle.kts"

F_TAIL = '    appendLine("pstore=" + pstorePanic())\n'

G_SECTION = '''    appendLine()
    appendLine("G. Provider attempt (what the jailbreak path actually did)")
    appendLine("  " + providerAttempt())
    appendLine("liteEvidence=" + liteEvidenceHint())
'''

G_HELPERS = '''
// 3.22.8-bw：G 段。provider 的证据都在 app 私有目录里，只读、失败只写 error。
private fun providerAttempt(): String = runCatching {
    val roots = listOf(
        "/data/user/0/com.blue.whale.mask/files/jailbreak/attempts",
        "/data/user_de/0/com.blue.whale.mask/files/jailbreak/attempts",
    )
    val dir = roots.asSequence()
        .map { java.io.File(it) }
        .filter { it.isDirectory }
        .flatMap { d ->
            val kids = d.listFiles() ?: return@flatMap emptySequence<java.io.File>()
            kids.asSequence()
        }
        .maxByOrNull { it.lastModified() }
        ?: return@runCatching "none"
    val out = mutableListOf<String>()
    out += "attempt=" + dir.name
    fun head(name: String, max: Int): String {
        val f = java.io.File(dir, name)
        if (!f.isFile) return "missing"
        val t = f.readText().replace("\\n", " ")
        return if (t.length <= max) t else t.take(max) + "..."
    }
    fun tail(name: String, count: Int, max: Int): String {
        val f = java.io.File(dir, name)
        if (!f.isFile) return "missing"
        val rows = f.readText().lineSequence().filter { it.isNotBlank() }.toList().takeLast(count)
        if (rows.isEmpty()) return "empty"
        val joined = rows.joinToString(" | ")
        return if (joined.length <= max) joined else joined.take(max) + "..."
    }
    out += "request=" + head("request.json", 240)
    out += "outcome=" + head("caller-outcome.json", 240)
    out += "status=" + head("status.json", 180)
    out += "progress=" + tail("progress.jsonl", 4, 320)
    out += "native=" + tail("native-stage.log", 5, 420)
    out.joinToString("\\n  ")
}.getOrDefault("error")

private fun liteEvidenceHint(): String = runCatching {
    val roots = listOf(
        "/data/user/0/com.blue.whale.mask/files",
        "/data/user_de/0/com.blue.whale.mask/files",
    ).map { java.io.File(it) }.filter { it.isDirectory }
    val names = roots.flatMap { d ->
        d.listFiles()?.map { it.name } ?: emptyList<String>()
    }
    val hits = names.filter { n ->
        val l = n.lowercase()
        l.contains("lite") || l.contains("mode_a") || l.contains("cred") ||
            l.contains("maplesu") || l.contains("su_state")
    }
    if (hits.isEmpty()) "none" else hits.distinct().take(8).joinToString(",")
}.getOrDefault("error")
'''

OLD_ATTEMPTS = "    const val ROOT_RETRY_ATTEMPTS = 2"
NEW_ATTEMPTS = (
    "    /** 3.22.8-bw：一次重试足够；2 会让首页冷启动探 4 次。 */\n"
    "    const val ROOT_RETRY_ATTEMPTS = 1"
)


def _p(root: Path, rel: str) -> Path:
    return root / rel


def patch_g_section(root: Path) -> None:
    p = _p(root, DIAG)
    if not p.is_file():
        print("SKIP g: RootDiagnostics.kt missing")
        return
    text = p.read_text(encoding="utf-8")
    if "G. Provider attempt" in text:
        print("SKIP g: already added")
        return
    if F_TAIL not in text:
        print("SKIP g: section F tail anchor missing")
        return
    text = text.replace(F_TAIL, F_TAIL + G_SECTION, 1)
    text = text.rstrip("\n") + "\n" + G_HELPERS + "\n"
    p.write_text(text, encoding="utf-8")
    print("patched: report section G (provider attempt + lite evidence)")


def patch_retry(root: Path) -> None:
    p = _p(root, POLICY)
    if not p.is_file():
        print("SKIP retry: LiteStartupStatusPolicy.kt missing")
        return
    text = p.read_text(encoding="utf-8")
    if NEW_ATTEMPTS in text:
        print("SKIP retry: already 1")
        return
    if OLD_ATTEMPTS not in text:
        print("SKIP retry: anchor missing")
        return
    text = text.replace(OLD_ATTEMPTS, NEW_ATTEMPTS, 1)
    p.write_text(text, encoding="utf-8")
    print("patched: ROOT_RETRY_ATTEMPTS 2 -> 1")


def bump_version(root: Path) -> None:
    path = _p(root, GRADLE)
    if not path.is_file():
        print("SKIP bump: missing %s" % GRADLE)
        return
    text = path.read_text(encoding="utf-8")
    pairs = (("versionCode = 32746", "versionCode = 32747"),
             ('versionName = "3.22.7-bw"', 'versionName = "3.22.8-bw"'))
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
        print("bumped manager version -> 32747/3.22.8-bw")


def patch_32747_diag2(root: Path) -> None:
    patch_g_section(root)
    patch_retry(root)
    bump_version(root)


if __name__ == "__main__":
    patch_32747_diag2(ROOT.resolve())
