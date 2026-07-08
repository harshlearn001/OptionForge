"""
============================================================
OptionForge
Test IV Rank Provider
============================================================
"""

from types import SimpleNamespace

import pytest

from optionforge.context.market_context import MarketContext
from optionforge.features.feature_group import FeatureGroup
from optionforge.features.feature_id import FeatureId
from optionforge.providers.volatility.iv_rank_provider import (
    IVRankProvider,
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
def iv_rank_result():
    """
    Fake IV Rank calculation result.
    """

    return SimpleNamespace(
        iv_rank=58.4,
        current_iv=0.22,
        low_iv=0.15,
        high_iv=0.30,
        lookback=252,
    )


# ---------------------------------------------------------
# Tests
# ---------------------------------------------------------

def test_provider_returns_expected_features(
    monkeypatch,
    context,
    iv_rank_result,
):

    monkeypatch.setattr(
        "optionforge.providers.volatility.iv_rank_provider.IVRank.calculate",
        lambda **kwargs: iv_rank_result,
    )

    provider = IVRankProvider()

    features = list(provider.calculate(context))

    assert len(features) == 1


def test_feature_id(
    monkeypatch,
    context,
    iv_rank_result,
):

    monkeypatch.setattr(
        "optionforge.providers.volatility.iv_rank_provider.IVRank.calculate",
        lambda **kwargs: iv_rank_result,
    )

    provider = IVRankProvider()

    feature = provider.calculate(context)[0]

    assert feature.id == FeatureId.IV_RANK


def test_feature_group(
    monkeypatch,
    context,
    iv_rank_result,
):

    monkeypatch.setattr(
        "optionforge.providers.volatility.iv_rank_provider.IVRank.calculate",
        lambda **kwargs: iv_rank_result,
    )

    provider = IVRankProvider()

    feature = provider.calculate(context)[0]

    assert feature.group == FeatureGroup.IMPLIED_VOLATILITY


def test_iv_rank_metadata(
    monkeypatch,
    context,
    iv_rank_result,
):

    monkeypatch.setattr(
        "optionforge.providers.volatility.iv_rank_provider.IVRank.calculate",
        lambda **kwargs: iv_rank_result,
    )

    provider = IVRankProvider()

    feature = provider.calculate(context)[0]

    assert feature.metadata["current_iv"] == 0.22
    assert feature.metadata["lowest_iv"] == 0.15
    assert feature.metadata["highest_iv"] == 0.30
    assert feature.metadata["lookback"] == 252


def test_provider_is_deterministic(
    monkeypatch,
    context,
    iv_rank_result,
):

    monkeypatch.setattr(
        "optionforge.providers.volatility.iv_rank_provider.IVRank.calculate",
        lambda **kwargs: iv_rank_result,
    )

    provider = IVRankProvider()

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
        "optionforge.providers.volatility.iv_rank_provider.IVRank.calculate",
        fake_calculate,
    )

    provider = IVRankProvider()

    with pytest.raises(ValueError):
        provider.calculate(context)