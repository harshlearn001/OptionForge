"""
==============================================================
Tests for InstitutionalResult
==============================================================
"""

from optionforge.intelligence.enums.institutional_state import (
    InstitutionalState,
)

from optionforge.intelligence.institutional_result import (
    InstitutionalResult,
)


def build_result():

    return InstitutionalResult(
        score=0.82,
        confidence=82,
        bias=InstitutionalState.STRONGLY_BULLISH,
    )


# ==========================================================
# Values
# ==========================================================

def test_score():

    assert build_result().score == 0.82


def test_confidence():

    assert build_result().confidence == 82


def test_bias():

    assert (
        build_result().bias
        is InstitutionalState.STRONGLY_BULLISH
    )


# ==========================================================
# Helpers
# ==========================================================

def test_is_bullish():

    assert build_result().is_bullish()


def test_not_bearish():

    assert not build_result().is_bearish()


def test_not_neutral():

    assert not build_result().is_neutral()


# ==========================================================
# Summary
# ==========================================================

def test_summary():

    summary = build_result().summary()

    assert summary["confidence"] == 82

    assert summary["bias"] == "STRONGLY_BULLISH"


# ==========================================================
# Dict
# ==========================================================

def test_to_dict():

    d = build_result().to_dict()

    assert d["score"] == 0.82

    assert d["bias"] == "STRONGLY_BULLISH"


# ==========================================================
# Repr
# ==========================================================

def test_repr():

    assert (
        "InstitutionalResult"
        in repr(build_result())
    )