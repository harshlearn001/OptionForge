"""
============================================================
OptionForge
Evidence Engine Tests
============================================================
"""

from types import SimpleNamespace

from optionforge.evidence.evidence_engine import EvidenceEngine
from optionforge.evidence.evidence_level import EvidenceLevel
from optionforge.evidence.evidence_type import EvidenceType
from optionforge.features.feature import Feature
from optionforge.features.feature_group import FeatureGroup
from optionforge.features.feature_id import FeatureId
from optionforge.features.registry import FeatureRegistry

# ==========================================================
# Helpers
# ==========================================================


def dealer_feature():

    return Feature(
        id=FeatureId.DEALER_POSITION,
        group=FeatureGroup.DEALER,
        value=-170.0,
        metadata={
            "dealer_bias": "LONG GAMMA",
            "confidence": 95.0,
            "institutional_score": 90.0,
        },
    )


def volatility_feature():

    return Feature(
        id=FeatureId.IV_RANK,
        group=FeatureGroup.VOLATILITY,
        value=82.0,
        confidence=88.0,
    )


# ==========================================================
# Tests
# ==========================================================


def test_build_returns_registry():

    registry = FeatureRegistry()

    registry.add(dealer_feature())

    evidence = EvidenceEngine().build(registry)

    assert len(evidence) == 1


def test_dealer_evidence():

    registry = FeatureRegistry()

    registry.add(dealer_feature())

    evidence = EvidenceEngine().build(registry)

    item = evidence.get("dealer_long_gamma")

    assert item.type == EvidenceType.DEALER

    assert item.level == EvidenceLevel.VERY_STRONG

    assert item.source == FeatureId.DEALER_POSITION


def test_volatility_evidence():

    registry = FeatureRegistry()

    registry.add(volatility_feature())

    evidence = EvidenceEngine().build(registry)

    item = evidence.get("iv_rank")

    assert item.type == EvidenceType.VOLATILITY

    assert item.source == FeatureId.IV_RANK


def test_empty_registry():

    evidence = EvidenceEngine().build(FeatureRegistry())

    assert len(evidence) == 0


def test_engine_is_deterministic():

    registry = FeatureRegistry()

    registry.add(dealer_feature())

    first = EvidenceEngine().build(registry)

    second = EvidenceEngine().build(registry)

    assert tuple(first) == tuple(second)


def test_registry_score():

    registry = FeatureRegistry()

    registry.add(dealer_feature())

    evidence = EvidenceEngine().build(registry)

    assert evidence.score == 90.0


def test_registry_confidence():

    registry = FeatureRegistry()

    registry.add(dealer_feature())

    evidence = EvidenceEngine().build(registry)

    assert evidence.confidence == 95.0
