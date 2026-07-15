"""
==============================================================
Tests for HistoricalResearchEngine
==============================================================
"""

from datetime import date

from optionforge.common.enums import TrendDirection

from optionforge.intelligence.enums.dealer_state import DealerState
from optionforge.intelligence.enums.institutional_state import (
    InstitutionalState,
)
from optionforge.intelligence.enums.volatility_state import (
    VolatilityState,
)

from optionforge.regime.enums.regime_state import RegimeState

from optionforge.research.historical_match import HistoricalMatch
from optionforge.research.historical_research_engine import (
    HistoricalResearchEngine,
)
from optionforge.research.historical_research_result import (
    HistoricalResearchResult,
)
from optionforge.research.research_query import ResearchQuery
from optionforge.research.similarity_engine import SimilarityEngine


def build_query():

    return ResearchQuery(

        symbol="NIFTY",

        regime=RegimeState.STRONG_UPTREND,

        institutional_state=InstitutionalState.STRONGLY_BULLISH,

        dealer_state=DealerState.LONG_GAMMA,

        trend=TrendDirection.STRONG_BULLISH,

        volatility=VolatilityState.CHEAP,

        iv_rank=20,

        iv_percentile=25,

        pcr=1.15,

    )


def build_engine():

    matches = [

        HistoricalMatch(

            trading_date=date(2024, 1, 10),

            similarity=0.95,

            return_1d=0.5,

            return_5d=2.0,

            return_10d=3.5,

            max_drawdown=-0.5,

            max_runup=5.0,

        ),

        HistoricalMatch(

            trading_date=date(2024, 2, 10),

            similarity=0.82,

            return_1d=0.2,

            return_5d=1.0,

            return_10d=2.0,

            max_drawdown=-1.0,

            max_runup=3.5,

        ),

    ]

    return HistoricalResearchEngine(

        query=build_query(),

        similarity_engine=SimilarityEngine(matches),

    )


def test_returns_result():

    result = build_engine().calculate()

    assert isinstance(result, HistoricalResearchResult)


def test_match_count():

    assert build_engine().calculate().match_count == 2


def test_average_return():

    assert build_engine().calculate().average_return > 0


def test_expected_value():

    assert build_engine().calculate().expected_value > 0


def test_summary():

    assert isinstance(
        build_engine().calculate().summary(),
        dict,
    )


def test_dict():

    assert isinstance(
        build_engine().calculate().to_dict(),
        dict,
    )


def test_repr():

    assert "HistoricalResearchEngine" in repr(build_engine())