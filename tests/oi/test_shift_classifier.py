"""
==============================================================
Tests for ShiftClassifier
==============================================================
"""

from optionforge.common.enums import ShiftDirection
from optionforge.oi.shift_classifier import ShiftClassifier


def test_strong_up():

    assert (
        ShiftClassifier.classify(0.40)
        is ShiftDirection.STRONG_UP
    )


def test_up():

    assert (
        ShiftClassifier.classify(0.15)
        is ShiftDirection.UP
    )


def test_neutral_positive():

    assert (
        ShiftClassifier.classify(0.05)
        is ShiftDirection.NEUTRAL
    )


def test_neutral_zero():

    assert (
        ShiftClassifier.classify(0.00)
        is ShiftDirection.NEUTRAL
    )


def test_neutral_negative():

    assert (
        ShiftClassifier.classify(-0.05)
        is ShiftDirection.NEUTRAL
    )


def test_down():

    assert (
        ShiftClassifier.classify(-0.15)
        is ShiftDirection.DOWN
    )


def test_strong_down():

    assert (
        ShiftClassifier.classify(-0.40)
        is ShiftDirection.STRONG_DOWN
    )


def test_boundary_positive():

    assert (
        ShiftClassifier.classify(0.30)
        is ShiftDirection.STRONG_UP
    )


def test_boundary_negative():

    assert (
        ShiftClassifier.classify(-0.30)
        is ShiftDirection.STRONG_DOWN
    )