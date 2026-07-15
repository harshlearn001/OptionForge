"""
==============================================================
OptionForge
Shift Classifier
--------------------------------------------------------------
Pure Open Interest Shift Classification.
==============================================================
"""

from __future__ import annotations

from optionforge.common.enums import ShiftDirection


class ShiftClassifier:
    """
    Pure OI shift classifier.
    """

    @staticmethod
    def classify(
        shift: float,
    ) -> ShiftDirection:
        """
        Classify normalized OI shift.

        Positive values indicate migration
        toward higher strikes.

        Negative values indicate migration
        toward lower strikes.
        """

        if shift >= 0.30:
            return ShiftDirection.STRONG_UP

        if shift >= 0.10:
            return ShiftDirection.UP

        if shift <= -0.30:
            return ShiftDirection.STRONG_DOWN

        if shift <= -0.10:
            return ShiftDirection.DOWN

        return ShiftDirection.NEUTRAL