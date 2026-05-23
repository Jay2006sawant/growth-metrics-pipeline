# Looker Studio setup

Goal: a public report link you can put on your resume next to the GitHub repo.

## 1. Refresh exports

```bash
make all
```

Confirm `dashboard/exports/` has the four CSV files.

## 2. Upload data

**Option A — Google Sheets (fastest)**

1. Create a new Google Sheet.
2. For each CSV: **File → Import → Upload** → pick file → **Insert new sheet**.
3. Name sheets: `daily_kpi`, `campaign_roas`, `funnel`, `cohort`.

**Option B — BigQuery**

Follow [bigquery/README.md](../bigquery/README.md), then connect Looker Studio to BigQuery tables.

## 3. Create the report

1. Open [Looker Studio](https://lookerstudio.google.com/).
2. **Create → Report →** add your Sheet or BigQuery source.
3. Suggested layout:
   - **Page 1:** Scorecards for total revenue and orders (from `daily_kpi_by_channel`, sum in chart or pre-aggregate).
   - **Page 2:** Time series of `net_revenue` by `report_date`, filter control on `channel`.
   - **Page 3:** Table from `campaign_roas`: `spend_usd`, `attributed_revenue`, `roas`.
   - **Page 4:** Line chart of `conversion_rate_pct` from `session_conversion_funnel`.
4. Add a text box linking to [business_insights.md](https://github.com/Jay2006sawant/growth-metrics-pipeline/blob/main/docs/business_insights.md) on GitHub.

## 4. Publish

1. **Share → Manage access →** change to **Anyone with the link** can view.
2. Copy the report URL.
3. Paste it in the repo README under **Live demos → Looker Studio** (replace `TBD`).

## 5. Optional check

Open the link in an incognito window to confirm viewers do not need a Google login.
