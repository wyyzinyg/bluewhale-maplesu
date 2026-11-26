#!/usr/bin/env python3
"""蓝鱼 · 收敛 MapleSU runtime 的构建目标集

公开快照里的 Ultra SDK 静态库还是 skroot 时代的产物（导出 skroot_env:: 符号），
而 ultra/probe 两个探针调用 maplesu::sdk::get_sdk_version / parse_module_desc_from_zip_file，
链接必然失败（run-21 的 ld.lld undefined symbol）。探针是设备端只读自检工具，
不进 APK 的打包集；所以让 cmake --build 只构建发布真正需要的五个目标。

用法：python3 patch_runtime_targets.py <上游源码根目录>
"""
import pathlib
import sys

ROOT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "src").resolve()
kt = ROOT / "manager/build.gradle.kts"
if not kt.is_file():
    print("缺 manager/build.gradle.kts", file=sys.stderr)
    sys.exit(1)
text = kt.read_text(encoding="utf-8")
old = '"--build", runtimeBuild.get().asFile, "-j", "6")'
new = ('"--build", runtimeBuild.get().asFile,\n'
       '            "--target", "maplesu-runtime", "maplesu-su", "maplesu_bootstrap",\n'
       '            "maplesu_parasite", "maplesu_ultra_bridge", "-j", "6")')
hits = text.count(old)
if hits != 1:
    print(f"runtime 构建目标行未命中（{hits} 处）", file=sys.stderr)
    sys.exit(1)
kt.write_text(text.replace(old, new), encoding="utf-8")
print("改好 build.gradle.kts: runtime 只构建发布所需目标（跳过 ultra 探针）")
