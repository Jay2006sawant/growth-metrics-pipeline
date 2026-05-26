from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_validate_raw_passes_on_bundled_feeds() -> None:
    result = subprocess.run(
        [sys.executable, str(ROOT / "python" / "validate_raw.py")],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr or result.stdout
