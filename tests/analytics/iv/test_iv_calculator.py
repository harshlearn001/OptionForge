from optionforge.analytics.iv.iv_calculator import (
    IVCalculator,
)


def test_call_iv():

    calc = IVCalculator()

    result = calc.calculate(

        spot=25000,

        strike=25000,

        time=30 / 365,

        rate=0.06,

        option_type="CE",

        market_price=633.98,

    )

    assert result.implied_volatility is not None

    assert result.implied_volatility > 0


def test_put_iv():

    calc = IVCalculator()

    result = calc.calculate(

        spot=25000,

        strike=25000,

        time=30 / 365,

        rate=0.06,

        option_type="PE",

        market_price=511.00,

    )

    assert result.implied_volatility is not None

    assert result.implied_volatility > 0


def test_repr():

    calc = IVCalculator()

    assert "IVCalculator" in repr(calc)