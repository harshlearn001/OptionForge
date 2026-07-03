"""
==============================================================
OptionForge
intelligence/dealer_hedging_flow.py
--------------------------------------------------------------
Dealer Hedging Flow Intelligence Engine
==============================================================
"""

from __future__ import annotations

from optionforge.models import (
    DealerHedgingFlowResult,
    DealerPositionResult,
    GammaFlipResult,
    ZeroGammaResult,
)


class DealerHedgingFlow:
    """
    Professional Dealer Hedging Flow Intelligence Engine.
    """

    @staticmethod
    def calculate(
        *,
        dealer: DealerPositionResult,
        gamma_flip: GammaFlipResult,
        zero_gamma: ZeroGammaResult,
    ) -> DealerHedgingFlowResult:

        # --------------------------------------------------
        # Hedging Bias
        # --------------------------------------------------

        if dealer.dealer_bias == "LONG GAMMA":

            hedging_bias = "CONTRARIAN"

        else:

            hedging_bias = "PRO-CYCLICAL"

        # --------------------------------------------------
        # Flow Direction
        # --------------------------------------------------

        if (
            dealer.dealer_bias == "SHORT GAMMA"
            and dealer.dealer_direction == "SHORT DELTA"
        ):

            flow_direction = "SELL FUTURES"

        elif (
            dealer.dealer_bias == "LONG GAMMA"
            and dealer.dealer_direction == "LONG DELTA"
        ):

            flow_direction = "BUY WEAKNESS"

        elif dealer.dealer_direction == "LONG DELTA":

            flow_direction = "BUY FUTURES"

        else:

            flow_direction = "SELL RALLIES"

        # --------------------------------------------------
        # Flow Strength
        # --------------------------------------------------

        score = dealer.institutional_score

        if score >= 80:

            flow_strength = "VERY STRONG"

        elif score >= 60:

            flow_strength = "STRONG"

        elif score >= 40:

            flow_strength = "MODERATE"

        else:

            flow_strength = "WEAK"

        # --------------------------------------------------
        # Volatility Effect
        # --------------------------------------------------

        if gamma_flip.dealer_regime == "NEGATIVE GAMMA":

            volatility_effect = "VOLATILITY EXPANSION"

        else:

            volatility_effect = "VOLATILITY SUPPRESSION"

        # --------------------------------------------------
        # Market Support
        # --------------------------------------------------

        if zero_gamma.dealer_regime == "STABLE":

            market_support = "SUPPORTED"

        else:

            market_support = "UNSUPPORTED"

        # --------------------------------------------------
        # Trend Effect
        # --------------------------------------------------

        if hedging_bias == "PRO-CYCLICAL":

            trend_effect = "TREND ACCELERATION"

        else:

            trend_effect = "MEAN REVERSION"

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

        if hedging_bias == "PRO-CYCLICAL":

            recommendation = (
                "Expect dealer hedging to reinforce market moves."
            )

        else:

            recommendation = (
                "Dealer hedging may dampen market volatility."
            )

        # --------------------------------------------------
        # Interpretation
        # --------------------------------------------------

        interpretation = (
            f"{flow_direction}. "
            f"{trend_effect.lower()}. "
            f"{volatility_effect.lower()}."
        )

        return DealerHedgingFlowResult(

            hedging_bias=hedging_bias,

            flow_direction=flow_direction,

            flow_strength=flow_strength,

            volatility_effect=volatility_effect,

            market_support=market_support,

            trend_effect=trend_effect,

            institutional_score=score,

            confidence=confidence,

            recommendation=recommendation,

            interpretation=interpretation,

        )