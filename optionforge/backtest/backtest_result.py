"""
============================================================
OptionForge
Backtest Result
============================================================

Author      : OptionForge
Module      : backtest_result.py

Purpose
-------
Immutable institutional backtest result.

Aggregates one or more Backtest objects and provides
portfolio-level simulation statistics.

============================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Mapping

from optionforge.backtest.backtest import Backtest


@dataclass(
    frozen=True,
    slots=True,
)
class BacktestResult:
    """
    Immutable backtest result.
    """

    # -----------------------------------------------------
    # Backtests
    # -----------------------------------------------------

    backtests: tuple[Backtest, ...] = ()

    # -----------------------------------------------------
    # Metadata
    # -----------------------------------------------------

    metadata: Mapping[str, Any] = field(
        default_factory=dict,
        compare=False,
    )

    # -----------------------------------------------------
    # Convenience
    # -----------------------------------------------------

    @property
    def backtest_count(self) -> int:

        return len(self.backtests)

    @property
    def total_return(self) -> float:

        return sum(bt.total_return for bt in self.backtests)

    @property
    def average_return(self) -> float:

        if self.backtest_count == 0:

            return 0.0

        return self.total_return / self.backtest_count

    @property
    def average_sharpe(self) -> float:

        if self.backtest_count == 0:

            return 0.0

        return sum(bt.sharpe_ratio for bt in self.backtests) / self.backtest_count

    @property
    def total_trades(self) -> int:

        return sum(bt.total_trades for bt in self.backtests)

    @property
    def average_win_rate(self) -> float:

        if self.backtest_count == 0:

            return 0.0

        return sum(bt.win_rate for bt in self.backtests) / self.backtest_count

    # -----------------------------------------------------
    # Serialization
    # -----------------------------------------------------

    def to_dict(self) -> dict[str, Any]:

        return {
            "backtests": [bt.to_dict() for bt in self.backtests],
            "backtest_count": self.backtest_count,
            "total_return": self.total_return,
            "average_return": self.average_return,
            "average_sharpe": self.average_sharpe,
            "average_win_rate": self.average_win_rate,
            "total_trades": self.total_trades,
            "metadata": dict(self.metadata),
        }

    # -----------------------------------------------------
    # Representation
    # -----------------------------------------------------

    def __str__(self) -> str:

        return f"BacktestResult(" f"{self.backtest_count} backtests)"

    def __repr__(self) -> str:

        return (
            f"BacktestResult("
            f"backtests={self.backtest_count}, "
            f"return={self.total_return:.2f})"
        )
