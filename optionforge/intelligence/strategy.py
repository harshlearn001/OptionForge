"""
==============================================================
OptionForge
intelligence/strategy.py
--------------------------------------------------------------
Professional Strategy Intelligence Engine
==============================================================
"""

from __future__ import annotations

from optionforge.models import (
    ProbabilityResult,
    StrategyResult,
)


class Strategy:
    """
    Professional Strategy Engine
    """

    @staticmethod
    def calculate(

        probability: ProbabilityResult,

        spot_price: float,

        expected_move: float,

    ) -> StrategyResult:

        bull = probability.bullish_probability

        # =====================================================
        # Action
        # =====================================================

        if bull >= 80:

            action = "BUY"

        elif bull >= 60:

            action = "BUY ON DIP"

        elif bull >= 40:

            action = "WAIT"

        else:

            action = "SELL"

        # =====================================================
        # Entry
        # =====================================================

        lower_entry = spot_price - expected_move * 0.20

        upper_entry = spot_price

        entry_zone = (
            f"{lower_entry:.2f}"
            f" - "
            f"{upper_entry:.2f}"
        )

        # =====================================================
        # Stop Loss
        # =====================================================

        stop_loss = round(

            lower_entry - expected_move * 0.25,

            2,

        )

        # =====================================================
        # Targets
        # =====================================================

        target_1 = round(

            spot_price + expected_move * 0.50,

            2,

        )

        target_2 = round(

            spot_price + expected_move,

            2,

        )

        # =====================================================
        # Risk Reward
        # =====================================================

        risk = upper_entry - stop_loss

        reward = target_2 - upper_entry

        risk_reward = round(

            reward / risk,

            2,

        )

        # =====================================================
        # Recommendation
        # =====================================================

        if action == "BUY":

            recommendation = (
                "Momentum favors buyers. "
                "Buying dips is preferred."
            )

        elif action == "BUY ON DIP":

            recommendation = (
                "Wait for a pullback before entering."
            )

        elif action == "WAIT":

            recommendation = (
                "No high-quality setup currently."
            )

        else:

            recommendation = (
                "Avoid longs. "
                "Selling rallies is preferred."
            )

        interpretation = (

            f"Strategy generated using "

            f"{bull:.2f}% "

            f"bullish probability."

        )

        return StrategyResult(

            action=action,

            entry_zone=entry_zone,

            stop_loss=stop_loss,

            target_1=target_1,

            target_2=target_2,

            risk_reward=risk_reward,

            trade_quality=probability.trade_quality,

            confidence=probability.confidence,

            stars=probability.stars,

            recommendation=recommendation,

            interpretation=interpretation,

        )