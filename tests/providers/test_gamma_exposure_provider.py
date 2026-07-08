"""
============================================================
OptionForge
Test Gamma Exposure Provider
============================================================
"""

from types import SimpleNamespace

import pytest

from optionforge.context.market_context import MarketContext
from optionforge.features.feature_group import FeatureGroup
from optionforge.features.feature_id import FeatureId
from optionforge.providers.greeks.gamma_exposure_provider import (
    GammaExposureProvider,
)

# ---------------------------------------------------------
# Fixtures
# ---------------------------------------------------------

@pytest.fixture
def context():
    """
    Minimal MarketContext required by the provider.
    """

    snapshot = SimpleNamespace(
        option_chain=[],
        spot=25000.0,
    )

    return MarketContext(
        market=SimpleNamespace(),
        snapshot=snapshot,
    )


@pytest.fixture
def gamma_result():
    """
    Fake GammaExposure calculation result.
    """

    return SimpleNamespace(
        gamma_exposure=1250000.0,
        zero_gamma=24850.0,
        gamma_flip=24920.0,
        dealer_gamma=850000.0,
        call_gamma=640000.0,
        put_gamma=610000.0,
    )


# ---------------------------------------------------------
# Tests
# ---------------------------------------------------------

def test_provider_returns_expected_features(
    monkeypatch,
    context,
    gamma_result,
):
    """
    Provider should return three Features.
    """

    def fake_calculate(**kwargs):
        return gamma_result

    monkeypatch.setattr(
        "optionforge.providers.greeks.gamma_exposure_provider.GammaExposure.calculate",
        fake_calculate,
    )

    provider = GammaExposureProvider()

    features = list(provider.calculate(context))

    assert len(features) == 3


def test_feature_ids(
    monkeypatch,
    context,
    gamma_result,
):

    monkeypatch.setattr(
        "optionforge.providers.greeks.gamma_exposure_provider.GammaExposure.calculate",
        lambda **kwargs: gamma_result,
    )

    provider = GammaExposureProvider()

    features = list(provider.calculate(context))

    ids = {feature.id for feature in features}

    assert ids == {
        FeatureId.GAMMA_EXPOSURE,
        FeatureId.ZERO_GAMMA,
        FeatureId.GAMMA_FLIP,
    }


def test_feature_group(
    monkeypatch,
    context,
    gamma_result,
):

    monkeypatch.setattr(
        "optionforge.providers.greeks.gamma_exposure_provider.GammaExposure.calculate",
        lambda **kwargs: gamma_result,
    )

    provider = GammaExposureProvider()

    features = list(provider.calculate(context))

    for feature in features:
        assert feature.group == FeatureGroup.GREEKS


def test_gamma_metadata(
    monkeypatch,
    context,
    gamma_result,
):

    monkeypatch.setattr(
        "optionforge.providers.greeks.gamma_exposure_provider.GammaExposure.calculate",
        lambda **kwargs: gamma_result,
    )

    provider = GammaExposureProvider()

    feature = provider.calculate(context)[0]

    assert feature.metadata["dealer_gamma"] == 850000.0
    assert feature.metadata["call_gamma"] == 640000.0
    assert feature.metadata["put_gamma"] == 610000.0


def test_provider_is_deterministic(
    monkeypatch,
    context,
    gamma_result,
):

    monkeypatch.setattr(
        "optionforge.providers.greeks.gamma_exposure_provider.GammaExposure.calculate",
        lambda **kwargs: gamma_result,
    )

    provider = GammaExposureProvider()

    first = provider.calculate(context)
    second = provider.calculate(context)

    assert first == second


def test_provider_propagates_exception(
    monkeypatch,
    context,
):

    def fake_calculate(**kwargs):
        raise ValueError("Calculation failed")

    monkeypatch.setattr(
        "optionforge.providers.greeks.gamma_exposure_provider.GammaExposure.calculate",
        fake_calculate,
    )

    provider = GammaExposureProvider()

    with pytest.raises(ValueError):
        provider.calculate(context)