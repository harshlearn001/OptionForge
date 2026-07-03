"""
==============================================================
OptionForge
intelligence/dealer_pressure.py
--------------------------------------------------------------
Dealer Pressure Intelligence Engine
==============================================================
"""

from __future__ import annotations

from optionforge.models import (
    DealerPositionResult,
    DealerHedgingFlowResult,
    InstitutionalSignalResult,
    DealerPressureResult,
)


class DealerPressure:
    """
    Professional Dealer Pressure Engine.
    """

    @staticmethod
    def calculate(
        *,
        dealer: DealerPositionResult,
        hedging: DealerHedgingFlowResult,
        signal: InstitutionalSignalResult,
    ) -> DealerPressureResult:

        # --------------------------------------------------
        # Pressure Score
        # --------------------------------------------------

        score = 0.0

        # Dealer Bias
        if dealer.dealer_bias == "SHORT GAMMA":
            score += 40.0

        # Dealer Direction
        if dealer.dealer_direction == "SHORT DELTA":
            score += 20.0

        # Hedging Flow
        if hedging.hedging_bias == "PRO-CYCLICAL":
            score += 20.0

        # Volatility
        if hedging.volatility_effect == "VOLATILITY EXPANSION":
            score += 10.0

        # Institutional Signal
        if signal.overall_signal == "STRONG BEARISH":
            score += 10.0

        score = min(score, 100.0)

        # --------------------------------------------------
        # Pressure Level
        # --------------------------------------------------

        if score >= 80:

            pressure_level = "EXTREME"

        elif score >= 60:

            pressure_level = "HIGH"

        elif score >= 40:

            pressure_level = "MODERATE"

        else:

            pressure_level = "LOW"

        # --------------------------------------------------
        # Direction
        # --------------------------------------------------

        if dealer.dealer_direction == "SHORT DELTA":

            pressure_direction = "DOWNSIDE"

        else:

            pressure_direction = "UPSIDE"

        # --------------------------------------------------
        # Volatility Bias
        # --------------------------------------------------

        if hedging.volatility_effect == "VOLATILITY EXPANSION":

            volatility_bias = "EXPANDING"

        else:

            volatility_bias = "STABLE"

        # --------------------------------------------------
        # Confidence
        # --------------------------------------------------

        confidence = signal.confidence

        # --------------------------------------------------
        # Interpretation
        # --------------------------------------------------

        interpretation = (
            f"{pressure_level} dealer pressure. "
            f"{pressure_direction.lower()} pressure with "
            f"{volatility_bias.lower()} volatility."
        )

        return DealerPressureResult(

            pressure_score=score,

            pressure_level=pressure_level,

            pressure_direction=pressure_direction,

            volatility_bias=volatility_bias,

            confidence=confidence,

            interpretation=interpretation,
        )