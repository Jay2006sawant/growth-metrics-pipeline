"""Generate synthetic multi-channel commerce + marketing data for analytics demos."""

from __future__ import annotations

import random
from datetime import date, timedelta
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
RAW.mkdir(parents=True, exist_ok=True)

CHANNELS = ["organic", "paid_search", "paid_social", "email", "affiliate"]
CAMPAIGNS = {
    "paid_search": ["brand_search_q4", "generic_shoes", "retargeting_search"],
    "paid_social": ["meta_prospecting", "meta_retarget", "tiktok_awareness"],
    "email": ["newsletter_weekly", "cart_abandon", "winback"],
    "affiliate": ["partner_blog", "coupon_site"],
    "organic": ["organic_direct"],
}


def daterange(start: date, days: int) -> list[date]:
    return [start + timedelta(days=i) for i in range(days)]


def main() -> None:
    random.seed(42)
    start = date(2025, 6, 1)
    days = 120
    dates = daterange(start, days)

    customers = []
    for i in range(1, 8001):
        customers.append(
            {
                "customer_id": i,
                "signup_date": start + timedelta(days=random.randint(0, days - 1)),
                "country": random.choice(["IN", "US", "UK", "AE", "SG"]),
            }
        )
    pd.DataFrame(customers).to_csv(RAW / "customers.csv", index=False)

    sessions = []
    sid = 1
    for d in dates:
        for _ in range(random.randint(400, 900)):
            ch = random.choices(CHANNELS, weights=[30, 25, 20, 15, 10])[0]
            camp = random.choice(CAMPAIGNS[ch])
            sessions.append(
                {
                    "session_id": sid,
                    "session_date": d.isoformat(),
                    "channel": ch,
                    "campaign": camp,
                    "landing_page": random.choice(["/home", "/product", "/sale", "/blog"]),
                    "device": random.choice(["mobile", "desktop", "tablet"]),
                }
            )
            sid += 1
    pd.DataFrame(sessions).to_csv(RAW / "sessions.csv", index=False)

    orders = []
    oid = 1
    for d in dates:
        n = random.randint(35, 110)
        for _ in range(n):
            cust = random.randint(1, 8000)
            ch = random.choices(CHANNELS, weights=[28, 26, 22, 14, 10])[0]
            gross = round(random.uniform(15, 280) * random.uniform(0.9, 1.1), 2)
            discount = round(gross * random.choice([0, 0, 0, 0.05, 0.1, 0.15]), 2)
            orders.append(
                {
                    "order_id": oid,
                    "customer_id": cust,
                    "order_date": d.isoformat(),
                    "channel": ch,
                    "campaign": random.choice(CAMPAIGNS[ch]),
                    "gross_amount": gross,
                    "discount_amount": discount,
                    "net_revenue": round(gross - discount, 2),
                    "currency": "USD",
                }
            )
            oid += 1
    pd.DataFrame(orders).to_csv(RAW / "orders.csv", index=False)

    spend_rows = []
    for d in dates:
        for ch in ("paid_search", "paid_social", "affiliate"):
            for camp in CAMPAIGNS[ch]:
                spend_rows.append(
                    {
                        "spend_date": d.isoformat(),
                        "channel": ch,
                        "campaign": camp,
                        "impressions": random.randint(5000, 80000),
                        "clicks": random.randint(80, 3500),
                        "spend_usd": round(random.uniform(40, 1200), 2),
                    }
                )
    pd.DataFrame(spend_rows).to_csv(RAW / "campaign_spend.csv", index=False)

    print(f"Wrote sample data to {RAW}")


if __name__ == "__main__":
    main()
