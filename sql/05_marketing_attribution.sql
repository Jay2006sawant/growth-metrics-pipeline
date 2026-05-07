-- Campaign spend vs attributed revenue and ROAS
WITH daily_orders AS (
    SELECT
        order_date,
        channel,
        campaign,
        SUM(net_revenue) AS attributed_revenue,
        COUNT(DISTINCT order_id) AS orders
    FROM orders
    GROUP BY 1, 2, 3
),
daily_spend AS (
    SELECT
        spend_date,
        channel,
        campaign,
        SUM(spend_usd) AS spend_usd,
        SUM(clicks) AS clicks,
        SUM(impressions) AS impressions
    FROM campaign_spend
    GROUP BY 1, 2, 3
)
SELECT
    s.spend_date AS report_date,
    s.channel,
    s.campaign,
    s.spend_usd,
    s.clicks,
    s.impressions,
    COALESCE(o.attributed_revenue, 0) AS attributed_revenue,
    COALESCE(o.orders, 0) AS orders,
    ROUND(COALESCE(o.attributed_revenue, 0) / NULLIF(s.spend_usd, 0), 2) AS roas,
    ROUND(s.spend_usd / NULLIF(o.orders, 0), 2) AS cost_per_order
FROM daily_spend s
LEFT JOIN daily_orders o
    ON s.spend_date = o.order_date
   AND s.channel = o.channel
   AND s.campaign = o.campaign
ORDER BY report_date, channel, campaign;
