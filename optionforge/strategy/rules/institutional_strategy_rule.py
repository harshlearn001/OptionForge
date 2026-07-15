"""
============================================================
OptionForge
Institutional Strategy Rule
============================================================

Author      : OptionForge
Module      : institutional_strategy_rule.py

Purpose
-------
Produces the primary institutional options strategy
from a Decision.

This rule contains the top-level institutional strategy
selection logic and delegates object construction to the
StrategyBuilder.

============================================================
"""

from __future__ import annotations

from optionforge.decision.decision import (
    Decision,
)

from optionforge.strategy.strategy import (
    Strategy,
)
from optionforge.strategy.strategy_builder import (
    StrategyBuilder,
)
from optionforge.strategy.rules.strategy_rule import (
    StrategyRule,
)


class InstitutionalStrategyRule(StrategyRule):
    """
    Primary institutional strategy rule.
    """

    # =====================================================
    # Public API
    # =====================================================

    def evaluate(
        self,
        *,
        decision: Decision,
        builder: StrategyBuilder,
    ) -> Strategy | None:
        """
        Produce the institutional strategy.

        Parameters
        ----------
        decision
            Institutional Decision.

        builder
            StrategyBuilder responsible for creating
            immutable Strategy objects.

        Returns
        -------
        Strategy
        """

        return builder.build(
            decision,
        )

    # =====================================================
    # Representation
    # =====================================================

    def __repr__(
        self,
    ) -> str:

        return f"{self.__class__.__name__}()"
