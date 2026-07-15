"""
Tests for BuildUpClassifier.
"""

from optionforge.common.enums import BuildUp
from optionforge.oi.buildup_classifier import BuildUpClassifier


def test_long_buildup():

    result = BuildUpClassifier.classify(
        price_change=10.0,
        oi_change=500,
    )

    assert result is BuildUp.LONG_BUILDUP


def test_short_buildup():

    result = BuildUpClassifier.classify(
        price_change=-10.0,
        oi_change=500,
    )

    assert result is BuildUp.SHORT_BUILDUP


def test_short_covering():

    result = BuildUpClassifier.classify(
        price_change=10.0,
        oi_change=-500,
    )

    assert result is BuildUp.SHORT_COVERING


def test_long_unwinding():

    result = BuildUpClassifier.classify(
        price_change=-10.0,
        oi_change=-500,
    )

    assert result is BuildUp.LONG_UNWINDING


def test_neutral_zero_price():

    result = BuildUpClassifier.classify(
        price_change=0.0,
        oi_change=500,
    )

    assert result is BuildUp.NEUTRAL


def test_neutral_zero_oi():

    result = BuildUpClassifier.classify(
        price_change=10.0,
        oi_change=0,
    )

    assert result is BuildUp.NEUTRAL


def test_neutral_zero_both():

    result = BuildUpClassifier.classify(
        price_change=0.0,
        oi_change=0,
    )

    assert result is BuildUp.NEUTRAL