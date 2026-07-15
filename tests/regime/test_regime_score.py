"""
==============================================================
Tests for RegimeScore
==============================================================
"""

from optionforge.regime.regime_score import (
    RegimeScore,
)


def build_score():

    return RegimeScore(

        institutional=0.90,

        trend=0.80,

        dealer=0.75,

        volatility=0.60,

    )


def test_calculate():

    assert isinstance(
        build_score().calculate(),
        float,
    )


def test_positive():

    assert build_score().calculate() > 0


def test_float():

    assert isinstance(
        float(build_score()),
        float,
    )


def test_repr():

    assert (
        "RegimeScore"
        in repr(build_score())
    )


def test_upper_bound():

    score = RegimeScore(

        institutional=5,

        trend=5,

        dealer=5,

        volatility=5,

    )

    assert score.calculate() == 1.0


def test_lower_bound():

    score = RegimeScore(

        institutional=-5,

        trend=-5,

        dealer=-5,

        volatility=-5,

    )

    assert score.calculate() == 0.0


def test_zero():

    score = RegimeScore(

        institutional=0,

        trend=0,

        dealer=0,

        volatility=0,

    )

    assert score.calculate() == 0.0