import pytest

from optionforge.analytics.greeks.greeks_result import (
    GreeksResult,
)


def sample():

    return GreeksResult(
        symbol="NIFTY",
        trade_date=20260714,
        expiry=20260716,
        strike=25000,
        spot=25010.50,
        option_type="CE",
        option_price=633.98,
        implied_volatility=0.20,
        delta=0.5456,
        gamma=0.000276,
        theta=-4236.48,
        vega=2840.59,
    )


def test_fields():

    result = sample()

    assert result.symbol == "NIFTY"

    assert result.option_type == "CE"

    assert result.delta > 0

    assert result.gamma > 0

    assert result.vega > 0


def test_repr():

    result = sample()

    assert "GreeksResult" in repr(result)


def test_frozen():

    result = sample()

    with pytest.raises(Exception):

        result.delta = 0.10
