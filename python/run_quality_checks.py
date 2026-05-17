"""Run lightweight QA queries against the SQLite warehouse."""

from __future__ import annotations

import sys
from pathlib import Path

from sqlalchemy import create_engine, text

ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / "warehouse" / "analytics.db"

CHECKS = [
    (
        "duplicate_order_id",
        "SELECT COUNT(*) FROM (SELECT order_id FROM orders GROUP BY order_id HAVING COUNT(*) > 1)",
    ),
    (
        "negative_net_revenue",
        "SELECT COUNT(*) FROM orders WHERE net_revenue < 0",
    ),
    (
        "orphan_orders",
        """
        SELECT COUNT(*) FROM orders o
        LEFT JOIN customers c ON o.customer_id = c.customer_id
        WHERE c.customer_id IS NULL
        """,
    ),
]


def main() -> None:
    if not DB.exists():
        print("warehouse missing; run etl_load.py first", file=sys.stderr)
        sys.exit(1)
    engine = create_engine(f"sqlite:///{DB}")
    failed = False
    with engine.connect() as conn:
        for name, sql in CHECKS:
            count = conn.execute(text(sql)).scalar()
            status = "ok" if count == 0 else "FAIL"
            print(f"{name}: {count} ({status})")
            if count != 0:
                failed = True
    if failed:
        sys.exit(1)


if __name__ == "__main__":
    main()
