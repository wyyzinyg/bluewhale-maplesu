#!/usr/bin/env python3
"""蓝鱼 · MapleSU 基座品牌化补丁

在上游 MapleSU 源码树上就地应用这些改动：
  1. applicationId  dev.maplesu.manager → com.blue.whale.mask
  2. 版本号        5.2.1 / 50201      → 3.17.0-bw / 32731
  3. 应用名        MapleSU            → 蓝色大肥鱼
  4. 默认主色     未设置(0)            → #2856D8（深海军蓝）
  5. 启动图标底色 #FF3267C0            → #FF08101F，前景换蓝鱼矢量鲸鱼
  6. preBuild 的 Ultra SDK 自检加属性开关（公开快照缺 .tmp 构建报告，自检必失败）
  7. provider 构建脚本的 cmake/ninja 可执行名改成跨平台（上游写死 .exe，Linux 必挂）

用法：python3 apply_bluewhale.py <上游源码根目录>
每个替换点都必须命中，命中不了直接报错退出——宁可失败，不要打出一个半改的包。
"""
import pathlib
import sys

ROOT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "src").resolve()
HERE = pathlib.Path(__file__).resolve().parent
failures: list[str] = []


def patch(rel: str, old: str, new: str, count: int = 1) -> None:
    path = ROOT / rel
    if not path.is_file():
        failures.append(f"缺文件: {rel}")
        return
    text = path.read_text(encoding="utf-8")
    hits = text.count(old)
    if hits != count:
        failures.append(f"{rel}: 期望命中 {count} 处，实际 {hits} 处 → {old[:60]!r}")
        return
    path.write_text(text.replace(old, new), encoding="utf-8")
    print(f"改好 {rel}")


# —— 1/2. 身份与版本 ——
patch("manager/build.gradle.kts", 'applicationId = "dev.maplesu.manager"',
      'applicationId = "com.blue.whale.mask"')
patch("manager/build.gradle.kts", "versionCode = 50201", "versionCode = 32731")
patch("manager/build.gradle.kts", 'versionName = "5.2.1"', 'versionName = "3.17.0-bw"')

# —— 3. 应用名 ——
patch("manager/src/main/res/values/maplesu_strings.xml",
      '<string name="app_name" translatable="false">MapleSU</string>',
      '<string name="app_name" translatable="false">蓝色大肥鱼</string>')

# —— 4. 默认主色 ——
patch("manager/src/main/java/com/maplesu/core/data/repository/SettingsRepositoryImpl.kt",
      'appearance.getInt("key_color", 0)',
      'appearance.getInt("key_color", BLUEWHALE_KEY_COLOR)')

const_block = (
    "/** 蓝鱼默认主色：深海军蓝（#2856D8），未设置时用它生成整套配色。 */\n"
    "private val BLUEWHALE_KEY_COLOR = 0xFF2856D8.toInt()\n"
)
repo_kt = ROOT / "manager/src/main/java/com/maplesu/core/data/repository/SettingsRepositoryImpl.kt"
if repo_kt.is_file():
    lines = repo_kt.read_text(encoding="utf-8").splitlines()
    if not any("BLUEWHALE_KEY_COLOR =" in line for line in lines):
        last_import = max(i for i, l in enumerate(lines) if l.startswith("import "))
        lines[last_import + 1:last_import + 1] = ["", const_block.rstrip("\n")]
        repo_kt.write_text("\n".join(lines) + "\n", encoding="utf-8")
        print("插入 BLUEWHALE_KEY_COLOR 常量")

# —— 5. 图标 ——
patch("manager/src/main/res/values/colors.xml",
      '<color name="ic_launcher_background">#FF3267C0</color>',
      '<color name="ic_launcher_background">#FF08101F</color>')

# 蓝鱼品牌图标：矢量鲸鱼（深蓝底 + 白描边），比整张位图更贴合深蓝风格。
# 上游在 drawable-*/ic_launcher_foreground.png 放了位图，同名同目录会冲突，先清掉再放矢量。
for png in ROOT.glob("manager/src/main/res/drawable*/ic_launcher_foreground.png"):
    png.unlink()
    print(f"移除位图 {png.parent.name}")
vector_src = HERE / "ic_launcher_foreground.xml"
if vector_src.is_file():
    (ROOT / "manager/src/main/res/drawable/ic_launcher_foreground.xml").write_text(
        vector_src.read_text(encoding="utf-8"), encoding="utf-8")
    print("放入矢量图标")
else:
    failures.append("缺 overlay/ic_launcher_foreground.xml")

# —— 6. Ultra SDK 自检开关 ——
patch(
    "manager/build.gradle.kts",
    'tasks.named("preBuild") { dependsOn(verifyUltraSdkIdentity) }',
    "// BlueWhale：公开源码快照未导出 .tmp/p1-source-r9-build/report/build-report.json，\n"
    "// 上游自检在快照上必然失败。用属性开关跳过，而不是删掉这项检查。\n"
    "val skipUltraSdkIdentityVerify = providers.gradleProperty(\"bluewhaleSkipSdkVerify\").orNull == \"true\"\n"
    "tasks.named(\"preBuild\") { if (!skipUltraSdkIdentityVerify) dependsOn(verifyUltraSdkIdentity) }",
)

# —— 7. provider 构建脚本的跨平台修正 ——
# 上游开发者在 Windows 上开发，build.py 把 cmake 可执行名写死成 cmake.exe / ninja.exe，
# 在 Linux/CI 上必然 FileNotFoundError，导致 buildJailbreakProviders 整条失败。
# 这里改成按 os.name 选后缀，两个平台的原始行为都保留。
prov = ROOT / "jailbreak-providers/build.py"
if prov.is_file():
    src = prov.read_text(encoding="utf-8")
    if 'args.sdk / "cmake/3.22.1/bin/cmake.exe"' in src:
        src = src.replace(
            'args.sdk / "cmake/3.22.1/bin/cmake.exe"',
            'args.sdk / ("cmake/3.22.1/bin/cmake.exe" if os.name == "nt" else "cmake/3.22.1/bin/cmake")')
        print("修好 build.py: cmake 可执行名跨平台")
    if "cmake.with_name('ninja.exe')" in src:
        src = src.replace("cmake.with_name('ninja.exe')",
                          "cmake.with_name('ninja.exe' if os.name == 'nt' else 'ninja')")
        print("修好 build.py: ninja 可执行名跨平台")
    if not src.lstrip().startswith("import os") and "\nimport os\n" not in src:
        lines = src.splitlines()
        first = next((i for i, l in enumerate(lines)
                      if l.startswith("import ") or l.startswith("from ")), 0)
        lines.insert(first, "import os")
        src = "\n".join(lines) + "\n"
        print("修好 build.py: 补 import os")
    # 自检只认「原始硬编码」是否还在：三元表达式里本就该出现 .exe 字样，不能当残留
    if 'args.sdk / "cmake/3.22.1/bin/cmake.exe"' in src:
        failures.append("jailbreak-providers/build.py: cmake 硬编码未替换")
    if "cmake.with_name('ninja.exe')" in src:
        failures.append("jailbreak-providers/build.py: ninja 硬编码未替换")
    prov.write_text(src, encoding="utf-8")
else:
    failures.append("缺文件: jailbreak-providers/build.py")

if failures:
    print("\n补丁失败：", file=sys.stderr)
    for item in failures:
        print(" - " + item, file=sys.stderr)
    sys.exit(1)
print("\n蓝鱼品牌化补丁已全部应用。")
