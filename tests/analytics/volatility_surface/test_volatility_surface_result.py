import pytest

from optionforge.analytics.volatility_surface.volatility_surface_result import (
    VolatilitySurfaceResult,
)


def sample():

    return VolatilitySurfaceResult(

        symbol="NIFTY",

        trade_date=20260716,

        points=[

            (20260723, 25000, 0.19),

            (20260723, 25500, 0.20),

            (20260730, 25000, 0.21),

            (20260730, 25500, 0.22),

        ],

    )


def test_fields():

    result = sample()

    assert result.symbol == "NIFTY"

    assert len(result.points) == 4

    assert result.points[0] == (20260723, 25000, 0.19)


def test_repr():

    result = sample()

    assert "VolatilitySurfaceResult" in repr(result)


def test_frozen():

    result = sample()

    with pytest.raises(Exception):

        result.symbol = "BANKNIFTY"