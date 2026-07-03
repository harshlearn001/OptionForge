"""
==============================================================
OptionForge
Dealer Position Tests
==============================================================
"""

import pytest

from optionforge.intelligence import DealerPosition

from optionforge.models import (
    GammaExposureResult,
    DeltaExposureResult,
    VannaExposureResult,
    CharmExposureResult,
    DealerPositionResult,
)


def gamma():

    return GammaExposureResult(

        total_call_gex=100,

        total_put_gex=-150,

        net_gex=-50,

        largest_positive_strike=25000,

        largest_negative_strike=25100,

        gamma_flip=25050,

        market_regime="NEGATIVE GAMMA",

        interpretation="Demo",
    )


def delta():

    return DeltaExposureResult(

        total_call_dex=120,

        total_put_dex=-180,

        net_dex=-60,

        largest_positive_strike=25000,

        largest_negative_strike=25100,

        dealer_position="SHORT DELTA",

        interpretation="Demo",
    )


def vanna():

    return VannaExposureResult(

        total_call_vanna=50,

        total_put_vanna=-80,

        net_vanna=-30,

        largest_positive_strike=25000,

        largest_negative_strike=25100,

        vanna_regime="NEGATIVE VANNA",

        interpretation="Demo",
    )


def charm():

    return CharmExposureResult(

        total_call_charm=40,

        total_put_charm=-70,

        net_charm=-30,

        largest_positive_strike=25000,

        largest_negative_strike=25100,

        charm_regime="NEGATIVE CHARM",

        interpretation="Demo",
    )


def result():

    return DealerPosition.calculate(

        gamma=gamma(),

        delta=delta(),

        vanna=vanna(),

        charm=charm(),
    )


# ==========================================================
# Result
# ==========================================================

def test_returns_result():

    assert isinstance(
        result(),
        DealerPositionResult,
    )


# ==========================================================
# Dealer Bias
# ==========================================================

def test_dealer_bias():

    assert result().dealer_bias == "SHORT GAMMA"


def test_dealer_direction():

    assert result().dealer_direction == "SHORT DELTA"


# ==========================================================
# Market
# ==========================================================

def test_market_condition():

    assert result().market_condition == "TRENDING"


def test_market_stability():

    assert result().market_stability == "LOW"


def test_directional_risk():

    assert result().directional_risk == "VERY HIGH"


# ==========================================================
# Score
# ==========================================================

def test_score():

    assert result().institutional_score == 15


def test_score_type():

    assert isinstance(
        result().institutional_score,
        float,
    )


# ==========================================================
# Confidence
# ==========================================================

def test_confidence():

    assert result().confidence == "★☆☆☆☆"


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
# Integrity
# ==========================================================

def test_result_fields():

    r = result()

    assert r.dealer_bias
    assert r.dealer_direction
    assert r.market_condition
    assert r.market_stability
    assert r.directional_risk
    assert r.confidence
    assert r.recommendation
    assert r.interpretation


# ==========================================================
# Alternate Scenario
# ==========================================================

def test_long_gamma():

    g = gamma()

    g.net_gex = 100

    r = DealerPosition.calculate(

        gamma=g,

        delta=delta(),

        vanna=vanna(),

        charm=charm(),

    )

    assert r.dealer_bias == "LONG GAMMA"


def test_long_delta():

    d = delta()

    d.net_dex = 100

    r = DealerPosition.calculate(

        gamma=gamma(),

        delta=d,

        vanna=vanna(),

        charm=charm(),

    )

    assert r.dealer_direction == "LONG DELTA"


# ==========================================================
# Stability
# ==========================================================

def test_high_stability():

    g = gamma()
    g.net_gex = 10

    d = delta()

    v = vanna()
    v.net_vanna = 10

    c = charm()
    c.net_charm = 10

    r = DealerPosition.calculate(

        gamma=g,

        delta=d,

        vanna=v,

        charm=c,

    )

    assert r.market_stability == "HIGH"


# ==========================================================
# Score Limits
# ==========================================================

def test_score_limits():

    r = result()

    assert 0 <= r.institutional_score <= 100


def test_confidence_not_empty():

    assert len(result().confidence) > 0


def test_recommendation_not_empty():

    assert len(result().recommendation) > 10


def test_interpretation_not_empty():

    assert len(result().interpretation) > 10