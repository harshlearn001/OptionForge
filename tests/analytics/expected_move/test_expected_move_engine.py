from optionforge.analytics.expected_move.expected_move_engine import (
    ExpectedMoveEngine,
)


def test_engine():

    engine = ExpectedMoveEngine()

    result = engine.calculate(
        symbol="NIFTY",
        trade_date=20260714,
        expiry=20260721,
        spot=25000,
        volatility=0.20,
        time=7 / 365,
    )

    assert result.symbol == "NIFTY"

    assert round(result.expected_move, 2) == 692.42

    assert round(result.upper_bound, 2) == 25692.42

    assert round(result.lower_bound, 2) == 24307.58


def test_bounds():

    engine = ExpectedMoveEngine()

    result = engine.calculate(
        symbol="BANKNIFTY",
        trade_date=20260714,
        expiry=20260721,
        spot=50000,
        volatility=0.15,
        time=14 / 365,
    )

    assert result.upper_bound > result.spot

    assert result.lower_bound < result.spot


def test_repr():

    engine = ExpectedMoveEngine()

    assert "ExpectedMoveEngine" in repr(engine)
