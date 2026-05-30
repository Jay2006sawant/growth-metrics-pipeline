# Metrics and decisions (one page)

**Project:** Growth Metrics Pipeline · **Author:** Jay Sawant  
**Data:** synthetic multi-channel sample (120 days) · **Warehouse:** SQLite / export CSVs

## Three business questions

### 1. Which channels drive revenue and order volume?

**SQL / export:** `sql/03_kpi_aggregations.sql`, `sql/exports/daily_kpi_by_channel.sql`  
**Insight:** Organic and paid search contribute the largest share of net revenue in the sample; affiliate is smallest but still tracked for completeness. Use this slice to sanity-check mix before changing budget.

### 2. Which campaigns return spend efficiently?

**SQL / export:** `sql/05_marketing_attribution.sql`, `sql/exports/campaign_roas.sql`  
**Insight:** `retargeting_search` on paid search shows the strongest blended ROAS among campaigns with meaningful spend (about **1.71** in the current snapshot). Prospecting campaigns should be compared on a cohort basis before cutting spend.

### 3. Where does the funnel leak?

**SQL / export:** `sql/exports/session_conversion_funnel.sql`  
**Insight:** Same-day conversion varies by channel; email and affiliate sessions convert at higher rates than broad paid social in this generator. Pair with landing-page dimension in a client engagement before reallocation.

## Quality bar before sharing dashboards

Run `python/run_quality_checks.py` and confirm zero duplicate orders, zero negative revenue, zero orphan customers.

## Actions a growth lead might take

1. Hold paid social scaling until ROAS matches retargeting search benchmarks.  
2. Keep organic landing paths healthy given revenue share.  
3. Document attribution (see `docs/attribution.md`) before client-facing ROAS slides.

Full narrative: [docs/business_insights.md](../docs/business_insights.md).
