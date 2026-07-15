"""
==============================================================
OptionForge
Trend Classifier
==============================================================
"""

from __future__ import annotations

from optionforge.common.enums import TrendDirection


class TrendClassifier:
    """
    Multi-session trend classifier.
    """

    @staticmethod
    def classify(score: float) -> TrendDirection:

        if score >= 0.60:
            return TrendDirection.STRONG_BULLISH

        if score >= 0.20:
            return TrendDirection.BULLISH

        if score <= -0.60:
            return TrendDirection.STRONG_BEARISH

        if score <= -0.20:
            return TrendDirection.BEARISH

        return TrendDirection.SIDEWAYS