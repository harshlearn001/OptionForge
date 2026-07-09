"""
============================================================
OptionForge
Knowledge Registry
============================================================

Author      : OptionForge
Module      : knowledge_registry.py

Purpose
-------
Stores immutable Knowledge objects produced by the
Knowledge Framework.

The registry provides efficient lookup, iteration,
aggregation and querying.

Responsibilities
----------------
- Store Knowledge objects
- Lookup by ID
- Query by KnowledgeType
- Aggregate score
- Aggregate confidence

This registry contains NO reasoning logic.
============================================================
"""

from __future__ import annotations

from collections.abc import Iterator

from optionforge.knowledge.knowledge import Knowledge
from optionforge.knowledge.knowledge_type import KnowledgeType


class KnowledgeRegistry:
    """
    Registry of Knowledge objects.
    """

    def __init__(self) -> None:

        self._registry: dict[str, Knowledge] = {}

    # =====================================================
    # CRUD
    # =====================================================

    def add(
        self,
        knowledge: Knowledge,
    ) -> None:
        """
        Add Knowledge.
        """

        self._registry[knowledge.id] = knowledge

    def remove(
        self,
        knowledge_id: str,
    ) -> None:
        """
        Remove Knowledge.
        """

        self._registry.pop(knowledge_id, None)

    def clear(self) -> None:
        """
        Remove everything.
        """

        self._registry.clear()

    # =====================================================
    # Lookup
    # =====================================================

    def get(
        self,
        knowledge_id: str,
    ) -> Knowledge | None:
        """
        Lookup by ID.
        """

        return self._registry.get(knowledge_id)

    def exists(
        self,
        knowledge_id: str,
    ) -> bool:
        """
        Returns True if Knowledge exists.
        """

        return knowledge_id in self._registry

    # =====================================================
    # Query
    # =====================================================

    def by_type(
        self,
        knowledge_type: KnowledgeType,
    ) -> list[Knowledge]:
        """
        Return all Knowledge of one type.
        """

        return [

            knowledge

            for knowledge in self

            if knowledge.type == knowledge_type

        ]

    # =====================================================
    # Aggregation
    # =====================================================

    @property
    def score(self) -> float:
        """
        Average knowledge score.
        """

        if not self._registry:

            return 0.0

        return sum(

            knowledge.score

            for knowledge in self

        ) / len(self)

    @property
    def confidence(self) -> float:
        """
        Average confidence.
        """

        if not self._registry:

            return 0.0

        return sum(

            knowledge.confidence

            for knowledge in self

        ) / len(self)

    # =====================================================
    # Serialization
    # =====================================================

    def to_dict(self) -> list[dict]:
        """
        Serialize registry.
        """

        return [

            knowledge.to_dict()

            for knowledge in self

        ]

    # =====================================================
    # Dunder
    # =====================================================

    def __len__(self) -> int:

        return len(self._registry)

    def __iter__(self) -> Iterator[Knowledge]:

        return iter(

            self._registry.values()

        )

    def __contains__(
        self,
        knowledge_id: str,
    ) -> bool:

        return knowledge_id in self._registry

    def __repr__(self) -> str:

        return (

            f"KnowledgeRegistry("

            f"{len(self)} knowledge)"

        )