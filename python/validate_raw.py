"""Validate raw CSV feeds before warehouse load."""

from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd
from pydantic import ValidationError

sys.path.insert(0, str(Path(__file__).resolve().parent))
from config_loader import load_config, resolve_path
from schemas import CustomerRow, OrderRow, SessionRow, SpendRow

ROOT = Path(__file__).resolve().parents[1]


def validate_frame(model, df: pd.DataFrame, label: str, sample: int = 500) -> None:
    subset = df.head(sample) if len(df) > sample else df
    for idx, row in subset.iterrows():
        try:
            model.model_validate(row.to_dict())
        except ValidationError as exc:
            raise ValueError(f"{label} row {idx}: {exc}") from exc


def check_file(path: Path, cols: list[str]) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(path)
    df = pd.read_csv(path)
    missing = [c for c in cols if c not in df.columns]
    if missing:
        raise ValueError(f"{path.name}: missing columns {missing}")
    if df.empty:
        raise ValueError(f"{path.name}: zero rows")
    return df


def main() -> None:
    cfg = load_config()
    raw_dir = resolve_path(cfg["warehouse"]["raw_dir"])

    customers = check_file(raw_dir / cfg["sources"]["customers"], ["customer_id", "signup_date", "country"])
    sessions = check_file(
        raw_dir / cfg["sources"]["sessions"],
        ["session_id", "session_date", "channel", "campaign"],
    )
    orders = check_file(
        raw_dir / cfg["sources"]["orders"],
        ["order_id", "customer_id", "order_date", "channel", "campaign", "net_revenue"],
    )
    spend = check_file(
        raw_dir / cfg["sources"]["campaign_spend"],
        ["spend_date", "channel", "campaign", "spend_usd"],
    )

    validate_frame(CustomerRow, customers, "customers")
    validate_frame(SessionRow, sessions, "sessions")
    validate_frame(OrderRow, orders, "orders")
    validate_frame(SpendRow, spend, "campaign_spend")

    dupes = orders["order_id"].duplicated().sum()
    if dupes:
        raise ValueError(f"orders: {dupes} duplicate order_id values")

    print(
        f"raw validation passed ({len(customers)} customers, {len(sessions)} sessions, "
        f"{len(orders)} orders, {len(spend)} spend rows)"
    )


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError) as exc:
        print(exc, file=sys.stderr)
        sys.exit(1)
