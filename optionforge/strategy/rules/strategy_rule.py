"""
============================================================
OptionForge
Strategy Rule
============================================================

Author      : OptionForge
Module      : strategy_rule.py

Purpose
-------
Abstract base class for institutional strategy rules.

Every strategy rule must evaluate a Decision and
produce either a Strategy or None.

============================================================
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from optionforge.decision.decision import (
    Decision,
)

from optionforge.strategy.strategy import (
    Strategy,
)
from optionforge.strategy.strategy_builder import (
    StrategyBuilder,
)


class StrategyRule(ABC):
    """
    Base class for all institutional strategy rules.
    """

    @abstractmethod
    def evaluate(
        self,
        *,
        decision: Decision,
        builder: StrategyBuilder,
    ) -> Strategy | None:
        """
        Evaluate the supplied Decision.

        Parameters
        ----------
        decision
            Institutional trading decision.

        builder
            StrategyBuilder used to construct immutable
            Strategy objects.

        Returns
        -------
        Strategy | None
            A Strategy if the rule applies,
            otherwise None.
        """

        raise NotImplementedError