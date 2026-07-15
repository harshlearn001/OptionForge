"""
==============================================================
OptionForge
Wall Classifier
--------------------------------------------------------------
Pure OI Wall Classification
==============================================================
"""

from __future__ import annotations

from optionforge.common.enums import WallType


class WallClassifier:
    """
    Pure OI Wall classifier.
    """

    @staticmethod
    def classify(
        call_share: float,
        put_share: float,
    ) -> WallType:
        """
        Classify OI Wall.
        """

        if call_share > put_share:
            return WallType.CALL_WALL

        if put_share > call_share:
            return WallType.PUT_WALL

        return WallType.BALANCED