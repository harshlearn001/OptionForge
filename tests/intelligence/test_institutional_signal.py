"""
==============================================================
OptionForge
Institutional Signal Tests
==============================================================
"""

from optionforge.intelligence import InstitutionalSignal

from optionforge.models import (
    DashboardResult,
    InstitutionalSignalResult,
)


def dashboard():

    return DashboardResult(

        dealer_bias="SHORT GAMMA",

        dealer_direction="SHORT DELTA",

        gamma_status="BELOW GAMMA FLIP",

        zero_gamma_status="BELOW ZERO GAMMA",

        hedging_flow="SELL FUTURES",

        institutional_score=15.0,

        confidence="★☆☆☆☆",

        market_bias="TREND FOLLOWING",

        risk_level="EXTREME",

        summary="Demo",
    )


def result():

    return InstitutionalSignal.calculate(

        dashboard=dashboard(),

    )


# ==========================================================
# Result
# ==========================================================

def test_returns_result():

    assert isinstance(

        result(),

        InstitutionalSignalResult,

    )


# ==========================================================
# Signal
# ==========================================================

def test_signal():

    assert result().overall_signal == "STRONG BEARISH"


def test_strength():

    assert result().signal_strength == 15.0


# ==========================================================
# Market
# ==========================================================

def test_market_regime():

    assert result().market_regime == "TREND FOLLOWING"


def test_volatility():

    assert result().volatility_outlook == "EXPANDING"


def test_dealer():

    assert result().dealer_regime == "SHORT GAMMA"


def test_risk():

    assert result().risk_level == "EXTREME"


# ==========================================================
# Trading
# ==========================================================

def test_action():

    assert result().action == "SELL RALLIES"


def test_confidence():

    assert result().confidence == "★☆☆☆☆"


# ==========================================================
# Summary
# ==========================================================

def test_summary():

    assert isinstance(

        result().summary,

        str,

    )


def test_summary_not_empty():

    assert len(

        result().summary,

    ) > 20


# ==========================================================
# Bullish Scenario
# ==========================================================

def test_bullish_case():

    d = dashboard()

    d.market_bias = "MEAN REVERTING"

    d.institutional_score = 90.0

    d.dealer_bias = "LONG GAMMA"

    d.risk_level = "LOW"

    d.confidence = "★★★★★"

    r = InstitutionalSignal.calculate(

        dashboard=d,

    )

    assert r.overall_signal == "STRONG BULLISH"

    assert r.action == "BUY DIPS"

    assert r.market_regime == "MEAN REVERTING"

    assert r.dealer_regime == "LONG GAMMA"

    assert r.volatility_outlook == "STABLE"


# ==========================================================
# Integrity
# ==========================================================

def test_fields():

    r = result()

    assert r.overall_signal
    assert r.market_regime
    assert r.volatility_outlook
    assert r.dealer_regime
    assert r.risk_level
    assert r.confidence
    assert r.action
    assert r.summary


# ==========================================================
# Types
# ==========================================================

def test_string_types():

    r = result()

    assert isinstance(r.overall_signal, str)
    assert isinstance(r.market_regime, str)
    assert isinstance(r.volatility_outlook, str)
    assert isinstance(r.dealer_regime, str)
    assert isinstance(r.risk_level, str)
    assert isinstance(r.action, str)


def test_score_type():

    assert isinstance(

        result().signal_strength,

        float,

    )