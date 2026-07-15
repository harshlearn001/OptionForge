"""
============================================================
OptionForge
Backtest
============================================================

Author      : OptionForge
Module      : backtest.py

Purpose
-------
Immutable institutional backtest summary.

Represents the final outcome of a complete
strategy simulation.

Contains NO business logic.

============================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from typing import Any, Mapping


@dataclass(
    frozen=True,
    slots=True,
)
class Backtest:
    """
    Immutable backtest summary.
    """

    # -----------------------------------------------------
    # Performance
    # -----------------------------------------------------

    total_return: float

    annual_return: float

    max_drawdown: float

    sharpe_ratio: float

    sortino_ratio: float

    win_rate: float

    total_trades: int

    profitable_trades: int

    losing_trades: int

    # -----------------------------------------------------
    # Metadata
    # -----------------------------------------------------

    timestamp: datetime = field(
        default_factory=lambda: datetime.now(UTC),
        compare=False,
    )

    metadata: Mapping[str, Any] = field(
        default_factory=dict,
        compare=False,
    )

    # -----------------------------------------------------
    # Validation
    # -----------------------------------------------------

    def __post_init__(self) -> None:

        if self.total_trades < 0:

            raise ValueError("total_trades cannot be negative.")

        if self.profitable_trades < 0:

            raise ValueError("profitable_trades cannot be negative.")

        if self.losing_trades < 0:

            raise ValueError("losing_trades cannot be negative.")

        if not (0.0 <= self.win_rate <= 100.0):

            raise ValueError("win_rate must be between 0 and 100.")

    # -----------------------------------------------------
    # Convenience
    # -----------------------------------------------------

    @property
    def expectancy(self) -> float:

        if self.total_trades == 0:

            return 0.0

        return self.total_return / self.total_trades

    @property
    def is_profitable(self) -> bool:

        return self.total_return > 0

    @property
    def has_drawdown(self) -> bool:

        return self.max_drawdown > 0

    # -----------------------------------------------------
    # Serialization
    # -----------------------------------------------------

    def to_dict(self) -> dict[str, Any]:

        return {
            "total_return": self.total_return,
            "annual_return": self.annual_return,
            "max_drawdown": self.max_drawdown,
            "sharpe_ratio": self.sharpe_ratio,
            "sortino_ratio": self.sortino_ratio,
            "win_rate": self.win_rate,
            "total_trades": self.total_trades,
            "profitable_trades": self.profitable_trades,
            "losing_trades": self.losing_trades,
            "expectancy": self.expectancy,
            "timestamp": self.timestamp.isoformat(),
            "metadata": dict(self.metadata),
        }

    # -----------------------------------------------------
    # Representation
    # -----------------------------------------------------

    def __str__(self) -> str:

        return (
            f"Backtest("
            f"return={self.total_return:.2f}%, "
            f"trades={self.total_trades})"
        )

    def __repr__(self) -> str:

        return (
            f"Backtest("
            f"return={self.total_return:.2f}, "
            f"sharpe={self.sharpe_ratio:.2f})"
        )
