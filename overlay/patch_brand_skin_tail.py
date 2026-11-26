#!/usr/bin/env python3
"""蓝鱼皮肤收尾（在 patch_runtime_targets.py 之后跑）

修三件 patch_runtime_targets.py 还没覆盖的事：
  1. 新装默认值：不飘叶、不弹漫画首屏（老用户由 patch_runtime_targets 里的一次性迁移兜住）。
  2. 界面残留的枫叶/MapleSU 字样：设置页「枫叶飘落」、后端版本行。
  3. Material 关于弹窗的 kind 是非空参数，patch_runtime_targets 传了 null 会编译失败，
     这里把签名放宽成可空并在为空时不画横幅。

另外把「降动效策略」里被写死的 snow_enabled=false 还原成跟随 enabled，
否则设置页的飘落开关点了没反应。最后把整块可见文案交给 patch_brand_text_sweep.py。

用法：python3 patch_brand_skin_tail.py <上游源码根目录>
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
        print(f"改好 {rel}: {old.strip()[:44]}")
    path.write_text(text, encoding="utf-8")


def patch_all(rel: str, old: str, new: str) -> None:
    path = ROOT / rel
    if not path.is_file():
        failures.append(f"缺文件: {rel}")
        return
    text = path.read_text(encoding="utf-8")
    hits = text.count(old)
    if hits < 1:
        failures.append(f"{rel}: 未命中 → {old.strip()[:50]!r}")
        return
    path.write_text(text.replace(old, new), encoding="utf-8")
    print(f"改好 {rel}: {hits} 处 {old.strip()[:36]}")


# 1a. 新装默认不飘叶
patch_text("manager/src/main/java/com/maplesu/core/data/repository/SettingsRepositoryImpl.kt", [
    ('appearance.getBoolean("snow_enabled", true)', 'appearance.getBoolean("snow_enabled", false)'),
])
# 1b. 新装不弹漫画首屏
patch_all("manager/src/main/java/com/maplesu/core/ui/viewmodel/MainActivityViewModel.kt",
          "AppearancePreferences.INTRO_COMIC, true", "AppearancePreferences.INTRO_COMIC, false")
# 1c. 降动效策略不要写死关飘落，否则设置里的开关点了没反应
patch_text("manager/src/main/java/com/maplesu/core/ui/util/AppearancePrefsPolicy.kt", [
    ('        "snow_enabled" to false,', '        "snow_enabled" to enabled,'),
])

# 2. 设置页与后端版本行的残留字样
patch_text("manager/src/main/res/values-zh-rCN/strings_ui_d.xml", [
    ('<string name="ui_d_appearance_summary">界面风格 · 主题 · 图片 · 枫叶飘落 · 壁纸</string>',
     '<string name="ui_d_appearance_summary">界面风格 · 主题 · 图片 · 飘落特效 · 壁纸</string>'),
    ('<string name="ui_d_fall_title">枫叶飘落</string>',
     '<string name="ui_d_fall_title">飘落特效</string>'),
    ('<string name="ui_d_fall_summary">让枫叶轻轻飘落，可随时关闭</string>',
     '<string name="ui_d_fall_summary">轻柔的飘落动效，默认关闭，可随时打开</string>'),
])
patch_text("manager/src/main/res/values/strings_ui_d.xml", [
    ('<string name="ui_d_appearance_summary">Style · theme · images · falling leaves · wallpaper</string>',
     '<string name="ui_d_appearance_summary">Style · theme · images · ambient particles · wallpaper</string>'),
    ('<string name="ui_d_fall_title">Falling maple leaves</string>',
     '<string name="ui_d_fall_title">Ambient particles</string>'),
    ('<string name="ui_d_fall_summary">Gentle falling leaves; turn off at any time</string>',
     '<string name="ui_d_fall_summary">Gentle falling particles; off by default</string>'),
])
patch_text("manager/src/main/res/values-zh-rCN/maplesu_strings.xml", [
    ('<string name="maplesu_backend_version">MapleSU · API %1$d</string>',
     '<string name="maplesu_backend_version">蓝鱼 · API %1$d</string>'),
])
patch_text("manager/src/main/res/values/maplesu_strings.xml", [
    ('<string name="maplesu_backend_version">MapleSU · API %1$d</string>',
     '<string name="maplesu_backend_version">BlueWhale · API %1$d</string>'),
])

# 3. Material 关于弹窗：放宽 kind 可空，空时不画横幅
patch_text("manager/src/main/java/com/maplesu/core/ui/component/maple/BrandDialogMaterial.kt", [
    ("internal fun BrandDialogMaterial(\n    kind: BrandBannerKind,",
     "internal fun BrandDialogMaterial(\n    kind: BrandBannerKind?,"),
    ("        icon = { BrandBanner(kind = kind, accent = MaterialTheme.colorScheme.primary, soft = false) },",
     "        icon = if (kind == null) null else {\n"
     "            { BrandBanner(kind = kind, accent = MaterialTheme.colorScheme.primary, soft = false) }\n"
     "        },"),
])

# 4. 把整块可见文案（工作模式名、市场、迁移页、安装提示）交给总清脚本
sweep = pathlib.Path(__file__).with_name("patch_brand_text_sweep.py")
if sweep.is_file():
    import runpy

    sys.argv = [str(sweep), str(ROOT)]
    runpy.run_path(str(sweep), run_name="__main__")
else:
    failures.append("缺文件: overlay/patch_brand_text_sweep.py")

if failures:
    print("\n皮肤收尾失败：", file=sys.stderr)
    for item in failures:
        print(" - " + item, file=sys.stderr)
    sys.exit(1)
print("皮肤收尾已应用。")
