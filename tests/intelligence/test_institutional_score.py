"""
==============================================================
Tests for InstitutionalScore
==============================================================
"""

from optionforge.intelligence.institutional_score import (
    InstitutionalScore,
)


def build_score():

    return InstitutionalScore(

        summary=0.60,

        change=0.70,

        buildup=0.80,

        wall=0.75,

        concentration=0.50,

        shift=0.65,

        trend=0.85,

    )


def test_calculate():

    score = build_score().calculate()

    assert isinstance(score, float)


def test_score_positive():

    assert build_score().calculate() > 0


def test_float():

    assert isinstance(float(build_score()), float)


def test_repr():

    assert "InstitutionalScore" in repr(build_score())


def test_upper_bound():

    score = InstitutionalScore(

        summary=5,

        change=5,

        buildup=5,

        wall=5,

        concentration=5,

        shift=5,

        trend=5,

    )

    assert score.calculate() == 1.0


def test_lower_bound():

    score = InstitutionalScore(

        summary=-5,

        change=-5,

        buildup=-5,

        wall=-5,

        concentration=-5,

        shift=-5,

        trend=-5,

    )

    assert score.calculate() == -1.0


def test_zero():

    score = InstitutionalScore(

        summary=0,

        change=0,

        buildup=0,

        wall=0,

        concentration=0,

        shift=0,

        trend=0,

    )

    assert score.calculate() == 0.0