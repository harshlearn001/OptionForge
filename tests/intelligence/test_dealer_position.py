"""
============================================================
OptionForge
Dealer Position Intelligence Tests
============================================================
"""

from optionforge.intelligence import DealerPosition

from optionforge.models import (
    GammaExposureResult,
    DeltaExposureResult,
    VannaExposureResult,
    CharmExposureResult,
    DealerPositionResult,
)


# ==========================================================
# Fixtures
# ==========================================================

def make_gamma(net_gex: float):

    return GammaExposureResult(

        total_call_gex=100.0,

        total_put_gex=-150.0,

        net_gex=net_gex,

        largest_positive_strike=25000,

        largest_negative_strike=25100,

        gamma_flip=25050,

        market_regime="DEMO",

        interpretation="Demo",
    )


def make_delta(net_dex: float):

    return DeltaExposureResult(

        total_call_dex=120.0,

        total_put_dex=-180.0,

        net_dex=net_dex,

        largest_positive_strike=25000,

        largest_negative_strike=25100,

        dealer_position="DEMO",

        interpretation="Demo",
    )


def make_vanna(net_vanna: float):

    return VannaExposureResult(

        total_call_vanna=50.0,

        total_put_vanna=-80.0,

        net_vanna=net_vanna,

        largest_positive_strike=25000,

        largest_negative_strike=25100,

        vanna_regime="DEMO",

        interpretation="Demo",
    )


def make_charm(net_charm: float):

    return CharmExposureResult(

        total_call_charm=40.0,

        total_put_charm=-70.0,

        net_charm=net_charm,

        largest_positive_strike=25000,

        largest_negative_strike=25100,

        charm_regime="DEMO",

        interpretation="Demo",
    )


def result():

    return DealerPosition.calculate(

        gamma=make_gamma(-50),

        delta=make_delta(-60),

        vanna=make_vanna(-30),

        charm=make_charm(-30),

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
# Quantitative Fields
# ==========================================================

def test_quantitative_fields():

    r = result()

    assert isinstance(r.dealer_position, float)
    assert isinstance(r.dealer_delta, float)
    assert isinstance(r.dealer_gamma, float)
    assert isinstance(r.net_exposure, float)
    assert isinstance(r.position_strength, float)


# ==========================================================
# Dealer Classification
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
# Institutional Score
# ==========================================================

def test_score_limits():

    score = result().institutional_score

    assert 0.0 <= score <= 100.0


def test_score_type():

    assert isinstance(
        result().institutional_score,
        float,
    )


# ==========================================================
# Confidence
# ==========================================================

def test_confidence():

    assert isinstance(
        result().confidence,
        float,
    )


def test_confidence_limits():

    assert 0.0 <= result().confidence <= 100.0


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
# Result Integrity
# ==========================================================

def test_result_fields():

    r = result()

    assert r.dealer_bias
    assert r.dealer_direction
    assert r.market_condition
    assert r.market_stability
    assert r.directional_risk
    assert r.recommendation
    assert r.interpretation


# ==========================================================
# Alternate Scenario
# ==========================================================

def test_long_gamma():

    r = DealerPosition.calculate(

        gamma=make_gamma(100),

        delta=make_delta(-60),

        vanna=make_vanna(-30),

        charm=make_charm(-30),

    )

    assert r.dealer_bias == "LONG GAMMA"


def test_long_delta():

    r = DealerPosition.calculate(

        gamma=make_gamma(-50),

        delta=make_delta(100),

        vanna=make_vanna(-30),

        charm=make_charm(-30),

    )

    assert r.dealer_direction == "LONG DELTA"


# ==========================================================
# High Stability
# ==========================================================

def test_high_stability():

    r = DealerPosition.calculate(

        gamma=make_gamma(10),

        delta=make_delta(-10),

        vanna=make_vanna(10),

        charm=make_charm(10),

    )

    assert r.market_stability == "HIGH"


# ==========================================================
# Deterministic
# ==========================================================

def test_engine_is_deterministic():

    first = result()

    second = result()

    assert first == second