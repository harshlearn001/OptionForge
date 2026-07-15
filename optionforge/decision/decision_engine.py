"""
============================================================
OptionForge
Decision Engine
============================================================

Author      : OptionForge
Module      : decision_engine.py

Purpose
-------
Executes DecisionRule objects and produces a
DecisionRegistry.

Responsibilities
----------------
✓ Execute all registered rules
✓ Build Decision objects
✓ Ignore None results
✓ Return immutable DecisionRegistry

Contains NO trading logic.

============================================================
"""

from __future__ import annotations

from collections.abc import Iterable

from optionforge.decision.decision_builder import (
    DecisionBuilder,
)
from optionforge.decision.decision_registry import (
    DecisionRegistry,
)
from optionforge.decision.rules.decision_rule import (
    DecisionRule,
)
from optionforge.marketdna.market_dna import (
    MarketDNA,
)


class DecisionEngine:
    """
    Executes institutional decision rules.
    """

    def __init__(
        self,
        rules: Iterable[DecisionRule],
    ) -> None:

        self._rules = tuple(rules)

        self._builder = DecisionBuilder()

    # -----------------------------------------------------

    def build(
        self,
        market_dna: MarketDNA,
    ) -> DecisionRegistry:

        registry = DecisionRegistry()

        for rule in self._rules:

            decision = rule.evaluate(
                market_dna=market_dna,
                builder=self._builder,
            )

            if decision is None:

                continue

            registry.add(decision)

        return registry

    # -----------------------------------------------------

    @property
    def rule_count(self) -> int:

        return len(self._rules)

    # -----------------------------------------------------

    def __len__(self) -> int:

        return len(self._rules)

    # -----------------------------------------------------

    def __repr__(self) -> str:

        return f"DecisionEngine(" f"{len(self)} rules)"
