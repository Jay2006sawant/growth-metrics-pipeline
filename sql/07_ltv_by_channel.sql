-- Trailing 90-day revenue per customer, rolled up to first-touch channel on first order

WITH ranked AS (
    SELECT
        customer_id,
        channel,
        order_date,
        net_revenue,
        ROW_NUMBER() OVER (
            PARTITION BY customer_id
            ORDER BY order_date, order_id
        ) AS order_rank
    FROM orders
),
first_touch AS (
    SELECT customer_id, channel AS first_channel
    FROM ranked
    WHERE order_rank = 1
),
windowed AS (
    SELECT
        o.customer_id,
        ft.first_channel,
        SUM(o.net_revenue) AS ltv_90d
    FROM orders o
    JOIN first_touch ft ON o.customer_id = ft.customer_id
    JOIN ranked r ON o.customer_id = r.customer_id AND r.order_rank = 1
    WHERE o.order_date BETWEEN r.order_date AND date(r.order_date, '+90 day')
    GROUP BY o.customer_id, ft.first_channel
)
SELECT
    first_channel,
    COUNT(*) AS customers,
    ROUND(AVG(ltv_90d), 2) AS avg_ltv_90d,
    ROUND(SUM(ltv_90d), 2) AS total_ltv_90d
FROM windowed
GROUP BY first_channel
ORDER BY total_ltv_90d DESC;
