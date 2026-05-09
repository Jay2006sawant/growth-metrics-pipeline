-- Monthly signup cohorts with order activity in months 0..3 (SQLite date math via strftime)

WITH first_order AS (
    SELECT
        customer_id,
        MIN(order_date) AS first_order_date
    FROM orders
    GROUP BY customer_id
),
cohort AS (
    SELECT
        c.customer_id,
        strftime('%Y-%m', c.signup_date) AS cohort_month,
        fo.first_order_date
    FROM customers c
    LEFT JOIN first_order fo ON c.customer_id = fo.customer_id
),
activity AS (
    SELECT
        co.cohort_month,
        co.customer_id,
        CAST(
            (
                strftime('%Y', o.order_date) - strftime('%Y', co.cohort_month || '-01')
            ) * 12
            + (
                strftime('%m', o.order_date) - strftime('%m', co.cohort_month || '-01')
            ) AS INTEGER
        ) AS month_index
    FROM cohort co
    JOIN orders o ON co.customer_id = o.customer_id
    WHERE month_index BETWEEN 0 AND 3
)
SELECT
    cohort_month,
    month_index,
    COUNT(DISTINCT customer_id) AS active_customers
FROM activity
GROUP BY cohort_month, month_index
ORDER BY cohort_month, month_index;
