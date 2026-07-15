"""
==============================================================
OptionForge
Vanna Exposure Tests
==============================================================
"""

import pytest

from optionforge.intelligence import VannaExposure
from optionforge.models import VannaExposureResult


def sample_chain():

    return [
        {
            "strike": 25000,
            "option_type": "CE",
            "vanna": 0.18,
            "open_interest": 150000,
            "lot_size": 75,
        },
        {
            "strike": 25000,
            "option_type": "PE",
            "vanna": -0.15,
            "open_interest": 120000,
            "lot_size": 75,
        },
        {
            "strike": 25100,
            "option_type": "CE",
            "vanna": 0.12,
            "open_interest": 90000,
            "lot_size": 75,
        },
        {
            "strike": 24900,
            "option_type": "PE",
            "vanna": -0.21,
            "open_interest": 140000,
            "lot_size": 75,
        },
    ]


def result():

    return VannaExposure.calculate(
        spot_price=25000,
        option_chain=sample_chain(),
    )


def test_returns_result():

    assert isinstance(
        result(),
        VannaExposureResult,
    )


def test_call_vanna_positive():

    assert result().total_call_vanna > 0


def test_put_vanna_negative():

    assert result().total_put_vanna < 0


def test_net_vanna_float():

    assert isinstance(
        result().net_vanna,
        float,
    )


def test_net_identity():

    r = result()

    assert r.net_vanna == pytest.approx(r.total_call_vanna + r.total_put_vanna)


def test_positive_strike():

    assert result().largest_positive_strike == 25000


def test_negative_strike():

    assert result().largest_negative_strike == 25100


def test_regime():

    assert result().vanna_regime in (
        "POSITIVE VANNA",
        "NEGATIVE VANNA",
    )


def test_interpretation():

    assert isinstance(
        result().interpretation,
        str,
    )


def test_invalid_spot():

    with pytest.raises(ValueError):

        VannaExposure.calculate(
            spot_price=0,
            option_chain=sample_chain(),
        )


def test_negative_spot():

    with pytest.raises(ValueError):

        VannaExposure.calculate(
            spot_price=-1,
            option_chain=sample_chain(),
        )


def test_empty_chain():

    with pytest.raises(ValueError):

        VannaExposure.calculate(
            spot_price=25000,
            option_chain=[],
        )


def test_unknown_option_type():

    bad = sample_chain()

    bad[0]["option_type"] = "XX"

    with pytest.raises(ValueError):

        VannaExposure.calculate(
            spot_price=25000,
            option_chain=bad,
        )


def test_positive_strike_type():

    assert isinstance(
        result().largest_positive_strike,
        float,
    )


def test_negative_strike_type():

    assert isinstance(
        result().largest_negative_strike,
        float,
    )


def test_regime_type():

    assert isinstance(
        result().vanna_regime,
        str,
    )


def test_interpretation_not_empty():

    assert len(result().interpretation) > 10


def test_large_spot():

    r = VannaExposure.calculate(
        spot_price=50000,
        option_chain=sample_chain(),
    )

    assert r.total_call_vanna > 0


def test_call_not_zero():

    assert result().total_call_vanna != 0


def test_put_not_zero():

    assert result().total_put_vanna != 0


def test_net_not_zero():

    assert result().net_vanna != 0


def test_result_fields():

    r = result()

    assert r.total_call_vanna is not None
    assert r.total_put_vanna is not None
    assert r.net_vanna is not None
    assert r.vanna_regime is not None
    assert r.interpretation is not None
