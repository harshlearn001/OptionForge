"""
============================================================
OptionForge
Intelligence Registry
============================================================

Author      : OptionForge
Module      : intelligence_registry.py

Purpose
-------
Immutable-style registry for Intelligence objects.

Responsibilities
----------------
- Store Intelligence objects
- Lookup by id
- Aggregate score
- Aggregate confidence
- Filter by IntelligenceType
============================================================
"""

from __future__ import annotations

from collections.abc import Iterator

from optionforge.intelligence.intelligence import Intelligence
from optionforge.intelligence.intelligence_type import IntelligenceType


class IntelligenceRegistry:
    """
    Registry of Intelligence objects.
    """

    def __init__(self) -> None:

        self._items: dict[str, Intelligence] = {}

    # -----------------------------------------------------
    # CRUD
    # -----------------------------------------------------

    def add(
        self,
        intelligence: Intelligence,
    ) -> None:

        self._items[intelligence.id] = intelligence

    def get(
        self,
        intelligence_id: str,
    ) -> Intelligence | None:

        return self._items.get(intelligence_id)

    def remove(
        self,
        intelligence_id: str,
    ) -> None:

        self._items.pop(intelligence_id, None)

    def exists(
        self,
        intelligence_id: str,
    ) -> bool:

        return intelligence_id in self._items

    def clear(
        self,
    ) -> None:

        self._items.clear()

    # -----------------------------------------------------
    # Filtering
    # -----------------------------------------------------

    def by_type(
        self,
        intelligence_type: IntelligenceType,
    ) -> list[Intelligence]:

        return [item for item in self._items.values() if item.type == intelligence_type]

    # -----------------------------------------------------
    # Aggregates
    # -----------------------------------------------------

    @property
    def score(
        self,
    ) -> float:

        if not self._items:

            return 0.0

        return sum(item.score for item in self._items.values()) / len(self._items)

    @property
    def confidence(
        self,
    ) -> float:

        if not self._items:

            return 0.0

        return sum(item.confidence for item in self._items.values()) / len(self._items)

    # -----------------------------------------------------
    # Collection
    # -----------------------------------------------------

    def __len__(
        self,
    ) -> int:

        return len(self._items)

    def __iter__(
        self,
    ) -> Iterator[Intelligence]:

        return iter(self._items.values())

    def __contains__(
        self,
        intelligence_id: str,
    ) -> bool:

        return intelligence_id in self._items

    # -----------------------------------------------------
    # Representation
    # -----------------------------------------------------

    def __repr__(
        self,
    ) -> str:

        return f"IntelligenceRegistry(" f"count={len(self)})"
