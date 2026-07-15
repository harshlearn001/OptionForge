"""
============================================================
OptionForge
Allocation
============================================================

Author      : OptionForge
Module      : allocation.py

Purpose
-------
Immutable institutional capital allocation.

Allocation represents how much capital from the
portfolio is assigned to a single Position.

============================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from typing import Any, Mapping

from optionforge.portfolio.position import (
    Position,
)


@dataclass(
    frozen=True,
    slots=True,
)
class Allocation:
    """
    Immutable capital allocation.
    """

    # -----------------------------------------------------
    # Position
    # -----------------------------------------------------

    position: Position

    # -----------------------------------------------------
    # Capital
    # -----------------------------------------------------

    allocated_capital: float

    available_capital: float

    portfolio_value: float

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
    # Validation
    # -----------------------------------------------------

    def __post_init__(self) -> None:

        if self.allocated_capital < 0:

            raise ValueError("allocated_capital cannot be negative.")

        if self.available_capital < 0:

            raise ValueError("available_capital cannot be negative.")

        if self.portfolio_value <= 0:

            raise ValueError("portfolio_value must be positive.")

        if self.allocated_capital > self.portfolio_value:

            raise ValueError("allocated_capital cannot exceed portfolio_value.")
        # -----------------------------------------------------

    # Convenience
    # -----------------------------------------------------

    @property
    def allocation_percentage(self) -> float:
        """
        Percentage of portfolio allocated
        to this position.
        """

        return (self.allocated_capital / self.portfolio_value) * 100.0

    @property
    def remaining_percentage(self) -> float:
        """
        Remaining portfolio percentage.
        """

        return (self.available_capital / self.portfolio_value) * 100.0

    @property
    def utilization_percentage(self) -> float:
        """
        Alias for allocation percentage.
        """

        return self.allocation_percentage

    @property
    def is_fully_allocated(self) -> bool:
        """
        Returns True if no capital remains.
        """

        return self.available_capital == 0.0

    @property
    def is_under_allocated(self) -> bool:
        """
        Returns True if capital remains available.
        """

        return self.available_capital > 0.0

    # -----------------------------------------------------
    # Serialization
    # -----------------------------------------------------

    def to_dict(
        self,
    ) -> dict[str, Any]:

        return {
            "position": self.position.to_dict(),
            "allocated_capital": self.allocated_capital,
            "available_capital": self.available_capital,
            "portfolio_value": self.portfolio_value,
            "allocation_percentage": (self.allocation_percentage),
            "remaining_percentage": (self.remaining_percentage),
            "utilization_percentage": (self.utilization_percentage),
            "timestamp": (self.timestamp.isoformat()),
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

        return f"Allocation(" f"{self.allocation_percentage:.2f}%)"

    def __repr__(
        self,
    ) -> str:

        return (
            f"Allocation("
            f"allocated={self.allocated_capital:.2f}, "
            f"available={self.available_capital:.2f})"
        )
