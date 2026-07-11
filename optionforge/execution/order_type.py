"""
============================================================
OptionForge
Order Type
============================================================
"""

from __future__ import annotations

from enum import Enum, auto


class OrderType(Enum):
    """
    Institutional order types.
    """

    MARKET = auto()

    LIMIT = auto()

    STOP = auto()

    STOP_LIMIT = auto()

    @property
    def is_market(self) -> bool:

        return self is OrderType.MARKET

    @property
    def is_limit(self) -> bool:

        return self is OrderType.LIMIT

    @property
    def is_stop(self) -> bool:

        return self is OrderType.STOP

    @property
    def is_stop_limit(self) -> bool:

        return self is OrderType.STOP_LIMIT

    def __str__(self) -> str:

        return self.name.replace(
            "_",
            " ",
        ).title()