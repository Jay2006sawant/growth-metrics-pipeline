-- Week-over-week revenue and rolling 7-day AOV by channel (window functions)
WITH daily AS (
    SELECT
        order_date,
        channel,
        SUM(net_revenue) AS net_revenue,
        COUNT(DISTINCT order_id) AS orders
    FROM orders
    GROUP BY order_date, channel
)
SELECT
    order_date,
    channel,
    net_revenue,
    orders,
    ROUND(net_revenue / NULLIF(orders, 0), 2) AS aov,
    LAG(net_revenue, 7) OVER (PARTITION BY channel ORDER BY order_date) AS revenue_7d_ago,
    ROUND(
        100.0 * (net_revenue - LAG(net_revenue, 7) OVER (PARTITION BY channel ORDER BY order_date))
        / NULLIF(LAG(net_revenue, 7) OVER (PARTITION BY channel ORDER BY order_date), 0),
        2
    ) AS wow_revenue_pct,
    ROUND(
        AVG(net_revenue) OVER (
            PARTITION BY channel
            ORDER BY order_date
            ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
        ),
        2
    ) AS rolling_7d_avg_revenue
FROM daily
ORDER BY channel, order_date;
