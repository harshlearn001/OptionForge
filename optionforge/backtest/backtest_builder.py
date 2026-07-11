"""
============================================================
OptionForge
Backtest Builder
============================================================

Author      : OptionForge
Module      : backtest_builder.py

Purpose
-------
Institutional builder for immutable BacktestResult
objects.

============================================================
"""

from __future__ import annotations

from optionforge.backtest.backtest import Backtest
from optionforge.backtest.backtest_result import (
    BacktestResult,
)


class BacktestBuilder:
    """
    Builds immutable BacktestResult objects.
    """

    def build(
        self,
        *,
        backtests: tuple[Backtest, ...] = (),
    ) -> BacktestResult:
        """
        Build a BacktestResult.
        """

        return BacktestResult(

            backtests=backtests,

        )