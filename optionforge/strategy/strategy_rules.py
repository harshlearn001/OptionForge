"""
============================================================
OptionForge
Strategy Rules
============================================================

Author      : OptionForge
Module      : strategy_rules.py
Purpose     : Institutional strategy selection rules.

StrategyRules encapsulates all business logic for
mapping Decision + MarketDNA + RiskProfile into
StrategyType.

============================================================
"""

from __future__ import annotations

from optionforge.decision.decision import (
    Decision,
)
from optionforge.decision.decision_type import (
    DecisionType,
)

from optionforge.strategy.risk_profile import (
    RiskProfile,
)
from optionforge.strategy.strategy_type import (
    StrategyType,
)


class StrategyRules:
    """
    Institutional strategy rule set.
    """

    # =====================================================
    # Public API
    # =====================================================

    @staticmethod
    def select(
        decision: Decision,
        risk: RiskProfile,
    ) -> StrategyType:
        """
        Select the optimal institutional strategy.
        """

        dna = decision.market_dna

        # --------------------------------------------------
        # Strong Bullish
        # --------------------------------------------------

        if decision.decision is DecisionType.STRONG_BUY:

            if dna.is_low_volatility:

                if risk is RiskProfile.CONSERVATIVE:
                    return StrategyType.BULL_CALL_SPREAD

                if risk is RiskProfile.MODERATE:
                    return StrategyType.BULL_CALL_SPREAD

                if risk is RiskProfile.AGGRESSIVE:
                    return StrategyType.LONG_CALL

                return StrategyType.SYNTHETIC_LONG

            else:

                if risk.prefers_defined_risk:
                    return StrategyType.BULL_PUT_SPREAD

                return StrategyType.LONG_CALL

        # --------------------------------------------------
        # Bullish
        # --------------------------------------------------

        if decision.decision in (
            DecisionType.BUY,
            DecisionType.ACCUMULATE,
        ):

            if risk.prefers_defined_risk:

                return StrategyType.BULL_CALL_SPREAD

            return StrategyType.LONG_CALL

        # --------------------------------------------------
        # Strong Bearish
        # --------------------------------------------------

        if decision.decision is DecisionType.STRONG_SELL:

            if dna.is_high_volatility:

                if risk is RiskProfile.CONSERVATIVE:
                    return StrategyType.BEAR_PUT_SPREAD

                if risk is RiskProfile.MODERATE:
                    return StrategyType.BEAR_PUT_SPREAD

                if risk is RiskProfile.AGGRESSIVE:
                    return StrategyType.LONG_PUT

                return StrategyType.SYNTHETIC_SHORT

            else:

                if risk.prefers_defined_risk:
                    return StrategyType.BEAR_CALL_SPREAD

                return StrategyType.LONG_PUT

        # --------------------------------------------------
        # Bearish
        # --------------------------------------------------

        if decision.decision is DecisionType.SELL:

            if risk.prefers_defined_risk:

                return StrategyType.BEAR_PUT_SPREAD

            return StrategyType.LONG_PUT

        # --------------------------------------------------
        # Hold
        # --------------------------------------------------

        if decision.decision is DecisionType.HOLD:

            if dna.is_low_volatility:

                return StrategyType.IRON_CONDOR

            return StrategyType.CALENDAR_SPREAD

        # --------------------------------------------------
        # Hedge
        # --------------------------------------------------

        if decision.decision is DecisionType.HEDGE:

            if dna.is_high_volatility:

                return StrategyType.PROTECTIVE_PUT

            return StrategyType.COLLAR

        # --------------------------------------------------
        # Reduce
        # --------------------------------------------------

        if decision.decision is DecisionType.REDUCE:

            return StrategyType.COVERED_CALL

        # --------------------------------------------------
        # Exit
        # --------------------------------------------------

        if decision.decision is DecisionType.EXIT:

            return StrategyType.NO_POSITION

        # --------------------------------------------------
        # No Action
        # --------------------------------------------------

        if decision.decision is DecisionType.NO_ACTION:

            return StrategyType.CASH

        # --------------------------------------------------
        # Fallback
        # --------------------------------------------------

        return StrategyType.NO_POSITION
