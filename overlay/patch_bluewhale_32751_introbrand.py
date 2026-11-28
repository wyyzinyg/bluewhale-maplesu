#!/usr/bin/env python3
"""32751 (3.22.12-bw): 首启引导页清掉上游品牌，换掉上游插画。

用户实测反馈（2026-11-28 21:56）：装完 32750 第一次打开，引导页预览卡上
还印着 "MapleSU"，配图还是上游那张二次元少女。两处都要处理：

1. AppearanceIntroScreen.kt 第 154 行是**硬编码字符串** IntroText("MapleSU", ...)，
   patch_brand_text_sweep.py 只扫 res/values* 里的 <string>，扫不到 Compose 里的
   字面量，所以这里一直露着上游名字。
2. art_default.jpg 是上游插画（drawable-nodpi 下一张人物线稿合成照），
   AppearanceIntroScreen 和 StatusDecoration.loadBuiltin 都在引用它。
   按既定授权边界（品牌资源不进包），换成我们自己的深海光斑底图。

顺带把预览卡的三句上游 slogan 换成蓝鱼口径。

Bumps 32750/3.22.11-bw -> 32751/3.22.12-bw.
"""
from __future__ import annotations

import base64
import sys
from pathlib import Path

ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else "src")

INTRO_KT = "manager/src/main/java/com/maplesu/core/ui/screen/settings/AppearanceIntroScreen.kt"
ZH_XML = "manager/src/main/res/values-zh-rCN/maple_appearance.xml"
EN_XML = "manager/src/main/res/values/maple_appearance.xml"
ART = "manager/src/main/res/drawable-nodpi/art_default.jpg"
GRADLE = "manager/build.gradle.kts"

# 1024->512 深海光斑底图（自绘，非上游素材）
ART_B64 = (
    "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"
)

KT_PAIRS = (
    ('IntroText("MapleSU", mode, text, 23, FontWeight.Medium)',
     'IntroText("BluefishSU", mode, text, 23, FontWeight.Medium)'),
)

ZH_PAIRS = (
    ('<string name="appearance_intro_preview_ready">自在掌控</string>',
     '<string name="appearance_intro_preview_ready">内核已接管</string>'),
    ('<string name="appearance_intro_preview_detail">让每一次使用，都更合心意</string>',
     '<string name="appearance_intro_preview_detail">接下来的每一步，都由你说了算</string>'),
    ('<string name="appearance_intro_preview_device">一目了然</string>',
     '<string name="appearance_intro_preview_device">设备信息</string>'),
)

EN_PAIRS = (
    ('<string name="appearance_intro_preview_ready">Make it yours</string>',
     '<string name="appearance_intro_preview_ready">Kernel online</string>'),
    ('<string name="appearance_intro_preview_detail">Your device, your style</string>',
     '<string name="appearance_intro_preview_detail">Every next step is yours</string>'),
    ('<string name="appearance_intro_preview_device">At a glance</string>',
     '<string name="appearance_intro_preview_device">Device info</string>'),
    ('gently falling maple leaves', 'gently falling particles'),
)


def swap_text(root: Path, rel: str, pairs, tag: str) -> None:
    p = root / rel
    if not p.is_file():
        print("SKIP 32751: missing %s" % rel)
        return
    text = p.read_text(encoding="utf-8")
    hit = 0
    for old, new in pairs:
        if old in text:
            text = text.replace(old, new, 1)
            hit += 1
        else:
            print("WARN 32751: %s anchor not found: %s" % (tag, old[:48]))
    if hit:
        p.write_text(text, encoding="utf-8")
        print("patched: %s (%d replacements)" % (tag, hit))


def replace_art(root: Path) -> None:
    p = root / ART
    if not p.parent.is_dir():
        print("SKIP 32751: missing dir %s" % p.parent)
        return
    data = base64.b64decode("".join(ART_B64))
    p.write_bytes(data)
    print("patched: art_default.jpg -> %d bytes (deep-sea backdrop)" % len(data))


def bump_version(root: Path) -> None:
    p = root / GRADLE
    if not p.is_file():
        print("SKIP bump: missing %s" % GRADLE)
        return
    text = p.read_text(encoding="utf-8")
    pairs = (("versionCode = 32750", "versionCode = 32751"),
             ('versionName = "3.22.11-bw"', 'versionName = "3.22.12-bw"'))
    hit = 0
    for old, new in pairs:
        if old in text:
            text = text.replace(old, new, 1)
            hit += 1
        else:
            print("WARN bump: '%s' not found (dry tree may be stale)" % old)
    if hit:
        p.write_text(text, encoding="utf-8")
        print("bumped manager version -> 32751/3.22.12-bw")


def main() -> None:
    print("32751: onboarding brand cleanup + own artwork")
    swap_text(ROOT, INTRO_KT, KT_PAIRS, "intro kt hardcoded title")
    swap_text(ROOT, ZH_XML, ZH_PAIRS, "zh preview copy")
    swap_text(ROOT, EN_XML, EN_PAIRS, "en preview copy")
    replace_art(ROOT)
    bump_version(ROOT)


if __name__ == "__main__":
    main()
