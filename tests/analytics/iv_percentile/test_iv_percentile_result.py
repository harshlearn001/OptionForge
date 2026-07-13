import pytest

from optionforge.analytics.iv_percentile.iv_percentile_result import (
    IVPercentileResult,
)


def sample():

    return IVPercentileResult(

        symbol="NIFTY",

        trade_date=20260714,

        expiry=20260716,

        current_iv=30.0,

        historical_observations=252,

        iv_percentile=60.0,

    )


def test_fields():

    result = sample()

    assert result.symbol == "NIFTY"

    assert result.current_iv == 30.0

    assert result.historical_observations == 252

    assert result.iv_percentile == 60.0


def test_repr():

    result = sample()

    assert "IVPercentileResult" in repr(result)


def test_frozen():

    result = sample()

    with pytest.raises(Exception):

        result.iv_percentile = 50.0