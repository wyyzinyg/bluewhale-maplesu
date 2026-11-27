#!/usr/bin/env python3
"""BlueWhale 32738 UI hotfix: no-root entry visibility + remove beta banner.

Run after patch_bluewhale_321.py (and 3210 for 32738).

Why:
  `showNoRootEntry` used `!suppressEntries && !hiddenConfirming`.  On an
  un-activated device HiddenStartupConfirm.current() can stay true because the
  hidden snapshot is absent, so the no-root card was permanently suppressed.
  The card must only be suppressed by a *real* hidden state (`masking`); the
  confirmation window may still suppress other manager entries.

Also removes the in-app beta banner calls from both Miuix and Material home
layouts.  The banner wording ("内测版") is intentionally gone; the banner
composable itself is left in place so a future, explainable use can reuse it.
"""
from pathlib import Path
import re
import sys

ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else "src").resolve()
HOME_SCREEN = ROOT / "manager/src/main/java/com/maplesu/core/ui/screen/home/HomeScreen.kt"
HOME_MIUIX = ROOT / "manager/src/main/java/com/maplesu/core/ui/screen/home/HomeMiuix.kt"
HOME_MATERIAL = ROOT / "manager/src/main/java/com/maplesu/core/ui/screen/home/HomeMaterial.kt"

OLD_CONDITION = """    val showNoRootEntry = !suppressEntries &&
        !statusState.isManager &&
        !statusState.isLateLoadMode &&
        !statusState.litePending &&
        !statusState.hiddenConfirming"""

NEW_CONDITION = """    // 3.20.2：环境失败/未确认时 hiddenConfirming 也可能为 true，
    // 不能把它当成“隐身中”的证据，否则无 root 设备上的入口会被永久压掉。
    // 真正的隐身只看 entryFacts.hidden.masking；确认窗口仍会压住其它管理器入口。
    val showNoRootEntry = !entryFacts.hidden.masking &&
        !statusState.isManager &&
        !statusState.isLateLoadMode &&
        !statusState.litePending &&
        !statusState.environmentChecking &&
        (!entryFacts.hidden.confirming || statusState.environmentFailure != null)"""

BANNER_LINE = re.compile(r"^[ \t]*HomeBetaBanner\(onClick = actions\.onFeedbackClick\)\r?\n", re.MULTILINE)

changed: list[str] = []


def read(path: Path) -> str | None:
    if not path.is_file():
        return None
    return path.read_text(encoding="utf-8")


def write(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8", newline="")
    changed.append(str(path.relative_to(ROOT)))


def patch_condition() -> None:
    text = read(HOME_SCREEN)
    if text is None:
        raise SystemExit(f"missing {HOME_SCREEN}")
    if NEW_CONDITION in text:
        print("no-root entry condition already fixed")
        return
    if OLD_CONDITION not in text:
        raise SystemExit("no-root entry condition anchor not found; refusing to guess")
    write(HOME_SCREEN, text.replace(OLD_CONDITION, NEW_CONDITION, 1))
    print("fixed no-root entry condition")


def patch_banner(path: Path) -> None:
    text = read(path)
    if text is None:
        raise SystemExit(f"missing {path}")
    if "HomeBetaBanner(onClick = actions.onFeedbackClick)" not in text:
        print(f"beta banner already absent: {path.name}")
        return
    new_text, count = BANNER_LINE.subn("", text)
    if count != 1:
        raise SystemExit(f"expected exactly one beta banner call in {path.name}, found {count}")
    write(path, new_text)
    print(f"removed beta banner: {path.name}")


for target in (HOME_SCREEN, HOME_MIUIX, HOME_MATERIAL):
    if not target.is_file():
        raise SystemExit(f"missing required file: {target}")

patch_condition()
patch_banner(HOME_MIUIX)
patch_banner(HOME_MATERIAL)

if not changed:
    print("32738 UI hotfix already applied")
else:
    print("32738 UI hotfix applied:", ", ".join(changed))
