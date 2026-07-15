"""
============================================================
OptionForge
Walk Forward Analysis
============================================================
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    frozen=True,
    slots=True,
)
class WalkForwardAnalysis:
    """
    Immutable walk-forward summary.
    """

    windows: int

    successful_windows: int

    failed_windows: int

    stability_score: float

    passed: bool

    def __post_init__(self) -> None:

        if self.windows <= 0:
            raise ValueError("windows must be positive.")

        if self.successful_windows < 0:
            raise ValueError("successful_windows cannot be negative.")

        if self.failed_windows < 0:
            raise ValueError("failed_windows cannot be negative.")

        if self.successful_windows + self.failed_windows != self.windows:
            raise ValueError("Window counts are inconsistent.")

        if not (0.0 <= self.stability_score <= 100.0):
            raise ValueError("stability_score must be between 0 and 100.")

    @property
    def success_rate(self) -> float:

        return (self.successful_windows / self.windows) * 100.0

    def to_dict(self) -> dict:

        return {
            "windows": self.windows,
            "successful_windows": self.successful_windows,
            "failed_windows": self.failed_windows,
            "stability_score": self.stability_score,
            "success_rate": self.success_rate,
            "passed": self.passed,
        }

    def __str__(self):

        return f"WalkForwardAnalysis(" f"success={self.success_rate:.1f}%)"
