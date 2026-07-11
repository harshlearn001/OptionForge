"""
============================================================
OptionForge
Research Engine
============================================================

Author      : OptionForge
Module      : research_engine.py

Purpose
-------
Institutional orchestration engine for Research.

Coordinates creation of immutable ResearchResult
objects.

Contains NO research algorithms.

============================================================
"""

from __future__ import annotations

from optionforge.analytics.performance_report import (
    PerformanceReport,
)
from optionforge.research.research import (
    Research,
)
from optionforge.research.research_registry import (
    ResearchRegistry,
)
from optionforge.research.research_result import (
    ResearchResult,
)


class ResearchEngine:
    """
    Institutional Research Engine.
    """

    def __init__(
        self,
        registry: ResearchRegistry | None = None,
    ) -> None:

        self._registry = (

            registry

            if registry is not None

            else ResearchRegistry()

        )

    @property
    def registry(
        self,
    ) -> ResearchRegistry:

        return self._registry

    def evaluate(
        self,
        *,
        research: Research,
        performance_report: PerformanceReport,
        research_score: float,
        approved: bool,
        recommendation: str = "",
    ) -> ResearchResult:
        """
        Produce a ResearchResult.
        """

        builder = self._registry.get_builder()

        return builder.build(

            research=research,

            performance_report=performance_report,

            research_score=research_score,

            approved=approved,

            recommendation=recommendation,

        )

    def __repr__(
        self,
    ) -> str:

        return (

            f"ResearchEngine("

            f"registry={self._registry.__class__.__name__})"

        )