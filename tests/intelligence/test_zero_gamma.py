"""
==============================================================
OptionForge
Zero Gamma Tests
==============================================================
"""

from optionforge.intelligence import ZeroGamma

from optionforge.models import (
    GammaExposureResult,
    ZeroGammaResult,
)


def gamma():

    return GammaExposureResult(

        total_call_gex=171562500000.0,

        total_put_gex=209062500000.0,

        net_gex=-37500000000.0,

        largest_positive_strike=25000.0,

        largest_negative_strike=25100.0,

        gamma_flip=25050.0,

        market_regime="NEGATIVE GAMMA",

        interpretation="Demo",
    )


def result():

    return ZeroGamma.calculate(

        gamma=gamma(),

        current_spot=24980.0,

    )


# ==========================================================
# Result
# ==========================================================

def test_returns_result():

    assert isinstance(

        result(),

        ZeroGammaResult,

    )


# ==========================================================
# Values
# ==========================================================

def test_zero_gamma():

    assert result().zero_gamma == 25050.0


def test_current_spot():

    assert result().current_spot == 24980.0


def test_distance():

    assert result().distance == -70.0


# ==========================================================
# Status
# ==========================================================

def test_status():

    assert result().status == "BELOW ZERO GAMMA"


def test_dealer_regime():

    assert result().dealer_regime == "UNSTABLE"


# ==========================================================
# Above Zero Gamma
# ==========================================================

def test_above_zero_gamma():

    r = ZeroGamma.calculate(

        gamma=gamma(),

        current_spot=25120.0,

    )

    assert r.status == "ABOVE ZERO GAMMA"

    assert r.dealer_regime == "STABLE"

    assert r.distance == 70.0


# ==========================================================
# At Zero Gamma
# ==========================================================

def test_at_zero_gamma():

    r = ZeroGamma.calculate(

        gamma=gamma(),

        current_spot=25050.0,

    )

    assert r.status == "AT ZERO GAMMA"

    assert r.distance == 0.0


# ==========================================================
# Interpretation
# ==========================================================

def test_interpretation():

    assert isinstance(

        result().interpretation,

        str,

    )


def test_interpretation_not_empty():

    assert len(

        result().interpretation

    ) > 20


# ==========================================================
# Dealer Regime
# ==========================================================

def test_stable_regime():

    r = ZeroGamma.calculate(

        gamma=gamma(),

        current_spot=26000.0,

    )

    assert r.dealer_regime == "STABLE"


def test_unstable_regime():

    r = ZeroGamma.calculate(

        gamma=gamma(),

        current_spot=24000.0,

    )

    assert r.dealer_regime == "UNSTABLE"


# ==========================================================
# Distance
# ==========================================================

def test_positive_distance():

    r = ZeroGamma.calculate(

        gamma=gamma(),

        current_spot=25200.0,

    )

    assert r.distance > 0


def test_negative_distance():

    r = ZeroGamma.calculate(

        gamma=gamma(),

        current_spot=24800.0,

    )

    assert r.distance < 0


def test_zero_distance():

    r = ZeroGamma.calculate(

        gamma=gamma(),

        current_spot=25050.0,

    )

    assert r.distance == 0


# ==========================================================
# Integrity
# ==========================================================

def test_fields():

    r = result()

    assert r.zero_gamma
    assert r.current_spot
    assert isinstance(r.distance, float)
    assert r.status
    assert r.dealer_regime
    assert r.interpretation


def test_distance_type():

    assert isinstance(

        result().distance,

        float,

    )


def test_status_type():

    assert isinstance(

        result().status,

        str,

    )


def test_regime_type():

    assert isinstance(

        result().dealer_regime,

        str,

    )