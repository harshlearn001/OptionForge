from optionforge.analytics.volatility_surface.volatility_surface_engine import (
    VolatilitySurfaceEngine,
)


def test_engine():

    engine = VolatilitySurfaceEngine()

    result = engine.calculate(

        symbol="NIFTY",

        trade_date=20260716,

        strikes=[25500, 25000, 25000],

        expiries=[20260730, 20260723, 20260730],

        ivs=[0.20, 0.19, 0.21],

    )

    assert result.symbol == "NIFTY"

    assert len(result.points) == 3

    assert result.points[0] == (20260723, 25000, 0.19)


def test_sorted():

    engine = VolatilitySurfaceEngine()

    result = engine.calculate(

        symbol="BANKNIFTY",

        trade_date=20260716,

        strikes=[55000, 54000, 54000],

        expiries=[20260730, 20260723, 20260730],

        ivs=[0.18, 0.21, 0.19],

    )

    assert result.points[0] == (20260723, 54000, 0.21)

    assert result.points[-1] == (20260730, 55000, 0.18)


def test_repr():

    engine = VolatilitySurfaceEngine()

    assert "VolatilitySurfaceEngine" in repr(engine)