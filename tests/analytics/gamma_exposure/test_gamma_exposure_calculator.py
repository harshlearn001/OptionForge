import pytest

from optionforge.analytics.gamma_exposure.gamma_exposure_calculator import (
    GammaExposureCalculator,
)


def test_gamma_exposure():

    value = GammaExposureCalculator.calculate(
        gamma=0.00025,
        open_interest=100000,
        contract_size=75,
        spot=25000,
    )

    expected = 0.00025 * 100000 * 75 * (25000**2) * 0.01

    assert value == expected


def test_negative_gamma():

    with pytest.raises(ValueError):

        GammaExposureCalculator.calculate(
            gamma=-0.001,
            open_interest=100,
            contract_size=75,
            spot=25000,
        )


def test_negative_oi():

    with pytest.raises(ValueError):

        GammaExposureCalculator.calculate(
            gamma=0.001,
            open_interest=-100,
            contract_size=75,
            spot=25000,
        )


def test_zero_contract():

    with pytest.raises(ValueError):

        GammaExposureCalculator.calculate(
            gamma=0.001,
            open_interest=100,
            contract_size=0,
            spot=25000,
        )


def test_repr():

    calc = GammaExposureCalculator()

    assert "GammaExposureCalculator" in repr(calc)
