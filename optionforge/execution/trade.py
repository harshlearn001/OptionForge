"""
============================================================
OptionForge
Trade
============================================================

Author      : OptionForge
Module      : trade.py

Purpose
-------
Immutable institutional trade.

A Trade aggregates one or more execution fills
belonging to the same order.

============================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from typing import Any, Mapping

from optionforge.execution.fill import Fill
from optionforge.execution.order import Order


@dataclass(
    frozen=True,
    slots=True,
)
class Trade:
    """
    Immutable institutional trade.
    """

    # -----------------------------------------------------
    # Parent Order
    # -----------------------------------------------------

    order: Order

    # -----------------------------------------------------
    # Executions
    # -----------------------------------------------------

    fills: tuple[Fill, ...] = ()

    # -----------------------------------------------------
    # Metadata
    # -----------------------------------------------------

    executed_at: datetime = field(
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

        total = sum(fill.quantity for fill in self.fills)

        if total > self.order.quantity:

            raise ValueError("total fill quantity exceeds order quantity.")

    # -----------------------------------------------------
    # Convenience
    # -----------------------------------------------------

    @property
    def fill_count(self) -> int:

        return len(self.fills)

    @property
    def total_quantity(self) -> int:

        return sum(fill.quantity for fill in self.fills)

    @property
    def remaining_quantity(self) -> int:

        return self.order.quantity - self.total_quantity

    @property
    def average_price(self) -> float:

        if self.total_quantity == 0:

            return 0.0

        total_value = sum(fill.price * fill.quantity for fill in self.fills)

        return total_value / self.total_quantity

    @property
    def notional_value(self) -> float:

        return sum(fill.notional_value for fill in self.fills)

    @property
    def is_complete(self) -> bool:

        return self.total_quantity == self.order.quantity

    @property
    def is_partial(self) -> bool:

        return 0 < self.total_quantity < self.order.quantity

    @property
    def is_unfilled(self) -> bool:

        return self.total_quantity == 0

    # -----------------------------------------------------
    # Serialization
    # -----------------------------------------------------

    def to_dict(self) -> dict[str, Any]:

        return {
            "order": self.order.to_dict(),
            "fills": [fill.to_dict() for fill in self.fills],
            "fill_count": self.fill_count,
            "total_quantity": self.total_quantity,
            "remaining_quantity": self.remaining_quantity,
            "average_price": self.average_price,
            "notional_value": self.notional_value,
            "is_complete": self.is_complete,
            "executed_at": self.executed_at.isoformat(),
            "metadata": dict(self.metadata),
        }

    # -----------------------------------------------------
    # Representation
    # -----------------------------------------------------

    def __str__(self) -> str:

        return f"Trade(" f"{self.order.symbol}, " f"{self.total_quantity})"

    def __repr__(self) -> str:

        return (
            f"Trade("
            f"fills={self.fill_count}, "
            f"average_price={self.average_price:.2f})"
        )
