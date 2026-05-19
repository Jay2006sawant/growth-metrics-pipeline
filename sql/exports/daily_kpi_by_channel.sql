SELECT
    order_date AS report_date,
    channel,
    COUNT(DISTINCT order_id) AS orders,
    COUNT(DISTINCT customer_id) AS unique_customers,
    ROUND(SUM(net_revenue), 2) AS net_revenue,
    ROUND(SUM(net_revenue) / NULLIF(COUNT(DISTINCT order_id), 0), 2) AS aov
FROM orders
GROUP BY 1, 2
ORDER BY 1, 2;
