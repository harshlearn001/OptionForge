import pytest

from optionforge.analytics.maxpain.max_pain_result import (
    MaxPainResult,
)


def sample():

    return MaxPainResult(
        symbol="NIFTY",
        trade_date=20260713,
        expiry=20260716,
        spot=25485.20,
        max_pain_strike=25500,
        total_pain=3245120.0,
        call_pain=1520000.0,
        put_pain=1725120.0,
        distance_from_spot=14.80,
        contracts=192,
    )


def test_fields():

    result = sample()

    assert result.symbol == "NIFTY"

    assert result.max_pain_strike == 25500

    assert result.contracts == 192


def test_repr():

    result = sample()

    assert "MaxPainResult" in repr(result)


def test_frozen():

    result = sample()

    with pytest.raises(Exception):

        result.symbol = "BANKNIFTY"
