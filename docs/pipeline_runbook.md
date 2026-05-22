# Pipeline runbook

Step-by-step order I use when refreshing the sample warehouse.

## 1. Regenerate feeds (optional)

```bash
python python/generate_sample_data.py
```

Fixed seed (`random.seed(42)`) so row counts stay reproducible unless you change the script.

## 2. FX snapshot

```bash
python python/ingest_fx_api.py
```

Requires network. Writes `data/raw/fx_rates.csv` and `fx_rates.json`. If the API is down, skip this step; `etl_load.py` does not require FX.

## 3. Validate raw files

```bash
python python/validate_raw.py
```

Checks required columns, nulls on keys, and basic numeric ranges before load.

## 4. Load SQLite warehouse

```bash
python python/etl_load.py
```

Creates `warehouse/analytics.db` and indexes on date columns.

## 5. Export BI tables

```bash
make exports
```

Or `python python/export_dashboard.py`. Outputs land in `dashboard/exports/`.

## 6. Warehouse QA

```bash
make quality
```

## 7. Tests

```bash
make test
```

You can also point a SQL client at `warehouse/analytics.db` and run `sql/02_data_quality_checks.sql` if you need manual inspection.

## Troubleshooting

| Symptom | Likely cause |
|---------|----------------|
| `FileNotFoundError` on load | Run the generator first |
| Empty ROAS rows | Spend file missing for that campaign date |
| SQLite locked | Close DB browser tabs holding the file |
