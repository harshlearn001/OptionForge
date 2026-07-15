"""
============================================================
OptionForge
Backtest Engine
============================================================

Author      : OptionForge
Module      : backtest_engine.py

Purpose
-------
Institutional backtest engine.

The BacktestEngine orchestrates creation of immutable
BacktestResult objects by delegating construction to the
BacktestBuilder obtained from the BacktestRegistry.

============================================================
"""

from __future__ import annotations

from optionforge.backtest.backtest import Backtest
from optionforge.backtest.backtest_registry import (
    BacktestRegistry,
)
from optionforge.backtest.backtest_result import (
    BacktestResult,
)


class BacktestEngine:
    """
    Institutional backtest engine.
    """

    def __init__(
        self,
        *,
        registry: BacktestRegistry | None = None,
    ) -> None:

        self._registry = registry or BacktestRegistry()

    @property
    def registry(self) -> BacktestRegistry:
        """
        Registered backtest registry.
        """

        return self._registry

    def execute(
        self,
        *,
        backtests: tuple[Backtest, ...] = (),
    ) -> BacktestResult:
        """
        Execute a backtest aggregation.
        """

        builder = self._registry.get_builder()

        return builder.build(
            backtests=backtests,
        )

    def __repr__(self) -> str:

        return f"BacktestEngine(" f"registry={self._registry.__class__.__name__})"
