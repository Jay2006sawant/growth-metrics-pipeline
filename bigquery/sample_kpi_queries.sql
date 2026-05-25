-- BigQuery: daily KPI by channel (adjust table names to your dataset)
SELECT
  order_date,
  channel,
  COUNT(DISTINCT order_id) AS orders,
  ROUND(SUM(net_revenue), 2) AS net_revenue,
  ROUND(SUM(net_revenue) / NULLIF(COUNT(DISTINCT order_id), 0), 2) AS aov
FROM `PROJECT.growth_metrics.orders`
GROUP BY 1, 2
ORDER BY 1, 2;
