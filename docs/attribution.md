# Attribution assumptions

This sample warehouse uses last-touch channel and campaign stored on each `orders` row. Sessions are joined on matching `order_date` and `channel` when we compute same-day conversion rates. That is a simplification for teaching funnels, not a full multi-touch model.

Paid spend ties to revenue on `(spend_date, channel, campaign)` equal to `(order_date, channel, campaign)`. Organic and email orders still carry campaign labels from the generator; they do not have matching rows in `campaign_spend`.

ROAS is `attributed_revenue / spend_usd`. Rows with zero spend return null ROAS in SQL via `NULLIF`.

For client work I would document the exact touch rules in the metrics dictionary and keep QA queries that flag orders with missing spend when marketing expects spend to exist.
