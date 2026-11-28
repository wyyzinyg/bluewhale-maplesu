#!/usr/bin/env python3
"""32753 (3.22.14-bw): BluefishSU 自家主题商店 + 10 套预设。

上游主题商店（fengqiufq.github.io/maplesu-theme-market）保留为可选源，
但默认源改成本家索引：10 套自家配色，索引与包全部托管在自家 CDN。
"""
import sys
from pathlib import Path

ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else "src").resolve()

STORE_SOURCE = "manager/src/main/java/com/maplesu/core/theme/ThemeStoreSource.kt"
STORE = "manager/src/main/java/com/maplesu/core/theme/ThemeStore.kt"
STORE_UI = "manager/src/main/java/com/maplesu/core/ui/screen/settings/ThemeStoreScreen.kt"
ZH = "manager/src/main/res/values-zh-rCN/strings_theme.xml"
EN = "manager/src/main/res/values/strings_theme.xml"
GRADLE = "manager/build.gradle.kts"

BLUEFISH_URL = "https://bluewhale-release-bluewhale-update-d8e0r9wc21f00b8.webapps.tcloudbase.com/theme-market/index.json"
BLUEFISH_BACKUP = "https://aka.doubaocdn.com/s/Q3CaI9osCh"

failures = []


def swap(rel: str, pairs, label: str) -> None:
    path = ROOT / rel
    if not path.is_file():
        failures.append(f"missing {rel}")
        return
    text = path.read_text(encoding="utf-8")
    hits = 0
    for old, new in pairs:
        if old not in text:
            print(f"MISS {rel}: {old[:52]!r}")
            continue
        text = text.replace(old, new, 1)
        hits += 1
    path.write_text(text, encoding="utf-8")
    print(f"patched: {label} ({hits})")


def add_bluefish_source() -> None:
    swap(STORE_SOURCE, [
        (
            '        val Fina = ThemeStoreSource("finasu", "https://folk.mysqil.com/api/themes")',
            '        val Fina = ThemeStoreSource("finasu", "https://folk.mysqil.com/api/themes")\n'
            '        // BluefishSU 自家主题商店：索引与主题包都在自家 CDN，不依赖任何上游服务。\n'
            f'        val Bluefish = ThemeStoreSource("bluefish", "{BLUEFISH_URL}")\n'
            f'        const val BLUEFISH_BACKUP = "{BLUEFISH_BACKUP}"',
        ),
        (
            '    val urls: List<String> get() = if (this == Maple) listOf(url, MAPLE_BACKUP) else listOf(url)',
            '    val urls: List<String> get() = when (this) {\n'
            '        Maple -> listOf(url, MAPLE_BACKUP)\n'
            '        Bluefish -> listOf(url, BLUEFISH_BACKUP)\n'
            '        else -> listOf(url)\n'
            '    }',
        ),
        (
            '''        internal fun resolve(id: String?, customUrl: String): ThemeStoreSource = when (id) {
            Maple.id -> Maple
            "custom" -> custom(customUrl)
            else -> Fina
        }''',
            '''        internal fun resolve(id: String?, customUrl: String): ThemeStoreSource = when (id) {
            Bluefish.id -> Bluefish
            Maple.id -> Maple
            "custom" -> custom(customUrl)
            // 首次进入（PREFERENCE 为空）走自家商店；上游商店仍可手动切换。
            else -> Bluefish
        }''',
        ),
    ], "theme store source")


def default_to_bluefish() -> None:
    swap(STORE, [
        ("}.getOrDefault(ThemeStoreSource.Fina)", "}.getOrDefault(ThemeStoreSource.Bluefish)"),
    ], "theme store default")


def source_picker() -> None:
    swap(STORE_UI, [
        (
            '                listOf("maplesu","finasu","custom").forEach { id ->',
            '                listOf("bluefish","maplesu","finasu","custom").forEach { id ->',
        ),
        (
            '''private fun catalogSourceLabel(id: String): String = when (id) {
    "maplesu" -> "MapleSU"
    "finasu" -> "FinaSU"
    else -> stringResource(R.string.theme_catalog_custom)
}''',
            '''private fun catalogSourceLabel(id: String): String = when (id) {
    "bluefish" -> "BluefishSU"
    "maplesu" -> "MapleSU"
    "finasu" -> "FinaSU"
    else -> stringResource(R.string.theme_catalog_custom)
}''',
        ),
        (
            '''            } else ThemeText(stringResource(if (sourceDraft == "maplesu")
                R.string.theme_catalog_maple_summary else R.string.theme_catalog_fina_summary),secondary=true)''',
            '''            } else ThemeText(stringResource(when (sourceDraft) {
                "bluefish" -> R.string.theme_catalog_bluefish_summary
                "maplesu" -> R.string.theme_catalog_maple_summary
                else -> R.string.theme_catalog_fina_summary
            }),secondary=true)''',
        ),
    ], "theme store picker")


def catalog_strings() -> None:
    swap(ZH, [
        (
            '    <string name="theme_catalog_fina_summary">',
            '    <string name="theme_catalog_bluefish_summary">BluefishSU 自家主题商店，内置 10 套预设配色（深海、月华、珊瑚、极光、夜潮、松石、琥珀、樱白、墨、蓝焰）。切换源不会删除已下载的主题。</string>\n'
            '    <string name="theme_catalog_fina_summary">',
        ),
    ], "zh catalog string")
    swap(EN, [
        (
            '    <string name="theme_catalog_fina_summary">',
            '    <string name="theme_catalog_bluefish_summary">The BluefishSU catalog with 10 built-in presets (Deep Sea, Moonlight, Coral, Aurora, Night Tide, Turquoise, Amber, Sakura, Ink, Blue Flame). Switching sources keeps downloaded themes.</string>\n'
            '    <string name="theme_catalog_fina_summary">',
        ),
    ], "en catalog string")


def bump() -> None:
    path = ROOT / GRADLE
    if not path.is_file():
        failures.append("missing gradle")
        return
    text = path.read_text(encoding="utf-8")
    old_code = "32752"
    old_name = "3.22.13-bw"
    if old_code not in text or old_name not in text:
        print(f"SKIP bump: 32752/3.22.13-bw not found")
        return
    text = text.replace(old_code, "32753", 1).replace(old_name, "3.22.14-bw", 1)
    path.write_text(text, encoding="utf-8")
    print("bumped manager version -> 32753/3.22.14-bw")


def main() -> int:
    print("32753: bluefish theme catalog + 10 presets")
    add_bluefish_source()
    default_to_bluefish()
    source_picker()
    catalog_strings()
    bump()
    if failures:
        print("FAILED:", *failures, sep="\n - ")
        return 1
    print("32753 done")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
