"""
============================================================
OptionForge
Execution Status
============================================================

Defines the execution state of an engine.

Author      : OptionForge
Module      : execution_status.py
Purpose     : Standard execution status enumeration.

============================================================
"""

from __future__ import annotations

from enum import Enum


class ExecutionStatus(str, Enum):
    """
    Execution status for an engine.
    """

    SUCCESS = "SUCCESS"

    FAILED = "FAILED"

    SKIPPED = "SKIPPED"

    WARNING = "WARNING"

    @property
    def is_success(self) -> bool:
        """
        True if execution completed successfully.
        """
        return self is ExecutionStatus.SUCCESS

    @property
    def is_failed(self) -> bool:
        """
        True if execution failed.
        """
        return self is ExecutionStatus.FAILED

    @property
    def is_skipped(self) -> bool:
        """
        True if execution was skipped.
        """
        return self is ExecutionStatus.SKIPPED

    @property
    def is_warning(self) -> bool:
        """
        True if execution completed with warnings.
        """
        return self is ExecutionStatus.WARNING

    def __str__(self) -> str:
        return self.value