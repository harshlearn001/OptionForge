"""
==============================================================
Tests for ConfidenceClassifier
==============================================================
"""

from optionforge.intelligence.confidence_classifier import (
    ConfidenceClassifier,
)


def test_positive():

    assert (
        ConfidenceClassifier.classify(0.75)
        == 75
    )


def test_negative():

    assert (
        ConfidenceClassifier.classify(-0.82)
        == 82
    )


def test_zero():

    assert (
        ConfidenceClassifier.classify(0.0)
        == 0
    )


def test_upper_bound():

    assert (
        ConfidenceClassifier.classify(2.5)
        == 100
    )


def test_lower_bound():

    assert (
        ConfidenceClassifier.classify(-5.0)
        == 100
    )


def test_half():

    assert (
        ConfidenceClassifier.classify(0.50)
        == 50
    )


def test_small():

    assert (
        ConfidenceClassifier.classify(0.12)
        == 12
    )