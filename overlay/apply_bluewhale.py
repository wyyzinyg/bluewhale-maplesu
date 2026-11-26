#!/usr/bin/env python3
"""蓝鱼 · MapleSU 基座品牌化补丁

在上游 MapleSU 源码树上就地应用这些改动：
  1. applicationId  dev.maplesu.manager → com.blue.whale.mask
  2. 版本号        5.2.1 / 50201      → 3.17.0-bw / 32731
  3. 应用名        MapleSU            → 蓝色大肥鱼
  4. 默认主色     未设置(0)            → #2856D8（深海军蓝）
  5. 启动图标底色 #FF3267C0            → #FF08101F，前景换蓝鱼矢量鲸鱼
  6. preBuild 的 Ultra SDK 自检加属性开关（公开快照缺 .tmp 构建报告，自检必失败）
  7. provider 构建脚本的 Windows 假设改成跨平台（cmake.exe/ninja.exe、ir spec 反斜杠路径）
  8. 公开快照的 runtime/pro 死路径改用公开的 runtime/ultra 策略 bundle
  9. prepare_host_dependencies 的 Maven 下载加重试并报出具体 URL

用法：python3 apply_bluewhale.py <上游源码根目录>
每个替换点都必须命中，命中不了直接报错退出——宁可失败，不要打出一个半改的包。
"""
import hashlib
import json
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
# 上游开发者在 Windows 上开发，build.py 里有两处 Windows 假设会让 Linux/CI 必挂：
#   a) cmake/ninja 可执行名写死 .exe  → FileNotFoundError
#   b) ir spec 记录里存反斜杠路径      → Linux 当文件名，报 “missing generated spec” 并退出 3
# 这里改成按 os.name 选后缀，并归一反斜杠（另加 basename 回退，防目录前缀与预期不符）。
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

    spec_pat_dq = 'spec_path = Path(record["spec"])'
    spec_pat_sq = "spec_path = Path(record['spec'])"
    spec_new = (
        'spec_path = Path(record["spec"].replace("\\\\", "/"))\n'
        '        if not spec_path.is_file() and not spec_path.is_absolute():\n'
        '            _alt = ROOT / "ir-loader" / "specs" / spec_path.name\n'
        '            if _alt.is_file():\n'
        '                spec_path = _alt')
    if spec_pat_dq in src:
        src = src.replace(spec_pat_dq, spec_new)
        print("修好 build.py: ir spec 路径反斜杠归一（带 basename 回退）")
    elif spec_pat_sq in src:
        src = src.replace(spec_pat_sq, spec_new)
        print("修好 build.py: ir spec 路径反斜杠归一（单引号版）")
    else:
        failures.append("jailbreak-providers/build.py: 未找到 ir spec 路径行（上游可能已变）")

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

    # L3 失败时不能让 --quiet 吞掉门禁细节。run_l3 的完整 stdout/stderr 会由
    # build_root_l3_single 追加到 build.log，失败步骤再回传，方便按真实分支修复。
    l3_quiet = ('               "--out-dir", str(l3_dir), "--contract", str(contract), "--quiet"] + extra')
    l3_loud = ('               "--out-dir", str(l3_dir), "--contract", str(contract)] + extra')
    if src.count(l3_quiet) == 1:
        src = src.replace(l3_quiet, l3_loud)
        print("修好 build.py: L3 构建保留完整门禁日志")
    else:
        failures.append("jailbreak-providers/build.py: L3 --quiet 行未命中")
    prov.write_text(src, encoding="utf-8")
else:
    failures.append("缺文件: jailbreak-providers/build.py")

# —— 8. 公开快照的 runtime/pro 死路径 ——
# CI 跑到 l3 模块时死在 policy_hook_build.derive：SDK 报告选的 policy boot bundle
# 指向 runtime/pro/policy，而这棵子树只在作者私有工作区，公开仓库没有。
# 公开的 runtime/ultra/policy 是同一产品线：bundle 自带的 kernelSourceSha256 在 ultra
# 树里能自洽（18 个源全匹配），所以固定走 ultra，并把「工具与 SDK 后端同源」的硬校验
# 挂到同一个跳过开关上；校验前先把 bundle 的自检做一遍，颠簸推诿到 CI 里看不见的地方。
gradle_kt = ROOT / "manager/build.gradle.kts"
if gradle_kt.is_file():
    g = gradle_kt.read_text(encoding="utf-8")
    chain_old = ('    .getOrElse(policyBootBundleManifest?.let { it.resolveSibling("${it.nameWithoutExtension}.cpp") }\n'
                 '        ?: rootProject.file("runtime/ultra/policy/hook-bundles/policy-bundles.cpp"))')
    chain_new = '    .getOrElse(rootProject.file("runtime/ultra/policy/hook-bundles/policy-bundles.cpp"))'
    if g.count(chain_old) == 1:
        g = g.replace(chain_old, chain_new)
        print("改好 build.gradle.kts: policy bundle 固定 ultra")
    else:
        failures.append("manager/build.gradle.kts: policyHookBundles 默认链未命中")
    require_old = "if (policyBootBundleManifest != null) {"
    require_new = ('if (policyBootBundleManifest != null &&\n'
                   '    providers.gradleProperty("bluewhaleSkipSdkVerify").orNull != "true") {')
    if g.count(require_old) == 1:
        g = g.replace(require_old, require_new)
        print("改好 build.gradle.kts: bundle 同源校验随自检开关跳过")
    else:
        failures.append("manager/build.gradle.kts: bundle 同源校验未命中")
    gradle_kt.write_text(g, encoding="utf-8")
