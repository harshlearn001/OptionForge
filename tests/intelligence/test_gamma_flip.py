"""
==============================================================
OptionForge
Gamma Flip Tests
==============================================================
"""

from optionforge.intelligence import GammaFlip

from optionforge.models import (
    GammaExposureResult,
    GammaFlipResult,
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

    return GammaFlip.calculate(

        gamma=gamma(),

        current_spot=24980.0,

    )


# ==========================================================
# Result
# ==========================================================

def test_returns_result():

    assert isinstance(

        result(),

        GammaFlipResult,

    )


# ==========================================================
# Values
# ==========================================================

def test_gamma_flip():

    assert result().gamma_flip == 25050.0


def test_current_spot():

    assert result().current_spot == 24980.0


def test_distance():

    assert result().distance == -70.0


# ==========================================================
# Status
# ==========================================================

def test_flip_status():

    assert result().flip_status == "BELOW GAMMA FLIP"


def test_dealer_regime():

    assert result().dealer_regime == "NEGATIVE GAMMA"


# ==========================================================
# Above Flip
# ==========================================================

def test_above_flip():

    r = GammaFlip.calculate(

        gamma=gamma(),

        current_spot=25120.0,

    )

    assert r.flip_status == "ABOVE GAMMA FLIP"

    assert r.dealer_regime == "POSITIVE GAMMA"

    assert r.distance == 70.0


# ==========================================================
# At Flip
# ==========================================================

def test_at_flip():

    r = GammaFlip.calculate(

        gamma=gamma(),

        current_spot=25050.0,

    )

    assert r.flip_status == "AT GAMMA FLIP"

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

def test_positive_gamma():

    r = GammaFlip.calculate(

        gamma=gamma(),

        current_spot=26000.0,

    )

    assert r.dealer_regime == "POSITIVE GAMMA"


def test_negative_gamma():

    r = GammaFlip.calculate(

        gamma=gamma(),

        current_spot=24000.0,

    )

    assert r.dealer_regime == "NEGATIVE GAMMA"


# ==========================================================
# Distance
# ==========================================================

def test_distance_positive():

    r = GammaFlip.calculate(

        gamma=gamma(),

        current_spot=25200.0,

    )

    assert r.distance > 0


def test_distance_negative():

    r = GammaFlip.calculate(

        gamma=gamma(),

        current_spot=24800.0,

    )

    assert r.distance < 0


def test_distance_zero():

    r = GammaFlip.calculate(

        gamma=gamma(),

        current_spot=25050.0,

    )

    assert r.distance == 0


# ==========================================================
# Integrity
# ==========================================================

def test_fields():

    r = result()

    assert r.gamma_flip
    assert r.current_spot
    assert isinstance(r.distance, float)
    assert r.flip_status
    assert r.dealer_regime
    assert r.interpretation


def test_distance_type():

    assert isinstance(

        result().distance,

        float,

    )


def test_flip_status_type():

    assert isinstance(

        result().flip_status,

        str,

    )


def test_regime_type():

    assert isinstance(

        result().dealer_regime,

        str,

    )