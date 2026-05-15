"""Fetch daily USD base FX rates (JSON API) for multi-currency reporting enrichment."""

from __future__ import annotations

import json
from datetime import date
from pathlib import Path

import pandas as pd
import requests

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
RAW.mkdir(parents=True, exist_ok=True)

# Public demo API — no key required for basic usage
API_URL = "https://open.er-api.com/v6/latest/USD"


def main() -> None:
    resp = requests.get(API_URL, timeout=30)
    resp.raise_for_status()
    payload = resp.json()
    if payload.get("result") != "success":
        raise RuntimeError(f"Unexpected API response: {json.dumps(payload)[:200]}")

    rates = payload["rates"]
    rows = [
        {
            "rate_date": date.today().isoformat(),
            "base_currency": "USD",
            "quote_currency": quote,
            "exchange_rate": rate,
            "source": "open.er-api.com",
        }
        for quote, rate in rates.items()
        if quote in {"INR", "GBP", "EUR", "AED", "SGD", "USD"}
    ]
    out = RAW / "fx_rates.json"
    out.write_text(json.dumps({"fetched": payload.get("time_last_update_utc"), "rates": rows}, indent=2))
    pd.DataFrame(rows).to_csv(RAW / "fx_rates.csv", index=False)
    print(f"Saved FX snapshot ({len(rows)} quotes) to {RAW}")


if __name__ == "__main__":
    main()
