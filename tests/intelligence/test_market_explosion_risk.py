"""
==============================================================
OptionForge
Market Explosion Risk Tests
==============================================================
"""

from optionforge.intelligence import MarketExplosionRisk

from optionforge.models import (
    DealerPressureResult,
    InstitutionalSignalResult,
    DealerHedgingFlowResult,
    DealerPositionResult,
    MarketExplosionRiskResult,
)


def pressure():

    return DealerPressureResult(

        pressure_score=100.0,

        pressure_level="EXTREME",

        pressure_direction="DOWNSIDE",

        volatility_bias="EXPANDING",

        confidence="★☆☆☆☆",

        interpretation="Demo",
    )


def signal():

    return InstitutionalSignalResult(

        overall_signal="STRONG BEARISH",

        signal_strength=15.0,

        market_regime="TREND FOLLOWING",

        volatility_outlook="EXPANDING",

        dealer_regime="SHORT GAMMA",

        risk_level="EXTREME",

        confidence="★☆☆☆☆",

        action="SELL RALLIES",

        summary="Demo",
    )


def hedging():

    return DealerHedgingFlowResult(

        hedging_bias="PRO-CYCLICAL",

        flow_direction="SELL FUTURES",

        flow_strength="WEAK",

        volatility_effect="VOLATILITY EXPANSION",

        market_support="UNSUPPORTED",

        trend_effect="TREND ACCELERATION",

        institutional_score=15.0,

        confidence="★☆☆☆☆",

        recommendation="Demo",

        interpretation="Demo",
    )


def dealer():

    return DealerPositionResult(

        dealer_bias="SHORT GAMMA",

        dealer_direction="SHORT DELTA",

        market_condition="TRENDING",

        market_stability="LOW",

        directional_risk="VERY HIGH",

        institutional_score=15.0,

        confidence="★☆☆☆☆",

        recommendation="Demo",

        interpretation="Demo",
    )


def result():

    return MarketExplosionRisk.calculate(

        pressure=pressure(),

        signal=signal(),

        hedging=hedging(),

        dealer=dealer(),
    )


# ==========================================================
# Result
# ==========================================================

def test_returns_result():

    assert isinstance(result(), MarketExplosionRiskResult)


# ==========================================================
# Explosion
# ==========================================================

def test_score():

    assert result().explosion_score == 100.0


def test_probability():

    assert result().explosion_probability == "VERY HIGH"


# ==========================================================
# Market
# ==========================================================

def test_market_state():

    assert result().market_state == "CRITICAL"


def test_behavior():

    assert result().expected_behavior == "LARGE TREND EXPANSION"


# ==========================================================
# Recommendation
# ==========================================================

def test_recommendation():

    assert "Reduce leverage" in result().recommendation


# ==========================================================
# Confidence
# ==========================================================

def test_confidence():

    assert result().confidence == "★☆☆☆☆"


# ==========================================================
# Interpretation
# ==========================================================

def test_interpretation():

    assert isinstance(result().interpretation, str)


def test_interpretation_length():

    assert len(result().interpretation) > 20


# ==========================================================
# Low Risk Scenario
# ==========================================================

def test_low_risk():

    p = pressure()
    p.pressure_score = 20.0
    p.pressure_level = "LOW"
    p.pressure_direction = "UPSIDE"
    p.volatility_bias = "STABLE"

    s = signal()
    s.overall_signal = "BULLISH"

    h = hedging()
    h.volatility_effect = "VOLATILITY STABLE"

    d = dealer()
    d.directional_risk = "LOW"

    r = MarketExplosionRisk.calculate(

        pressure=p,

        signal=s,

        hedging=h,

        dealer=d,
    )

    assert r.explosion_probability == "LOW"
    assert r.market_state == "STABLE"
    assert r.expected_behavior == "NORMAL"


# ==========================================================
# Bounds
# ==========================================================

def test_score_bounds():

    assert 0.0 <= result().explosion_score <= 100.0


# ==========================================================
# Types
# ==========================================================

def test_types():

    r = result()

    assert isinstance(r.explosion_score, float)
    assert isinstance(r.explosion_probability, str)
    assert isinstance(r.market_state, str)
    assert isinstance(r.expected_behavior, str)
    assert isinstance(r.recommendation, str)
    assert isinstance(r.confidence, str)
    assert isinstance(r.interpretation, str)