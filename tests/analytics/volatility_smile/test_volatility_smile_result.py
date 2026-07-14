import pytest

from optionforge.analytics.volatility_smile.volatility_smile_result import (
    VolatilitySmileResult,
)


def sample():

    return VolatilitySmileResult(

        symbol="NIFTY",

        trade_date=20260715,

        expiry=20260723,

        points=[

            (24000, 0.23),

            (24500, 0.21),

            (25000, 0.19),

            (25500, 0.20),

            (26000, 0.22),

        ],

    )


def test_fields():

    result = sample()

    assert result.symbol == "NIFTY"

    assert len(result.points) == 5

    assert result.points[2] == (25000, 0.19)


def test_repr():

    result = sample()

    assert "VolatilitySmileResult" in repr(result)


def test_frozen():

    result = sample()

    with pytest.raises(Exception):

        result.symbol = "BANKNIFTY"