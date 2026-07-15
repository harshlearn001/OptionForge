"""
============================================================
OptionForge
Volatility Smile Result
============================================================

Immutable result object for Volatility Smile.

============================================================
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    frozen=True,
    slots=True,
)
class VolatilitySmileResult:
    """
    Result returned by VolatilitySmileEngine.
    """

    symbol: str

    trade_date: int

    expiry: int

    points: list[tuple[float, float]]

    def __repr__(self):

        return (
            f"VolatilitySmileResult("
            f"symbol={self.symbol}, "
            f"points={len(self.points)})"
        )

    __str__ = __repr__
