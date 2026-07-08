"""
============================================================
OptionForge
Test Expected Move Provider
============================================================
"""

from types import SimpleNamespace

import pytest

from optionforge.context.market_context import MarketContext
from optionforge.features.feature_group import FeatureGroup
from optionforge.features.feature_id import FeatureId
from optionforge.providers.volatility.expected_move_provider import (
    ExpectedMoveProvider,
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
        spot=25000.0,
        atm_iv=0.20,
        days_to_expiry=7,
    )

    return MarketContext(
        market=SimpleNamespace(),
        snapshot=snapshot,
    )


@pytest.fixture
def expected_move_result():
    """
    Fake ExpectedMove calculation result.
    """

    return SimpleNamespace(
        expected_move=695.0,
        upper_68=25695.0,
        lower_68=24305.0,
        upper_95=26390.0,
        lower_95=23610.0,
        one_day_move=262.5,
        weekly_move=695.0,
        monthly_move=1435.0,
    )


# ---------------------------------------------------------
# Tests
# ---------------------------------------------------------

def test_provider_returns_expected_features(
    monkeypatch,
    context,
    expected_move_result,
):

    monkeypatch.setattr(
        "optionforge.providers.volatility.expected_move_provider.ExpectedMove.calculate",
        lambda **kwargs: expected_move_result,
    )

    provider = ExpectedMoveProvider()

    features = list(provider.calculate(context))

    assert len(features) == 1


def test_feature_id(
    monkeypatch,
    context,
    expected_move_result,
):

    monkeypatch.setattr(
        "optionforge.providers.volatility.expected_move_provider.ExpectedMove.calculate",
        lambda **kwargs: expected_move_result,
    )

    provider = ExpectedMoveProvider()

    feature = provider.calculate(context)[0]

    assert feature.id == FeatureId.EXPECTED_MOVE


def test_feature_group(
    monkeypatch,
    context,
    expected_move_result,
):

    monkeypatch.setattr(
        "optionforge.providers.volatility.expected_move_provider.ExpectedMove.calculate",
        lambda **kwargs: expected_move_result,
    )

    provider = ExpectedMoveProvider()

    feature = provider.calculate(context)[0]

    assert feature.group == FeatureGroup.IMPLIED_VOLATILITY


def test_expected_move_metadata(
    monkeypatch,
    context,
    expected_move_result,
):

    monkeypatch.setattr(
        "optionforge.providers.volatility.expected_move_provider.ExpectedMove.calculate",
        lambda **kwargs: expected_move_result,
    )

    provider = ExpectedMoveProvider()

    feature = provider.calculate(context)[0]

    assert feature.metadata["upper68"] == 25695.0
    assert feature.metadata["lower68"] == 24305.0
    assert feature.metadata["upper95"] == 26390.0
    assert feature.metadata["lower95"] == 23610.0
    assert feature.metadata["daily"] == 262.5
    assert feature.metadata["weekly"] == 695.0
    assert feature.metadata["monthly"] == 1435.0


def test_provider_is_deterministic(
    monkeypatch,
    context,
    expected_move_result,
):

    monkeypatch.setattr(
        "optionforge.providers.volatility.expected_move_provider.ExpectedMove.calculate",
        lambda **kwargs: expected_move_result,
    )

    provider = ExpectedMoveProvider()

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
        "optionforge.providers.volatility.expected_move_provider.ExpectedMove.calculate",
        fake_calculate,
    )

    provider = ExpectedMoveProvider()

    with pytest.raises(ValueError):
        provider.calculate(context)