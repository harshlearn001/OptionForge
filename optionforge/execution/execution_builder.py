"""
============================================================
OptionForge
Execution Builder
============================================================

Author      : OptionForge
Module      : execution_builder.py

Purpose
-------
Build immutable ExecutionResult objects.

============================================================
"""

from __future__ import annotations

from optionforge.execution.execution_result import (
    ExecutionResult,
)
from optionforge.execution.trade import (
    Trade,
)


class ExecutionBuilder:
    """
    Institutional ExecutionResult builder.
    """

    def build(
        self,
        *,
        trades: tuple[Trade, ...] = (),
    ) -> ExecutionResult:
        """
        Build an immutable ExecutionResult.
        """

        return ExecutionResult(

            trades=trades,

        )