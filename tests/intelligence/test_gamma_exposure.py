"""
==============================================================
OptionForge
Gamma Exposure Tests
==============================================================
"""

import pytest

from optionforge.intelligence import GammaExposure
from optionforge.models import GammaExposureResult


def sample_chain():

    return [

        {
            "strike": 25000,
            "option_type": "CE",
            "gamma": 0.0018,
            "open_interest": 150000,
            "lot_size": 75,
        },

        {
            "strike": 25000,
            "option_type": "PE",
            "gamma": 0.0015,
            "open_interest": 120000,
            "lot_size": 75,
        },

        {
            "strike": 25100,
            "option_type": "CE",
            "gamma": 0.0012,
            "open_interest": 80000,
            "lot_size": 75,
        },

        {
            "strike": 24900,
            "option_type": "PE",
            "gamma": 0.0019,
            "open_interest": 140000,
            "lot_size": 75,
        },

    ]


def result():

    return GammaExposure.calculate(
        spot_price=25000,
        option_chain=sample_chain(),
    )


def test_returns_result():

    assert isinstance(
        result(),
        GammaExposureResult,
    )


def test_call_gex_positive():

    assert result().total_call_gex > 0


def test_put_gex_positive():

    assert result().total_put_gex > 0


def test_net_gex_is_float():

    assert isinstance(
        result().net_gex,
        float,
    )


def test_positive_strike():

    assert result().largest_positive_strike == 25000


def test_negative_strike():

    assert result().largest_negative_strike == 25100


def test_market_regime():

    assert result().market_regime in (
        "POSITIVE GAMMA",
        "NEGATIVE GAMMA",
    )


def test_interpretation():

    assert isinstance(
        result().interpretation,
        str,
    )


def test_gamma_flip_default():

    assert result().gamma_flip == 0


def test_invalid_spot():

    with pytest.raises(ValueError):

        GammaExposure.calculate(
            spot_price=0,
            option_chain=sample_chain(),
        )


def test_negative_spot():

    with pytest.raises(ValueError):

        GammaExposure.calculate(
            spot_price=-100,
            option_chain=sample_chain(),
        )


def test_empty_chain():

    with pytest.raises(ValueError):

        GammaExposure.calculate(
            spot_price=25000,
            option_chain=[],
        )


def test_call_greater_than_zero():

    assert result().total_call_gex > 0


def test_put_greater_than_zero():

    assert result().total_put_gex > 0


def test_regime_type():

    assert isinstance(
        result().market_regime,
        str,
    )


def test_interpretation_not_empty():

    assert len(
        result().interpretation
    ) > 10


def test_positive_strike_float():

    assert isinstance(
        result().largest_positive_strike,
        float,
    )


def test_negative_strike_float():

    assert isinstance(
        result().largest_negative_strike,
        float,
    )


def test_net_equals_difference():

    r = result()

    assert r.net_gex == pytest.approx(
        r.total_call_gex - r.total_put_gex
    )


def test_result_fields():

    r = result()

    assert r.total_call_gex is not None
    assert r.total_put_gex is not None
    assert r.net_gex is not None
    assert r.market_regime is not None
    assert r.interpretation is not None


def test_large_numbers():

    r = GammaExposure.calculate(
        spot_price=50000,
        option_chain=sample_chain(),
    )

    assert r.total_call_gex > 0