# Google Sheets reporting

Fast path when Looker Studio is not ready yet.

## Import

1. Create a Sheet named `growth-metrics-sample`.
2. Import each file from `dashboard/exports/` as a new tab:
   - `daily_kpi_by_channel.csv` → tab `daily_kpi`
   - `campaign_roas.csv` → tab `roas`
   - `session_conversion_funnel.csv` → tab `funnel`
   - `cohort_retention_summary.csv` → tab `cohort`

## Charts

- **daily_kpi:** Insert chart → Column chart → dimension `channel`, metric `net_revenue`.
- **roas:** Table chart → dimensions `channel`, `campaign`, metrics `spend_usd`, `attributed_revenue`, `roas`.
- **funnel:** Line chart → `report_date` vs `conversion_rate_pct`, filter `channel`.

## Publish

**File → Share → Publish to web** (entire workbook or per sheet). Add the published URL to the root README under **Live demos → Google Sheets**.
