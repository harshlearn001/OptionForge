import pytest

from optionforge.analytics.gamma_exposure.gamma_exposure_result import (
    GammaExposureResult,
)


def sample():

    return GammaExposureResult(

        symbol="NIFTY",

        trade_date=20260715,

        expiry=20260723,

        strike=25000,

        gamma=0.00025,

        open_interest=100000,

        contract_size=75,

        spot=25000,

        gamma_exposure=11718750000.0,

    )


def test_fields():

    result = sample()

    assert result.symbol == "NIFTY"

    assert result.strike == 25000

    assert result.gamma == 0.00025

    assert result.gamma_exposure == 11718750000.0


def test_repr():

    result = sample()

    assert "GammaExposureResult" in repr(result)


def test_frozen():

    result = sample()

    with pytest.raises(Exception):

        result.gamma_exposure = 0