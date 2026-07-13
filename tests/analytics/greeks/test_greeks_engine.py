from optionforge.analytics.greeks.greeks_engine import (
    GreeksEngine,
)


def test_call_engine():

    engine = GreeksEngine()

    result = engine.calculate(

        symbol="NIFTY",

        trade_date=20260714,

        expiry=20260716,

        spot=25000,

        strike=25000,

        time=30 / 365,

        rate=0.06,

        volatility=0.20,

        option_type="CE",

        market_price=633.98,

    )

    assert result.symbol == "NIFTY"

    assert result.option_type == "CE"

    assert result.option_price > 0

    assert result.delta > 0

    assert result.gamma > 0

    assert result.vega > 0

    assert result.implied_volatility is not None


def test_put_engine():

    engine = GreeksEngine()

    result = engine.calculate(

        symbol="NIFTY",

        trade_date=20260714,

        expiry=20260716,

        spot=25000,

        strike=25000,

        time=30 / 365,

        rate=0.06,

        volatility=0.20,

        option_type="PE",

    )

    assert result.option_type == "PE"

    assert result.delta < 0


def test_repr():

    engine = GreeksEngine()

    assert "GreeksEngine" in repr(engine)