"""
==============================================================
Tests for RegimeClassifier
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

from optionforge.regime.enums.regime_state import (
    RegimeState,
)

from optionforge.regime.regime_classifier import (
    RegimeClassifier,
)


def test_strong_uptrend():

    regime = RegimeClassifier.classify(

        institutional_state=InstitutionalState.STRONGLY_BULLISH,

        trend=TrendDirection.STRONG_BULLISH,

        volatility=VolatilityState.FAIR,
        dealer_state=DealerState.LONG_GAMMA,

    )

    assert regime is RegimeState.STRONG_UPTREND


def test_uptrend():

    regime = RegimeClassifier.classify(

        institutional_state=InstitutionalState.BULLISH,

        trend=TrendDirection.BULLISH,

        volatility=VolatilityState.FAIR,

        dealer_state=DealerState.NEUTRAL,

    )

    assert regime is RegimeState.UPTREND


def test_strong_downtrend():

    regime = RegimeClassifier.classify(

        institutional_state=InstitutionalState.STRONGLY_BEARISH,

        trend=TrendDirection.STRONG_BEARISH,

        volatility=VolatilityState.FAIR,
        dealer_state=DealerState.SHORT_GAMMA,

    )

    assert regime is RegimeState.STRONG_DOWNTREND


def test_downtrend():

    regime = RegimeClassifier.classify(

        institutional_state=InstitutionalState.BEARISH,

        trend=TrendDirection.BEARISH,

        volatility=VolatilityState.FAIR,

        dealer_state=DealerState.NEUTRAL,

    )

    assert regime is RegimeState.DOWNTREND


def test_volatility_expansion():

    regime = RegimeClassifier.classify(

        institutional_state=InstitutionalState.NEUTRAL,

        trend=TrendDirection.SIDEWAYS,

        volatility=VolatilityState.EXPENSIVE,

        dealer_state=DealerState.NEUTRAL,

    )

    assert regime is RegimeState.VOLATILITY_EXPANSION


def test_volatility_compression():

    regime = RegimeClassifier.classify(

        institutional_state=InstitutionalState.NEUTRAL,

        trend=TrendDirection.SIDEWAYS,

        volatility=VolatilityState.CHEAP,

        dealer_state=DealerState.NEUTRAL,

    )

    assert regime is RegimeState.VOLATILITY_COMPRESSION


def test_range_bound():

    regime = RegimeClassifier.classify(

        institutional_state=InstitutionalState.NEUTRAL,

        trend=TrendDirection.SIDEWAYS,

        volatility=VolatilityState.FAIR,

        dealer_state=DealerState.NEUTRAL,

    )

    assert regime is RegimeState.RANGE_BOUND