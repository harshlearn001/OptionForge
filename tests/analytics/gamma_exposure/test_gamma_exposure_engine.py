from optionforge.analytics.gamma_exposure.gamma_exposure_engine import (
    GammaExposureEngine,
)


def test_engine():

    engine = GammaExposureEngine()

    result = engine.calculate(
        symbol="NIFTY",
        trade_date=20260715,
        expiry=20260723,
        strike=25000,
        gamma=0.00025,
        open_interest=100000,
        contract_size=75,
        spot=25000,
    )

    assert result.symbol == "NIFTY"

    assert result.strike == 25000

    assert result.gamma == 0.00025

    assert result.gamma_exposure > 0


def test_large_exposure():

    engine = GammaExposureEngine()

    result = engine.calculate(
        symbol="BANKNIFTY",
        trade_date=20260715,
        expiry=20260723,
        strike=55000,
        gamma=0.00018,
        open_interest=250000,
        contract_size=35,
        spot=55000,
    )

    assert result.gamma_exposure > 0

    assert result.open_interest == 250000


def test_repr():

    engine = GammaExposureEngine()

    assert "GammaExposureEngine" in repr(engine)
