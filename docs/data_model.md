# Data model

Star-style layout for reporting. All keys are integers or short strings so the SQLite warehouse stays easy to inspect.

## Entity diagram (logical)

```
customers (customer_id)
    ^
    | 1:N
orders (order_id, customer_id, order_date, channel, campaign, net_revenue, ...)

sessions (session_id, session_date, channel, campaign, ...)

campaign_spend (spend_date, channel, campaign, spend_usd, impressions, clicks)
    PK: (spend_date, channel, campaign)

fx_rates (rate_date, base_currency, quote_currency, exchange_rate)
```

## Column notes

**orders**

- `net_revenue` is the field aggregated in KPI queries.
- `currency` is `USD` in the generator; FX table is there if you extend to multi-currency reporting later.

**sessions**

- One row per site visit. Conversion logic joins to orders on `session_date = order_date` and matching `channel`.

**campaign_spend**

- Only paid channels appear (`paid_search`, `paid_social`, `affiliate`). Organic and email have no spend rows in the sample.

DDL for Postgres-compatible tools: `sql/01_schema_postgres.sql`.
