"""
============================================================
OptionForge
Volatility Surface Result
============================================================

Immutable result object for Volatility Surface.

============================================================
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    frozen=True,
    slots=True,
)
class VolatilitySurfaceResult:
    """
    Result returned by VolatilitySurfaceEngine.
    """

    symbol: str

    trade_date: int

    points: list[tuple[int, float, float]]

    def __repr__(self):

        return (

            f"VolatilitySurfaceResult("

            f"symbol={self.symbol}, "

            f"points={len(self.points)})"

        )

    __str__ = __repr__