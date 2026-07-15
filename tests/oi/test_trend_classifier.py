from optionforge.common.enums import TrendDirection
from optionforge.oi.trend_classifier import TrendClassifier


def test_strong_bullish():
    assert TrendClassifier.classify(0.80) is TrendDirection.STRONG_BULLISH


def test_bullish():
    assert TrendClassifier.classify(0.35) is TrendDirection.BULLISH


def test_sideways_positive():
    assert TrendClassifier.classify(0.05) is TrendDirection.SIDEWAYS


def test_sideways_zero():
    assert TrendClassifier.classify(0.00) is TrendDirection.SIDEWAYS


def test_sideways_negative():
    assert TrendClassifier.classify(-0.05) is TrendDirection.SIDEWAYS


def test_bearish():
    assert TrendClassifier.classify(-0.35) is TrendDirection.BEARISH


def test_strong_bearish():
    assert TrendClassifier.classify(-0.80) is TrendDirection.STRONG_BEARISH


def test_boundary_positive():
    assert TrendClassifier.classify(0.60) is TrendDirection.STRONG_BULLISH


def test_boundary_negative():
    assert TrendClassifier.classify(-0.60) is TrendDirection.STRONG_BEARISH