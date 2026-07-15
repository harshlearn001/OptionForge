import pytest

from optionforge.intelligence import IVPercentile
from optionforge.models import IVPercentileResult


def history():
    return [10, 12, 14, 16, 18, 20, 22, 24, 26, 28]


def test_returns_result():

    result = IVPercentile.calculate(
        current_iv=20,
        historical_iv=history(),
    )

    assert isinstance(result, IVPercentileResult)


def test_observation_count():

    result = IVPercentile.calculate(
        current_iv=20,
        historical_iv=history(),
    )

    assert result.observations == 10


def test_below_count():

    result = IVPercentile.calculate(
        current_iv=20,
        historical_iv=history(),
    )

    assert result.below_count == 5


def test_percentile_formula():

    result = IVPercentile.calculate(
        current_iv=20,
        historical_iv=history(),
    )

    assert result.iv_percentile == pytest.approx(50.0)


def test_zero_percentile():

    result = IVPercentile.calculate(
        current_iv=5,
        historical_iv=history(),
    )

    assert result.iv_percentile == 0


def test_hundred_percentile():

    result = IVPercentile.calculate(
        current_iv=100,
        historical_iv=history(),
    )

    assert result.iv_percentile == 100


@pytest.mark.parametrize(
    ("current_iv", "status"),
    [
        (5, "VERY LOW"),
        (16, "LOW"),
        (20, "NORMAL"),
        (24, "HIGH"),
        (100, "VERY HIGH"),
    ],
)
def test_status(current_iv, status):

    result = IVPercentile.calculate(
        current_iv=current_iv,
        historical_iv=history(),
    )

    assert result.status == status


def test_interpretation_exists():

    result = IVPercentile.calculate(
        current_iv=20,
        historical_iv=history(),
    )

    assert isinstance(
        result.interpretation,
        str,
    )

    assert result.interpretation


def test_empty_history():

    with pytest.raises(ValueError):

        IVPercentile.calculate(
            current_iv=20,
            historical_iv=[],
        )
