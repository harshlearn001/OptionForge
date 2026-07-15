"""
==============================================================
Tests for InstitutionalBiasClassifier
==============================================================
"""

from optionforge.intelligence.enums.institutional_state import (
    InstitutionalState,
)

from optionforge.intelligence.institutional_bias_classifier import (
    InstitutionalBiasClassifier,
)


def test_strong_bullish():

    assert (
        InstitutionalBiasClassifier.classify(0.90)
        is InstitutionalState.STRONGLY_BULLISH
    )


def test_bullish():

    assert (
        InstitutionalBiasClassifier.classify(0.35)
        is InstitutionalState.BULLISH
    )


def test_neutral_positive():

    assert (
        InstitutionalBiasClassifier.classify(0.10)
        is InstitutionalState.NEUTRAL
    )


def test_neutral_zero():

    assert (
        InstitutionalBiasClassifier.classify(0.00)
        is InstitutionalState.NEUTRAL
    )


def test_neutral_negative():

    assert (
        InstitutionalBiasClassifier.classify(-0.10)
        is InstitutionalState.NEUTRAL
    )


def test_bearish():

    assert (
        InstitutionalBiasClassifier.classify(-0.35)
        is InstitutionalState.BEARISH
    )


def test_strong_bearish():

    assert (
        InstitutionalBiasClassifier.classify(-0.90)
        is InstitutionalState.STRONGLY_BEARISH
    )


def test_upper_boundary():

    assert (
        InstitutionalBiasClassifier.classify(0.60)
        is InstitutionalState.STRONGLY_BULLISH
    )


def test_lower_boundary():

    assert (
        InstitutionalBiasClassifier.classify(-0.60)
        is InstitutionalState.STRONGLY_BEARISH
    )