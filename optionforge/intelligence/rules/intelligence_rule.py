"""
============================================================
OptionForge
Intelligence Rule Contract
============================================================

Author      : OptionForge
Module      : intelligence_rule.py

Purpose
-------
Defines the abstract contract for all Intelligence
Rules.

Intelligence Rules transform Knowledge into
Institutional Intelligence.

Responsibilities
----------------
- Evaluate Knowledge
- Produce Intelligence
- Return None when the rule does not apply

Contains NO business logic.
============================================================
"""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from optionforge.intelligence.intelligence import Intelligence
from optionforge.intelligence.intelligence_builder import (
    IntelligenceBuilder,
)
from optionforge.knowledge.knowledge_registry import (
    KnowledgeRegistry,
)


class IntelligenceRule(ABC):
    """
    Base contract for all Intelligence Rules.
    """

    @abstractmethod
    def evaluate(
        self,
        *,
        knowledge: KnowledgeRegistry,
        builder: IntelligenceBuilder,
    ) -> Intelligence | None:
        """
        Evaluate Knowledge and produce one
        Intelligence object.

        Returns
        -------
        Intelligence | None
            Institutional intelligence if the rule
            applies, otherwise None.
        """