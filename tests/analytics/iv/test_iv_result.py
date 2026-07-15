import pytest

from optionforge.analytics.iv.iv_result import (
    IVResult,
)


def sample():

    return IVResult(
        symbol="NIFTY",
        trade_date=20260714,
        expiry=20260716,
        strike=25000,
        spot=25010.50,
        option_type="CE",
        market_price=633.98,
        implied_volatility=0.2015,
        contracts=192,
    )


def test_fields():

    result = sample()

    assert result.symbol == "NIFTY"

    assert result.option_type == "CE"

    assert result.market_price == 633.98

    assert result.implied_volatility > 0

    assert result.contracts == 192


def test_repr():

    result = sample()

    assert "IVResult" in repr(result)


def test_frozen():

    result = sample()

    with pytest.raises(Exception):

        result.implied_volatility = 0.25
