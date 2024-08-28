run_dagster_definitions:
	cd ratepay_project/ratepay_dagster && dagster dev -f definitions.py

run_dagster_assets:
	cd ratepay_project/ratepay_dagster && dagster dev -f assets.py




