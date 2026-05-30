# Business insights (sample warehouse)

Synthetic data, real pipeline. Numbers below come from `python/generate_insights.py` on the committed CSV feeds.

## Questions we asked

1. **Where is revenue coming from?**  
   Channel-level net revenue and order volume (`sql/exports/daily_kpi_by_channel.sql`).

2. **Which paid campaigns earn back spend?**  
   ROAS by campaign (`sql/05_marketing_attribution.sql`, export `campaign_roas.csv`).

3. **Which channels convert sessions to orders on the same day?**  
   Session-to-order rate by channel (`session_conversion_funnel.csv`).

4. **Do signup cohorts come back to buy again?**  
   Repeat rate by cohort month (`cohort_retention_summary.csv`).

## Snapshot (current sample)

| Metric | Value |
|--------|------:|
| Total net revenue (USD) | 1,249,011.94 |
| Blended AOV (USD) | 139.87 |

**Revenue by channel (top to bottom):** organic (~349k), paid_search (~323k), paid_social (~282k), email (~176k), affiliate (~119k). Organic and paid search drive the largest share; affiliate is smallest but still material.

**ROAS (campaigns with meaningful spend):** `retargeting_search` on paid_search leads at roughly **1.71** ROAS on blended sample totals. Use this to prioritize budget reviews, not as a live client number.

**Conversion rate (same-day, session join):** email and affiliate tend to show higher session-to-order rates than broad paid social in this generator. That pattern is useful for funnel debugging, not for claiming channel quality without holdout tests.

**Cohort repeat:** repeat rates by signup month are in `cohort_retention_summary.csv` and the [dashboard report](dashboard/index.html).

## Decisions a stakeholder might take

- Shift paid social creative tests before scaling spend if ROAS trails retargeting search.  
- Keep organic landing paths healthy since they contribute the largest revenue slice in the sample.  
- Run `make quality` before any BI refresh so orphan orders and duplicate keys do not pollute dashboards.

## Definitions

See [metrics_dictionary.md](metrics_dictionary.md) and [attribution.md](attribution.md).
