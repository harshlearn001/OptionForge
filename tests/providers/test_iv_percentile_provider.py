"""
============================================================
OptionForge
Test IV Percentile Provider
============================================================
"""

from types import SimpleNamespace

import pytest

from optionforge.context.market_context import MarketContext
from optionforge.features.feature_group import FeatureGroup
from optionforge.features.feature_id import FeatureId
from optionforge.providers.volatility.iv_percentile_provider import (
    IVPercentileProvider,
)


@pytest.fixture
def context():

    snapshot = SimpleNamespace(

        current_iv=0.22,

        historical_iv=[
            0.15,
            0.18,
            0.20,
            0.25,
            0.30,
        ],

    )

    return MarketContext(
        market=SimpleNamespace(),
        snapshot=snapshot,
    )


@pytest.fixture
def iv_percentile_result():

    return SimpleNamespace(

        iv_percentile=75.0,

        current_iv=0.22,

        lookback=252,

        observations=252,

    )


def test_provider_returns_expected_features(
    monkeypatch,
    context,
    iv_percentile_result,
):

    monkeypatch.setattr(
        "optionforge.providers.volatility.iv_percentile_provider.IVPercentile.calculate",
        lambda **kwargs: iv_percentile_result,
    )

    provider = IVPercentileProvider()

    features = list(provider.calculate(context))

    assert len(features) == 1


def test_feature_id(
    monkeypatch,
    context,
    iv_percentile_result,
):

    monkeypatch.setattr(
        "optionforge.providers.volatility.iv_percentile_provider.IVPercentile.calculate",
        lambda **kwargs: iv_percentile_result,
    )

    provider = IVPercentileProvider()

    feature = provider.calculate(context)[0]

    assert feature.id == FeatureId.IV_PERCENTILE


def test_feature_group(
    monkeypatch,
    context,
    iv_percentile_result,
):

    monkeypatch.setattr(
        "optionforge.providers.volatility.iv_percentile_provider.IVPercentile.calculate",
        lambda **kwargs: iv_percentile_result,
    )

    provider = IVPercentileProvider()

    feature = provider.calculate(context)[0]

    assert feature.group == FeatureGroup.IMPLIED_VOLATILITY


def test_iv_percentile_metadata(
    monkeypatch,
    context,
    iv_percentile_result,
):

    monkeypatch.setattr(
        "optionforge.providers.volatility.iv_percentile_provider.IVPercentile.calculate",
        lambda **kwargs: iv_percentile_result,
    )

    provider = IVPercentileProvider()

    feature = provider.calculate(context)[0]

    assert feature.metadata["current_iv"] == 0.22
    assert feature.metadata["lookback"] == 252
    assert feature.metadata["observations"] == 252


def test_provider_is_deterministic(
    monkeypatch,
    context,
    iv_percentile_result,
):

    monkeypatch.setattr(
        "optionforge.providers.volatility.iv_percentile_provider.IVPercentile.calculate",
        lambda **kwargs: iv_percentile_result,
    )

    provider = IVPercentileProvider()

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
        "optionforge.providers.volatility.iv_percentile_provider.IVPercentile.calculate",
        fake_calculate,
    )

    provider = IVPercentileProvider()

    with pytest.raises(ValueError):
        provider.calculate(context)