"""
============================================================
OptionForge
Order Status
============================================================
"""

from __future__ import annotations

from enum import Enum, auto


class OrderStatus(Enum):
    """
    Institutional order status.
    """

    PENDING = auto()

    SUBMITTED = auto()

    PARTIALLY_FILLED = auto()

    FILLED = auto()

    CANCELLED = auto()

    REJECTED = auto()

    EXPIRED = auto()

    @property
    def is_open(self) -> bool:

        return self in (
            OrderStatus.PENDING,
            OrderStatus.SUBMITTED,
            OrderStatus.PARTIALLY_FILLED,
        )

    @property
    def is_closed(self) -> bool:

        return not self.is_open

    @property
    def is_filled(self) -> bool:

        return self is OrderStatus.FILLED

    @property
    def is_rejected(self) -> bool:

        return self is OrderStatus.REJECTED

    @property
    def is_cancelled(self) -> bool:

        return self is OrderStatus.CANCELLED

    def __str__(self) -> str:

        return self.name.replace(
            "_",
            " ",
        ).title()
