"""
==============================================================
OptionForge
Delta Exposure Tests
==============================================================
"""

import pytest

from optionforge.intelligence import DeltaExposure
from optionforge.models import DeltaExposureResult


def sample_chain():

    return [

        {
            "strike": 25000,
            "option_type": "CE",
            "delta": 0.55,
            "open_interest": 150000,
            "lot_size": 75,
        },

        {
            "strike": 25000,
            "option_type": "PE",
            "delta": -0.45,
            "open_interest": 120000,
            "lot_size": 75,
        },

        {
            "strike": 25100,
            "option_type": "CE",
            "delta": 0.38,
            "open_interest": 80000,
            "lot_size": 75,
        },

        {
            "strike": 24900,
            "option_type": "PE",
            "delta": -0.62,
            "open_interest": 140000,
            "lot_size": 75,
        },

    ]


def result():

    return DeltaExposure.calculate(
        spot_price=25000,
        option_chain=sample_chain(),
    )


def test_returns_result():

    assert isinstance(
        result(),
        DeltaExposureResult,
    )


def test_call_dex_positive():

    assert result().total_call_dex > 0


def test_put_dex_negative():

    assert result().total_put_dex < 0


def test_net_dex_float():

    assert isinstance(
        result().net_dex,
        float,
    )


def test_positive_strike():

    assert result().largest_positive_strike == 25000


def test_negative_strike():

    assert result().largest_negative_strike == 25100


def test_dealer_position():

    assert result().dealer_position in (
        "LONG DELTA",
        "SHORT DELTA",
    )


def test_interpretation():

    assert isinstance(
        result().interpretation,
        str,
    )


def test_invalid_spot():

    with pytest.raises(ValueError):

        DeltaExposure.calculate(
            spot_price=0,
            option_chain=sample_chain(),
        )


def test_negative_spot():

    with pytest.raises(ValueError):

        DeltaExposure.calculate(
            spot_price=-1,
            option_chain=sample_chain(),
        )


def test_empty_chain():

    with pytest.raises(ValueError):

        DeltaExposure.calculate(
            spot_price=25000,
            option_chain=[],
        )


def test_unknown_option_type():

    bad = sample_chain()

    bad[0]["option_type"] = "XX"

    with pytest.raises(ValueError):

        DeltaExposure.calculate(
            spot_price=25000,
            option_chain=bad,
        )


def test_net_equals_sum():

    r = result()

    assert r.net_dex == pytest.approx(
        r.total_call_dex + r.total_put_dex
    )


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


def test_dealer_position_type():

    assert isinstance(
        result().dealer_position,
        str,
    )


def test_interpretation_not_empty():

    assert len(
        result().interpretation
    ) > 10


def test_large_spot():

    r = DeltaExposure.calculate(
        spot_price=50000,
        option_chain=sample_chain(),
    )

    assert r.total_call_dex > 0


def test_call_not_zero():

    assert result().total_call_dex != 0


def test_put_not_zero():

    assert result().total_put_dex != 0


def test_net_not_zero():

    assert result().net_dex != 0


def test_result_fields():

    r = result()

    assert r.total_call_dex is not None
    assert r.total_put_dex is not None
    assert r.net_dex is not None
    assert r.dealer_position is not None
    assert r.interpretation is not None