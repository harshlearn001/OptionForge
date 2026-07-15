"""
Tests for ConcentrationClassifier.
"""

from optionforge.common.enums import ConcentrationLevel
from optionforge.oi.concentration_classifier import (
    ConcentrationClassifier,
)


def test_very_high():

    assert (
        ConcentrationClassifier.classify(0.25)
        is ConcentrationLevel.VERY_HIGH
    )


def test_high():

    assert (
        ConcentrationClassifier.classify(0.18)
        is ConcentrationLevel.HIGH
    )


def test_medium():

    assert (
        ConcentrationClassifier.classify(0.12)
        is ConcentrationLevel.MEDIUM
    )


def test_low():

    assert (
        ConcentrationClassifier.classify(0.06)
        is ConcentrationLevel.LOW
    )


def test_very_low():

    assert (
        ConcentrationClassifier.classify(0.03)
        is ConcentrationLevel.VERY_LOW
    )


def test_boundary_20():

    assert (
        ConcentrationClassifier.classify(0.20)
        is ConcentrationLevel.VERY_HIGH
    )


def test_boundary_15():

    assert (
        ConcentrationClassifier.classify(0.15)
        is ConcentrationLevel.HIGH
    )


def test_boundary_10():

    assert (
        ConcentrationClassifier.classify(0.10)
        is ConcentrationLevel.MEDIUM
    )


def test_boundary_05():

    assert (
        ConcentrationClassifier.classify(0.05)
        is ConcentrationLevel.LOW
    )