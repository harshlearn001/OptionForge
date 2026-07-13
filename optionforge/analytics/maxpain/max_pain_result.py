"""
============================================================
OptionForge
Max Pain Result
============================================================

Immutable result object for Max Pain analytics.

============================================================
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    frozen=True,
    slots=True,
)
class MaxPainResult:
    """
    Result returned by Max Pain Engine.
    """

    symbol: str

    trade_date: int

    expiry: int

    spot: float

    max_pain_strike: int

    total_pain: float

    call_pain: float

    put_pain: float

    distance_from_spot: float

    contracts: int

    def __repr__(self) -> str:

        return (
            f"MaxPainResult("
            f"symbol={self.symbol}, "
            f"max_pain={self.max_pain_strike}, "
            f"distance={self.distance_from_spot:.2f})"
        )

    __str__ = __repr__