WITH first_order AS (
    SELECT customer_id, MIN(order_date) AS first_order_date
    FROM orders
    GROUP BY customer_id
),
cohort AS (
    SELECT
        c.customer_id,
        strftime('%Y-%m', c.signup_date) AS cohort_month
    FROM customers c
),
repeat_buyers AS (
    SELECT
        co.cohort_month,
        COUNT(DISTINCT co.customer_id) AS cohort_size,
        COUNT(DISTINCT CASE WHEN o.order_date > fo.first_order_date THEN co.customer_id END) AS repeat_customers
    FROM cohort co
    JOIN first_order fo ON co.customer_id = fo.customer_id
    LEFT JOIN orders o ON co.customer_id = o.customer_id
    GROUP BY co.cohort_month
)
SELECT
    cohort_month,
    cohort_size,
    repeat_customers,
    ROUND(100.0 * repeat_customers / NULLIF(cohort_size, 0), 2) AS repeat_rate_pct
FROM repeat_buyers
ORDER BY cohort_month;
