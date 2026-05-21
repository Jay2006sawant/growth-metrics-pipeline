# Metrics dictionary

| Metric | Definition | Grain |
|--------|------------|-------|
| Net revenue | `gross_amount - discount_amount` on each order, summed | day x channel |
| AOV | Net revenue divided by distinct order count | day x channel |
| ROAS | Attributed revenue divided by ad spend | day x channel x campaign |
| Conversion rate | Distinct orders divided by distinct sessions | day x channel (same calendar day join) |
| WoW revenue % | Change vs revenue seven days earlier | day x channel |
| Repeat rate % | Customers with a second order after first purchase, by signup cohort month | cohort month |
| Avg LTV 90d | Mean net revenue in the 90 days after a customer first order, grouped by first-touch channel | channel |

## Sources

- `orders`, `sessions`, `customers`, `campaign_spend` from `python/generate_sample_data.py` unless you replace the CSVs
- `fx_rates` optional via `python/ingest_fx_api.py`

## Reporting notes

Paid performance uses last-touch channel and campaign on the order row. See [attribution.md](attribution.md).

Run `python/run_quality_checks.py` before refreshing dashboards. `sql/02_data_quality_checks.sql` mirrors the same checks for Postgres or BigQuery clients.
