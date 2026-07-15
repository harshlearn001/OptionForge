"""
==============================================================
OptionForge
Concentration Classifier
--------------------------------------------------------------
Pure OI Concentration Classification
==============================================================
"""

from __future__ import annotations

from optionforge.common.enums import ConcentrationLevel


class ConcentrationClassifier:
    """
    Pure concentration classifier.

    Uses OI share to classify institutional concentration.
    """

    @staticmethod
    def classify(
        oi_share: float,
    ) -> ConcentrationLevel:
        """
        Classify OI concentration.
        """

        if oi_share >= 0.20:
            return ConcentrationLevel.VERY_HIGH

        if oi_share >= 0.15:
            return ConcentrationLevel.HIGH

        if oi_share >= 0.10:
            return ConcentrationLevel.MEDIUM

        if oi_share >= 0.05:
            return ConcentrationLevel.LOW

        return ConcentrationLevel.VERY_LOW