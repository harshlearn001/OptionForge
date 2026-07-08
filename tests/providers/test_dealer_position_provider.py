"""
============================================================
OptionForge
Dealer Position Provider Tests
============================================================
"""

from types import SimpleNamespace

import pytest

from optionforge.context.market_context import MarketContext
from optionforge.features.feature_group import FeatureGroup
from optionforge.features.feature_id import FeatureId
from optionforge.models import DealerPositionResult
from optionforge.providers.dealer.dealer_position_provider import (
    DealerPositionProvider,
)


# ==========================================================
# Fixtures
# ==========================================================

@pytest.fixture
def context():

    snapshot = SimpleNamespace(
        gamma_result=SimpleNamespace(),
        delta_result=SimpleNamespace(),
        vanna_result=SimpleNamespace(),
        charm_result=SimpleNamespace(),
    )

    return MarketContext(
        market=SimpleNamespace(),
        snapshot=snapshot,
    )


@pytest.fixture
def dealer_result():

    return DealerPositionResult(

        # Quantitative
        dealer_position=-170.0,
        dealer_delta=-60.0,
        dealer_gamma=-50.0,
        net_exposure=-170.0,
        position_strength=170.0,
        institutional_score=15.0,

        # Classification
        dealer_bias="SHORT GAMMA",
        dealer_direction="SHORT DELTA",
        market_condition="TRENDING",
        market_stability="LOW",
        directional_risk="VERY HIGH",

        # Decision
        confidence=15.0,
        recommendation="Expect strong directional moves.",
        interpretation="SHORT GAMMA | SHORT DELTA",
    )


# ==========================================================
# Provider
# ==========================================================

def test_provider_returns_expected_features(
    monkeypatch,
    context,
    dealer_result,
):

    monkeypatch.setattr(
        "optionforge.providers.dealer.dealer_position_provider.DealerPosition.calculate",
        lambda **kwargs: dealer_result,
    )

    provider = DealerPositionProvider()

    features = list(provider.calculate(context))

    assert len(features) == 1


def test_feature_id(
    monkeypatch,
    context,
    dealer_result,
):

    monkeypatch.setattr(
        "optionforge.providers.dealer.dealer_position_provider.DealerPosition.calculate",
        lambda **kwargs: dealer_result,
    )

    provider = DealerPositionProvider()

    feature = provider.calculate(context)[0]

    assert feature.id == FeatureId.DEALER_POSITION


def test_feature_group(
    monkeypatch,
    context,
    dealer_result,
):

    monkeypatch.setattr(
        "optionforge.providers.dealer.dealer_position_provider.DealerPosition.calculate",
        lambda **kwargs: dealer_result,
    )

    provider = DealerPositionProvider()

    feature = provider.calculate(context)[0]

    assert feature.group == FeatureGroup.DEALER


def test_metadata(
    monkeypatch,
    context,
    dealer_result,
):

    monkeypatch.setattr(
        "optionforge.providers.dealer.dealer_position_provider.DealerPosition.calculate",
        lambda **kwargs: dealer_result,
    )

    provider = DealerPositionProvider()

    feature = provider.calculate(context)[0]

    assert feature.metadata["dealer_delta"] == -60.0
    assert feature.metadata["dealer_gamma"] == -50.0
    assert feature.metadata["net_exposure"] == -170.0
    assert feature.metadata["position_strength"] == 170.0
    assert feature.metadata["institutional_score"] == 15.0
    assert feature.metadata["dealer_bias"] == "SHORT GAMMA"
    assert feature.metadata["dealer_direction"] == "SHORT DELTA"
    assert feature.metadata["market_condition"] == "TRENDING"


def test_provider_is_deterministic(
    monkeypatch,
    context,
    dealer_result,
):

    monkeypatch.setattr(
        "optionforge.providers.dealer.dealer_position_provider.DealerPosition.calculate",
        lambda **kwargs: dealer_result,
    )

    provider = DealerPositionProvider()

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
        "optionforge.providers.dealer.dealer_position_provider.DealerPosition.calculate",
        fake_calculate,
    )

    provider = DealerPositionProvider()

    with pytest.raises(ValueError):
        provider.calculate(context)