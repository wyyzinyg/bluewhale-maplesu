#!/usr/bin/env python3
"""32746 (3.22.7-bw): the environment status card stops outliving the probe.

Real root cause of the card the user still sees on 32745:

  HomeUiState.showEnvironmentStatusCard fed `environmentFailure != null` into
  the gate, so a *finished* probe with a terminal failure (UNCONFIRMED /
  TIMED_OUT / BUSY) kept rendering `CheckingStatusCard` — title
  `home_environment_check_failed` ("未检测到可用的 root 环境"), body
  `home_environment_check_unconfirmed_summary` ("运行环境还没确认。点重试；
  没 root 时先空着是正常的。") — right below the Root entry card.

  That is a *different* card from the `showEnvironmentRefreshWarning` block
  deleted in 32745 (which said "探测超时了…或点「重新检测」"). Deleting the
  refresh block was correct but insufficient: both skins still reach the same
  stale card through `showEnvironmentStatusCard`.

After this patch the card exists only while the probe is genuinely running;
every terminal outcome (timeout / busy / unconfirmed) is carried by the Root
entry card's own title + summary, which 32745 already made visible during
checking.

Bumps manager version 32745/3.22.6-bw -> 32746/3.22.7-bw.
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else "src")

UI_STATE = "manager/src/main/java/com/maplesu/core/ui/screen/home/HomeUiState.kt"
GRADLE = "manager/build.gradle.kts"

OLD_GATE = '''    val showEnvironmentStatusCard: Boolean
        get() = (!ultraBrandVisible || hiddenConfirming) &&
            (showLiteChecking || environmentFailure != null)'''

NEW_GATE = '''    // 3.22.7-bw：状态卡只在「真的在探测」时存在。
    // 之前 `|| environmentFailure != null` 会让探测结束后的终态（UNCONFIRMED /
    // TIMED_OUT / BUSY）继续渲染 CheckingStatusCard，正文是「运行环境还没确认。
    // 点重试；没 root 时先空着是正常的。」—— 用户在 32745 上看到的就是这张卡。
    // 终态一律交给 Root 入口卡承载（32745 已保证它在检查中也可见）。
    val showEnvironmentStatusCard: Boolean
        get() = (!ultraBrandVisible || hiddenConfirming) &&
            showLiteChecking'''


def _p(root: Path, rel: str) -> Path:
    return root / rel


def patch_gate(root: Path) -> None:
    path = _p(root, UI_STATE)
    if not path.is_file():
        print(f"SKIP gate: missing {UI_STATE}")
        return
    text = path.read_text(encoding="utf-8")
    if NEW_GATE in text:
        print("skip: environment status card gate already narrowed")
        return
    if OLD_GATE not in text:
        raise SystemExit(f"FATAL: gate anchor not found in {UI_STATE}")
    if text.count(OLD_GATE) != 1:
        raise SystemExit(f"FATAL: gate anchor occurs {text.count(OLD_GATE)} times")
    text = text.replace(OLD_GATE, NEW_GATE, 1)
    path.write_text(text, encoding="utf-8")
    print("patched: showEnvironmentStatusCard no longer keeps a finished probe on screen")


def bump_version(root: Path) -> None:
    path = _p(root, GRADLE)
    if not path.is_file():
        print(f"SKIP bump: missing {GRADLE}")
        return
    text = path.read_text(encoding="utf-8")
    pairs = (("versionCode = 32745", "versionCode = 32746"),
             ('versionName = "3.22.6-bw"', 'versionName = "3.22.7-bw"'))
    hit = 0
    for old, new in pairs:
        if new in text:
            hit += 1
            continue
        if old not in text:
            # 干跑树可能还停在上一个版本；只提示不失败，真构建会拿到 32745。
            print(f"WARN bump: '{old}' not found (dry tree may be stale)")
            continue
        text = text.replace(old, new, 1)
        hit += 1
    path.write_text(text, encoding="utf-8")
    if hit:
        print("bumped manager version -> 32746/3.22.7-bw")


def patch_32746_statcard(root: Path) -> None:
    patch_gate(root)
    bump_version(root)


if __name__ == "__main__":
    patch_32746_statcard(ROOT.resolve())
