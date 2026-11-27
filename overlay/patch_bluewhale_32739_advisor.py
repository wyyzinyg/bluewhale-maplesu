#!/usr/bin/env python3
"""32739 advisor dialog: hide the unpopulated beta roster and show only the BluefishSU icon."""
import sys
from pathlib import Path

REL = "manager/src/main/java/com/maplesu/core/ui/screen/home/AdvisorWall.kt"


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else "src")
    path = root / REL
    if not path.exists():
        print(f"FATAL: {path} not found")
        return 1
    text = path.read_text(encoding="utf-8")
    if "BluefishAdvisorEmpty" in text:
        print(f"skip: {REL} already patched")
        return 0

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
        print("FATAL: AdvisorWallCard empty-return marker not found")
        return 1
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
        "            painter = painterResource(R.mipmap.ic_launcher_foreground_bluewhale),\n"
        "            contentDescription = null,\n"
        "            modifier = Modifier.size(96.dp),\n"
        "        )\n"
        "    }\n"
        "}\n\n"
    )
    if marker not in text:
        print("FATAL: AdvisorWallCard marker not found")
        return 1
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
        print("FATAL: AdvisorAssets roster marker not found")
        return 1
    text = text.replace(old_roster, new_roster, 1)
    path.write_text(text, encoding="utf-8")
    print(f"patched {REL}: empty advisor state -> BluefishSU icon")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
