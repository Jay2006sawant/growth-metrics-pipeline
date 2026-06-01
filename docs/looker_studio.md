# Looker Studio report spec

Data source: CSV exports in `dashboard/exports/` (refreshed via `make all`). Connector can be Google Sheets (imported tabs) or BigQuery tables loaded from the same files.

## Source tables

| Export file | Grain | Key fields |
|-------------|-------|------------|
| `daily_kpi_by_channel.csv` | day × channel | `report_date`, `channel`, `orders`, `unique_customers`, `net_revenue`, `aov` |
| `campaign_roas.csv` | day × channel × campaign | `spend_usd`, `attributed_revenue`, `roas` |
| `session_conversion_funnel.csv` | day × channel | `sessions`, `orders`, `conversion_rate_pct` |
| `cohort_retention_summary.csv` | signup cohort month | `cohort_size`, `repeat_customers`, `repeat_rate_pct` |

## Suggested pages

**Executive** — scorecards from `daily_kpi_by_channel`: sum of `net_revenue`, sum of `orders`, blended `aov`.

**Channels** — time series of `net_revenue` by `report_date`; filter control on `channel`.

**Paid media** — table from `campaign_roas` sorted by `roas` descending.

**Funnel** — line chart of `conversion_rate_pct` over `report_date`, broken down by `channel`.

Metric definitions: [metrics_dictionary.md](metrics_dictionary.md). Attribution rules: [attribution.md](attribution.md).
