"""
============================================================
OptionForge
Trade Statistics
============================================================

Author      : OptionForge
Module      : trade_statistics.py

Purpose
-------
Immutable institutional trade statistics.

Contains trade-level statistics generated from
backtesting.

Contains NO business logic.

============================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Mapping


@dataclass(
    frozen=True,
    slots=True,
)
class TradeStatistics:
    """
    Immutable trade statistics.
    """

    # =====================================================
    # Trade Counts
    # =====================================================

    total_trades: int

    winning_trades: int

    losing_trades: int

    # =====================================================
    # Profitability
    # =====================================================

    average_win: float

    average_loss: float

    largest_win: float

    largest_loss: float

    profit_factor: float

    expectancy: float

    # =====================================================
    # Streaks
    # =====================================================

    longest_winning_streak: int

    longest_losing_streak: int

    # =====================================================
    # Metadata
    # =====================================================

    metadata: Mapping[str, Any] = field(
        default_factory=dict,
        compare=False,
    )

    # =====================================================
    # Validation
    # =====================================================

    def __post_init__(self) -> None:

        if self.total_trades < 0:
            raise ValueError("total_trades cannot be negative.")

        if self.winning_trades < 0:
            raise ValueError("winning_trades cannot be negative.")

        if self.losing_trades < 0:
            raise ValueError("losing_trades cannot be negative.")

        if self.winning_trades + self.losing_trades > self.total_trades:
            raise ValueError("Winning and losing trades exceed total trades.")

        if self.profit_factor < 0:
            raise ValueError("profit_factor cannot be negative.")

    # =====================================================
    # Convenience
    # =====================================================

    @property
    def win_rate(self) -> float:

        if self.total_trades == 0:
            return 0.0

        return (self.winning_trades / self.total_trades) * 100.0

    @property
    def loss_rate(self) -> float:

        if self.total_trades == 0:
            return 0.0

        return (self.losing_trades / self.total_trades) * 100.0

    @property
    def is_profitable(self) -> bool:

        return self.expectancy > 0

    # =====================================================
    # Serialization
    # =====================================================

    def to_dict(self) -> dict[str, Any]:

        return {
            "total_trades": self.total_trades,
            "winning_trades": self.winning_trades,
            "losing_trades": self.losing_trades,
            "win_rate": self.win_rate,
            "loss_rate": self.loss_rate,
            "average_win": self.average_win,
            "average_loss": self.average_loss,
            "largest_win": self.largest_win,
            "largest_loss": self.largest_loss,
            "profit_factor": self.profit_factor,
            "expectancy": self.expectancy,
            "longest_winning_streak": self.longest_winning_streak,
            "longest_losing_streak": self.longest_losing_streak,
            "metadata": dict(self.metadata),
        }

    # =====================================================
    # Representation
    # =====================================================

    def __str__(self) -> str:

        return (
            f"TradeStatistics("
            f"trades={self.total_trades}, "
            f"win_rate={self.win_rate:.1f}%)"
        )

    def __repr__(self) -> str:

        return (
            f"TradeStatistics("
            f"trades={self.total_trades}, "
            f"profit_factor={self.profit_factor:.2f})"
        )
