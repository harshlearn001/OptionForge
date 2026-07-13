from optionforge.analytics.greeks.greeks_calculator import (
    GreeksCalculator,
)


def test_call():

    calc = GreeksCalculator()

    result = calc.calculate(

        spot=25000,

        strike=25000,

        time=30 / 365,

        rate=0.06,

        volatility=0.20,

        option_type="CE",

    )

    assert result.price > 0

    assert result.delta > 0

    assert result.gamma > 0

    assert result.vega > 0


def test_put():

    calc = GreeksCalculator()

    result = calc.calculate(

        spot=25000,

        strike=25000,

        time=30 / 365,

        rate=0.06,

        volatility=0.20,

        option_type="PE",

    )

    assert result.price > 0

    assert result.delta < 0

    assert result.gamma > 0

    assert result.vega > 0


def test_repr():

    calc = GreeksCalculator()

    assert "GreeksCalculator" in repr(calc)