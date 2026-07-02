from datetime import date

import pandas as pd
import pytest

from optionforge.analytics import OptionChainAnalytics


def build_chain() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "SYMBOL": "NIFTY",
                "TRADE_DATE": date(2026, 6, 27),
                "EXPIRY_DATE": date(2026, 7, 2),
                "STRIKE_PRICE": 25000,
                "OPTION_TYPE": "CE",
                "OPTION_CLOSE": 633.98,
                "SPOT_CLOSE": 25000,
                "RISK_FREE_RATE": 0.06,
                "TIME_TO_EXPIRY": 30 / 365,
            },
            {
                "SYMBOL": "NIFTY",
                "TRADE_DATE": date(2026, 6, 27),
                "EXPIRY_DATE": date(2026, 7, 2),
                "STRIKE_PRICE": 25100,
                "OPTION_TYPE": "PE",
                "OPTION_CLOSE": 720.25,
                "SPOT_CLOSE": 25000,
                "RISK_FREE_RATE": 0.06,
                "TIME_TO_EXPIRY": 30 / 365,
            },
        ]
    )


def test_returns_dataframe():

    result = OptionChainAnalytics.calculate(
        build_chain()
    )

    assert isinstance(result, pd.DataFrame)


def test_row_count_preserved():

    df = build_chain()

    result = OptionChainAnalytics.calculate(df)

    assert len(result) == len(df)


def test_original_dataframe_unchanged():

    df = build_chain()

    original_columns = list(df.columns)

    OptionChainAnalytics.calculate(df)

    assert list(df.columns) == original_columns


@pytest.mark.parametrize(
    "column",
    [
        "IV",
        "DELTA",
        "GAMMA",
        "THETA",
        "VEGA",
        "INTRINSIC_VALUE",
        "TIME_VALUE",
    ],
)
def test_output_contains_column(column):

    result = OptionChainAnalytics.calculate(
        build_chain()
    )

    assert column in result.columns


def test_iv_positive():

    result = OptionChainAnalytics.calculate(
        build_chain()
    )

    assert (result["IV"] > 0).all()


def test_gamma_positive():

    result = OptionChainAnalytics.calculate(
        build_chain()
    )

    assert (result["GAMMA"] > 0).all()


def test_vega_positive():

    result = OptionChainAnalytics.calculate(
        build_chain()
    )

    assert (result["VEGA"] > 0).all()


def test_delta_in_valid_range():

    result = OptionChainAnalytics.calculate(
        build_chain()
    )

    assert (
        result["DELTA"]
        .abs()
        .le(1)
        .all()
    )


def test_missing_column_validation():

    df = build_chain().drop(
        columns=["SPOT_CLOSE"]
    )

    with pytest.raises(ValueError):

        OptionChainAnalytics.calculate(df)