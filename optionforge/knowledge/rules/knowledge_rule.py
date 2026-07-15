"""
============================================================
OptionForge
Knowledge Rule Contract
============================================================

Author      : OptionForge
Module      : knowledge_rule.py

Purpose
-------
Defines the abstract contract for all Knowledge Rules.

Knowledge Rules transform Evidence into immutable
Knowledge objects.

Responsibilities
----------------
- Evaluate Evidence
- Produce Knowledge
- Return None when the rule does not apply

Knowledge Rules contain business reasoning.

They do NOT:
- calculate analytics
- modify registries
- execute strategies
============================================================
"""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from optionforge.evidence.evidence_registry import EvidenceRegistry

from optionforge.knowledge.knowledge import Knowledge
from optionforge.knowledge.knowledge_builder import KnowledgeBuilder


class KnowledgeRule(ABC):
    """
    Abstract base class for all Knowledge Rules.
    """

    @abstractmethod
    def evaluate(
        self,
        *,
        evidence: EvidenceRegistry,
        builder: KnowledgeBuilder,
    ) -> Knowledge | None:
        """
        Evaluate evidence.

        Returns
        -------
        Knowledge | None
            Returns a Knowledge object when the rule
            applies; otherwise returns None.
        """
