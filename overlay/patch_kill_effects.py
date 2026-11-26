#!/usr/bin/env python3
"""蓝鱼 3.18.2 收口：撤掉飘落/巨魔雨，清掉启动页里属于上游人物的位图

3.18.1 装上去暴露两个真问题：
  1. 启动页显示的是上游的红发人物。原因不是主题指错，而是 drawable-mdpi/…/xxxhdpi
     下还留着 `ic_launcher_splash.png` 五个密度位图（上游人物），密度变体优先级高于
     `drawable/ic_launcher_splash.xml`，手机上走的就是这些位图。删掉它们，XML 才会生效
     （XML 指向 3.16 的蓝鱼女仆 ic_app_brand）。
  2. 首页/超级用户/模块/设置上浮着一层蓝色小方块，那是「巨魔雨」和「枫叶」两个覆盖层。
     巨魔雨开关在旧数据里是开的，皮肤补丁只关了枫叶没关它。这里把两个覆盖层都停掉，
     设置页的「飘落特效 / 巨魔雨 / 倾斜」整组一并撤掉（开关点了也不再有任何效果）。

用法：python3 patch_kill_effects.py <上游源码根目录>
"""
import pathlib
import sys

ROOT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "src").resolve()
failures: list[str] = []


def patch_text(rel: str, pairs: list[tuple[str, str]]) -> None:
    path = ROOT / rel
    if not path.is_file():
        failures.append(f"缺文件: {rel}")
        return
    text = path.read_text(encoding="utf-8")
    for old, new in pairs:
        hits = text.count(old)
        if hits != 1:
            failures.append(f"{rel}: 期望 1 处，实际 {hits} 处 → {old.strip()[:60]!r}")
            return
        text = text.replace(old, new)
        print(f"改好 {rel}: {old.strip()[:46]}")
    path.write_text(text, encoding="utf-8")


def drop_call(rel: str, marker: str) -> None:
    """把以 marker 开头的一次完整调用（括号配平）整行删掉。"""
    path = ROOT / rel
    if not path.is_file():
        failures.append(f"缺文件: {rel}")
        return
    text = path.read_text(encoding="utf-8")
    start = text.find(marker)
    if start < 0:
        failures.append(f"{rel}: 未找到 {marker[:50]!r}")
        return
    open_idx = text.find("(", start)
    depth = 0
    end = -1
    for i in range(open_idx, len(text)):
        char = text[i]
        if char == "(":
            depth += 1
        elif char == ")":
            depth -= 1
            if depth == 0:
                end = i + 1
                break
    if end < 0:
        failures.append(f"{rel}: 括号未配平 {marker[:50]!r}")
        return
    line_start = text.rfind("\n", 0, start) + 1
    newline = text.find("\n", end)
    tail = text[newline + 1:] if newline >= 0 else ""
    path.write_text(text[:line_start] + tail, encoding="utf-8")
    print(f"删掉 {rel}: {marker.strip()[:60]}")


# 1) 启动页：删掉五个密度的上游人物位图，让 drawable 里的蓝鱼 XML 生效
removed = 0
for density in ("mdpi", "hdpi", "xhdpi", "xxhdpi", "xxxhdpi"):
    target = ROOT / f"manager/src/main/res/drawable-{density}/ic_launcher_splash.png"
    if target.is_file():
        target.unlink()
        removed += 1
if removed == 0:
    failures.append("没找到任何 drawable-*/ic_launcher_splash.png")
else:
    print(f"删掉启动页上游人物位图: {removed} 个")

# 2) 两个覆盖层停掉（保留代码与引用，只把条件断开；以后要做得重新设计）
patch_text("manager/src/main/java/com/maplesu/core/ui/MainActivity.kt", [
    ("                    if (uiState.snowEnabled) {",
     "                    // 蓝鱼 3.18.2：飘落层停用\n"
     "                    if (false && uiState.snowEnabled) {"),
    ("                    if (skin.appliedScene && uiState.trollRainEnabled) {",
     "                    // 蓝鱼 3.18.2：巨魔雨停用\n"
     "                    if (false && skin.appliedScene && uiState.trollRainEnabled) {"),
])

# 3) 设置页撤掉整组「飘落 / 巨魔雨 / 倾斜」
drop_call("manager/src/main/java/com/maplesu/core/ui/screen/settings/AppearanceSettingsBody.kt",
          "AppearanceGroup(stringResource(R.string.theme_section_effects)")

# 4) 升级迁移：把旧特效开关一并关掉（防止以后恢复开关时又冒出来）
patch_text("manager/src/main/java/com/maplesu/core/ui/viewmodel/MainActivityViewModel.kt", [
    ('                .putBoolean("snow_enabled", false).apply()',
     '                .putBoolean("snow_enabled", false)\n'
     '                .putBoolean("troll_rain_enabled", false)\n'
     '                .putBoolean("gravity_enabled", false).apply()'),
])

# 5) 外观摘要不再提飘落特效
patch_text("manager/src/main/res/values-zh-rCN/strings_ui_d.xml", [
    ('<string name="ui_d_appearance_summary">界面风格 · 主题 · 图片 · 飘落特效 · 壁纸</string>',
     '<string name="ui_d_appearance_summary">界面风格 · 主题 · 图片 · 壁纸</string>'),
])
patch_text("manager/src/main/res/values/strings_ui_d.xml", [
    ('<string name="ui_d_appearance_summary">Style · theme · images · ambient particles · wallpaper</string>',
     '<string name="ui_d_appearance_summary">Style · theme · images · wallpaper</string>'),
])

# 6) 版本收尾
patch_text("manager/build.gradle.kts", [
    ("        versionCode = 32733", "        versionCode = 32734"),
    ('        versionName = "3.18.1-bw"', '        versionName = "3.18.2-bw"'),
])

if failures:
    print("\n特效收口失败：", file=sys.stderr)
    for item in failures:
        print(" - " + item, file=sys.stderr)
    sys.exit(1)
print("特效收口已应用，版本 3.18.2-bw (32734)。")
