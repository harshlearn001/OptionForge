"""
============================================================
OptionForge
Execution Engine
============================================================

Author      : OptionForge
Module      : execution_engine.py

Purpose
-------
Institutional execution engine.

The ExecutionEngine orchestrates execution by delegating
construction to the ExecutionBuilder obtained from the
ExecutionRegistry.

============================================================
"""

from __future__ import annotations

from optionforge.execution.execution_registry import (
    ExecutionRegistry,
)
from optionforge.execution.execution_result import (
    ExecutionResult,
)
from optionforge.execution.trade import (
    Trade,
)


class ExecutionEngine:
    """
    Institutional execution engine.
    """

    def __init__(
        self,
        *,
        registry: ExecutionRegistry | None = None,
    ) -> None:

        self._registry = registry or ExecutionRegistry()

    @property
    def registry(self) -> ExecutionRegistry:
        """
        Registered execution registry.
        """

        return self._registry

    def execute(
        self,
        *,
        trades: tuple[Trade, ...] = (),
    ) -> ExecutionResult:
        """
        Execute trades and build an ExecutionResult.
        """

        builder = self._registry.get_builder()

        return builder.build(
            trades=trades,
        )

    def __repr__(self) -> str:

        return f"ExecutionEngine(" f"registry={self._registry.__class__.__name__})"
