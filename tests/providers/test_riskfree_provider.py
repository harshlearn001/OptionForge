from optionforge.providers.riskfree_provider import (
    RiskFreeRateProvider,
)


def test_default_rate():

    provider = RiskFreeRateProvider()

    assert provider.current_rate() == 0.06


def test_rate_positive():

    provider = RiskFreeRateProvider()

    assert provider.current_rate() > 0


def test_repr():

    provider = RiskFreeRateProvider()

    assert "RiskFreeRateProvider" in repr(provider)