"""
==============================================================
OptionForge
intelligence/dealer_position.py
--------------------------------------------------------------
Dealer Positioning Intelligence Engine
==============================================================
"""

from __future__ import annotations

from optionforge.models import (
    CharmExposureResult,
    DealerPositionResult,
    DeltaExposureResult,
    GammaExposureResult,
    VannaExposureResult,
)


class DealerPosition:
    """
    Combines all dealer exposure engines into one
    institutional positioning assessment.
    """

    @staticmethod
    def calculate(
        *,
        gamma: GammaExposureResult,
        delta: DeltaExposureResult,
        vanna: VannaExposureResult,
        charm: CharmExposureResult,
    ) -> DealerPositionResult:

        # --------------------------------------------------
        # Dealer Bias (Gamma)
        # --------------------------------------------------

        if gamma.net_gex >= 0:
            dealer_bias = "LONG GAMMA"
        else:
            dealer_bias = "SHORT GAMMA"

        # --------------------------------------------------
        # Dealer Direction (Delta)
        # --------------------------------------------------

        if delta.net_dex >= 0:
            dealer_direction = "LONG DELTA"
        else:
            dealer_direction = "SHORT DELTA"

        # --------------------------------------------------
        # Market Stability
        # --------------------------------------------------

        stability_score = 0

        if gamma.net_gex >= 0:
            stability_score += 1

        if vanna.net_vanna >= 0:
            stability_score += 1

        if charm.net_charm >= 0:
            stability_score += 1

        if stability_score == 3:

            market_stability = "HIGH"

        elif stability_score == 2:

            market_stability = "MODERATE"

        else:

            market_stability = "LOW"

        # --------------------------------------------------
        # Market Condition
        # --------------------------------------------------

        if dealer_bias == "LONG GAMMA":

            market_condition = "RANGE-BOUND"

        else:

            market_condition = "TRENDING"

        # --------------------------------------------------
        # Directional Risk
        # --------------------------------------------------

        if (
            dealer_bias == "SHORT GAMMA"
            and dealer_direction == "SHORT DELTA"
        ):

            directional_risk = "VERY HIGH"

        elif dealer_bias == "SHORT GAMMA":

            directional_risk = "HIGH"

        elif dealer_direction == "SHORT DELTA":

            directional_risk = "MEDIUM"

        else:

            directional_risk = "LOW"

        # --------------------------------------------------
        # Institutional Score
        # --------------------------------------------------

        score = 100.0

        if dealer_bias == "SHORT GAMMA":
            score -= 30

        if dealer_direction == "SHORT DELTA":
            score -= 25

        if vanna.net_vanna < 0:
            score -= 15

        if charm.net_charm < 0:
            score -= 15

        score = max(0.0, min(100.0, score))

        # --------------------------------------------------
        # Confidence
        # --------------------------------------------------

        if score >= 85:
            confidence = "★★★★★"

        elif score >= 70:
            confidence = "★★★★☆"

        elif score >= 55:
            confidence = "★★★☆☆"

        elif score >= 40:
            confidence = "★★☆☆☆"

        else:
            confidence = "★☆☆☆☆"

        # --------------------------------------------------
        # Recommendation
        # --------------------------------------------------

        if directional_risk == "VERY HIGH":

            recommendation = (
                "Expect strong directional moves. "
                "Risk management is essential."
            )

        elif directional_risk == "HIGH":

            recommendation = (
                "Directional moves may accelerate."
            )

        elif directional_risk == "MEDIUM":

            recommendation = (
                "Balanced market with moderate risk."
            )

        else:

            recommendation = (
                "Dealer positioning favors market stability."
            )

        # --------------------------------------------------
        # Interpretation
        # --------------------------------------------------

        interpretation = (
            f"{dealer_bias} / {dealer_direction}. "
            f"Market appears {market_condition.lower()} "
            f"with {directional_risk.lower()} directional risk."
        )

        return DealerPositionResult(

            dealer_bias=dealer_bias,

            dealer_direction=dealer_direction,

            market_condition=market_condition,

            market_stability=market_stability,

            directional_risk=directional_risk,

            institutional_score=score,

            confidence=confidence,

            recommendation=recommendation,

            interpretation=interpretation,
        )