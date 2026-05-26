.PHONY: data fx validate load exports quality insights test all

data:
	python python/generate_sample_data.py

fx:
	python python/ingest_fx_api.py

validate:
	python python/validate_raw.py

load:
	python python/etl_load.py

exports:
	python python/export_dashboard.py

quality:
	python python/run_quality_checks.py

insights:
	python python/generate_insights.py

test:
	pytest tests/ -q

all: data fx validate load exports insights
