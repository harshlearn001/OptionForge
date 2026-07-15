import pytest

from optionforge.intelligence import Probability
from optionforge.models import (
    MarketStructureResult,
    ProbabilityResult,
)


def market(score: float) -> MarketStructureResult:

    return MarketStructureResult(
        score=score,
        bias="BULLISH",
        confidence="HIGH",
        stars=5,
        recommendation="Buy",
        support_strength=80.0,
        resistance_strength=25.0,
        expected_move=250.0,
        iv_rank=45.0,
        iv_percentile=55.0,
        max_pain=25000.0,
        interpretation="Market structure test",
    )


def test_returns_probability_result():

    result = Probability.calculate(
        market(75),
    )

    assert isinstance(result, ProbabilityResult)


@pytest.mark.parametrize(
    ("score", "bull", "bear"),
    [
        (0, 0, 100),
        (25, 25, 75),
        (50, 50, 50),
        (75, 75, 25),
        (100, 100, 0),
    ],
)
def test_probability_values(score, bull, bear):

    result = Probability.calculate(
        market(score),
    )

    assert result.bullish_probability == bull
    assert result.bearish_probability == bear


@pytest.mark.parametrize(
    ("score", "grade"),
    [
        (95, "A+"),
        (82, "A"),
        (75, "B"),
        (62, "C"),
        (45, "D"),
    ],
)
def test_trade_quality(score, grade):

    result = Probability.calculate(
        market(score),
    )

    assert result.trade_quality == grade


@pytest.mark.parametrize(
    ("score", "risk"),
    [
        (95, "LOW"),
        (80, "MEDIUM"),
        (70, "MEDIUM"),
        (60, "HIGH"),
        (25, "HIGH"),
    ],
)
def test_risk(score, risk):

    result = Probability.calculate(
        market(score),
    )

    assert result.risk_level == risk


@pytest.mark.parametrize(
    ("score", "text"),
    [
        (90, "Bullish"),
        (70, "Moderately bullish"),
        (50, "Balanced"),
        (20, "Bearish"),
    ],
)
def test_recommendation(score, text):

    result = Probability.calculate(
        market(score),
    )

    assert text in result.recommendation


def test_confidence_preserved():

    result = Probability.calculate(
        market(70),
    )

    assert result.confidence == "HIGH"


def test_stars_preserved():

    result = Probability.calculate(
        market(70),
    )

    assert result.stars == 5


def test_interpretation_exists():

    result = Probability.calculate(
        market(70),
    )

    assert isinstance(result.interpretation, str)
    assert result.interpretation


def test_probability_sum():

    result = Probability.calculate(
        market(73),
    )

    assert (result.bullish_probability + result.bearish_probability) == pytest.approx(
        100.0
    )
