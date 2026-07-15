"""
============================================================
OptionForge
IV Percentile Result
============================================================

Immutable result object for IV Percentile.

============================================================
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    frozen=True,
    slots=True,
)
class IVPercentileResult:
    """
    Result returned by IVPercentileEngine.
    """

    symbol: str

    trade_date: int

    expiry: int

    current_iv: float

    historical_observations: int

    iv_percentile: float

    def __repr__(self) -> str:

        return (
            f"IVPercentileResult("
            f"symbol={self.symbol}, "
            f"iv_percentile={self.iv_percentile:.2f})"
        )

    __str__ = __repr__
