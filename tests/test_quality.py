from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_warehouse_quality_checks() -> None:
    load = subprocess.run(
        [sys.executable, str(ROOT / "python" / "etl_load.py")],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert load.returncode == 0, load.stderr

    qa = subprocess.run(
        [sys.executable, str(ROOT / "python" / "run_quality_checks.py")],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert qa.returncode == 0, qa.stdout + qa.stderr
