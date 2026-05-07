-- Data quality checks before publishing dashboards

-- Duplicate primary keys
SELECT 'orders_duplicate_order_id' AS check_name, COUNT(*) AS failures
FROM (
    SELECT order_id FROM orders GROUP BY order_id HAVING COUNT(*) > 1
) d;

-- Future-dated orders (should be zero on clean data)
SELECT 'orders_future_dates' AS check_name, COUNT(*) AS failures
FROM orders
WHERE order_date > CURRENT_DATE;

-- Negative revenue
SELECT 'orders_negative_net_revenue' AS check_name, COUNT(*) AS failures
FROM orders
WHERE net_revenue < 0;

-- Orphan orders (no matching customer)
SELECT 'orders_orphan_customer' AS check_name, COUNT(*) AS failures
FROM orders o
LEFT JOIN customers c ON o.customer_id = c.customer_id
WHERE c.customer_id IS NULL;

-- Spend without channel/campaign
SELECT 'spend_null_dimensions' AS check_name, COUNT(*) AS failures
FROM campaign_spend
WHERE channel IS NULL OR campaign IS NULL OR spend_usd IS NULL;
