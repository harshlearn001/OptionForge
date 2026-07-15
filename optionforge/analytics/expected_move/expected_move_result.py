"""
============================================================
OptionForge
Expected Move Result
============================================================
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    frozen=True,
    slots=True,
)
class ExpectedMoveResult:
    """
    Result returned by ExpectedMoveEngine.
    """

    symbol: str

    trade_date: int

    expiry: int

    spot: float

    volatility: float

    time: float

    expected_move: float

    upper_bound: float

    lower_bound: float

    def __repr__(self):

        return (
            f"ExpectedMoveResult("
            f"symbol={self.symbol}, "
            f"expected_move={self.expected_move:.2f})"
        )

    __str__ = __repr__
