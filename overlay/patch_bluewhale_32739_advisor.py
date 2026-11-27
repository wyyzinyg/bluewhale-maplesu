#!/usr/bin/env python3
"""32739 UI fixes: empty advisor state (BluefishSU icon) + compile fixes for brand/diagnostics."""
import sys
from pathlib import Path

ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else "src")


def patch_advisor(root: Path) -> None:
    rel = "manager/src/main/java/com/maplesu/core/ui/screen/home/AdvisorWall.kt"
    path = root / rel
    text = path.read_text(encoding="utf-8")
    if "BluefishAdvisorEmpty" in text:
        print(f"skip: {rel} already patched")
        return
    if "import androidx.compose.foundation.layout.fillMaxWidth\n" not in text:
        text = text.replace(
            "import androidx.compose.foundation.layout.Box\n",
            "import androidx.compose.foundation.layout.Box\nimport androidx.compose.foundation.layout.fillMaxWidth\n",
            1,
        )
    if "import androidx.compose.foundation.Image\n" not in text:
        text = text.replace(
            "import androidx.compose.foundation.background\n",
            "import androidx.compose.foundation.Image\nimport androidx.compose.foundation.background\n",
            1,
        )
    if "import androidx.compose.ui.res.painterResource\n" not in text:
        text = text.replace(
            "import androidx.compose.ui.platform.LocalContext\n",
            "import androidx.compose.ui.platform.LocalContext\nimport androidx.compose.ui.res.painterResource\n",
            1,
        )
    old_return = "    if (members.isEmpty()) return\n"
    new_return = (
        "    if (members.isEmpty()) {\n"
        "        BluefishAdvisorEmpty()\n"
        "        return\n"
        "    }\n"
    )
    if old_return not in text:
        raise SystemExit("FATAL: AdvisorWallCard empty-return marker not found")
    text = text.replace(old_return, new_return, 1)
    marker = (
        "@OptIn(ExperimentalFoundationApi::class)\n"
        "@Composable\n"
        "internal fun AdvisorWallCard("
    )
    empty_state = (
        "@Composable\n"
        "private fun BluefishAdvisorEmpty() {\n"
        "    Box(\n"
        "        modifier = Modifier.fillMaxWidth().padding(vertical = 28.dp).clearAndSetSemantics {},\n"
        "        contentAlignment = Alignment.Center,\n"
        "    ) {\n"
        "        Image(\n"
        "            painter = painterResource(R.drawable.ic_launcher_foreground),\n"
        "            contentDescription = null,\n"
        "            modifier = Modifier.size(96.dp),\n"
        "        )\n"
        "    }\n"
        "}\n\n"
    )
    if marker not in text:
        raise SystemExit("FATAL: AdvisorWallCard marker not found")
    text = text.replace(marker, empty_state + marker, 1)
    old_roster = (
        "private object AdvisorAssets {\n"
        "    fun roster(context: Context): List<Advisor> = runCatching {\n"
        "        context.assets.open(AdvisorRoster.MEMBERS_ASSET).use { AdvisorRoster.parse(it.readBytes().toString(Charsets.UTF_8)) }\n"
        "    }.getOrDefault(emptyList())\n"
    )
    new_roster = (
        "private object AdvisorAssets {\n"
        "    // 内测名单尚未开放：先只展示 BluefishSU 图标，等真实内测用户产生后再恢复 members.json。\n"
        "    fun roster(context: Context): List<Advisor> = emptyList()\n"
    )
    if old_roster not in text:
        raise SystemExit("FATAL: AdvisorAssets roster marker not found")
    text = text.replace(old_roster, new_roster, 1)
    path.write_text(text, encoding="utf-8")
    print(f"patched {rel}: empty advisor state -> BluefishSU icon")


def patch_brand(root: Path) -> None:
    rel = "manager/src/main/java/com/maplesu/core/ui/component/maple/BrandBannerArt.kt"
    path = root / rel
    text = path.read_text(encoding="utf-8")
    old = "addOval(RectF(20f, 41f, 27f, 48f))"
    new = "addOval(RectF(20f, 41f, 27f, 48f), android.graphics.Path.Direction.CW)"
    if old not in text:
        raise SystemExit(f"FATAL: {rel}: addOval marker not found")
    text = text.replace(old, new, 1)
    path.write_text(text, encoding="utf-8")
    print(f"patched {rel}: addOval direction")


def patch_diagnostics(root: Path) -> None:
    rel = "manager/src/main/java/com/maplesu/core/ui/screen/home/RootDiagnostics.kt"
    path = root / rel
    text = path.read_text(encoding="utf-8")
    old = "when (state.systemInfo.seccompStatus) {"
    new = "when (state.systemInfo.seccompStatus.toInt()) {"
    if old not in text:
        raise SystemExit(f"FATAL: {rel}: seccomp when marker not found")
    text = text.replace(old, new, 1)
    path.write_text(text, encoding="utf-8")
    print(f"patched {rel}: seccomp int comparison")


def patch_diag_v3_literal(root: Path) -> None:
    rel = "manager/src/main/java/com/maplesu/core/ui/screen/home/RootDiagnostics.kt"
    path = root / rel
    text = path.read_text(encoding="utf-8")
    old = "0xf05368c0 -> v3 = true"
    new = "0xf05368c0.toInt() -> v3 = true"
    if old not in text:
        raise SystemExit(f"FATAL: {rel}: v3 literal marker not found")
    text = text.replace(old, new, 1)
    path.write_text(text, encoding="utf-8")
    print(f"patched {rel}: v3 block id Int comparison")


def patch_legacy_claim_gate(root: Path) -> None:
    rel = "manager/build.gradle.kts"
    path = root / rel
    text = path.read_text(encoding="utf-8")
    old = '''check(ultraManagerClaimDirectory != null ||
            providers.gradleProperty("bluewhaleSkipUltraBridge").orNull == "true") {'''
    new = '''check(ultraManagerClaimDirectory != null ||
            providers.gradleProperty("bluewhaleSkipUltraBridge").orNull == "true" ||
            rootProject.file("manager/src/main/assets/ultra-manager-claim/manifest.json").isFile) {'''
    if old not in text:
        raise SystemExit(f"FATAL: {rel}: claim gate marker not found")
    text = text.replace(old, new, 1)
    path.write_text(text, encoding="utf-8")
    print(f"patched {rel}: legacy claim assets allowed (bridge remains real)")


def main() -> int:
    patch_advisor(ROOT)
    patch_brand(ROOT)
    patch_diagnostics(ROOT)
    patch_diag_v3_literal(ROOT)
    patch_legacy_claim_gate(ROOT)
    print("32739 advisor + compile fixes applied")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
