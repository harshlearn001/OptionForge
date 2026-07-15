"""
============================================================
OptionForge
ResearchReport Tests
============================================================
"""

import pytest

from optionforge.research.research_report import (
    ResearchReport,
)


def report():

    return ResearchReport(
        strategy_name="Momentum Strategy",
        overall_score=91.5,
        overall_grade="A",
        approved=True,
        recommendation="Deploy",
    )


# ==========================================================
# Construction
# ==========================================================


def test_create():

    assert isinstance(
        report(),
        ResearchReport,
    )


# ==========================================================
# Values
# ==========================================================


def test_strategy():

    assert report().strategy_name == "Momentum Strategy"


def test_score():

    assert report().overall_score == 91.5


def test_grade():

    assert report().overall_grade == "A"


def test_approved():

    assert report().approved


def test_recommendation():

    assert report().recommendation == "Deploy"


# ==========================================================
# Property
# ==========================================================


def test_passed():

    assert report().passed


# ==========================================================
# Validation
# ==========================================================


def test_empty_strategy():

    with pytest.raises(ValueError):

        ResearchReport(
            strategy_name="",
            overall_score=90,
            overall_grade="A",
            approved=True,
            recommendation="Deploy",
        )


@pytest.mark.parametrize(
    "score",
    [
        -1,
        101,
    ],
)
def test_invalid_score(score):

    with pytest.raises(ValueError):

        ResearchReport(
            strategy_name="Test",
            overall_score=score,
            overall_grade="A",
            approved=True,
            recommendation="Deploy",
        )


def test_empty_grade():

    with pytest.raises(ValueError):

        ResearchReport(
            strategy_name="Test",
            overall_score=90,
            overall_grade="",
            approved=True,
            recommendation="Deploy",
        )


def test_empty_recommendation():

    with pytest.raises(ValueError):

        ResearchReport(
            strategy_name="Test",
            overall_score=90,
            overall_grade="A",
            approved=True,
            recommendation="",
        )


# ==========================================================
# Serialization
# ==========================================================


def test_to_dict():

    data = report().to_dict()

    assert data["strategy_name"] == "Momentum Strategy"

    assert data["overall_grade"] == "A"

    assert data["passed"]


# ==========================================================
# Representation
# ==========================================================


def test_str():

    assert "ResearchReport" in str(
        report(),
    )


def test_repr():

    assert "ResearchReport" in repr(
        report(),
    )
