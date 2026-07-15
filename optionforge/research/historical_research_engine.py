"""
============================================================
OptionForge
Historical Research Engine
============================================================

Author      : OptionForge Engineering Team

Purpose
-------
Coordinates the historical research pipeline.

Consumes historical market matches and produces an
immutable HistoricalResearchResult.

Contains NO similarity algorithms.

============================================================
"""

from __future__ import annotations

from optionforge.research.historical_research_result import (
    HistoricalResearchResult,
)
from optionforge.research.probability_engine import (
    ProbabilityEngine,
)
from optionforge.research.research_query import (
    ResearchQuery,
)
from optionforge.research.similarity_engine import (
    SimilarityEngine,
)


class HistoricalResearchEngine:
    """
    Historical Research Engine.
    """

    def __init__(
        self,
        query: ResearchQuery,
        similarity_engine: SimilarityEngine,
    ) -> None:

        self._query = query
        self._similarity_engine = similarity_engine

    @property
    def query(self) -> ResearchQuery:

        return self._query

    @property
    def similarity_engine(self) -> SimilarityEngine:

        return self._similarity_engine

    # =====================================================
    # Main Pipeline
    # =====================================================

    def calculate(
        self,
    ) -> HistoricalResearchResult:
        """
        Execute historical research.
        """

        matches = self._similarity_engine.rank()

        probability = ProbabilityEngine(matches)

        return HistoricalResearchResult(

            matches=matches,

            win_rate=probability.win_rate(),

            average_return=probability.average_return(),

            median_return=probability.median_return(),

            average_drawdown=probability.average_drawdown(),

            average_runup=probability.average_runup(),

            expected_value=probability.expected_value(),

        )

    def __repr__(self) -> str:

        return (
            f"HistoricalResearchEngine("
            f"symbol={self._query.symbol}, "
            f"matches={len(self._similarity_engine)})"
        )