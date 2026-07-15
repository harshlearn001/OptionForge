"""
==============================================================
OptionForge
Dealer Hedging Flow Tests
==============================================================
"""

from optionforge.intelligence import DealerHedgingFlow
from dataclasses import replace
from optionforge.models import (
    DealerHedgingFlowResult,
    DealerPositionResult,
    GammaFlipResult,
    ZeroGammaResult,
)


def dealer():

    return DealerPositionResult(
        # ==================================================
        # Quantitative Metrics
        # ==================================================
        dealer_position=-250000.0,
        dealer_delta=-18500.0,
        dealer_gamma=-4200.0,
        net_exposure=-268700.0,
        position_strength=82.0,
        institutional_score=15.0,
        # ==================================================
        # Classification
        # ==================================================
        dealer_bias="SHORT GAMMA",
        dealer_direction="SHORT DELTA",
        market_condition="TRENDING",
        market_stability="LOW",
        directional_risk="VERY HIGH",
        # ==================================================
        # Decision Support
        # ==================================================
        confidence=0.15,
        recommendation="Demo",
        interpretation="Demo",
    )


def gamma_flip():

    return GammaFlipResult(
        gamma_flip=25050.0,
        current_spot=24980.0,
        distance=-70.0,
        flip_status="BELOW GAMMA FLIP",
        dealer_regime="NEGATIVE GAMMA",
        interpretation="Demo",
    )


def zero_gamma():

    return ZeroGammaResult(
        zero_gamma=25050.0,
        current_spot=24980.0,
        distance=-70.0,
        status="BELOW ZERO GAMMA",
        dealer_regime="UNSTABLE",
        interpretation="Demo",
    )


def result():

    return DealerHedgingFlow.calculate(
        dealer=dealer(),
        gamma_flip=gamma_flip(),
        zero_gamma=zero_gamma(),
    )


# ==========================================================
# Result
# ==========================================================


def test_returns_result():

    assert isinstance(
        result(),
        DealerHedgingFlowResult,
    )


# ==========================================================
# Bias
# ==========================================================


def test_hedging_bias():

    assert result().hedging_bias == "PRO-CYCLICAL"


def test_flow_direction():

    assert result().flow_direction == "SELL FUTURES"


def test_flow_strength():

    assert result().flow_strength == "WEAK"


# ==========================================================
# Market
# ==========================================================


def test_volatility_effect():

    assert result().volatility_effect == "VOLATILITY EXPANSION"


def test_market_support():

    assert result().market_support == "UNSUPPORTED"


def test_trend_effect():

    assert result().trend_effect == "TREND ACCELERATION"


# ==========================================================
# Score
# ==========================================================


def test_score():

    assert result().institutional_score == 15.0


def test_score_type():

    assert isinstance(
        result().institutional_score,
        float,
    )


# ==========================================================
# Confidence
# ==========================================================


def test_confidence():

    assert isinstance(result().confidence, str)
    assert len(result().confidence) > 0


# ==========================================================
# Recommendation
# ==========================================================


def test_recommendation():

    assert isinstance(
        result().recommendation,
        str,
    )


def test_interpretation():

    assert isinstance(
        result().interpretation,
        str,
    )


# ==========================================================
# Alternate Scenario
# ==========================================================

from dataclasses import replace


def test_long_gamma():

    d = replace(
        dealer(),
        dealer_bias="LONG GAMMA",
        dealer_direction="LONG DELTA",
        institutional_score=90.0,
    )

    g = replace(
        gamma_flip(),
        dealer_regime="POSITIVE GAMMA",
    )

    z = replace(
        zero_gamma(),
        dealer_regime="STABLE",
    )

    r = DealerHedgingFlow.calculate(
        dealer=d,
        gamma_flip=g,
        zero_gamma=z,
    )

    assert r.hedging_bias == "CONTRARIAN"

    assert r.flow_direction == "BUY WEAKNESS"

    assert r.flow_strength == "VERY STRONG"

    assert r.market_support == "SUPPORTED"

    assert r.volatility_effect == "VOLATILITY SUPPRESSION"

    assert r.trend_effect == "MEAN REVERSION"


# ==========================================================
# Integrity
# ==========================================================


def test_fields():

    r = result()

    assert r.hedging_bias
    assert r.flow_direction
    assert r.flow_strength
    assert r.volatility_effect
    assert r.market_support
    assert r.trend_effect
    assert r.confidence
    assert r.recommendation
    assert r.interpretation


def test_confidence_not_empty():

    assert len(result().confidence) > 0


def test_recommendation_not_empty():

    assert len(result().recommendation) > 10


def test_interpretation_not_empty():

    assert len(result().interpretation) > 10


# ==========================================================
# Types
# ==========================================================


def test_string_types():

    r = result()

    assert isinstance(r.hedging_bias, str)
    assert isinstance(r.flow_direction, str)
    assert isinstance(r.flow_strength, str)
    assert isinstance(r.volatility_effect, str)
    assert isinstance(r.market_support, str)
    assert isinstance(r.trend_effect, str)
