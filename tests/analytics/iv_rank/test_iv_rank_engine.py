import pytest

from optionforge.analytics.iv_rank.iv_rank_engine import (
    IVRankEngine,
)


def test_engine():

    engine = IVRankEngine()

    result = engine.calculate(
        symbol="NIFTY",
        trade_date=20260714,
        expiry=20260716,
        current_iv=30,
        historical_iv=[10, 15, 20, 30, 40, 50],
    )

    assert result.symbol == "NIFTY"

    assert result.lowest_iv == 10

    assert result.highest_iv == 50

    assert result.iv_rank == 50.0


def test_empty_history():

    engine = IVRankEngine()

    with pytest.raises(ValueError):

        engine.calculate(
            symbol="NIFTY",
            trade_date=20260714,
            expiry=20260716,
            current_iv=20,
            historical_iv=[],
        )


def test_repr():

    engine = IVRankEngine()

    assert "IVRankEngine" in repr(engine)
