"""
============================================================
OptionForge
Portfolio Result
============================================================

Author      : OptionForge
Module      : portfolio_result.py

Purpose
-------
Immutable result produced by the PortfolioEngine.

A PortfolioResult wraps the completed Portfolio and
provides metadata for downstream reporting,
analytics and execution systems.

============================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from typing import Any, Mapping

from optionforge.portfolio.portfolio import (
    Portfolio,
)


@dataclass(
    frozen=True,
    slots=True,
)
class PortfolioResult:
    """
    Final output of the Portfolio Engine.
    """

    # -----------------------------------------------------
    # Core
    # -----------------------------------------------------

    portfolio: Portfolio

    # -----------------------------------------------------
    # Metadata
    # -----------------------------------------------------

    timestamp: datetime = field(
        default_factory=lambda: datetime.now(UTC),
        compare=False,
    )

    metadata: Mapping[str, Any] = field(
        default_factory=dict,
        compare=False,
    )

    # -----------------------------------------------------
    # Convenience
    # -----------------------------------------------------

    @property
    def total_capital(self) -> float:
        """
        Portfolio capital.
        """

        return self.portfolio.total_capital

    @property
    def total_pnl(self) -> float:
        """
        Portfolio profit/loss.
        """

        return self.portfolio.total_pnl

    @property
    def return_percentage(self) -> float:
        """
        Portfolio return percentage.
        """

        return self.portfolio.return_percentage

    @property
    def position_count(self) -> int:
        """
        Number of positions.
        """

        return self.portfolio.position_count
    @property
    def allocation_count(self) -> int:
        """
        Number of allocations.
        """

        return self.portfolio.allocation_count

    @property
    def is_profitable(self) -> bool:
        """
        Returns True if the portfolio is profitable.
        """

        return self.portfolio.is_profitable

    @property
    def is_empty(self) -> bool:
        """
        Returns True if the portfolio contains
        no positions.
        """

        return self.portfolio.is_empty

    # -----------------------------------------------------
    # Serialization
    # -----------------------------------------------------

    def to_dict(
        self,
    ) -> dict[str, Any]:

        return {

            "portfolio": (

                self.portfolio.to_dict()

            ),

            "timestamp": (

                self.timestamp.isoformat()

            ),

            "metadata": dict(

                self.metadata,

            ),

        }

    # -----------------------------------------------------
    # Representation
    # -----------------------------------------------------

    def __str__(
        self,
    ) -> str:

        return (

            f"PortfolioResult("

            f"{self.portfolio.name}, "

            f"{self.return_percentage:.2f}%)"

        )

    def __repr__(
        self,
    ) -> str:

        return (

            f"PortfolioResult("

            f"portfolio={self.portfolio.name!r})"

        )