"""
============================================================
OptionForge
Knowledge Engine
============================================================

Author      : OptionForge
Module      : knowledge_engine.py

Purpose
-------
Transforms Evidence into institutional Knowledge.

The engine orchestrates Knowledge generation by
executing registered Knowledge Rules.

Responsibilities
----------------
- Iterate over Knowledge Rules
- Execute Rules
- Build immutable Knowledge objects
- Return KnowledgeRegistry

The engine contains NO business logic.

Business reasoning belongs exclusively to
Knowledge Rules.
============================================================
"""

from __future__ import annotations

from collections.abc import Iterable

from optionforge.evidence.evidence_registry import EvidenceRegistry

from optionforge.knowledge.knowledge_builder import KnowledgeBuilder
from optionforge.knowledge.knowledge_registry import KnowledgeRegistry


class KnowledgeEngine:
    """
    Orchestrates Knowledge generation.
    """

    def __init__(
        self,
        rules: Iterable | None = None,
        builder: KnowledgeBuilder | None = None,
    ) -> None:

        self._rules = list(rules or [])

        self._builder = builder or KnowledgeBuilder()

    # =====================================================
    # Build Knowledge
    # =====================================================

    def build(
        self,
        evidence: EvidenceRegistry,
    ) -> KnowledgeRegistry:
        """
        Build a KnowledgeRegistry from Evidence.
        """

        registry = KnowledgeRegistry()

        for rule in self._rules:

            knowledge = rule.evaluate(

                evidence=evidence,

                builder=self._builder,

            )

            if knowledge is not None:

                registry.add(knowledge)

        return registry

    # =====================================================
    # Rule Management
    # =====================================================

    def register(
        self,
        rule,
    ) -> None:
        """
        Register a Knowledge Rule.
        """

        self._rules.append(rule)

    @property
    def rules(self):

        """
        Registered rules.
        """

        return tuple(self._rules)

    # =====================================================
    # Dunder
    # =====================================================

    def __len__(self) -> int:

        return len(self._rules)

    def __repr__(self) -> str:

        return (

            f"KnowledgeEngine("

            f"rules={len(self)})"

        )