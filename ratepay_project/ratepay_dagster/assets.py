from pathlib import Path

from dagster import AssetCheckExecutionContext, AssetIn, asset
from dagster_dbt import DbtCliResource, dbt_assets

# @dbt_assets(manifest=dbt_project.manifest_path)
# def jaffle_shop_dbt_assets(context: AssetExecutionContext, dbt: DbtCliResource):
#     yield from dbt.cli(["build"], context=context).stream()


@asset(compute_kind="dbt", key="load_raw_data")
def load_raw_data(context: AssetCheckExecutionContext):
    """

    Args:
        context (AssetCheckExecutionContext): _description_
    """

    return None


@asset(
    compute_kind="python",
    key="test_hour_values",
    ins={
        "raw_data": AssetIn("load_raw_data"),
    },
)
def test_hour_values(context: AssetCheckExecutionContext, raw_data):
    """

    Args:
        context (AssetCheckExecutionContext): _description_
    """

    return None


@asset(
    compute_kind="python",
    ins={
        "raw_data": AssetIn("load_raw_data"),
    },
    key="test_schema_validation",
)
def test_schema_validation(context: AssetCheckExecutionContext, raw_data):
    """

    Args:
        context (AssetCheckExecutionContext): _description_
    """

    return None


@asset(
    compute_kind="python",
    ins={
        "raw_data": AssetIn("load_raw_data"),
    },
    key="invalid_value_check",
)
def invalid_value_check(context: AssetCheckExecutionContext, raw_data):
    """

    Args:
        context (AssetCheckExecutionContext): _description_
    """

    return None


@asset(
    compute_kind="python",
    ins={
        "test_hour_values_result": AssetIn("test_hour_values"),
        "test_schema_validation_result": AssetIn("test_schema_validation"),
        "invalid_value_check_result": AssetIn("invalid_value_check"),
    },
    key="date_transformation",
)
def date_transformation(
    context: AssetCheckExecutionContext,
    test_hour_values_result,
    test_schema_validation_result,
    invalid_value_check_result,
):
    """

    Args:
        context (AssetCheckExecutionContext): _description_
    """

    return None


@asset(
    compute_kind="python",
    ins={
        "test_hour_values_result": AssetIn("test_hour_values"),
        "test_schema_validation_result": AssetIn("test_schema_validation"),
        "invalid_value_check_result": AssetIn("invalid_value_check"),
    },
    key="other_transformation",
)
def other_transformation(
    context: AssetCheckExecutionContext,
    test_hour_values_result,
    test_schema_validation_result,
    invalid_value_check_result,
):
    """

    Args:
        context (AssetCheckExecutionContext): _description_
    """

    return None


@asset(
    compute_kind="report",
    ins={
        "date_transformation_result": AssetIn("date_transformation"),
        "other_transformation_result": AssetIn("other_transformation"),
    },
    key="trend_hour_of_day",
)
def trend_hour_of_day(
    context: AssetCheckExecutionContext,
    date_transformation_result,
    other_transformation_result,
):
    """

    Args:
        context (AssetCheckExecutionContext): _description_
    """

    return None
