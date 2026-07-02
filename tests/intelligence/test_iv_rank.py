import pytest

from optionforge.intelligence import IVRank
from optionforge.models import IVRankResult


def test_returns_iv_rank_result():

    result = IVRank.calculate(
        current_iv=18.0,
        low_iv=10.0,
        high_iv=30.0,
    )

    assert isinstance(result, IVRankResult)


def test_formula():

    result = IVRank.calculate(
        current_iv=20.0,
        low_iv=10.0,
        high_iv=30.0,
    )

    assert result.iv_rank == pytest.approx(50.0)


def test_zero_percent():

    result = IVRank.calculate(
        current_iv=10.0,
        low_iv=10.0,
        high_iv=30.0,
    )

    assert result.iv_rank == pytest.approx(0.0)


def test_hundred_percent():

    result = IVRank.calculate(
        current_iv=30.0,
        low_iv=10.0,
        high_iv=30.0,
    )

    assert result.iv_rank == pytest.approx(100.0)


def test_clamped_below_zero():

    result = IVRank.calculate(
        current_iv=5.0,
        low_iv=10.0,
        high_iv=30.0,
    )

    assert result.iv_rank == 0.0


def test_clamped_above_hundred():

    result = IVRank.calculate(
        current_iv=35.0,
        low_iv=10.0,
        high_iv=30.0,
    )

    assert result.iv_rank == 100.0


@pytest.mark.parametrize(
    ("iv_rank", "expected_status"),
    [
        (15.0, "VERY LOW"),
        (30.0, "LOW"),
        (50.0, "NORMAL"),
        (70.0, "HIGH"),
        (90.0, "VERY HIGH"),
    ],
)
def test_status(iv_rank, expected_status):

    current_iv = 10 + (iv_rank / 100) * (30 - 10)

    result = IVRank.calculate(
        current_iv=current_iv,
        low_iv=10.0,
        high_iv=30.0,
    )

    assert result.status == expected_status


def test_interpretation_not_empty():

    result = IVRank.calculate(
        current_iv=18.0,
        low_iv=10.0,
        high_iv=30.0,
    )

    assert result.interpretation
    assert isinstance(result.interpretation, str)


@pytest.mark.parametrize(
    ("low_iv", "high_iv"),
    [
        (20.0, 20.0),
        (30.0, 20.0),
    ],
)
def test_invalid_range(low_iv, high_iv):

    with pytest.raises(ValueError):

        IVRank.calculate(
            current_iv=18.0,
            low_iv=low_iv,
            high_iv=high_iv,
        )