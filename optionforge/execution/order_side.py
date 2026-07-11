"""
============================================================
OptionForge
Order Side
============================================================

Author      : OptionForge
Module      : order_side.py

Purpose
-------
Institutional order side enumeration.

============================================================
"""

from __future__ import annotations

from enum import Enum, auto


class OrderSide(Enum):
    """
    Institutional order side.
    """

    BUY = auto()

    SELL = auto()

    @property
    def is_buy(self) -> bool:

        return self is OrderSide.BUY

    @property
    def is_sell(self) -> bool:

        return self is OrderSide.SELL

    def __str__(self) -> str:

        return self.name.title()