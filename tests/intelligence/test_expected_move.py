from math import sqrt

import pytest

from optionforge.intelligence.expected_move import ExpectedMove
from optionforge.models import ExpectedMoveResult


def test_returns_expected_move_result():

    result = ExpectedMove.calculate(
        spot=25000,
        atm_iv=0.20,
        days=30,
    )

    assert isinstance(result, ExpectedMoveResult)


def test_expected_move_positive():

    result = ExpectedMove.calculate(
        spot=25000,
        atm_iv=0.20,
        days=30,
    )

    assert result.expected_move > 0


def test_expected_move_formula():

    spot = 25000
    iv = 0.20
    days = 30

    expected = (
        spot *
        iv *
        sqrt(days / 365)
    )

    result = ExpectedMove.calculate(
        spot=spot,
        atm_iv=iv,
        days=days,
    )

    assert result.expected_move == pytest.approx(expected)


def test_upper_68():

    result = ExpectedMove.calculate(
        spot=25000,
        atm_iv=0.20,
        days=30,
    )

    assert result.upper_68 == pytest.approx(
        25000 + result.expected_move
    )


def test_lower_68():

    result = ExpectedMove.calculate(
        spot=25000,
        atm_iv=0.20,
        days=30,
    )

    assert result.lower_68 == pytest.approx(
        25000 - result.expected_move
    )


def test_upper_95():

    result = ExpectedMove.calculate(
        spot=25000,
        atm_iv=0.20,
        days=30,
    )

    assert result.upper_95 == pytest.approx(
        25000 + (2 * result.expected_move)
    )


def test_lower_95():

    result = ExpectedMove.calculate(
        spot=25000,
        atm_iv=0.20,
        days=30,
    )

    assert result.lower_95 == pytest.approx(
        25000 - (2 * result.expected_move)
    )


def test_daily_move_positive():

    result = ExpectedMove.calculate(
        spot=25000,
        atm_iv=0.20,
        days=30,
    )

    assert result.one_day_move > 0


def test_weekly_move_greater_than_daily():

    result = ExpectedMove.calculate(
        spot=25000,
        atm_iv=0.20,
        days=30,
    )

    assert result.weekly_move > result.one_day_move


def test_monthly_move_greater_than_weekly():

    result = ExpectedMove.calculate(
        spot=25000,
        atm_iv=0.20,
        days=30,
    )

    assert result.monthly_move > result.weekly_move


@pytest.mark.parametrize(
    "spot",
    [0, -1, -25000],
)
def test_invalid_spot(spot):

    with pytest.raises(ValueError):

        ExpectedMove.calculate(
            spot=spot,
            atm_iv=0.20,
            days=30,
        )


@pytest.mark.parametrize(
    "iv",
    [0, -0.20],
)
def test_invalid_iv(iv):

    with pytest.raises(ValueError):

        ExpectedMove.calculate(
            spot=25000,
            atm_iv=iv,
            days=30,
        )


@pytest.mark.parametrize(
    "days",
    [0, -1, -30],
)
def test_invalid_days(days):

    with pytest.raises(ValueError):

        ExpectedMove.calculate(
            spot=25000,
            atm_iv=0.20,
            days=days,
        )