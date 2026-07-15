"""
==============================================================
Tests for ResearchQuery
==============================================================
"""

from optionforge.common.enums import TrendDirection

from optionforge.intelligence.enums.dealer_state import DealerState
from optionforge.intelligence.enums.institutional_state import InstitutionalState
from optionforge.intelligence.enums.volatility_state import VolatilityState

from optionforge.regime.enums.regime_state import RegimeState

from optionforge.research.research_query import ResearchQuery


def build_query():

    return ResearchQuery(

        symbol="NIFTY",

        regime=RegimeState.STRONG_UPTREND,

        institutional_state=InstitutionalState.STRONGLY_BULLISH,

        dealer_state=DealerState.LONG_GAMMA,

        trend=TrendDirection.STRONG_BULLISH,

        volatility=VolatilityState.CHEAP,

        iv_rank=18.4,

        iv_percentile=21.5,

        pcr=1.18,

    )


def test_symbol():

    assert build_query().symbol == "NIFTY"


def test_regime():

    assert build_query().regime is RegimeState.STRONG_UPTREND


def test_summary():

    assert isinstance(
        build_query().summary(),
        dict,
    )


def test_to_dict():

    d = build_query().to_dict()

    assert d["symbol"] == "NIFTY"

    assert d["regime"] == "STRONG_UPTREND"


def test_repr():

    assert "ResearchQuery" in repr(build_query())


def test_iv_rank():

    assert build_query().iv_rank == 18.4


def test_pcr():

    assert build_query().pcr == 1.18


def test_dealer():

    assert (

        build_query().dealer_state

        is DealerState.LONG_GAMMA

    )


def test_volatility():

    assert (

        build_query().volatility

        is VolatilityState.CHEAP

    )