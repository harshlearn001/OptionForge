from optionforge.analytics.volatility_smile.volatility_smile_engine import (
    VolatilitySmileEngine,
)


def test_engine():

    engine = VolatilitySmileEngine()

    result = engine.calculate(
        symbol="NIFTY",
        trade_date=20260716,
        expiry=20260723,
        strikes=[25500, 25000, 26000],
        ivs=[0.20, 0.19, 0.22],
    )

    assert result.symbol == "NIFTY"

    assert len(result.points) == 3

    assert result.points[0] == (25000, 0.19)


def test_sorted():

    engine = VolatilitySmileEngine()

    result = engine.calculate(
        symbol="BANKNIFTY",
        trade_date=20260716,
        expiry=20260723,
        strikes=[55000, 54000, 56000],
        ivs=[0.18, 0.21, 0.19],
    )

    assert result.points[0][0] == 54000

    assert result.points[-1][0] == 56000


def test_repr():

    engine = VolatilitySmileEngine()

    assert "VolatilitySmileEngine" in repr(engine)
