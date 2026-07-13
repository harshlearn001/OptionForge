import pytest

from optionforge.analytics.iv_rank.iv_rank_result import (
    IVRankResult,
)


def sample():

    return IVRankResult(

        symbol="NIFTY",

        trade_date=20260714,

        expiry=20260716,

        current_iv=22.5,

        lowest_iv=12.0,

        highest_iv=35.0,

        iv_rank=45.65,

    )


def test_fields():

    result = sample()

    assert result.symbol == "NIFTY"

    assert result.current_iv == 22.5

    assert result.lowest_iv == 12.0

    assert result.highest_iv == 35.0

    assert result.iv_rank == 45.65


def test_repr():

    result = sample()

    assert "IVRankResult" in repr(result)


def test_frozen():

    result = sample()

    with pytest.raises(Exception):

        result.iv_rank = 50.0