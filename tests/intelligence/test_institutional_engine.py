"""
==============================================================
Tests for InstitutionalEngine
==============================================================
"""

from optionforge.intelligence.institutional_engine import (
    InstitutionalEngine,
)

from optionforge.intelligence.institutional_result import (
    InstitutionalResult,
)


def build_engine():

    return InstitutionalEngine(

        summary=0.60,

        change=0.70,

        buildup=0.80,

        wall=0.75,

        concentration=0.55,

        shift=0.65,

        trend=0.90,

    )


# ==========================================================
# Result
# ==========================================================

def test_returns_result():

    result = build_engine().calculate()

    assert isinstance(
        result,
        InstitutionalResult,
    )


# ==========================================================
# Score
# ==========================================================

def test_score():

    result = build_engine().calculate()

    assert isinstance(result.score, float)


# ==========================================================
# Confidence
# ==========================================================

def test_confidence():

    result = build_engine().calculate()

    assert isinstance(result.confidence, int)


# ==========================================================
# Bias
# ==========================================================

def test_bias():

    result = build_engine().calculate()

    assert result.bias is not None


# ==========================================================
# Bullish
# ==========================================================

def test_bullish():

    result = build_engine().calculate()

    assert result.is_bullish()


# ==========================================================
# Summary
# ==========================================================

def test_summary():

    assert isinstance(
        build_engine().calculate().summary(),
        dict,
    )


# ==========================================================
# Dictionary
# ==========================================================

def test_dict():

    assert isinstance(
        build_engine().calculate().to_dict(),
        dict,
    )


# ==========================================================
# Representation
# ==========================================================

def test_repr():

    assert (
        "InstitutionalEngine"
        in repr(build_engine())
    )