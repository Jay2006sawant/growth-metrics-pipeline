# Growth Metrics Pipeline

End-to-end analytics engineering sample: bronze CSV feeds, silver SQLite warehouse, gold KPI exports, and BI handoff for Looker Studio, Sheets, or BigQuery.

Built by [Jay Sawant](https://github.com/Jay2006sawant) to show the full loop agencies run for growth clients (CRO, paid media, executive reporting).

## Live demos

| Demo | Link |
|------|------|
| Chart preview (GitHub Pages) | https://jay2006sawant.github.io/growth-metrics-pipeline/ |
| Metrics + decisions (one page) | [reports/METRICS_AND_DECISIONS.md](reports/METRICS_AND_DECISIONS.md) |
| Business narrative | [docs/business_insights.md](docs/business_insights.md) |
| Looker Studio | *Add your published report URL here after [docs/looker_studio_setup.md](docs/looker_studio_setup.md)* |
| Google Sheets | *Add published sheet URL after [sheets/README.md](sheets/README.md)* |
| BigQuery | [docs/gcp/bigquery_console_guide.md](docs/gcp/bigquery_console_guide.md) (+ optional screenshot in `docs/gcp/`) |

Enable GitHub Pages: **Settings → Pages → GitHub Actions**. See [docs/PORTFOLIO.md](docs/PORTFOLIO.md).

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

Runbook: [docs/pipeline_runbook.md](docs/pipeline_runbook.md).

## Layout

```
config/           pipeline manifest (paths, export query map)
data/raw/         bronze CSV feeds
sql/              analytics, marts, gold, export queries
python/           ingest, validate, load, exports, insights JSON
warehouse/        local SQLite (not committed)
dashboard/exports gold tables for BI
docs/             metrics, GCP, portfolio, static dashboard
reports/          one-page metrics + decisions
sheets/           Google Sheets publishing steps
bigquery/         partitioned DDL + samples
tests/            pytest
```

## License

MIT · Jay Sawant
