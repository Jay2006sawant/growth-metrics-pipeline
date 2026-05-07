-- Executive KPIs: revenue, orders, AOV by day and channel
SELECT
    o.order_date,
    o.channel,
    COUNT(DISTINCT o.order_id) AS orders,
    COUNT(DISTINCT o.customer_id) AS unique_customers,
    ROUND(SUM(o.net_revenue), 2) AS net_revenue,
    ROUND(SUM(o.net_revenue) / NULLIF(COUNT(DISTINCT o.order_id), 0), 2) AS average_order_value
FROM orders o
GROUP BY o.order_date, o.channel
ORDER BY o.order_date, o.channel;
