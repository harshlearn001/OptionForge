"""
==============================================================
OptionForge
intelligence/institutional_signal.py
--------------------------------------------------------------
Institutional Signal Intelligence Engine
==============================================================
"""

from __future__ import annotations

from optionforge.models import (
    DashboardResult,
    InstitutionalSignalResult,
)


class InstitutionalSignal:
    """
    Professional Institutional Signal Engine.
    """

    @staticmethod
    def calculate(
        *,
        dashboard: DashboardResult,
    ) -> InstitutionalSignalResult:

        score = dashboard.institutional_score

        # --------------------------------------------------
        # Overall Signal
        # --------------------------------------------------

        if dashboard.market_bias == "TREND FOLLOWING":

            if score <= 20:

                overall_signal = "STRONG BEARISH"

                action = "SELL RALLIES"

            elif score <= 40:

                overall_signal = "BEARISH"

                action = "SELL STRENGTH"

            else:

                overall_signal = "NEUTRAL"

                action = "WAIT"

        else:

            if score >= 80:

                overall_signal = "STRONG BULLISH"

                action = "BUY DIPS"

            elif score >= 60:

                overall_signal = "BULLISH"

                action = "BUY WEAKNESS"

            else:

                overall_signal = "NEUTRAL"

                action = "WAIT"

        # --------------------------------------------------
        # Volatility Outlook
        # --------------------------------------------------

        if dashboard.risk_level in ("EXTREME", "HIGH"):

            volatility_outlook = "EXPANDING"

        else:

            volatility_outlook = "STABLE"

        # --------------------------------------------------
        # Dealer Regime
        # --------------------------------------------------

        dealer_regime = dashboard.dealer_bias

        # --------------------------------------------------
        # Confidence
        # --------------------------------------------------

        confidence = dashboard.confidence

        # --------------------------------------------------
        # Executive Summary
        # --------------------------------------------------

        summary = (
            f"{overall_signal}. "
            f"Market regime: {dashboard.market_bias.lower()}. "
            f"Dealer regime: {dealer_regime.lower()}. "
            f"Suggested action: {action.lower()}."
        )

        return InstitutionalSignalResult(

            overall_signal=overall_signal,

            signal_strength=score,

            market_regime=dashboard.market_bias,

            volatility_outlook=volatility_outlook,

            dealer_regime=dealer_regime,

            risk_level=dashboard.risk_level,

            confidence=confidence,

            action=action,

            summary=summary,
        )