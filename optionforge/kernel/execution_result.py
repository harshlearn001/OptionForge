"""
============================================================
OptionForge
Execution Result
============================================================

Represents the execution outcome of one engine.

Author      : OptionForge
Module      : execution_result.py
Purpose     : Immutable runtime execution result.

============================================================
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from optionforge.kernel.execution_status import (
    ExecutionStatus,
)


@dataclass(
    frozen=True,
    slots=True,
)
class ExecutionResult:
    """
    Represents the outcome of one engine execution.
    """

    engine: str

    status: ExecutionStatus

    result: Any | None = None

    duration: float = 0.0

    exception: Exception | None = None

    @property
    def succeeded(self) -> bool:
        """
        True if execution succeeded.
        """
        return self.status.is_success

    @property
    def failed(self) -> bool:
        """
        True if execution failed.
        """
        return self.status.is_failed

    @property
    def skipped(self) -> bool:
        """
        True if execution was skipped.
        """
        return self.status.is_skipped

    @property
    def warning(self) -> bool:
        """
        True if execution completed with warnings.
        """
        return self.status.is_warning

    def __repr__(self) -> str:

        return (
            "ExecutionResult("
            f"engine='{self.engine}', "
            f"status={self.status.value}, "
            f"duration={self.duration:.6f}s)"
        )

    __str__ = __repr__