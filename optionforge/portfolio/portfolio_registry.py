"""
============================================================
OptionForge
Portfolio Registry
============================================================

Author      : OptionForge
Module      : portfolio_registry.py

Purpose
-------
Immutable registry for PortfolioResult objects.

The PortfolioRegistry stores completed PortfolioResult
instances produced by the PortfolioEngine.

Contains NO business logic.

============================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterator

from optionforge.portfolio.portfolio_result import (
    PortfolioResult,
)


@dataclass(
    frozen=True,
    slots=True,
)
class PortfolioRegistry:
    """
    Immutable collection of PortfolioResult objects.
    """

    results: tuple[PortfolioResult, ...] = field(
        default_factory=tuple,
    )

    # =====================================================
    # Collection
    # =====================================================

    def __len__(
        self,
    ) -> int:

        return len(
            self.results,
        )

    def __iter__(
        self,
    ) -> Iterator[PortfolioResult]:

        return iter(
            self.results,
        )

    def __getitem__(
        self,
        index: int,
    ) -> PortfolioResult:

        return self.results[index]

    # =====================================================
    # Convenience
    # =====================================================

    @property
    def empty(
        self,
    ) -> bool:

        return (
            len(
                self,
            )
            == 0
        )

    @property
    def count(
        self,
    ) -> int:

        return len(
            self,
        )

    @property
    def latest(
        self,
    ) -> PortfolioResult | None:

        if self.empty:

            return None

        return self.results[-1]
        # =====================================================

    # Immutable Updates
    # =====================================================

    def add(
        self,
        result: PortfolioResult,
    ) -> "PortfolioRegistry":
        """
        Return a new registry with one PortfolioResult
        added.
        """

        return PortfolioRegistry(
            results=(
                *self.results,
                result,
            ),
        )

    def extend(
        self,
        results: tuple[PortfolioResult, ...],
    ) -> "PortfolioRegistry":
        """
        Return a new registry with multiple
        PortfolioResult objects added.
        """

        return PortfolioRegistry(
            results=(
                *self.results,
                *results,
            ),
        )

    # =====================================================
    # Serialization
    # =====================================================

    def to_dict(
        self,
    ) -> dict:

        return {
            "count": self.count,
            "results": [result.to_dict() for result in self.results],
        }

    # =====================================================
    # Representation
    # =====================================================

    def __str__(
        self,
    ) -> str:

        return f"PortfolioRegistry(" f"{self.count} portfolios)"

    def __repr__(
        self,
    ) -> str:

        return f"PortfolioRegistry(" f"count={self.count})"
