import pytest

from optionforge.analytics.volatility_smile.volatility_smile_calculator import (
    VolatilitySmileCalculator,
)


def test_sorted():

    result = VolatilitySmileCalculator.calculate(

        strikes=[25500, 25000, 26000],

        ivs=[0.20, 0.19, 0.22],

    )

    assert result == [

        (25000, 0.19),

        (25500, 0.20),

        (26000, 0.22),

    ]


def test_empty():

    result = VolatilitySmileCalculator.calculate(

        strikes=[],

        ivs=[],

    )

    assert result == []


def test_length_mismatch():

    with pytest.raises(ValueError):

        VolatilitySmileCalculator.calculate(

            strikes=[25000],

            ivs=[],

        )


def test_single():

    result = VolatilitySmileCalculator.calculate(

        strikes=[25000],

        ivs=[0.19],

    )

    assert result == [

        (25000, 0.19)

    ]


def test_repr():

    calc = VolatilitySmileCalculator()

    assert "VolatilitySmileCalculator" in repr(calc)