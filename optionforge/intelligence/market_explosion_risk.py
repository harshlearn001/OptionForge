"""
==============================================================
OptionForge
intelligence/market_explosion_risk.py
--------------------------------------------------------------
Market Explosion Risk Intelligence Engine
==============================================================
"""

from __future__ import annotations

from optionforge.models import (
    DealerPressureResult,
    InstitutionalSignalResult,
    DealerHedgingFlowResult,
    DealerPositionResult,
    MarketExplosionRiskResult,
)


class MarketExplosionRisk:
    """
    Professional Market Explosion Risk Engine.
    """

    @staticmethod
    def calculate(
        *,
        pressure: DealerPressureResult,
        signal: InstitutionalSignalResult,
        hedging: DealerHedgingFlowResult,
        dealer: DealerPositionResult,
    ) -> MarketExplosionRiskResult:

        # --------------------------------------------------
        # Explosion Score
        # --------------------------------------------------

        score = pressure.pressure_score

        if signal.overall_signal == "STRONG BEARISH":
            score += 10

        if hedging.volatility_effect == "VOLATILITY EXPANSION":
            score += 10

        if dealer.directional_risk == "VERY HIGH":
            score += 10

        score = min(score, 100.0)

        # --------------------------------------------------
        # Probability
        # --------------------------------------------------

        if score >= 90:

            probability = "VERY HIGH"

        elif score >= 75:

            probability = "HIGH"

        elif score >= 55:

            probability = "MODERATE"

        else:

            probability = "LOW"

        # --------------------------------------------------
        # Market State
        # --------------------------------------------------

        if score >= 90:

            market_state = "CRITICAL"

        elif score >= 70:

            market_state = "UNSTABLE"

        else:

            market_state = "STABLE"

        # --------------------------------------------------
        # Expected Behaviour
        # --------------------------------------------------

        if probability == "VERY HIGH":

            behavior = "LARGE TREND EXPANSION"

        elif probability == "HIGH":

            behavior = "TREND ACCELERATION"

        elif probability == "MODERATE":

            behavior = "VOLATILE"

        else:

            behavior = "NORMAL"

        # --------------------------------------------------
        # Recommendation
        # --------------------------------------------------

        if probability == "VERY HIGH":

            recommendation = (
                "Reduce leverage. " "Prepare for sharp directional movement."
            )

        elif probability == "HIGH":

            recommendation = "Expect increased volatility."

        elif probability == "MODERATE":

            recommendation = "Maintain disciplined risk management."

        else:

            recommendation = "Normal market conditions."

        # --------------------------------------------------
        # Confidence
        # --------------------------------------------------

        confidence = pressure.confidence

        # --------------------------------------------------
        # Interpretation
        # --------------------------------------------------

        interpretation = (
            f"{probability} explosion risk. "
            f"Market appears {market_state.lower()} with "
            f"{behavior.lower()} expected."
        )

        return MarketExplosionRiskResult(
            explosion_score=score,
            explosion_probability=probability,
            market_state=market_state,
            expected_behavior=behavior,
            recommendation=recommendation,
            confidence=confidence,
            interpretation=interpretation,
        )
