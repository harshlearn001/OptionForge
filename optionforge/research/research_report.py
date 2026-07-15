"""
============================================================
OptionForge
Research Report
============================================================
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    frozen=True,
    slots=True,
)
class ResearchReport:
    """
    Immutable research report.
    """

    strategy_name: str

    overall_score: float

    overall_grade: str

    approved: bool

    recommendation: str

    def __post_init__(self) -> None:

        if not self.strategy_name.strip():

            raise ValueError("strategy_name cannot be empty.")

        if not (0.0 <= self.overall_score <= 100.0):

            raise ValueError("overall_score must be between 0 and 100.")

        if not self.overall_grade.strip():

            raise ValueError("overall_grade cannot be empty.")

        if not self.recommendation.strip():

            raise ValueError("recommendation cannot be empty.")

    @property
    def passed(self) -> bool:

        return self.approved

    def to_dict(self) -> dict:

        return {
            "strategy_name": self.strategy_name,
            "overall_score": self.overall_score,
            "overall_grade": self.overall_grade,
            "approved": self.approved,
            "recommendation": self.recommendation,
            "passed": self.passed,
        }

    def __str__(self):

        return f"ResearchReport(" f"{self.strategy_name})"

    def __repr__(self):

        return f"ResearchReport(" f"strategy='{self.strategy_name}')"
