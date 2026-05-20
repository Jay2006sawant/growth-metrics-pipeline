"""Merge new order rows into an existing warehouse table by order_id."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import pandas as pd
from sqlalchemy import create_engine

sys.path.insert(0, str(Path(__file__).resolve().parent))
from config_loader import load_config, resolve_path


def merge_orders(db_path: Path, patch_csv: Path) -> tuple[int, int]:
    engine = create_engine(f"sqlite:///{db_path}")
    existing = pd.read_sql("SELECT * FROM orders", engine)
    patch = pd.read_csv(patch_csv)
    if patch.empty:
        return len(existing), 0

    combined = pd.concat([existing, patch], ignore_index=True)
    combined = combined.drop_duplicates(subset=["order_id"], keep="last")
    combined.to_sql("orders", engine, if_exists="replace", index=False)
    inserted = len(combined) - len(existing)
    return len(combined), max(inserted, 0)


def main() -> None:
    parser = argparse.ArgumentParser(description="Incremental merge for orders table")
    parser.add_argument("patch_csv", type=Path, help="CSV with new or updated orders")
    args = parser.parse_args()

    cfg = load_config()
    db_path = resolve_path(cfg["warehouse"]["sqlite_path"])
    if not db_path.exists():
        raise FileNotFoundError("warehouse missing; run etl_load.py first")

    total, delta = merge_orders(db_path, args.patch_csv)
    print(f"orders table rows: {total} (delta {delta})")


if __name__ == "__main__":
    main()
