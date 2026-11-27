#!/usr/bin/env python3
"""BlueWhale 3.21.0 (32738): verifiable SU-log evidence export.

Run after patch_bluewhale_3210.py. The unified diff is applied with git apply so the
upstream CRLF files keep their existing line endings. Re-running validates the reverse
patch instead of applying a second copy.
"""
from pathlib import Path
import subprocess
import sys

ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else "src").resolve()
PATCH = Path(__file__).with_name("bluewhale_322.patch").resolve()
MARKER = ROOT / "manager/src/main/java/com/maplesu/core/ui/util/SulogEvidenceArchive.kt"


def git_apply(*args: str) -> None:
    subprocess.run(
        ["git", "apply", "--ignore-whitespace", *args, str(PATCH)],
        cwd=ROOT,
        check=True,
    )


if not ROOT.is_dir() or not PATCH.is_file():
    raise SystemExit("Missing source root or bluewhale_322.patch")

if MARKER.is_file():
    git_apply("--reverse", "--check")
    print("BlueWhale 32738 SU-log evidence export is already applied; reverse check passed.")
else:
    git_apply("--check")
    git_apply()
    if not MARKER.is_file():
        raise SystemExit("Patch completed without SulogEvidenceArchive.kt")
    print("BlueWhale 32738 SU-log evidence export applied.")
