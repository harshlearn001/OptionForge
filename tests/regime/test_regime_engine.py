"""
==============================================================
Tests for RegimeEngine
==============================================================
"""

from optionforge.common.enums import TrendDirection

from optionforge.intelligence.enums.dealer_state import (
    DealerState,
)
from optionforge.intelligence.enums.institutional_state import (
    InstitutionalState,
)
from optionforge.intelligence.enums.volatility_state import (
    VolatilityState,
)

from optionforge.regime.regime_engine import (
    RegimeEngine,
)
from optionforge.regime.regime_result import (
    RegimeResult,
)


def build_engine():

    return RegimeEngine(

        institutional_state=InstitutionalState.STRONGLY_BULLISH,

        trend=TrendDirection.STRONG_BULLISH,

        volatility=VolatilityState.FAIR,

        dealer_state=DealerState.LONG_GAMMA,

        institutional_score=0.90,

        trend_score=0.85,

        dealer_score=0.80,

        volatility_score=0.75,

    )


# ==========================================================
# Result
# ==========================================================

def test_returns_result():

    result = build_engine().calculate()

    assert isinstance(result, RegimeResult)


def test_regime():

    result = build_engine().calculate()

    assert result.regime.name == "STRONG_UPTREND"


def test_confidence():

    result = build_engine().calculate()

    assert result.confidence > 0


def test_trending():

    assert build_engine().calculate().is_trending()


def test_bullish():

    assert build_engine().calculate().is_bullish()


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

    assert "RegimeEngine" in repr(build_engine())