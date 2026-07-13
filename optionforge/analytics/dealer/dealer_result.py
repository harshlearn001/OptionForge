"""
============================================================
OptionForge
Dealer Result
============================================================

Immutable result object for Dealer Position analytics.

============================================================
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    frozen=True,
    slots=True,
)
class DealerResult:
    """
    Result returned by Dealer Engine.
    """

    symbol: str

    trade_date: int

    expiry: int

    spot: float

    major_call_strike: int

    major_put_strike: int

    total_call_oi: int

    total_put_oi: int

    net_oi: int

    dealer_bias: str

    confidence: float

    contracts: int

    def __repr__(self) -> str:

        return (

            f"DealerResult("

            f"symbol={self.symbol}, "

            f"bias='{self.dealer_bias}', "

            f"confidence={self.confidence:.1f}%)"

        )

    __str__ = __repr__