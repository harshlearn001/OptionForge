"""
==============================================================
OptionForge
Charm Exposure Tests
==============================================================
"""

import pytest

from optionforge.intelligence import CharmExposure
from optionforge.models import CharmExposureResult


def sample_chain():

    return [
        {
            "strike": 25000,
            "option_type": "CE",
            "charm": 0.11,
            "open_interest": 150000,
            "lot_size": 75,
        },
        {
            "strike": 25000,
            "option_type": "PE",
            "charm": -0.09,
            "open_interest": 120000,
            "lot_size": 75,
        },
        {
            "strike": 25100,
            "option_type": "CE",
            "charm": 0.08,
            "open_interest": 90000,
            "lot_size": 75,
        },
        {
            "strike": 24900,
            "option_type": "PE",
            "charm": -0.13,
            "open_interest": 140000,
            "lot_size": 75,
        },
    ]


def result():

    return CharmExposure.calculate(
        spot_price=25000,
        option_chain=sample_chain(),
    )


def test_returns_result():

    assert isinstance(
        result(),
        CharmExposureResult,
    )


def test_call_charm_positive():

    assert result().total_call_charm > 0


def test_put_charm_negative():

    assert result().total_put_charm < 0


def test_net_charm_float():

    assert isinstance(
        result().net_charm,
        float,
    )


def test_net_identity():

    r = result()

    assert r.net_charm == pytest.approx(r.total_call_charm + r.total_put_charm)


def test_positive_strike():

    assert result().largest_positive_strike == 25000


def test_negative_strike():

    assert result().largest_negative_strike == 25100


def test_regime():

    assert result().charm_regime in (
        "POSITIVE CHARM",
        "NEGATIVE CHARM",
    )


def test_interpretation():

    assert isinstance(
        result().interpretation,
        str,
    )


def test_invalid_spot():

    with pytest.raises(ValueError):

        CharmExposure.calculate(
            spot_price=0,
            option_chain=sample_chain(),
        )


def test_negative_spot():

    with pytest.raises(ValueError):

        CharmExposure.calculate(
            spot_price=-1,
            option_chain=sample_chain(),
        )


def test_empty_chain():

    with pytest.raises(ValueError):

        CharmExposure.calculate(
            spot_price=25000,
            option_chain=[],
        )


def test_unknown_option_type():

    bad = sample_chain()

    bad[0]["option_type"] = "XX"

    with pytest.raises(ValueError):

        CharmExposure.calculate(
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
        result().charm_regime,
        str,
    )


def test_interpretation_not_empty():

    assert len(result().interpretation) > 10


def test_large_spot():

    r = CharmExposure.calculate(
        spot_price=50000,
        option_chain=sample_chain(),
    )

    assert r.total_call_charm > 0


def test_call_not_zero():

    assert result().total_call_charm != 0


def test_put_not_zero():

    assert result().total_put_charm != 0


def test_net_not_zero():

    assert result().net_charm != 0


def test_result_fields():

    r = result()

    assert r.total_call_charm is not None
    assert r.total_put_charm is not None
    assert r.net_charm is not None
    assert r.charm_regime is not None
    assert r.interpretation is not None
