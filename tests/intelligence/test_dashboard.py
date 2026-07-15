"""
==============================================================
OptionForge
Dashboard Tests
==============================================================
"""

from optionforge.intelligence import Dashboard
from dataclasses import replace
from optionforge.models import (
    DashboardResult,
    DealerPositionResult,
    GammaFlipResult,
    ZeroGammaResult,
    DealerHedgingFlowResult,
)


def dealer():

    return DealerPositionResult(
        # --------------------------------------------------
        # Quantitative Metrics
        # --------------------------------------------------
        dealer_position=-250000.0,
        dealer_delta=-18500.0,
        dealer_gamma=-4200.0,
        net_exposure=-268700.0,
        position_strength=82.0,
        institutional_score=15.0,
        # --------------------------------------------------
        # Classification
        # --------------------------------------------------
        dealer_bias="SHORT GAMMA",
        dealer_direction="SHORT DELTA",
        market_condition="TRENDING",
        market_stability="LOW",
        directional_risk="VERY HIGH",
        # --------------------------------------------------
        # Decision Support
        # --------------------------------------------------
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


def result():

    return Dashboard.calculate(
        dealer=dealer(),
        gamma_flip=gamma_flip(),
        zero_gamma=zero_gamma(),
        hedging=hedging(),
    )


# ==========================================================
# Result
# ==========================================================


def test_returns_result():

    assert isinstance(result(), DashboardResult)


# ==========================================================
# Dealer
# ==========================================================


def test_dealer_bias():

    assert result().dealer_bias == "SHORT GAMMA"


def test_dealer_direction():

    assert result().dealer_direction == "SHORT DELTA"


# ==========================================================
# Status
# ==========================================================


def test_gamma_status():

    assert result().gamma_status == "BELOW GAMMA FLIP"


def test_zero_gamma_status():

    assert result().zero_gamma_status == "BELOW ZERO GAMMA"


# ==========================================================
# Flow
# ==========================================================


def test_hedging_flow():

    assert result().hedging_flow == "SELL FUTURES"


# ==========================================================
# Score
# ==========================================================


def test_score():

    assert result().institutional_score == 15.0


def test_score_type():

    assert isinstance(result().institutional_score, float)


# ==========================================================
# Confidence
# ==========================================================


def test_confidence():

    assert result().confidence == 0.15


# ==========================================================
# Market
# ==========================================================


def test_market_bias():

    assert result().market_bias == "TREND FOLLOWING"


def test_risk():

    assert result().risk_level == "EXTREME"


# ==========================================================
# Summary
# ==========================================================


def test_summary():

    assert isinstance(result().summary, str)


def test_summary_not_empty():

    assert len(result().summary) > 20


# ==========================================================
# Alternate Scenario
# ==========================================================


def test_mean_reversion():

    d = replace(
        dealer(),
        dealer_bias="LONG GAMMA",
        dealer_direction="LONG DELTA",
        institutional_score=95.0,
    )

    h = replace(
        hedging(),
        flow_direction="BUY WEAKNESS",
    )

    r = Dashboard.calculate(
        dealer=d,
        gamma_flip=gamma_flip(),
        zero_gamma=zero_gamma(),
        hedging=h,
    )

    assert r.market_bias == "MEAN REVERTING"

    assert r.risk_level == "LOW"


# ==========================================================
# Integrity
# ==========================================================


def test_fields():

    r = result()

    assert r.dealer_bias
    assert r.dealer_direction
    assert r.gamma_status
    assert r.zero_gamma_status
    assert r.hedging_flow
    assert r.confidence
    assert r.market_bias
    assert r.risk_level
    assert r.summary


# ==========================================================
# Types
# ==========================================================


def test_string_types():

    r = result()

    assert isinstance(r.dealer_bias, str)
    assert isinstance(r.dealer_direction, str)
    assert isinstance(r.gamma_status, str)
    assert isinstance(r.zero_gamma_status, str)
    assert isinstance(r.hedging_flow, str)
    assert isinstance(r.market_bias, str)
    assert isinstance(r.risk_level, str)
