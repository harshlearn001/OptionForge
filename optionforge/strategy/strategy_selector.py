"""
============================================================
OptionForge
Strategy Selector
============================================================

Author      : OptionForge
Module      : strategy_selector.py
Purpose     : Select the optimal options strategy.

The StrategySelector delegates strategy selection to
StrategyRules and acts as the entry point for the
Strategy Engine.

============================================================
"""

from __future__ import annotations

from optionforge.decision.decision import Decision
from optionforge.decision.strategy_type import StrategyType

from optionforge.strategy.risk_profile import RiskProfile
from optionforge.strategy.strategy_rules import StrategyRules


class StrategySelector:
    """
    Institutional Strategy Selector.
    """

    def __init__(
        self,
        risk_profile: RiskProfile = RiskProfile.MODERATE,
    ) -> None:

        self._risk_profile = risk_profile

    # -----------------------------------------------------

    @property
    def risk_profile(self) -> RiskProfile:
        """
        Active risk profile.
        """

        return self._risk_profile

    # -----------------------------------------------------

    def select(
        self,
        decision: Decision,
    ) -> StrategyType:
        """
        Select the best strategy.
        """

        return StrategyRules.select(

            decision=decision,

            risk=self._risk_profile,

        )

    # -----------------------------------------------------

    def __call__(
        self,
        decision: Decision,
    ) -> StrategyType:
        """
        Callable interface.
        """

        return self.select(decision)

    # -----------------------------------------------------

    def __repr__(self) -> str:

        return (

            f"{self.__class__.__name__}("

            f"risk_profile={self._risk_profile.name})"

        )