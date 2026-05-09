-- Gold grain: one row per report_date x channel with core KPIs

SELECT
    o.order_date AS report_date,
    o.channel,
    d.channel_group,
    COUNT(DISTINCT o.order_id) AS orders,
    COUNT(DISTINCT o.customer_id) AS buyers,
    ROUND(SUM(o.net_revenue), 2) AS net_revenue,
    ROUND(SUM(o.net_revenue) / NULLIF(COUNT(DISTINCT o.order_id), 0), 2) AS aov
FROM orders o
LEFT JOIN v_dim_channel d ON o.channel = d.channel
GROUP BY o.order_date, o.channel, d.channel_group
ORDER BY o.order_date, o.channel;
