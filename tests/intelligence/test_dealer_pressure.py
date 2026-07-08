"""
==============================================================
OptionForge
Dealer Pressure Tests
==============================================================
"""

from os import replace
from dataclasses import replace
from optionforge.intelligence import DealerPressure

from optionforge.models import (
    DealerPositionResult,
    DealerHedgingFlowResult,
    InstitutionalSignalResult,
    DealerPressureResult,
)


def dealer():

    return DealerPositionResult(

        # Quantitative Metrics
        dealer_position=-250000.0,
        dealer_delta=-18500.0,
        dealer_gamma=-4200.0,
        net_exposure=-268700.0,
        position_strength=92.0,
        institutional_score=15.0,

        # Classification
        dealer_bias="SHORT GAMMA",
        dealer_direction="SHORT DELTA",
        market_condition="TRENDING",
        market_stability="LOW",
        directional_risk="VERY HIGH",

        # Decision Support
        confidence=0.15,
        recommendation="Demo",
        interpretation="Demo",
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


def result():

    return DealerPressure.calculate(

        dealer=dealer(),

        hedging=hedging(),

        signal=signal(),
    )


# ==========================================================
# Result
# ==========================================================

def test_returns_result():

    assert isinstance(result(), DealerPressureResult)


# ==========================================================
# Pressure
# ==========================================================

def test_pressure_score():

    assert result().pressure_score == 100.0


def test_pressure_level():

    assert result().pressure_level == "EXTREME"


# ==========================================================
# Direction
# ==========================================================

def test_direction():

    assert result().pressure_direction == "DOWNSIDE"


# ==========================================================
# Volatility
# ==========================================================

def test_volatility():

    assert result().volatility_bias == "EXPANDING"


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


def test_interpretation_not_empty():

    assert len(result().interpretation) > 20


# ==========================================================
# Low Pressure Scenario
# ==========================================================

def test_low_pressure():
 
    d = replace(
        dealer(),
        dealer_bias="LONG GAMMA",
        dealer_direction="LONG DELTA",
    )

    h = replace(
        hedging(),
        hedging_bias="COUNTER-CYCLICAL",
        volatility_effect="VOLATILITY STABLE",
    )

    s = replace(
        signal(),
        overall_signal="BULLISH",
    )

    r = DealerPressure.calculate(

        dealer=d,

        hedging=h,

        signal=s,
    )

    assert r.pressure_level == "LOW"

    assert r.pressure_direction == "UPSIDE"

    assert r.volatility_bias == "STABLE"


# ==========================================================
# Integrity
# ==========================================================

def test_fields():

    r = result()

    assert r.pressure_score
    assert r.pressure_level
    assert r.pressure_direction
    assert r.volatility_bias
    assert r.confidence
    assert r.interpretation


# ==========================================================
# Types
# ==========================================================

def test_types():

    r = result()

    assert isinstance(r.pressure_score, float)
    assert isinstance(r.pressure_level, str)
    assert isinstance(r.pressure_direction, str)
    assert isinstance(r.volatility_bias, str)
    assert isinstance(r.confidence, str)
    assert isinstance(r.interpretation, str)


# ==========================================================
# Bounds
# ==========================================================

def test_score_bounds():

    assert 0.0 <= result().pressure_score <= 100.0
    