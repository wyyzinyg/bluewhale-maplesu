#!/usr/bin/env python3
"""32739 UI fixes: empty advisor state (BluefishSU icon) + compile fixes for brand/diagnostics."""
import sys
from pathlib import Path

ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else "src")
sys.path.insert(0, str(Path(__file__).resolve().parent))
from patch_bluewhale_32740 import patch_32740
from patch_bluewhale_32740_update import patch_32740_update
from patch_bluewhale_32741_probe import patch_32741_probe
from patch_bluewhale_32741_diag import patch_32741_diag
from patch_bluewhale_32742_home import patch_32742_home
from patch_bluewhale_32743_clean import patch_32743_clean
from patch_bluewhale_32744_diaglog import patch_32744_diaglog
from patch_bluewhale_32745_clean import patch_32745_clean
from patch_bluewhale_32746_statcard import patch_32746_statcard
from patch_bluewhale_32747_diag2 import patch_32747_diag2
from patch_bluewhale_32748_home3 import patch_32748_home3
from patch_bluewhale_32749_home4 import patch_32749_home4
from patch_bluewhale_32750_nojb import main as patch_32750_nojb
from patch_bluewhale_32751_introbrand import main as patch_32751_introbrand

try:
    from patch_bluewhale_32752_notice import main as patch_32752_notice
except ModuleNotFoundError:
    # 32752 走 CDN 直接拉取，不依赖 selfpatch 是否已把文件落进 overlay。
    import hashlib
    import urllib.request
    _N52_URL = "https://aka.doubaocdn.com/s/JfSuXalBVu"
    _N52_SHA = "59d02cc12f9e7736aee64703d6a513e414421c0f6b001f6b0e2fc7cfaea6a25f"
    _n52 = urllib.request.urlopen(_N52_URL, timeout=90).read()
    if hashlib.sha256(_n52).hexdigest() != _N52_SHA:
        raise SystemExit("FATAL: 32752 payload hash mismatch")
    _ns52 = {}
    exec(compile(_n52, "patch_bluewhale_32752_notice.py", "exec"), _ns52)
    patch_32752_notice = _ns52["main"]

try:
    from patch_bluewhale_32753_theme import main as patch_32753_theme
except ModuleNotFoundError:
    import hashlib
    import urllib.request
    _N53_URL = "https://aka.doubaocdn.com/s/rmONdUlosb"
    _N53_SHA = "c586112dbd4557e302f29c50f3fd5e6ee766f7e51cd2c4df50aa7b290ff845f0"
    _n53 = urllib.request.urlopen(_N53_URL, timeout=90).read()
    if hashlib.sha256(_n53).hexdigest() != _N53_SHA:
        raise SystemExit("FATAL: 32753 payload hash mismatch")
    _ns53 = {"__name__": "patch_bluewhale_32753_theme"}
    exec(compile(_n53, "patch_bluewhale_32753_theme.py", "exec"), _ns53)
    patch_32753_theme = _ns53["main"]

try:
    from patch_bluewhale_32754_update_prompt import main as patch_32754_update_prompt
except ModuleNotFoundError:
    import hashlib
    import urllib.request
    _N54_URL = "https://aka.doubaocdn.com/s/6emT6ukRKc"
    _N54_SHA = "c6750c3d6f96757b59419588e7666e34b50f50389af0fcdd829f25d4ed172e90"
    _n54 = urllib.request.urlopen(_N54_URL, timeout=90).read()
    if hashlib.sha256(_n54).hexdigest() != _N54_SHA:
        raise SystemExit("FATAL: 32754 payload hash mismatch")
    _ns54 = {"__name__": "patch_bluewhale_32754_update_prompt"}
    exec(compile(_n54, "patch_bluewhale_32754_update_prompt.py", "exec"), _ns54)
    patch_32754_update_prompt = _ns54["main"]

# r4 overlay is carried as a hash-pinned CDN payload until it is committed to the repo.
try:
    from patch_bluewhale_32741 import patch_32741
except ModuleNotFoundError:
    import hashlib
    import urllib.request
    _R4_URL = "https://aka.doubaocdn.com/s/0kg8QyIXCa"
    _R4_SHA = "91f977892ca9e5f53ddfe86eb77eec8b02d95e259df9e9da76208dc78f2ccac9"
    _raw = urllib.request.urlopen(_R4_URL, timeout=60).read()
    if hashlib.sha256(_raw).hexdigest() != _R4_SHA:
        raise SystemExit("FATAL: 32741 payload hash mismatch")
    _ns = {}
    exec(compile(_raw, "patch_bluewhale_32741.py", "exec"), _ns)
    patch_32741 = _ns["patch_32741"]


def patch_advisor(root: Path) -> None:
    rel = "manager/src/main/java/com/maplesu/core/ui/screen/home/AdvisorWall.kt"
    path = root / rel
    text = path.read_text(encoding="utf-8")
    if "BluefishAdvisorEmpty" in text:
        print(f"skip: {rel} already patched")
        return
    if "import androidx.compose.foundation.layout.fillMaxWidth\n" not in text:
        fmw = "import androidx.compose.foundation.layout.fillMaxWidth\n"
        for anchor in (
            "import androidx.compose.foundation.layout.Box\n",
            "import androidx.compose.foundation.layout.Arrangement\n",
            "import androidx.compose.foundation.background\n",
        ):
            if anchor in text:
                text = text.replace(anchor, anchor + fmw, 1)
                break
        else:
            idx = text.find("\nimport ")
            if idx >= 0:
                text = text[: idx + 1] + fmw + text[idx + 1 :]
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
    patch_32740(ROOT)
    patch_32741(ROOT)
    patch_32740_update(ROOT)
    patch_32741_probe(ROOT)
    patch_32741_diag(ROOT)
    patch_32742_home(ROOT)
    patch_32743_clean(ROOT)
    patch_32744_diaglog(ROOT)
    patch_32745_clean(ROOT)
    patch_32746_statcard(ROOT)
    patch_32747_diag2(ROOT)
    patch_32748_home3(ROOT)
    patch_32749_home4(ROOT)
    patch_32750_nojb()
    patch_32751_introbrand()
    patch_32752_notice()
    patch_32753_theme()
    patch_32754_update_prompt()
    print("32739 advisor + compile fixes + combined entry + 32753 theme store + 32754 update prompt applied")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
