from optionforge.analytics.iv_rank.iv_rank_calculator import (
    IVRankCalculator,
)


def test_middle():

    value = IVRankCalculator.calculate(
        current_iv=30,
        lowest_iv=10,
        highest_iv=50,
    )

    assert value == 50.0


def test_zero():

    value = IVRankCalculator.calculate(
        current_iv=10,
        lowest_iv=10,
        highest_iv=50,
    )

    assert value == 0.0


def test_hundred():

    value = IVRankCalculator.calculate(
        current_iv=50,
        lowest_iv=10,
        highest_iv=50,
    )

    assert value == 100.0


def test_equal_range():

    value = IVRankCalculator.calculate(
        current_iv=20,
        lowest_iv=20,
        highest_iv=20,
    )

    assert value == 0.0


def test_repr():

    calc = IVRankCalculator()

    assert "IVRankCalculator" in repr(calc)
