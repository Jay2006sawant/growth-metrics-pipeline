"""Load raw CSVs into SQLite warehouse with indexes and mart views."""

from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd
from sqlalchemy import create_engine, text

sys.path.insert(0, str(Path(__file__).resolve().parent))
from config_loader import load_config, resolve_path

ROOT = Path(__file__).resolve().parents[1]


def load_table(engine, name: str, path: Path) -> int:
    df = pd.read_csv(path)
    df.to_sql(name, engine, if_exists="replace", index=False)
    return len(df)


def apply_views(engine) -> None:
    view_sql = resolve_path("sql/marts/v_dim_channel.sql").read_text(encoding="utf-8")
    with engine.connect() as conn:
        conn.execute(text(view_sql))
        conn.commit()


def main() -> None:
    cfg = load_config()
    raw_dir = resolve_path(cfg["warehouse"]["raw_dir"])
    db_path = resolve_path(cfg["warehouse"]["sqlite_path"])
    db_path.parent.mkdir(parents=True, exist_ok=True)

    engine = create_engine(f"sqlite:///{db_path}")
    counts: dict[str, int] = {}
    for table, filename in cfg["sources"].items():
        if table == "fx_rates":
            continue
        path = raw_dir / filename
        if not path.exists():
            raise FileNotFoundError(f"Missing {path}; run generate_sample_data.py first")
        counts[table] = load_table(engine, table, path)

    fx_name = cfg["sources"].get("fx_rates")
    if fx_name:
        fx_path = raw_dir / fx_name
        if fx_path.exists():
            counts["fx_rates"] = load_table(engine, "fx_rates", fx_path)

    indexes = [
        "CREATE INDEX IF NOT EXISTS idx_orders_date ON orders(order_date)",
        "CREATE INDEX IF NOT EXISTS idx_orders_customer ON orders(customer_id)",
        "CREATE INDEX IF NOT EXISTS idx_sessions_date ON sessions(session_date)",
        "CREATE INDEX IF NOT EXISTS idx_spend_date ON campaign_spend(spend_date)",
    ]
    with engine.connect() as conn:
        for stmt in indexes:
            conn.execute(text(stmt))
        conn.commit()

    apply_views(engine)
    print(f"Loaded warehouse at {db_path}: {counts}")


if __name__ == "__main__":
    main()
