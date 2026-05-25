# BigQuery

Use this when you want the same metrics on GCP instead of SQLite.

1. Create dataset `growth_metrics` in your project.
2. Apply `ddl_partitioned.sql` for partitioned, clustered tables.
3. Load CSVs from `data/raw/` with `bq load` or a scheduled transfer.
4. Port queries from `sql/exports/` and `sample_kpi_queries.sql` (replace table names with `` `project.growth_metrics.orders` ``).

Example:

```bash
bq mk --dataset PROJECT:growth_metrics
bq query --use_legacy_sql=false < bigquery/ddl_partitioned.sql
bq load --autodetect --source_format=CSV PROJECT:growth_metrics.orders data/raw/orders.csv
```

For Looker Studio, point the connector at BigQuery rather than uploaded CSVs once tables are in place.
