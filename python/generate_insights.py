"""Build docs/dashboard/summary.json for the static report page."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pandas as pd
from sqlalchemy import create_engine

sys.path.insert(0, str(Path(__file__).resolve().parent))
from config_loader import load_config, resolve_path


def main() -> None:
    cfg = load_config()
    db_path = resolve_path(cfg["warehouse"]["sqlite_path"])
    if not db_path.exists():
        raise FileNotFoundError("Run etl_load.py first")

    engine = create_engine(f"sqlite:///{db_path}")
    daily = pd.read_sql(
        """
        SELECT channel,
               COUNT(DISTINCT order_id) AS orders,
               ROUND(SUM(net_revenue), 2) AS net_revenue
        FROM orders
        GROUP BY channel
        ORDER BY net_revenue DESC
        """,
        engine,
    )
    roas = pd.read_sql(
        """
        WITH o AS (
            SELECT channel, campaign, SUM(net_revenue) AS rev
            FROM orders
            GROUP BY 1, 2
        ),
        s AS (
            SELECT channel, campaign, SUM(spend_usd) AS spend
            FROM campaign_spend
            GROUP BY 1, 2
        )
        SELECT o.channel,
               o.campaign,
               ROUND(o.rev, 2) AS revenue,
               ROUND(s.spend, 2) AS spend_usd,
               ROUND(o.rev / NULLIF(s.spend, 0), 2) AS roas
        FROM o
        JOIN s USING (channel, campaign)
        WHERE s.spend > 500
        ORDER BY roas DESC
        LIMIT 5
        """,
        engine,
    )
    funnel = pd.read_sql(
        """
        SELECT s.channel,
               ROUND(
                   100.0 * COUNT(DISTINCT o.order_id)
                   / NULLIF(COUNT(DISTINCT s.session_id), 0),
                   2
               ) AS conv_pct
        FROM sessions s
        LEFT JOIN orders o
            ON s.session_date = o.order_date AND s.channel = o.channel
        GROUP BY s.channel
        ORDER BY conv_pct DESC
        """,
        engine,
    )
    cohort_path = resolve_path("dashboard/exports/cohort_retention_summary.csv")
    cohort = pd.read_csv(cohort_path) if cohort_path.exists() else pd.DataFrame()

    total = float(pd.read_sql("SELECT SUM(net_revenue) AS t FROM orders", engine).iloc[0, 0])
    aov = float(
        pd.read_sql(
            "SELECT SUM(net_revenue) / COUNT(DISTINCT order_id) AS aov FROM orders",
            engine,
        ).iloc[0, 0]
    )

    payload = {
        "total_net_revenue_usd": round(total, 2),
        "blended_aov_usd": round(aov, 2),
        "by_channel": daily.to_dict(orient="records"),
        "top_roas_campaigns": roas.to_dict(orient="records"),
        "conversion_by_channel": funnel.to_dict(orient="records"),
        "cohort_repeat": cohort.to_dict(orient="records"),
    }

    out_dir = resolve_path("docs/dashboard")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / "summary.json"
    out_file.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(f"Wrote {out_file}")


if __name__ == "__main__":
    main()
