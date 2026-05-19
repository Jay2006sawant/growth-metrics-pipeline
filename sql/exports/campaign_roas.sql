WITH order_rev AS (
    SELECT order_date, channel, campaign, SUM(net_revenue) AS revenue
    FROM orders
    GROUP BY 1, 2, 3
),
spend AS (
    SELECT spend_date, channel, campaign, SUM(spend_usd) AS spend_usd
    FROM campaign_spend
    GROUP BY 1, 2, 3
)
SELECT
    COALESCE(s.spend_date, o.order_date) AS report_date,
    COALESCE(s.channel, o.channel) AS channel,
    COALESCE(s.campaign, o.campaign) AS campaign,
    ROUND(COALESCE(s.spend_usd, 0), 2) AS spend_usd,
    ROUND(COALESCE(o.revenue, 0), 2) AS attributed_revenue,
    ROUND(COALESCE(o.revenue, 0) / NULLIF(s.spend_usd, 0), 2) AS roas
FROM spend s
LEFT JOIN order_rev o
    ON s.spend_date = o.order_date AND s.channel = o.channel AND s.campaign = o.campaign
ORDER BY 1, 2, 3;
