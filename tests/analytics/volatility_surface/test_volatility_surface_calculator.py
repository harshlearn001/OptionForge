import pytest

from optionforge.analytics.volatility_surface.volatility_surface_calculator import (
    VolatilitySurfaceCalculator,
)


def test_sorted():

    result = VolatilitySurfaceCalculator.calculate(
        strikes=[25500, 25000, 25000],
        expiries=[20260730, 20260723, 20260730],
        ivs=[0.20, 0.19, 0.21],
    )

    assert result == [
        (20260723, 25000, 0.19),
        (20260730, 25000, 0.21),
        (20260730, 25500, 0.20),
    ]


def test_empty():

    result = VolatilitySurfaceCalculator.calculate(
        strikes=[],
        expiries=[],
        ivs=[],
    )

    assert result == []


def test_length():

    with pytest.raises(ValueError):

        VolatilitySurfaceCalculator.calculate(
            strikes=[25000],
            expiries=[],
            ivs=[],
        )


def test_single():

    result = VolatilitySurfaceCalculator.calculate(
        strikes=[25000],
        expiries=[20260723],
        ivs=[0.20],
    )

    assert result == [(20260723, 25000, 0.20)]


def test_repr():

    calc = VolatilitySurfaceCalculator()

    assert "VolatilitySurfaceCalculator" in repr(calc)
