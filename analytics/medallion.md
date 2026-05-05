# Medallion layout

## Bronze (`data/raw/`)

Source files as landed: orders, sessions, customers, campaign_spend, optional fx_rates. No business rules beyond generator constraints.

## Silver (`warehouse/*.db` tables)

Typed load via `etl_load.py`. Indexes on dates. `v_dim_channel` view for consistent channel groupings.

## Gold (`sql/gold/`, `dashboard/exports/`)

Aggregated KPI tables for BI tools. Built by `export_dashboard.py` reading manifest queries in `config/pipeline.yaml`.

Refresh order: `make all` then `make quality`.
