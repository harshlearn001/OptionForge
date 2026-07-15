"""
==============================================================
OptionForge
intelligence/dashboard.py
--------------------------------------------------------------
Institutional Dashboard Engine
==============================================================
"""

from __future__ import annotations

from optionforge.models import (
    DashboardResult,
    DealerPositionResult,
    GammaFlipResult,
    ZeroGammaResult,
    DealerHedgingFlowResult,
)


class Dashboard:
    """
    Professional Institutional Dashboard Engine.
    """

    @staticmethod
    def calculate(
        *,
        dealer: DealerPositionResult,
        gamma_flip: GammaFlipResult,
        zero_gamma: ZeroGammaResult,
        hedging: DealerHedgingFlowResult,
    ) -> DashboardResult:

        # --------------------------------------------------
        # Market Bias
        # --------------------------------------------------

        if dealer.dealer_bias == "LONG GAMMA":

            market_bias = "MEAN REVERTING"

        else:

            market_bias = "TREND FOLLOWING"

        # --------------------------------------------------
        # Risk
        # --------------------------------------------------

        score = dealer.institutional_score

        if score >= 80:

            risk = "LOW"

        elif score >= 60:

            risk = "MODERATE"

        elif score >= 40:

            risk = "HIGH"

        else:

            risk = "EXTREME"

        # --------------------------------------------------
        # Executive Summary
        # --------------------------------------------------

        summary = (
            f"{dealer.dealer_bias}, "
            f"{dealer.dealer_direction}, "
            f"{hedging.flow_direction}. "
            f"{hedging.volatility_effect.lower()}. "
            f"Market is {market_bias.lower()}."
        )

        return DashboardResult(
            dealer_bias=dealer.dealer_bias,
            dealer_direction=dealer.dealer_direction,
            gamma_status=gamma_flip.flip_status,
            zero_gamma_status=zero_gamma.status,
            hedging_flow=hedging.flow_direction,
            institutional_score=score,
            confidence=dealer.confidence,
            market_bias=market_bias,
            risk_level=risk,
            summary=summary,
        )
