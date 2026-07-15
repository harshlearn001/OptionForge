"""
==============================================================
OptionForge
intelligence/probability.py
--------------------------------------------------------------
Probability Intelligence Engine
==============================================================
"""

from __future__ import annotations

from optionforge.models import (
    MarketStructureResult,
    ProbabilityResult,
)


class Probability:
    """
    Professional Probability Engine
    """

    @staticmethod
    def calculate(
        market: MarketStructureResult,
    ) -> ProbabilityResult:

        score = market.score

        # ----------------------------------------
        # Bull / Bear Probability
        # ----------------------------------------

        bullish_probability = round(score, 2)
        bearish_probability = round(100 - score, 2)

        # ----------------------------------------
        # Confidence
        # ----------------------------------------

        confidence = market.confidence
        stars = market.stars

        # ----------------------------------------
        # Trade Quality
        # ----------------------------------------

        if score >= 90:
            trade_quality = "A+"

        elif score >= 80:
            trade_quality = "A"

        elif score >= 70:
            trade_quality = "B"

        elif score >= 60:
            trade_quality = "C"

        else:
            trade_quality = "D"

        # ----------------------------------------
        # Risk
        # ----------------------------------------

        if score >= 85:
            risk_level = "LOW"

        elif score >= 70:
            risk_level = "MEDIUM"

        else:
            risk_level = "HIGH"

        # ----------------------------------------
        # Recommendation
        # ----------------------------------------

        if bullish_probability >= 80:

            recommendation = "Bullish setup with favorable probability."

        elif bullish_probability >= 60:

            recommendation = "Moderately bullish. Confirmation is advised."

        elif bullish_probability >= 40:

            recommendation = "Balanced market. Wait for stronger signals."

        else:

            recommendation = "Bearish setup. Avoid aggressive long positions."

        interpretation = f"Bullish probability is " f"{bullish_probability:.2f}%."

        return ProbabilityResult(
            bullish_probability=bullish_probability,
            bearish_probability=bearish_probability,
            confidence=confidence,
            stars=stars,
            trade_quality=trade_quality,
            risk_level=risk_level,
            recommendation=recommendation,
            interpretation=interpretation,
        )
