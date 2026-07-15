"""
============================================================
OptionForge
Position
============================================================

Author      : OptionForge
Module      : position.py

Purpose
-------
Immutable institutional portfolio position.

A Position represents an executed strategy allocated
within a portfolio.

============================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from typing import Any, Mapping

from optionforge.strategy.strategy_result import (
    StrategyResult,
)


@dataclass(
    frozen=True,
    slots=True,
)
class Position:
    """
    Immutable institutional portfolio position.
    """

    # -----------------------------------------------------
    # Identity
    # -----------------------------------------------------

    symbol: str

    strategy_result: StrategyResult

    # -----------------------------------------------------
    # Quantity
    # -----------------------------------------------------

    lots: int

    quantity: int

    # -----------------------------------------------------
    # Pricing
    # -----------------------------------------------------

    entry_price: float

    current_price: float

    # -----------------------------------------------------
    # Capital
    # -----------------------------------------------------

    capital_used: float

    # -----------------------------------------------------
    # Profit / Loss
    # -----------------------------------------------------

    unrealized_pnl: float = 0.0

    realized_pnl: float = 0.0

    # -----------------------------------------------------
    # Metadata
    # -----------------------------------------------------

    opened_at: datetime = field(
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

        if not self.symbol.strip():

            raise ValueError("symbol cannot be empty.")

        if self.lots <= 0:

            raise ValueError("lots must be positive.")

        if self.quantity <= 0:

            raise ValueError("quantity must be positive.")

        if self.entry_price < 0:

            raise ValueError("entry_price cannot be negative.")

        if self.current_price < 0:

            raise ValueError("current_price cannot be negative.")

        if self.capital_used < 0:

            raise ValueError("capital_used cannot be negative.")
        # -----------------------------------------------------

    # Convenience
    # -----------------------------------------------------

    @property
    def market_value(self) -> float:
        """
        Current market value of the position.
        """

        return self.current_price * self.quantity

    @property
    def total_pnl(self) -> float:
        """
        Total profit/loss.
        """

        return self.realized_pnl + self.unrealized_pnl

    @property
    def return_percentage(self) -> float:
        """
        Return percentage based on capital used.
        """

        if self.capital_used == 0:

            return 0.0

        return (self.total_pnl / self.capital_used) * 100.0

    @property
    def is_profitable(self) -> bool:
        """
        Returns True if position is profitable.
        """

        return self.total_pnl > 0

    @property
    def is_loss(self) -> bool:
        """
        Returns True if position is losing.
        """

        return self.total_pnl < 0

    @property
    def is_flat(self) -> bool:
        """
        Returns True if position has no P/L.
        """

        return self.total_pnl == 0

    # -----------------------------------------------------
    # Serialization
    # -----------------------------------------------------

    def to_dict(
        self,
    ) -> dict[str, Any]:

        return {
            "symbol": self.symbol,
            "strategy_result": (self.strategy_result.to_dict()),
            "lots": self.lots,
            "quantity": self.quantity,
            "entry_price": self.entry_price,
            "current_price": self.current_price,
            "capital_used": self.capital_used,
            "market_value": self.market_value,
            "unrealized_pnl": self.unrealized_pnl,
            "realized_pnl": self.realized_pnl,
            "total_pnl": self.total_pnl,
            "return_percentage": (self.return_percentage),
            "opened_at": (self.opened_at.isoformat()),
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

        return f"Position(" f"{self.symbol}, " f"{self.total_pnl:.2f})"

    def __repr__(
        self,
    ) -> str:

        return (
            f"Position("
            f"symbol={self.symbol}, "
            f"lots={self.lots}, "
            f"quantity={self.quantity})"
        )
