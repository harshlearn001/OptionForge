"""
============================================================
OptionForge
Portfolio
============================================================

Author      : OptionForge
Module      : portfolio.py

Purpose
-------
Immutable institutional portfolio.

A Portfolio aggregates Positions and Allocations
into a single immutable portfolio snapshot.

============================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from typing import Any, Mapping

from optionforge.portfolio.allocation import (
    Allocation,
)
from optionforge.portfolio.portfolio_risk import (
    PortfolioRisk,
)
from optionforge.portfolio.portfolio_type import (
    PortfolioType,
)
from optionforge.portfolio.position import (
    Position,
)


@dataclass(
    frozen=True,
    slots=True,
)
class Portfolio:
    """
    Immutable institutional portfolio.
    """

    # -----------------------------------------------------
    # Identity
    # -----------------------------------------------------

    name: str

    portfolio_type: PortfolioType

    portfolio_risk: PortfolioRisk

    # -----------------------------------------------------
    # Holdings
    # -----------------------------------------------------

    positions: tuple[Position, ...] = ()

    allocations: tuple[Allocation, ...] = ()

    # -----------------------------------------------------
    # Capital
    # -----------------------------------------------------

    total_capital: float = 0.0

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

        if not self.name.strip():

            raise ValueError("name cannot be empty.")

        if self.total_capital < 0:

            raise ValueError("total_capital cannot be negative.")
        # -----------------------------------------------------

    # Holdings
    # -----------------------------------------------------

    @property
    def position_count(self) -> int:
        """
        Number of positions.
        """

        return len(
            self.positions,
        )

    @property
    def allocation_count(self) -> int:
        """
        Number of allocations.
        """

        return len(
            self.allocations,
        )

    # -----------------------------------------------------
    # Capital
    # -----------------------------------------------------

    @property
    def allocated_capital(self) -> float:
        """
        Total allocated capital.
        """

        return sum(allocation.allocated_capital for allocation in self.allocations)

    @property
    def available_capital(self) -> float:
        """
        Remaining capital.
        """

        return max(
            self.total_capital - self.allocated_capital,
            0.0,
        )

    @property
    def capital_utilization(self) -> float:
        """
        Portfolio capital utilization (%).
        """

        if self.total_capital == 0:

            return 0.0

        return (self.allocated_capital / self.total_capital) * 100.0

    # -----------------------------------------------------
    # Market Value
    # -----------------------------------------------------

    @property
    def market_value(self) -> float:
        """
        Current market value.
        """

        return sum(position.market_value for position in self.positions)

    # -----------------------------------------------------
    # Profit & Loss
    # -----------------------------------------------------

    @property
    def unrealized_pnl(self) -> float:
        """
        Portfolio unrealized P/L.
        """

        return sum(position.unrealized_pnl for position in self.positions)

    @property
    def realized_pnl(self) -> float:
        """
        Portfolio realized P/L.
        """

        return sum(position.realized_pnl for position in self.positions)

    @property
    def total_pnl(self) -> float:
        """
        Portfolio total P/L.
        """

        return self.unrealized_pnl + self.realized_pnl

    @property
    def return_percentage(self) -> float:
        """
        Portfolio return percentage.
        """

        if self.total_capital == 0:

            return 0.0

        return (self.total_pnl / self.total_capital) * 100.0

    @property
    def is_profitable(self) -> bool:
        """
        Returns True if profitable.
        """

        return self.total_pnl > 0

    @property
    def is_loss(self) -> bool:
        """
        Returns True if the portfolio is losing.
        """

        return self.total_pnl < 0

    @property
    def is_flat(self) -> bool:
        """
        Returns True if the portfolio has zero P/L.
        """

        return self.total_pnl == 0.0

    @property
    def is_fully_invested(self) -> bool:
        """
        Returns True if no capital remains.
        """

        return self.available_capital == 0.0

    @property
    def is_empty(self) -> bool:
        """
        Returns True if the portfolio contains
        no positions.
        """

        return self.position_count == 0

    # -----------------------------------------------------
    # Serialization
    # -----------------------------------------------------

    def to_dict(
        self,
    ) -> dict[str, Any]:

        return {
            "name": self.name,
            "portfolio_type": self.portfolio_type.name,
            "portfolio_risk": self.portfolio_risk.name,
            "positions": [position.to_dict() for position in self.positions],
            "allocations": [allocation.to_dict() for allocation in self.allocations],
            "position_count": self.position_count,
            "allocation_count": self.allocation_count,
            "total_capital": self.total_capital,
            "allocated_capital": self.allocated_capital,
            "available_capital": self.available_capital,
            "capital_utilization": self.capital_utilization,
            "market_value": self.market_value,
            "unrealized_pnl": self.unrealized_pnl,
            "realized_pnl": self.realized_pnl,
            "total_pnl": self.total_pnl,
            "return_percentage": self.return_percentage,
            "timestamp": self.timestamp.isoformat(),
            "metadata": dict(self.metadata),
        }

    # -----------------------------------------------------
    # Representation
    # -----------------------------------------------------

    def __str__(
        self,
    ) -> str:

        return f"Portfolio(" f"{self.name}, " f"{self.position_count} positions)"

    def __repr__(
        self,
    ) -> str:

        return (
            f"Portfolio("
            f"name={self.name!r}, "
            f"type={self.portfolio_type.name}, "
            f"risk={self.portfolio_risk.name}, "
            f"positions={self.position_count})"
        )
