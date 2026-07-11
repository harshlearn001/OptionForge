"""
============================================================
OptionForge
Fill
============================================================

Author      : OptionForge
Module      : fill.py

Purpose
-------
Immutable institutional execution fill.

Represents a single execution against an Order.

============================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from typing import Any, Mapping

from optionforge.execution.fill_status import FillStatus
from optionforge.execution.order import Order


@dataclass(
    frozen=True,
    slots=True,
)
class Fill:
    """
    Immutable execution fill.
    """

    # -----------------------------------------------------
    # Parent Order
    # -----------------------------------------------------

    order: Order

    # -----------------------------------------------------
    # Execution
    # -----------------------------------------------------

    quantity: int

    price: float

    status: FillStatus

    # -----------------------------------------------------
    # Metadata
    # -----------------------------------------------------

    filled_at: datetime = field(
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

        if self.quantity <= 0:

            raise ValueError(

                "quantity must be positive."

            )

        if self.price < 0:

            raise ValueError(

                "price cannot be negative."

            )

        if self.quantity > self.order.quantity:

            raise ValueError(

                "fill quantity cannot exceed order quantity."

            )

    # -----------------------------------------------------
    # Convenience
    # -----------------------------------------------------

    @property
    def notional_value(self) -> float:

        return self.quantity * self.price

    @property
    def remaining_quantity(self) -> int:

        return self.order.quantity - self.quantity

    @property
    def is_complete(self) -> bool:

        return self.status.is_complete

    @property
    def is_partial(self) -> bool:

        return self.status.is_partial

    # -----------------------------------------------------
    # Serialization
    # -----------------------------------------------------

    def to_dict(self) -> dict[str, Any]:

        return {

            "order": self.order.to_dict(),

            "quantity": self.quantity,

            "price": self.price,

            "status": self.status.name,

            "notional_value": self.notional_value,

            "remaining_quantity": self.remaining_quantity,

            "filled_at": self.filled_at.isoformat(),

            "metadata": dict(self.metadata),

        }

    # -----------------------------------------------------
    # Representation
    # -----------------------------------------------------

    def __str__(self) -> str:

        return (

            f"Fill("

            f"{self.quantity}@{self.price})"

        )

    def __repr__(self) -> str:

        return (

            f"Fill("

            f"quantity={self.quantity}, "

            f"price={self.price}, "

            f"status={self.status.name})"

        )