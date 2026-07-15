"""
==============================================================
OptionForge
Intelligence
Market Intelligence Engine
==============================================================

Interprets market analytics into an immutable
MarketIntelligence object.

Version : 1.0
Author  : OptionForge
==============================================================
"""

from __future__ import annotations

from optionforge.intelligence.enums.market_state import MarketState
from optionforge.intelligence.models.market_intelligence import (
    MarketIntelligence,
)

from optionforge.models import (
    MarketStructureResult,
    ProbabilityResult,
)


class MarketEngine:
    """
    Market Intelligence Engine.

    This engine DOES NOT calculate analytics.

    It interprets existing analytics and produces an
    institutional assessment of the current market regime.
    """

    HIGH_CONFIDENCE = 90.0
    MEDIUM_CONFIDENCE = 75.0
    LOW_CONFIDENCE = 60.0

    @classmethod
    def evaluate(
        cls,
        *,
        market_structure: MarketStructureResult,
        probability: ProbabilityResult,
    ) -> MarketIntelligence:

        evidence: list[str] = []
        risks: list[str] = []

        # -----------------------------------------------------
        # Evidence
        # -----------------------------------------------------

        evidence.append(f"Market Structure Score = {market_structure.score:.2f}")

        evidence.append(
            f"Bullish Probability = " f"{probability.bullish_probability:.2f}%"
        )

        evidence.append(f"Trade Quality = {probability.trade_quality}")

        score = market_structure.score

        # -----------------------------------------------------
        # Market State
        # -----------------------------------------------------

        if score >= 85:

            state = MarketState.BULLISH_TREND

            confidence = cls.HIGH_CONFIDENCE

            summary = "Market analytics strongly support a bullish trend."

            risks.append("Watch for resistance rejection.")

        elif score >= 70:

            state = MarketState.BREAKOUT

            confidence = cls.MEDIUM_CONFIDENCE

            summary = "Market is attempting a bullish breakout."

            risks.append("Breakout requires confirmation.")

        elif score >= 55:

            state = MarketState.RANGE_BOUND

            confidence = cls.LOW_CONFIDENCE

            summary = "Market remains range-bound with no dominant trend."

            risks.append("False breakouts are possible.")

        elif score >= 40:

            state = MarketState.TRANSITION

            confidence = cls.LOW_CONFIDENCE

            summary = "Market is transitioning toward a bearish regime."

            risks.append("Trend direction remains uncertain.")

        else:

            state = MarketState.BEARISH_TREND

            confidence = cls.HIGH_CONFIDENCE

            summary = "Market analytics strongly support a bearish trend."

            risks.append("Short covering rallies may occur.")

        return MarketIntelligence(
            state=state,
            confidence=confidence,
            evidence=tuple(evidence),
            risks=tuple(risks),
            summary=summary,
        )
