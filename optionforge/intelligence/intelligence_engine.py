"""
============================================================
OptionForge
Intelligence Engine
============================================================

Author      : OptionForge
Module      : intelligence_engine.py

Purpose
-------
Transforms Knowledge into Institutional Intelligence.

The Intelligence Engine orchestrates Intelligence Rules.

Responsibilities
----------------
- Execute Intelligence Rules
- Collect Intelligence
- Build IntelligenceRegistry

Contains NO business logic.
============================================================
"""

from __future__ import annotations

from collections.abc import Iterable

from optionforge.intelligence.intelligence_builder import (
    IntelligenceBuilder,
)
from optionforge.intelligence.intelligence_registry import (
    IntelligenceRegistry,
)

from optionforge.knowledge.knowledge_registry import (
    KnowledgeRegistry,
)

from optionforge.intelligence.rules.intelligence_rule import (
    IntelligenceRule,
)


class IntelligenceEngine:
    """
    Orchestrates Intelligence Rules.
    """

    def __init__(
        self,
        *,
        rules: Iterable[IntelligenceRule] = (),
    ) -> None:

        self._rules = tuple(rules)

        self._builder = IntelligenceBuilder()

    # -----------------------------------------------------
    # Properties
    # -----------------------------------------------------

    @property
    def rules(
        self,
    ) -> tuple[IntelligenceRule, ...]:

        return self._rules

    # -----------------------------------------------------
    # Build
    # -----------------------------------------------------

    def build(
        self,
        registry: KnowledgeRegistry,
    ) -> IntelligenceRegistry:

        intelligence = IntelligenceRegistry()

        for rule in self._rules:

            result = rule.evaluate(

                knowledge=registry,

                builder=self._builder,

            )

            if result is not None:

                intelligence.add(result)

        return intelligence

    # -----------------------------------------------------
    # Collection
    # -----------------------------------------------------

    def __len__(
        self,
    ) -> int:

        return len(self._rules)

    def __iter__(
        self,
    ):

        return iter(self._rules)