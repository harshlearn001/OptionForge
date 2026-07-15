"""
==============================================================
OptionForge
Build-up Classifier
--------------------------------------------------------------
Pure Open Interest Build-up Classification Engine.

This module classifies market positioning using
price change and open interest change.

No pandas.
No OptionChain.
No analytics.

Pure business rules only.
==============================================================
"""

from __future__ import annotations

from optionforge.common.enums import BuildUp


class BuildUpClassifier:
    """
    Pure Build-up classifier.

    Classification Matrix

        Price↑   OI↑  -> Long Build-up

        Price↓   OI↑  -> Short Build-up

        Price↑   OI↓  -> Short Covering

        Price↓   OI↓  -> Long Unwinding
    """

    @staticmethod
    def classify(
        price_change: float,
        oi_change: int,
    ) -> BuildUp:
        """
        Classify build-up from price and OI changes.
        """

        if price_change > 0 and oi_change > 0:
            return BuildUp.LONG_BUILDUP

        if price_change < 0 and oi_change > 0:
            return BuildUp.SHORT_BUILDUP

        if price_change > 0 and oi_change < 0:
            return BuildUp.SHORT_COVERING

        if price_change < 0 and oi_change < 0:
            return BuildUp.LONG_UNWINDING

        return BuildUp.NEUTRAL