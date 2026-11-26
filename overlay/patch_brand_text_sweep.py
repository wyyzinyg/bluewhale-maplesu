#!/usr/bin/env python3
"""蓝鱼文案总清（在 patch_brand_skin_tail.py 之后跑）

前两个补丁只改了首页横幅、关于页、错误提示。真正扎眼的还在资源里：
工作模式叫 "MapleSU_Normal（玩机兼容模式）"、市场叫 "MapleSU 市场"、
主题商店、迁移页、安装提示里满屏都是 MapleSU。这里按语言把可见文案统一换掉：

  - 简体/繁体中文 → 蓝鱼 / 藍魚；其他语言 → BlueWhale
  - "MapleSU_xxx" 带下划线的模式名 → "蓝鱼 xxx"（去掉下划线，不像内部代号）
  - 枫叶相关措辞改成飘落粒子
  - "查看源码"链接改到蓝鱼仓库（上游致谢与 GPL 行保留原文，不动）
  - 版本号收尾：32732/3.18.0-bw → 32733/3.18.1-bw

保留不动的：about_maple_* （关于页上游署名）、含 GPL / MapleAutumn 的句子、
MapleSU_98260 这种带内核代号的内部标识（另行单独改写成人话）。

用法：python3 patch_brand_text_sweep.py <上游源码根目录>
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "src").resolve()
failures: list[str] = []
CHANGED = 0

STRING = re.compile(r'(<string[^>]*name="([^"]+)"[^>]*>)(.*?)(</string>)', re.S)
SKIP_NAMES = ("about_maple_",)
SKIP_TEXT = ("GPL", "MapleAutumn")


def locale_token(dirname: str) -> str:
    if dirname in ("values-zh-rTW", "values-zh-rHK"):
        return "藍魚"
    if dirname.startswith("values-zh"):
        return "蓝鱼"
    return "BlueWhale"


def rewrite_file(path: pathlib.Path) -> None:
    global CHANGED
    token = locale_token(path.parent.name)
    source = path.read_text(encoding="utf-8")

    def replace(match: re.Match[str]) -> str:
        global CHANGED
        name = match.group(2)
        body = match.group(3)
        if name.startswith(SKIP_NAMES) or any(mark in body for mark in SKIP_TEXT):
            return match.group(0)
        new = body
        new = new.replace("https://github.com/FengQiuFQ/MapleSU",
                          "https://github.com/wyyzinyg/bluewhale-maplesu")
        new = new.replace("MapleSU_98260", "98260").replace("MapleSU_93260", "93260")
        new = new.replace("MapleSU_", token + " ").replace("MapleSU", token)
        new = new.replace("枫叶飘落", "飘落特效").replace("枫叶大小", "粒子大小")
        new = new.replace("枫叶和图标", "粒子和图标").replace("伴随枫叶轻轻飘落", "伴随粒子轻轻飘落")
        new = new.replace("枫叶", "落叶")
        new = new.replace("内核方案由 " + token + " 维护", "内核方案沿用上游 MapleSU 的实现")
        if new != body:
            CHANGED += 1
        return match.group(1) + new + match.group(4)

    result = STRING.sub(replace, source)
    if result != source:
        path.write_text(result, encoding="utf-8")


res = ROOT / "manager/src/main/res"
if not res.is_dir():
    failures.append("缺目录: manager/src/main/res")
else:
    files = sorted(res.glob("values*/*.xml")) + sorted(res.glob("values*/*/*.xml"))
    for path in files:
        if path.is_file() and path.suffix == ".xml":
            rewrite_file(path)
    print(f"文案统一完成: {CHANGED} 条")

# 版本号收尾：3.18.1-bw / 32733
kt = ROOT / "manager/build.gradle.kts"
if kt.is_file():
    text = kt.read_text(encoding="utf-8")
    for old, new in (("        versionCode = 32732", "        versionCode = 32733"),
                     ('        versionName = "3.18.0-bw"', '        versionName = "3.18.1-bw"')):
        hits = text.count(old)
        if hits != 1:
            failures.append(f"manager/build.gradle.kts: {old.strip()} 命中 {hits} 处")
        else:
            text = text.replace(old, new)
    kt.write_text(text, encoding="utf-8")
else:
    failures.append("缺文件: manager/build.gradle.kts")

if failures:
    print("\n文案总清失败：", file=sys.stderr)
    for item in failures:
        print(" - " + item, file=sys.stderr)
    sys.exit(1)
print("文案总清已应用，版本 3.18.1-bw (32733)。")
