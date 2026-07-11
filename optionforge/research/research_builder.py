"""
============================================================
OptionForge
Research Builder
============================================================

Author      : OptionForge
Module      : research_builder.py

Purpose
-------
Institutional builder for immutable ResearchResult
objects.

Contains NO business logic.

============================================================
"""

from __future__ import annotations

from optionforge.analytics.performance_report import (
    PerformanceReport,
)
from optionforge.research.research import (
    Research,
)
from optionforge.research.research_result import (
    ResearchResult,
)


class ResearchBuilder:
    """
    Builds immutable ResearchResult objects.
    """

    def build(
        self,
        *,
        research: Research,
        performance_report: PerformanceReport,
        research_score: float,
        approved: bool,
        recommendation: str = "",
    ) -> ResearchResult:
        """
        Build a ResearchResult.
        """

        return ResearchResult(

            research=research,

            performance_report=performance_report,

            research_score=research_score,

            approved=approved,

            recommendation=recommendation,

        )