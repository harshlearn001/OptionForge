"""
============================================================
OptionForge
Backtest Registry
============================================================

Author      : OptionForge
Module      : backtest_registry.py

Purpose
-------
Registry for backtest builders.

============================================================
"""

from __future__ import annotations

from optionforge.backtest.backtest_builder import (
    BacktestBuilder,
)


class BacktestRegistry:
    """
    Registry of backtest builders.
    """

    def __init__(self) -> None:

        self._builder = BacktestBuilder()

    @property
    def builder(self) -> BacktestBuilder:
        """
        Default backtest builder.
        """

        return self._builder

    def get_builder(self) -> BacktestBuilder:
        """
        Return the registered builder.
        """

        return self._builder

    def __repr__(self) -> str:

        return f"BacktestRegistry(" f"builder={self._builder.__class__.__name__})"
