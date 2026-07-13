import pytest

from optionforge.analytics.expected_move.expected_move_result import (
    ExpectedMoveResult,
)


def sample():

    return ExpectedMoveResult(

        symbol="NIFTY",

        trade_date=20260714,

        expiry=20260721,

        spot=25000,

        volatility=0.20,

        time=7 / 365,

        expected_move=692.42,

        upper_bound=25692.42,

        lower_bound=24307.58,

    )


def test_fields():

    result = sample()

    assert result.symbol == "NIFTY"

    assert result.expected_move == 692.42

    assert result.upper_bound == 25692.42

    assert result.lower_bound == 24307.58


def test_repr():

    result = sample()

    assert "ExpectedMoveResult" in repr(result)


def test_frozen():

    result = sample()

    with pytest.raises(Exception):

        result.expected_move = 700