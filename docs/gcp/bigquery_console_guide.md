# BigQuery console walkthrough

Use this after you load tables with `bigquery/ddl_partitioned.sql` and `bq load`.

## 1. Create dataset

```bash
export PROJECT=your-gcp-project
bq mk --dataset --location=US ${PROJECT}:growth_metrics
```

## 2. Load orders (example)

```bash
bq load --autodetect --source_format=CSV \
  ${PROJECT}:growth_metrics.orders data/raw/orders.csv
```

## 3. KPI query (paste in Cloud Console → BigQuery → Query)

```sql
SELECT
  order_date,
  channel,
  COUNT(DISTINCT order_id) AS orders,
  ROUND(SUM(net_revenue), 2) AS net_revenue
FROM `your-gcp-project.growth_metrics.orders`
GROUP BY 1, 2
ORDER BY net_revenue DESC
LIMIT 20;
```

## Expected shape (local SQLite reference)

Run the same logic locally:

```bash
sqlite3 warehouse/analytics.db < sql/03_kpi_aggregations.sql | head
```

Save a **screenshot** of your BigQuery results grid as `docs/gcp/bigquery_kpi_screenshot.png` and link it from the README when you have a GCP project. Do not commit fake screenshots.

## Scheduled refresh

For production, schedule a query export to GCS and point Looker Studio at BigQuery instead of Sheets.
