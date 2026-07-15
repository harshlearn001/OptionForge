import pytest

from optionforge.analytics.iv_percentile.iv_percentile_engine import (
    IVPercentileEngine,
)


def test_engine():

    engine = IVPercentileEngine()

    result = engine.calculate(
        symbol="NIFTY",
        trade_date=20260714,
        expiry=20260716,
        current_iv=30,
        historical_iv=[
            10,
            12,
            18,
            20,
            25,
            28,
            30,
            35,
            40,
            45,
        ],
    )

    assert result.symbol == "NIFTY"

    assert result.historical_observations == 10

    assert result.iv_percentile == 60.0


def test_empty_history():

    engine = IVPercentileEngine()

    with pytest.raises(ValueError):

        engine.calculate(
            symbol="NIFTY",
            trade_date=20260714,
            expiry=20260716,
            current_iv=20,
            historical_iv=[],
        )


def test_repr():

    engine = IVPercentileEngine()

    assert "IVPercentileEngine" in repr(engine)
