"""
============================================================
OptionForge
Execution Result
============================================================

Author      : OptionForge
Module      : execution_result.py

Purpose
-------
Immutable result produced by the Execution Engine.

ExecutionResult aggregates completed trades and
provides portfolio-level execution statistics.

============================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Mapping

from optionforge.execution.trade import Trade


@dataclass(
    frozen=True,
    slots=True,
)
class ExecutionResult:
    """
    Immutable execution result.
    """

    # -----------------------------------------------------
    # Trades
    # -----------------------------------------------------

    trades: tuple[Trade, ...] = ()

    # -----------------------------------------------------
    # Metadata
    # -----------------------------------------------------

    metadata: Mapping[str, Any] = field(
        default_factory=dict,
        compare=False,
    )

    # -----------------------------------------------------
    # Convenience
    # -----------------------------------------------------

    @property
    def trade_count(self) -> int:
        """
        Number of executed trades.
        """

        return len(self.trades)

    @property
    def total_quantity(self) -> int:
        """
        Total executed quantity.
        """

        return sum(trade.total_quantity for trade in self.trades)

    @property
    def total_notional(self) -> float:
        """
        Total traded value.
        """

        return sum(trade.notional_value for trade in self.trades)

    @property
    def average_execution_price(self) -> float:
        """
        Quantity-weighted average execution price.
        """

        if self.total_quantity == 0:

            return 0.0

        return self.total_notional / self.total_quantity

    @property
    def complete_trade_count(self) -> int:

        return sum(trade.is_complete for trade in self.trades)

    @property
    def partial_trade_count(self) -> int:

        return sum(trade.is_partial for trade in self.trades)

    @property
    def unfilled_trade_count(self) -> int:

        return sum(trade.is_unfilled for trade in self.trades)

    # -----------------------------------------------------
    # Serialization
    # -----------------------------------------------------

    def to_dict(
        self,
    ) -> dict[str, Any]:

        return {
            "trades": [trade.to_dict() for trade in self.trades],
            "trade_count": self.trade_count,
            "total_quantity": self.total_quantity,
            "total_notional": self.total_notional,
            "average_execution_price": self.average_execution_price,
            "complete_trade_count": self.complete_trade_count,
            "partial_trade_count": self.partial_trade_count,
            "unfilled_trade_count": self.unfilled_trade_count,
            "metadata": dict(self.metadata),
        }

    # -----------------------------------------------------
    # Representation
    # -----------------------------------------------------

    def __str__(
        self,
    ) -> str:

        return f"ExecutionResult(" f"{self.trade_count} trades)"

    def __repr__(
        self,
    ) -> str:

        return (
            f"ExecutionResult("
            f"trades={self.trade_count}, "
            f"quantity={self.total_quantity})"
        )
