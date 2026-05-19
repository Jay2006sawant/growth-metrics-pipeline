SELECT
    s.session_date AS report_date,
    s.channel,
    COUNT(DISTINCT s.session_id) AS sessions,
    COUNT(DISTINCT o.order_id) AS orders,
    ROUND(100.0 * COUNT(DISTINCT o.order_id) / NULLIF(COUNT(DISTINCT s.session_id), 0), 2) AS conversion_rate_pct
FROM sessions s
LEFT JOIN orders o
    ON s.session_date = o.order_date AND s.channel = o.channel
GROUP BY 1, 2
ORDER BY 1, 2;
