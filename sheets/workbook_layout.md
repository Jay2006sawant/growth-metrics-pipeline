# Workbook layout (Google Sheets)

Each export CSV maps to one tab. Import from `dashboard/exports/` after `make all`.

| Tab name | Source file | Primary use |
|----------|-------------|-------------|
| `daily_kpi` | `daily_kpi_by_channel.csv` | Column chart: `channel` vs `net_revenue` |
| `roas` | `campaign_roas.csv` | Table: `channel`, `campaign`, `spend_usd`, `attributed_revenue`, `roas` |
| `funnel` | `session_conversion_funnel.csv` | Line chart: `report_date` vs `conversion_rate_pct` |
| `cohort` | `cohort_retention_summary.csv` | Table: `cohort_month`, `repeat_rate_pct` |

Column definitions match [docs/looker_studio.md](../docs/looker_studio.md).
