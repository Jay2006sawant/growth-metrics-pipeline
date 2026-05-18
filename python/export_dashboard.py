"""Run KPI SQL from sql/exports and write BI-ready CSVs."""

from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd
from sqlalchemy import create_engine

sys.path.insert(0, str(Path(__file__).resolve().parent))
from config_loader import load_config, resolve_path

ROOT = Path(__file__).resolve().parents[1]


def read_sql(rel_path: str) -> str:
    path = resolve_path(rel_path)
    return path.read_text(encoding="utf-8")


def main() -> None:
    cfg = load_config()
    db_rel = cfg["warehouse"]["sqlite_path"]
    db_path = resolve_path(db_rel)
    if not db_path.exists():
        raise FileNotFoundError("Run etl_load.py first")

    out_dir = resolve_path(cfg["exports"]["output_dir"])
    out_dir.mkdir(parents=True, exist_ok=True)

    engine = create_engine(f"sqlite:///{db_path}")
    for name, rel_sql in cfg["exports"]["queries"].items():
        sql = read_sql(rel_sql)
        df = pd.read_sql(sql, engine)
        target = out_dir / f"{name}.csv"
        df.to_csv(target, index=False)
        print(f"Wrote {target} ({len(df)} rows)")


if __name__ == "__main__":
    main()
