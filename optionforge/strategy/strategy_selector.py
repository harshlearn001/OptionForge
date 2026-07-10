"""
============================================================
OptionForge
Strategy Selector
============================================================

Author      : OptionForge
Module      : strategy_selector.py
Purpose     : Select the optimal institutional options
              strategy.

The StrategySelector is the entry point into the
Strategy Rules subsystem.

It contains NO business logic.

============================================================
"""

from __future__ import annotations

from optionforge.decision.decision import (
    Decision,
)

from optionforge.strategy.risk_profile import (
    RiskProfile,
)
from optionforge.strategy.strategy_rules import (
    StrategyRules,
)
from optionforge.strategy.strategy_type import (
    StrategyType,
)


class StrategySelector:
    """
    Institutional Strategy Selector.

    Delegates all strategy selection to StrategyRules.
    """

    # =====================================================
    # Constructor
    # =====================================================

    def __init__(
        self,
        risk_profile: RiskProfile = RiskProfile.MODERATE,
    ) -> None:

        self._risk_profile = risk_profile

    # =====================================================
    # Properties
    # =====================================================

    @property
    def risk_profile(
        self,
    ) -> RiskProfile:
        """
        Active institutional risk profile.
        """

        return self._risk_profile

    # =====================================================
    # Public API
    # =====================================================

    def select(
        self,
        decision: Decision,
    ) -> StrategyType:
        """
        Select the optimal strategy.

        Strategy selection is fully delegated to
        StrategyRules.
        """

        return StrategyRules.select(

            decision=decision,

            risk=self._risk_profile,

        )

    # =====================================================
    # Callable Interface
    # =====================================================

    def __call__(
        self,
        decision: Decision,
    ) -> StrategyType:
        """
        Callable shortcut.

        Equivalent to:

            selector.select(decision)
        """

        return self.select(
            decision,
        )

    # =====================================================
    # Risk Profile
    # =====================================================

    def with_risk_profile(
        self,
        risk_profile: RiskProfile,
    ) -> "StrategySelector":
        """
        Return a new selector using a different
        institutional risk profile.
        """

        return StrategySelector(

            risk_profile=risk_profile,

        )

    # =====================================================
    # Representation
    # =====================================================

    def __repr__(
        self,
    ) -> str:

        return (

            f"{self.__class__.__name__}("

            f"risk_profile="

            f"{self._risk_profile.name})"

        )