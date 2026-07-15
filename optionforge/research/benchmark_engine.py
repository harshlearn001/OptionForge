"""
============================================================
OptionForge
Benchmark Engine
============================================================

Author      : OptionForge
Module      : benchmark_engine.py

Purpose
-------
Executes a benchmark comparison and returns an immutable
BenchmarkComparison.

============================================================
"""

from __future__ import annotations

from optionforge.research.benchmark_comparison import (
    BenchmarkComparison,
)


class BenchmarkEngine:
    """
    Executes benchmark comparison.
    """

    def run(
        self,
        strategy_return: float,
        benchmark_name: str,
        benchmark_return: float,
    ) -> BenchmarkComparison:
        """
        Execute benchmark comparison.
        """

        alpha = round(
            strategy_return - benchmark_return,
            10,
        )

        tracking_error = 0.0

        information_ratio = 0.0

        outperformed = strategy_return >= benchmark_return

        passed = outperformed

        return BenchmarkComparison(
            benchmark_name=benchmark_name,
            strategy_return=strategy_return,
            benchmark_return=benchmark_return,
            alpha=alpha,
            tracking_error=tracking_error,
            information_ratio=information_ratio,
            outperformed=outperformed,
            passed=passed,
        )

    def __repr__(self) -> str:

        return "BenchmarkEngine()"

    __str__ = __repr__