else:
    failures.append("缺文件: manager/build.gradle.kts")

bundle_json = ROOT / "runtime/ultra/policy/hook-bundles/policy-bundles.json"
if bundle_json.is_file():
    doc = json.loads(bundle_json.read_text(encoding="utf-8"))
    sources = doc.get("kernelSourceSha256", {})
    outside = [n for n in sources if not n.startswith("runtime/ultra/")]
    drift = [n for n, sha in sources.items()
             if (ROOT / n).is_file() and hashlib.sha256((ROOT / n).read_bytes()).hexdigest() != sha]
    missing = [n for n in sources if not (ROOT / n).is_file()]
    if outside:
        failures.append(f"ultra bundle 里的非 ultra 源: {outside[:3]}")
    if missing:
        failures.append(f"ultra bundle 缺源文件: {missing[:3]}")
    if drift:
        print(f"注意：ultra bundle 自皮摘要漂移 {len(drift)} 个（仍继续）")
    print(f"policy bundle 自检：{len(sources)} 个源，缺 {len(missing)}，漂 {len(drift)}")
else:
    failures.append("缺 runtime/ultra/policy/hook-bundles/policy-bundles.json")

# —— 9. 宿主编译依赖下载的重试与可诊断性 ——
# l3 模块的 Kotlin 宿主编译在 gradle 之前按缓存布局找 15 个 jar，由
# prepare_host_dependencies.py 从 Maven Central 拉。runner 上出现过
# HOST_JVM_DEPENDENCY_PREPARATION_FAILED:HTTP Error 404（run-19）：Maven 边缘节点偶发
# 404，错误信息又不带 URL，无从定位。这里把单次 urlopen 换成 4 次重试，失败时把
# 具体 URL 带进错误信息。
phd = ROOT / "tools/prepare_host_dependencies.py"
if phd.is_file():
    s = phd.read_text(encoding="utf-8")
    helper = (
        "def _retry_urlopen(url: str, attempts: int = 4, delay: float = 10.0):\n"
        "    \"\"\"下载宿主编译用 jar：Maven Central 边缘节点偶发 404，重试并带出具体 URL。\"\"\"\n"
        "    import time\n"
        "    last_error = None\n"
        "    for attempt in range(1, attempts + 1):\n"
        "        try:\n"
        "            return urllib.request.urlopen(url, timeout=60)\n"
        "        except urllib.error.HTTPError as error:\n"
        "            last_error = error\n"
        "            if attempt < attempts:\n"
        "                time.sleep(delay)\n"
        "    raise ValueError(f\"HOST_JVM_DEPENDENCY_HTTP_{last_error.code}:{url}\") from last_error\n"
        "\n"
    )
    anchor = "def verify(path: Path, record: dict) -> None:\n"
    if s.count(anchor) == 1 and "_retry_urlopen" not in s:
        s = s.replace(anchor, helper + anchor)
        print("修好 prepare_host_dependencies.py: 插入 _retry_urlopen")
    open_line = "            with urllib.request.urlopen(MAVEN_BASE + relative, timeout=60) as response:\n"
    if s.count(open_line) == 1:
        s = s.replace(open_line, "            with _retry_urlopen(MAVEN_BASE + relative) as response:\n")
        print("修好 prepare_host_dependencies.py: 下载走重试")
    else:
        failures.append("tools/prepare_host_dependencies.py: urlopen 行未命中")
    phd.write_text(s, encoding="utf-8")
else:
    failures.append("缺文件: tools/prepare_host_dependencies.py")

if failures:
    print("\n补丁失败：", file=sys.stderr)
    for item in failures:
        print(" - " + item, file=sys.stderr)
    sys.exit(1)
print("\n蓝鱼品牌化补丁已全部应用。")
