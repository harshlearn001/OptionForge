"""
============================================================
OptionForge
intelligence/dealer_position.py
------------------------------------------------------------
Institutional Dealer Position Intelligence Engine
============================================================
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
    Institutional Dealer Position Engine.

    Combines Gamma, Delta, Vanna and Charm into a single
    institutional dealer positioning assessment.
    """

    @staticmethod
    def calculate(
        *,
        gamma: GammaExposureResult,
        delta: DeltaExposureResult,
        vanna: VannaExposureResult,
        charm: CharmExposureResult,
    ) -> DealerPositionResult:

        # ==================================================
        # Quantitative Metrics
        # ==================================================

        dealer_gamma = gamma.net_gex
        dealer_delta = delta.net_dex

        net_exposure = dealer_gamma + dealer_delta + vanna.net_vanna + charm.net_charm

        position_strength = abs(net_exposure)

        # ==================================================
        # Dealer Bias
        # ==================================================

        dealer_bias = "LONG GAMMA" if dealer_gamma >= 0 else "SHORT GAMMA"

        dealer_direction = "LONG DELTA" if dealer_delta >= 0 else "SHORT DELTA"

        # ==================================================
        # Market Stability
        # ==================================================

        stability_score = sum(
            [
                dealer_gamma >= 0,
                vanna.net_vanna >= 0,
                charm.net_charm >= 0,
            ]
        )

        if stability_score == 3:
            market_stability = "HIGH"

        elif stability_score == 2:
            market_stability = "MODERATE"

        else:
            market_stability = "LOW"

        # ==================================================
        # Market Condition
        # ==================================================

        market_condition = "RANGE-BOUND" if dealer_gamma >= 0 else "TRENDING"

        # ==================================================
        # Directional Risk
        # ==================================================

        if dealer_gamma < 0 and dealer_delta < 0:

            directional_risk = "VERY HIGH"

        elif dealer_gamma < 0:

            directional_risk = "HIGH"

        elif dealer_delta < 0:

            directional_risk = "MEDIUM"

        else:

            directional_risk = "LOW"

        # ==================================================
        # Institutional Score
        # ==================================================

        score = 100.0

        if dealer_gamma < 0:
            score -= 30

        if dealer_delta < 0:
            score -= 25

        if vanna.net_vanna < 0:
            score -= 15

        if charm.net_charm < 0:
            score -= 15

        score = max(0.0, min(100.0, score))

        confidence = score

        # ==================================================
        # Recommendation
        # ==================================================

        if directional_risk == "VERY HIGH":

            recommendation = (
                "Expect strong directional moves. " "Maintain strict risk management."
            )

        elif directional_risk == "HIGH":

            recommendation = "Directional volatility is elevated."

        elif directional_risk == "MEDIUM":

            recommendation = "Balanced environment with moderate risk."

        else:

            recommendation = "Dealer positioning favors market stability."

        # ==================================================
        # Interpretation
        # ==================================================

        interpretation = (
            f"{dealer_bias} | "
            f"{dealer_direction} | "
            f"{market_condition} | "
            f"Risk: {directional_risk}"
        )

        # ==================================================
        # Result
        # ==================================================

        return DealerPositionResult(
            dealer_position=float(net_exposure),
            dealer_delta=float(dealer_delta),
            dealer_gamma=float(dealer_gamma),
            net_exposure=float(net_exposure),
            position_strength=float(position_strength),
            institutional_score=float(score),
            dealer_bias=dealer_bias,
            dealer_direction=dealer_direction,
            market_condition=market_condition,
            market_stability=market_stability,
            directional_risk=directional_risk,
            confidence=float(confidence),
            recommendation=recommendation,
            interpretation=interpretation,
        )
