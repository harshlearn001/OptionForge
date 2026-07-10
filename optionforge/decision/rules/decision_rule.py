"""
============================================================
OptionForge
Decision Rule
============================================================

Author      : OptionForge
Module      : decision_rule.py

Purpose
-------
Abstract base class for all Decision rules.

Every institutional decision rule must inherit from
DecisionRule and implement evaluate().

Contains NO business logic.

============================================================
"""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from optionforge.decision.decision import (
    Decision,
)
from optionforge.decision.decision_builder import (
    DecisionBuilder,
)
from optionforge.marketdna.market_dna import (
    MarketDNA,
)


class DecisionRule(ABC):
    """
    Base class for all Decision rules.
    """

    @abstractmethod
    def evaluate(
        self,
        *,
        market_dna: MarketDNA,
        builder: DecisionBuilder,
    ) -> Decision | None:
        """
        Evaluate MarketDNA and return a Decision.

        Returns
        -------
        Decision
            Generated institutional trading decision.

        None
            When the rule chooses not to produce
            a decision.
        """
        raise NotImplementedError