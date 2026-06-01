# BigQuery console guide

Prerequisites: tables created from [ddl_partitioned.sql](../../bigquery/ddl_partitioned.sql) and CSV loads via `bq load`.

## Dataset

```bash
export PROJECT=your-gcp-project
bq mk --dataset --location=US ${PROJECT}:growth_metrics
```

## Load orders

```bash
bq load --autodetect --source_format=CSV \
  ${PROJECT}:growth_metrics.orders data/raw/orders.csv
```

## KPI query

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

Local equivalent:

```bash
sqlite3 warehouse/analytics.db < sql/03_kpi_aggregations.sql | head
```

Scheduled exports to GCS can feed Looker Studio on the BigQuery connector.
