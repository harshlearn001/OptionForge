"""
============================================================
OptionForge
Research Result
============================================================

Author      : OptionForge
Module      : research_result.py

Purpose
-------
Immutable institutional research result.

Aggregates the outcome of a complete research study.

Contains NO business logic.

============================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Mapping

from optionforge.analytics.performance_report import (
    PerformanceReport,
)
from optionforge.research.research import (
    Research,
)


@dataclass(
    frozen=True,
    slots=True,
)
class ResearchResult:
    """
    Immutable institutional research result.
    """

    # =====================================================
    # Core
    # =====================================================

    research: Research

    performance_report: PerformanceReport

    research_score: float

    approved: bool

    recommendation: str = ""

    # =====================================================
    # Metadata
    # =====================================================

    metadata: Mapping[str, Any] = field(
        default_factory=dict,
        compare=False,
    )

    # =====================================================
    # Validation
    # =====================================================

    def __post_init__(self) -> None:

        if not (

            0.0

            <= self.research_score

            <= 100.0

        ):

            raise ValueError(

                "research_score must be between 0 and 100."

            )

    # =====================================================
    # Convenience
    # =====================================================

    @property
    def is_approved(self) -> bool:

        return self.approved

    @property
    def total_return(self) -> float:

        return self.performance_report.total_return

    @property
    def trade_count(self) -> int:

        return self.performance_report.trade_count

    # =====================================================
    # Serialization
    # =====================================================

    def to_dict(self) -> dict[str, Any]:

        return {

            "research": self.research.to_dict(),

            "performance_report":

                self.performance_report.to_dict(),

            "research_score":

                self.research_score,

            "approved":

                self.approved,

            "recommendation":

                self.recommendation,

            "metadata":

                dict(self.metadata),

        }

    # =====================================================
    # Representation
    # =====================================================

    def __str__(self) -> str:

        return (

            f"ResearchResult("

            f"score={self.research_score:.1f})"

        )

    def __repr__(self) -> str:

        return (

            f"ResearchResult("

            f"approved={self.approved}, "

            f"score={self.research_score:.1f})"

        )