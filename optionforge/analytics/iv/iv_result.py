"""
============================================================
OptionForge
IV Result
============================================================

Immutable result object for Implied Volatility analytics.

============================================================
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    frozen=True,
    slots=True,
)
class IVResult:
    """
    Result returned by IVEngine.
    """

    symbol: str

    trade_date: int

    expiry: int

    strike: float

    spot: float

    option_type: str

    market_price: float

    implied_volatility: float

    contracts: int

    def __repr__(self) -> str:

        return (

            f"IVResult("

            f"symbol={self.symbol}, "

            f"type='{self.option_type}', "

            f"iv={self.implied_volatility:.4f})"

        )

    __str__ = __repr__