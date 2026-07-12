"""
============================================================
OptionForge
Integration Result
============================================================

Author      : OptionForge
Module      : integration_result.py

Purpose
-------
Immutable result returned by the Integration Layer.

============================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True, slots=True)
class IntegrationResult:
    """
    Result returned after MarketForge integration.
    """

    success: bool

    filepath: str

    rows: int

    columns: int

    warnings: tuple[str, ...] = field(default_factory=tuple)

    errors: tuple[str, ...] = field(default_factory=tuple)

    @property
    def warning_count(self) -> int:
        """
        Number of warnings.
        """
        return len(self.warnings)

    @property
    def error_count(self) -> int:
        """
        Number of errors.
        """
        return len(self.errors)

    @property
    def has_warnings(self) -> bool:
        """
        Returns True if warnings exist.
        """
        return self.warning_count > 0

    @property
    def has_errors(self) -> bool:
        """
        Returns True if errors exist.
        """
        return self.error_count > 0

    @property
    def is_valid(self) -> bool:
        """
        Returns True if integration succeeded
        without errors.
        """
        return self.success and not self.has_errors

    def to_dict(self) -> dict:

        return {

            "success": self.success,

            "filepath": self.filepath,

            "rows": self.rows,

            "columns": self.columns,

            "warnings": list(self.warnings),

            "errors": list(self.errors),

            "warning_count": self.warning_count,

            "error_count": self.error_count,

            "is_valid": self.is_valid,

        }

    def __repr__(self) -> str:

        return (

            "IntegrationResult("

            f"success={self.success}, "

            f"rows={self.rows}, "

            f"columns={self.columns})"

        )

    __str__ = __repr__