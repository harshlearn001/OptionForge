"""
============================================================
OptionForge
Execution Registry
============================================================

Author      : OptionForge
Module      : execution_registry.py

Purpose
-------
Registry for execution builders.

============================================================
"""

from __future__ import annotations

from optionforge.execution.execution_builder import (
    ExecutionBuilder,
)


class ExecutionRegistry:
    """
    Registry of execution builders.
    """

    def __init__(self) -> None:

        self._builder = ExecutionBuilder()

    @property
    def builder(self) -> ExecutionBuilder:
        """
        Default execution builder.
        """

        return self._builder

    def get_builder(self) -> ExecutionBuilder:
        """
        Return the registered builder.
        """

        return self._builder

    def __repr__(self) -> str:

        return (

            f"ExecutionRegistry("

            f"builder={self._builder.__class__.__name__})"

        )