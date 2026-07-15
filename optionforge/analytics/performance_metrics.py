"""
============================================================
OptionForge
Performance Metrics
============================================================

Author      : OptionForge
Module      : performance_metrics.py

Purpose
-------
Immutable institutional performance metrics.

Contains validated performance statistics generated from
backtesting and analytics.

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
class PerformanceMetrics:
    """
    Immutable institutional performance metrics.
    """

    # =====================================================
    # Returns
    # =====================================================

    total_return: float

    annual_return: float

    cagr: float

    # =====================================================
    # Risk
    # =====================================================

    volatility: float

    max_drawdown: float

    # =====================================================
    # Risk Adjusted
    # =====================================================

    sharpe_ratio: float

    sortino_ratio: float

    calmar_ratio: float

    # =====================================================
    # Trading
    # =====================================================

    win_rate: float

    profit_factor: float

    expectancy: float

    recovery_factor: float

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

        for name in (
            "win_rate",
            "max_drawdown",
        ):

            value = getattr(
                self,
                name,
            )

            if not (0.0 <= value <= 100.0):

                raise ValueError(f"{name} must be between 0 and 100.")

        if self.volatility < 0:

            raise ValueError("volatility cannot be negative.")

        if self.profit_factor < 0:

            raise ValueError("profit_factor cannot be negative.")

    # =====================================================
    # Convenience
    # =====================================================

    @property
    def is_profitable(self) -> bool:

        return self.total_return > 0

    @property
    def has_positive_expectancy(self) -> bool:

        return self.expectancy > 0

    @property
    def is_low_risk(self) -> bool:

        return self.max_drawdown < 10.0

    # =====================================================
    # Serialization
    # =====================================================

    def to_dict(self) -> dict[str, Any]:

        return {
            "total_return": self.total_return,
            "annual_return": self.annual_return,
            "cagr": self.cagr,
            "volatility": self.volatility,
            "max_drawdown": self.max_drawdown,
            "sharpe_ratio": self.sharpe_ratio,
            "sortino_ratio": self.sortino_ratio,
            "calmar_ratio": self.calmar_ratio,
            "win_rate": self.win_rate,
            "profit_factor": self.profit_factor,
            "expectancy": self.expectancy,
            "recovery_factor": self.recovery_factor,
            "metadata": dict(self.metadata),
        }

    # =====================================================
    # Representation
    # =====================================================

    def __str__(self) -> str:

        return (
            f"PerformanceMetrics("
            f"return={self.total_return:.2f}%, "
            f"sharpe={self.sharpe_ratio:.2f})"
        )

    def __repr__(self) -> str:

        return (
            f"PerformanceMetrics("
            f"return={self.total_return:.2f}, "
            f"drawdown={self.max_drawdown:.2f})"
        )
