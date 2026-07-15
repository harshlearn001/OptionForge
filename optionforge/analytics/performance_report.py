"""
============================================================
OptionForge
Performance Report
============================================================

Author      : OptionForge
Module      : performance_report.py

Purpose
-------
Immutable institutional performance report.

Aggregates analytics produced by the Backtest and
Analytics subsystems.

Contains NO business logic.

============================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Mapping

from optionforge.analytics.drawdown_analysis import (
    DrawdownAnalysis,
)
from optionforge.analytics.equity_curve import (
    EquityCurve,
)
from optionforge.analytics.performance_metrics import (
    PerformanceMetrics,
)
from optionforge.analytics.trade_statistics import (
    TradeStatistics,
)
from optionforge.backtest.backtest_result import (
    BacktestResult,
)


@dataclass(
    frozen=True,
    slots=True,
)
class PerformanceReport:
    """
    Immutable institutional performance report.
    """

    backtest_result: BacktestResult

    equity_curve: EquityCurve

    drawdown_analysis: DrawdownAnalysis

    performance_metrics: PerformanceMetrics

    trade_statistics: TradeStatistics

    summary: str = ""

    metadata: Mapping[str, Any] = field(
        default_factory=dict,
        compare=False,
    )

    @property
    def is_profitable(self) -> bool:

        return self.performance_metrics.is_profitable

    @property
    def trade_count(self) -> int:

        return self.trade_statistics.total_trades

    @property
    def total_return(self) -> float:

        return self.performance_metrics.total_return

    def to_dict(self) -> dict[str, Any]:

        return {
            "backtest_result": self.backtest_result.to_dict(),
            "equity_curve": self.equity_curve.to_dict(),
            "drawdown_analysis": self.drawdown_analysis.to_dict(),
            "performance_metrics": self.performance_metrics.to_dict(),
            "trade_statistics": self.trade_statistics.to_dict(),
            "summary": self.summary,
            "metadata": dict(self.metadata),
        }

    def __str__(self) -> str:

        return f"PerformanceReport(" f"return={self.total_return:.2f}%)"

    def __repr__(self) -> str:

        return (
            f"PerformanceReport("
            f"trades={self.trade_count}, "
            f"return={self.total_return:.2f})"
        )
