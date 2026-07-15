"""
==============================================================
Tests for ResearchFilter
==============================================================
"""

from optionforge.common.enums import TrendDirection

from optionforge.intelligence.enums.dealer_state import DealerState
from optionforge.intelligence.enums.institutional_state import InstitutionalState
from optionforge.intelligence.enums.volatility_state import VolatilityState

from optionforge.regime.enums.regime_state import RegimeState

from optionforge.research.research_filter import (
    ResearchFilter,
)

from optionforge.research.research_query import (
    ResearchQuery,
)


def build_query():

    return ResearchQuery(

        symbol="NIFTY",

        regime=RegimeState.STRONG_UPTREND,

        institutional_state=InstitutionalState.STRONGLY_BULLISH,

        dealer_state=DealerState.LONG_GAMMA,

        trend=TrendDirection.STRONG_BULLISH,

        volatility=VolatilityState.CHEAP,

        iv_rank=18,

        iv_percentile=20,

        pcr=1.15,

    )


def test_match():

    assert ResearchFilter.matches(

        build_query(),

        build_query(),

    )


def test_symbol():

    q = build_query()

    c = build_query()

    c = ResearchQuery(

        symbol="BANKNIFTY",

        regime=c.regime,

        institutional_state=c.institutional_state,

        dealer_state=c.dealer_state,

        trend=c.trend,

        volatility=c.volatility,

        iv_rank=c.iv_rank,

        iv_percentile=c.iv_percentile,

        pcr=c.pcr,

    )

    assert not ResearchFilter.matches(q, c)


def test_regime():

    q = build_query()

    c = build_query()

    c = ResearchQuery(

        symbol=c.symbol,

        regime=RegimeState.DOWNTREND,

        institutional_state=c.institutional_state,

        dealer_state=c.dealer_state,

        trend=c.trend,

        volatility=c.volatility,

        iv_rank=c.iv_rank,

        iv_percentile=c.iv_percentile,

        pcr=c.pcr,

    )

    assert not ResearchFilter.matches(q, c)


def test_institutional():

    q = build_query()

    c = build_query()

    c = ResearchQuery(

        symbol=c.symbol,

        regime=c.regime,

        institutional_state=InstitutionalState.BEARISH,

        dealer_state=c.dealer_state,

        trend=c.trend,

        volatility=c.volatility,

        iv_rank=c.iv_rank,

        iv_percentile=c.iv_percentile,

        pcr=c.pcr,

    )

    assert not ResearchFilter.matches(q, c)


def test_dealer():

    q = build_query()

    c = build_query()

    c = ResearchQuery(

        symbol=c.symbol,

        regime=c.regime,

        institutional_state=c.institutional_state,

        dealer_state=DealerState.SHORT_GAMMA,

        trend=c.trend,

        volatility=c.volatility,

        iv_rank=c.iv_rank,

        iv_percentile=c.iv_percentile,

        pcr=c.pcr,

    )

    assert not ResearchFilter.matches(q, c)


def test_repr():

    assert "ResearchFilter" in repr(ResearchFilter())