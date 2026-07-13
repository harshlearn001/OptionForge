import pytest

from optionforge.analytics.dealer.dealer_result import (
    DealerResult,
)


def sample():

    return DealerResult(

        symbol="NIFTY",

        trade_date=20260714,

        expiry=20260716,

        spot=25510.40,

        major_call_strike=25600,

        major_put_strike=25400,

        total_call_oi=43200000,

        total_put_oi=46800000,

        net_oi=3600000,

        dealer_bias="Bullish",

        confidence=82.5,

        contracts=194,

    )


def test_fields():

    result = sample()

    assert result.symbol == "NIFTY"

    assert result.major_call_strike == 25600

    assert result.major_put_strike == 25400

    assert result.net_oi == 3600000

    assert result.contracts == 194


def test_repr():

    result = sample()

    assert "DealerResult" in repr(result)


def test_frozen():

    result = sample()

    with pytest.raises(Exception):

        result.symbol = "BANKNIFTY"