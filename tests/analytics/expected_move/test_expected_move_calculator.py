import pytest

from optionforge.analytics.expected_move.expected_move_calculator import (
    ExpectedMoveCalculator,
)


def test_expected_move():

    move = ExpectedMoveCalculator.calculate(

        spot=25000,

        volatility=0.20,

        time=7 / 365,

    )

    assert round(move, 2) == 692.42


def test_negative_volatility():

    with pytest.raises(ValueError):

        ExpectedMoveCalculator.calculate(

            spot=25000,

            volatility=-0.20,

            time=7 / 365,

        )


def test_negative_time():

    with pytest.raises(ValueError):

        ExpectedMoveCalculator.calculate(

            spot=25000,

            volatility=0.20,

            time=-1,

        )


def test_zero_spot():

    with pytest.raises(ValueError):

        ExpectedMoveCalculator.calculate(

            spot=0,

            volatility=0.20,

            time=7 / 365,

        )


def test_repr():

    calc = ExpectedMoveCalculator()

    assert "ExpectedMoveCalculator" in repr(calc)