"""
==============================================================
OptionForge
Institutional Bias Classifier
--------------------------------------------------------------

Converts a normalized institutional score into an
institutional market bias.

Score Range
-----------
-1.0 ................. +1.0

==============================================================
"""

from __future__ import annotations

from optionforge.intelligence.enums.institutional_state import (
    InstitutionalState,
)


class InstitutionalBiasClassifier:
    """
    Converts a normalized institutional score into
    an institutional market bias.
    """

    STRONG_BULLISH = 0.60
    BULLISH = 0.20

    BEARISH = -0.20
    STRONG_BEARISH = -0.60

    @classmethod
    def classify(
        cls,
        score: float,
    ) -> InstitutionalState:
        """
        Classify institutional bias.
        """

        if score >= cls.STRONG_BULLISH:
            return InstitutionalState.STRONGLY_BULLISH

        if score >= cls.BULLISH:
            return InstitutionalState.BULLISH

        if score <= cls.STRONG_BEARISH:
            return InstitutionalState.STRONGLY_BEARISH

        if score <= cls.BEARISH:
            return InstitutionalState.BEARISH

        return InstitutionalState.NEUTRAL