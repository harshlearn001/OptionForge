"""
============================================================
OptionForge
IV Rank Result
============================================================

Immutable result object for IV Rank.

============================================================
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    frozen=True,
    slots=True,
)
class IVRankResult:
    """
    Result returned by IVRankEngine.
    """

    symbol: str

    trade_date: int

    expiry: int

    current_iv: float

    lowest_iv: float

    highest_iv: float

    iv_rank: float

    def __repr__(self) -> str:

        return f"IVRankResult(" f"symbol={self.symbol}, " f"iv_rank={self.iv_rank:.2f})"

    __str__ = __repr__
