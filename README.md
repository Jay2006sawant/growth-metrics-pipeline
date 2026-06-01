# Growth Metrics Pipeline

Multi-channel commerce and marketing analytics: bronze CSV feeds, SQLite warehouse, SQL KPI layer, and CSV exports for Looker Studio, Google Sheets, or BigQuery.

## Outputs

| Output | Location |
|--------|----------|
| Interactive chart preview | https://jay2006sawant.github.io/growth-metrics-pipeline/ |
| Metrics and decisions summary | [reports/METRICS_AND_DECISIONS.md](reports/METRICS_AND_DECISIONS.md) |
| Narrative insights | [docs/business_insights.md](docs/business_insights.md) |
| Looker Studio field map | [docs/looker_studio.md](docs/looker_studio.md) |
| Sheets tab layout | [sheets/workbook_layout.md](sheets/workbook_layout.md) |
| BigQuery DDL and queries | [bigquery/](bigquery/) · [docs/gcp/bigquery_console_guide.md](docs/gcp/bigquery_console_guide.md) |

Gold CSVs live in `dashboard/exports/` after `make all`.

## What the SQL answers

| Question | Where |
|----------|--------|
| Revenue, orders, AOV by channel/day | `sql/03_kpi_aggregations.sql`, `sql/exports/daily_kpi_by_channel.sql` |
| WoW and rolling revenue | `sql/04_window_functions_cohort.sql` |
| ROAS and spend efficiency | `sql/05_marketing_attribution.sql`, `sql/exports/campaign_roas.sql` |
| Cohort retention / repeat rate | `sql/06_cohort_retention.sql`, `cohort_retention_summary` export |
| 90-day LTV by first-touch channel | `sql/07_ltv_by_channel.sql` |
| Gold performance mart | `sql/gold/daily_performance.sql` |
| QA before BI refresh | `sql/02_data_quality_checks.sql`, `python/run_quality_checks.py` |

Definitions: [docs/metrics_dictionary.md](docs/metrics_dictionary.md). Attribution: [docs/attribution.md](docs/attribution.md). Layers: [analytics/medallion.md](analytics/medallion.md).

## Run locally

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r python/requirements.txt
make all
make quality
pytest tests/ -q
```

Runbook: [docs/pipeline_runbook.md](docs/pipeline_runbook.md). Static site deploy: [docs/deploy.md](docs/deploy.md).

## Layout

```
config/           pipeline manifest (paths, export query map)
data/raw/         bronze CSV feeds
sql/              analytics, marts, gold, export queries
python/           ingest, validate, load, exports, insights JSON
warehouse/        local SQLite (not committed)
dashboard/exports gold tables for BI
docs/             metrics, GCP, static dashboard
reports/          metrics + decisions summary
sheets/           workbook layout notes
bigquery/         partitioned DDL + samples
tests/            pytest
```

## License

MIT · Jay Sawant
