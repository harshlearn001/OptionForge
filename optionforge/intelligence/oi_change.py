"""
==============================================================
OptionForge
intelligence/oi_change.py
--------------------------------------------------------------
OI Change Intelligence Engine
==============================================================
"""

from __future__ import annotations

from optionforge.models import OIChangeResult


class OIChange:
    """
    Open Interest Change Intelligence
    """

    @staticmethod
    def analyze(
        strike: float,
        option_type: str,
        price_change: float,
        oi_change: int,
    ) -> OIChangeResult:

        # -----------------------------------------
        # Classification
        # -----------------------------------------

        if price_change > 0 and oi_change > 0:

            classification = "LONG BUILD-UP"
            sentiment = "BULLISH"

        elif price_change < 0 and oi_change > 0:

            classification = "SHORT BUILD-UP"
            sentiment = "BEARISH"

        elif price_change > 0 and oi_change < 0:

            classification = "SHORT COVERING"
            sentiment = "BULLISH"

        elif price_change < 0 and oi_change < 0:

            classification = "LONG UNWINDING"
            sentiment = "BEARISH"

        else:

            classification = "NEUTRAL"
            sentiment = "NEUTRAL"

        # -----------------------------------------
        # Interpretation
        # -----------------------------------------

        if classification == "LONG BUILD-UP":

            interpretation = (
                "Price and Open Interest are increasing together, "
                "indicating fresh long positions."
            )

        elif classification == "SHORT BUILD-UP":

            interpretation = (
                "Price is falling while Open Interest is increasing, "
                "indicating fresh short positions."
            )

        elif classification == "SHORT COVERING":

            interpretation = (
                "Price is rising while Open Interest is decreasing, "
                "indicating short covering."
            )

        elif classification == "LONG UNWINDING":

            interpretation = (
                "Price and Open Interest are both decreasing, "
                "indicating long liquidation."
            )

        else:

            interpretation = "No significant build-up or unwinding detected."

        return OIChangeResult(
            strike=float(strike),
            option_type=option_type,
            price_change=float(price_change),
            oi_change=int(oi_change),
            classification=classification,
            sentiment=sentiment,
            interpretation=interpretation,
        )
