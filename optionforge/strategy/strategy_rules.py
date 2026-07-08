"""
============================================================
OptionForge
Strategy Rules
============================================================

Author      : OptionForge
Module      : strategy_rules.py
Purpose     : Institutional strategy selection rules.

StrategyRules encapsulates the mapping between
Decision, MarketDNA and RiskProfile.

============================================================
"""

from __future__ import annotations

from optionforge.decision.decision import Decision
from optionforge.decision.decision_type import DecisionType
from optionforge.decision.strategy_type import StrategyType
from optionforge.strategy.risk_profile import RiskProfile


class StrategyRules:
    """
    Institutional strategy rule set.
    """

    @staticmethod
    def select(
        decision: Decision,
        risk: RiskProfile,
    ) -> StrategyType:
        """
        Select the preferred strategy.
        """

        # --------------------------------------------------
        # Strong Bullish
        # --------------------------------------------------

        if decision.decision is DecisionType.STRONG_BUY:

            if risk is RiskProfile.CONSERVATIVE:
                return StrategyType.BULL_PUT_SPREAD

            if risk is RiskProfile.MODERATE:
                return StrategyType.BULL_CALL_SPREAD

            if risk is RiskProfile.AGGRESSIVE:
                return StrategyType.LONG_CALL

            return StrategyType.SYNTHETIC_LONG

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

            if risk is RiskProfile.CONSERVATIVE:
                return StrategyType.BEAR_CALL_SPREAD

            if risk is RiskProfile.MODERATE:
                return StrategyType.BEAR_PUT_SPREAD

            if risk is RiskProfile.AGGRESSIVE:
                return StrategyType.LONG_PUT

            return StrategyType.SYNTHETIC_SHORT

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

            return StrategyType.CASH

        # --------------------------------------------------
        # Hedge
        # --------------------------------------------------

        if decision.decision is DecisionType.HEDGE:

            return StrategyType.PROTECTIVE_PUT

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
        # Fallback
        # --------------------------------------------------

        return StrategyType.NO_POSITION