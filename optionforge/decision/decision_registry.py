"""
============================================================
OptionForge
Decision Registry
============================================================

Author      : OptionForge
Module      : decision_registry.py

Purpose
-------
Stores immutable Decision objects.

Responsibilities
----------------
✓ Add decisions
✓ Retrieve decisions
✓ Query by decision type
✓ Return best decision
✓ Aggregate confidence

============================================================
"""

from __future__ import annotations

from collections.abc import Iterator

from optionforge.decision.decision import Decision
from optionforge.decision.decision_type import DecisionType


class DecisionRegistry:
    """
    Repository of Decision objects.
    """

    def __init__(self) -> None:

        self._items: dict[str, Decision] = {}

    # -----------------------------------------------------
    # Collection
    # -----------------------------------------------------

    def add(
        self,
        decision: Decision,
    ) -> None:

        self._items[decision.decision.name] = decision

    def get(
        self,
        name: str,
    ) -> Decision | None:

        return self._items.get(name)

    def exists(
        self,
        name: str,
    ) -> bool:

        return name in self._items

    def clear(self) -> None:

        self._items.clear()

    # -----------------------------------------------------
    # Queries
    # -----------------------------------------------------

    def by_type(
        self,
        decision_type: DecisionType,
    ) -> Decision | None:

        return self._items.get(decision_type.name)

    @property
    def best(self) -> Decision | None:

        if not self._items:

            return None

        return max(
            self._items.values(),
            key=lambda x: x.confidence,
        )

    @property
    def confidence(self) -> float:

        if not self._items:

            return 0.0

        return max(x.confidence for x in self._items.values())

    @property
    def average_confidence(self) -> float:

        if not self._items:

            return 0.0

        return sum(x.confidence for x in self._items.values()) / len(self._items)

    # -----------------------------------------------------
    # Python Protocol
    # -----------------------------------------------------

    def __len__(self) -> int:

        return len(self._items)

    def __iter__(
        self,
    ) -> Iterator[Decision]:

        return iter(self._items.values())

    def __contains__(
        self,
        item: str,
    ) -> bool:

        return item in self._items

    # -----------------------------------------------------
    # Serialization
    # -----------------------------------------------------

    def to_dict(self) -> list[dict]:

        return [d.to_dict() for d in self]

    # -----------------------------------------------------

    def __repr__(self) -> str:

        return f"DecisionRegistry(" f"{len(self)} decisions)"
