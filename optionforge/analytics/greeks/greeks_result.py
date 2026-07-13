"""
============================================================
OptionForge
Greeks Result
============================================================

Immutable result object for Greeks analytics.

============================================================
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    frozen=True,
    slots=True,
)
class GreeksResult:
    """
    Result returned by GreeksEngine.
    """

    symbol: str

    trade_date: int

    expiry: int

    strike: float

    spot: float

    option_type: str

    option_price: float

    implied_volatility: float | None

    delta: float

    gamma: float

    theta: float

    vega: float

    def __repr__(self) -> str:

        return (

            f"GreeksResult("

            f"symbol={self.symbol}, "

            f"type='{self.option_type}', "

            f"delta={self.delta:.4f}, "

            f"gamma={self.gamma:.6f})"

        )

    __str__ = __repr__