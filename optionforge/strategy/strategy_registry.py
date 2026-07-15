"""
============================================================
OptionForge
Strategy Registry
============================================================

Author      : OptionForge
Module      : strategy_registry.py

Purpose
-------
Immutable registry for institutional Strategy objects.

The StrategyRegistry stores completed Strategy
instances produced by the StrategyEngine.

Responsibilities
----------------
✓ Store strategies
✓ Retrieve strategies
✓ Iterate strategies
✓ Serialize registry

Contains NO business logic.

============================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterator

from optionforge.strategy.strategy import (
    Strategy,
)


@dataclass(
    frozen=True,
    slots=True,
)
class StrategyRegistry:
    """
    Immutable collection of Strategy objects.
    """

    strategies: tuple[Strategy, ...] = field(
        default_factory=tuple,
    )

    # =====================================================
    # Collection
    # =====================================================

    def __len__(
        self,
    ) -> int:

        return len(self.strategies)

    def __iter__(
        self,
    ) -> Iterator[Strategy]:

        return iter(
            self.strategies,
        )

    def __getitem__(
        self,
        index: int,
    ) -> Strategy:

        return self.strategies[index]

    # =====================================================
    # Convenience
    # =====================================================

    @property
    def empty(
        self,
    ) -> bool:

        return len(self) == 0

    @property
    def count(
        self,
    ) -> int:

        return len(self)

    @property
    def latest(
        self,
    ) -> Strategy | None:

        if self.empty:

            return None

        return self.strategies[-1]

    # =====================================================
    # Immutable Updates
    # =====================================================

    def add(
        self,
        strategy: Strategy,
    ) -> "StrategyRegistry":
        """
        Return a new registry with the strategy added.
        """

        return StrategyRegistry(
            strategies=(
                *self.strategies,
                strategy,
            )
        )

    def extend(
        self,
        strategies: tuple[Strategy, ...],
    ) -> "StrategyRegistry":
        """
        Return a new registry with multiple strategies.
        """

        return StrategyRegistry(
            strategies=(
                *self.strategies,
                *strategies,
            )
        )

    # =====================================================
    # Serialization
    # =====================================================

    def to_dict(
        self,
    ) -> dict:

        return {
            "count": self.count,
            "strategies": [strategy.to_dict() for strategy in self.strategies],
        }

    # =====================================================
    # Representation
    # =====================================================

    def __str__(
        self,
    ) -> str:

        return f"StrategyRegistry(" f"{self.count} strategies)"

    def __repr__(
        self,
    ) -> str:

        return f"StrategyRegistry(" f"count={self.count})"
