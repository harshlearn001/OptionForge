import pytest

from optionforge.intelligence import Strategy
from optionforge.models import (
    ProbabilityResult,
    StrategyResult,
)


def probability(score: float) -> ProbabilityResult:

    return ProbabilityResult(
        bullish_probability=score,
        bearish_probability=100 - score,
        confidence="HIGH",
        stars=5,
        trade_quality="A",
        risk_level="LOW",
        recommendation="Test",
        interpretation="Probability Test",
    )


def test_returns_strategy_result():

    result = Strategy.calculate(
        probability(85),
        spot_price=25000,
        expected_move=500,
    )

    assert isinstance(result, StrategyResult)


@pytest.mark.parametrize(
    ("bull", "action"),
    [
        (90, "BUY"),
        (70, "BUY ON DIP"),
        (50, "WAIT"),
        (20, "SELL"),
    ],
)
def test_action(bull, action):

    result = Strategy.calculate(
        probability(bull),
        25000,
        500,
    )

    assert result.action == action


def test_entry_zone():

    result = Strategy.calculate(
        probability(80),
        25000,
        500,
    )

    assert result.entry_zone == "24900.00 - 25000.00"


def test_stop_loss():

    result = Strategy.calculate(
        probability(80),
        25000,
        500,
    )

    assert result.stop_loss == pytest.approx(24775.00)


def test_target1():

    result = Strategy.calculate(
        probability(80),
        25000,
        500,
    )

    assert result.target_1 == pytest.approx(25250.00)


def test_target2():

    result = Strategy.calculate(
        probability(80),
        25000,
        500,
    )

    assert result.target_2 == pytest.approx(25500.00)


def test_risk_reward():

    result = Strategy.calculate(
        probability(80),
        25000,
        500,
    )

    assert result.risk_reward == pytest.approx(2.22)


def test_trade_quality_preserved():

    result = Strategy.calculate(
        probability(80),
        25000,
        500,
    )

    assert result.trade_quality == "A"


def test_confidence_preserved():

    result = Strategy.calculate(
        probability(80),
        25000,
        500,
    )

    assert result.confidence == "HIGH"


def test_stars_preserved():

    result = Strategy.calculate(
        probability(80),
        25000,
        500,
    )

    assert result.stars == 5


@pytest.mark.parametrize(
    ("bull", "text"),
    [
        (90, "Momentum"),
        (70, "pullback"),
        (50, "No high-quality"),
        (20, "Selling rallies"),
    ],
)
def test_recommendation(bull, text):

    result = Strategy.calculate(
        probability(bull),
        25000,
        500,
    )

    assert text in result.recommendation


def test_interpretation_exists():

    result = Strategy.calculate(
        probability(75),
        25000,
        500,
    )

    assert isinstance(result.interpretation, str)
    assert "75.00%" in result.interpretation


def test_targets_order():

    result = Strategy.calculate(
        probability(80),
        25000,
        500,
    )

    assert result.target_2 > result.target_1


def test_stop_below_entry():

    result = Strategy.calculate(
        probability(80),
        25000,
        500,
    )

    assert result.stop_loss < 24900


def test_target_above_entry():

    result = Strategy.calculate(
        probability(80),
        25000,
        500,
    )

    assert result.target_1 > 25000
    assert result.target_2 > 25000