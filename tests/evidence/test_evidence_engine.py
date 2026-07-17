"""
============================================================
OptionForge
Evidence Engine Tests
============================================================

Tests the orchestration performed by EvidenceEngine.

============================================================
"""

from optionforge.evidence.evidence import Evidence
from optionforge.evidence.evidence_collection import (
    EvidenceCollection,
)
from optionforge.evidence.evidence_direction import (
    EvidenceDirection,
)
from optionforge.evidence.evidence_engine import (
    EvidenceEngine,
)
from optionforge.evidence.evidence_level import (
    EvidenceLevel,
)
from optionforge.evidence.evidence_provider_registry import (
    EvidenceProviderRegistry,
)
from optionforge.evidence.evidence_source import (
    EvidenceSource,
)


# ==========================================================
# Dummy Analytics Result
# ==========================================================


class DummyResult:
    pass


# ==========================================================
# Dummy Execution
# ==========================================================


class DummyExecution:

    def __init__(
        self,
        succeeded: bool = True,
    ) -> None:

        self.succeeded = succeeded

        self.result = DummyResult()


# ==========================================================
# Dummy Result Collection
# ==========================================================


class DummyResultCollection:

    def __init__(self):

        self._items = [
            DummyExecution(),
        ]

    def __iter__(self):

        return iter(self._items)


# ==========================================================
# Dummy Provider
# ==========================================================


class DummyProvider:

    def build(
        self,
        result,
    ) -> EvidenceCollection:

        evidence = Evidence(

            id="TEST001",

            title="Dummy Evidence",

            source=EvidenceSource.GREEKS,

            direction=EvidenceDirection.BULLISH,

            level=EvidenceLevel.STRONG,

            score=1.0,

            confidence=1.0,

            description="Dummy provider.",

        )

        return EvidenceCollection().add(
            evidence,
        )


# ==========================================================
# Tests
# ==========================================================


def test_build_returns_registry():

    providers = EvidenceProviderRegistry()

    providers.register(
        DummyResult,
        DummyProvider(),
    )

    engine = EvidenceEngine(
        providers,
    )

    registry = engine.build(
        DummyResultCollection(),
    )

    assert len(registry) == 1


def test_registry_contains_evidence():

    providers = EvidenceProviderRegistry()

    providers.register(
        DummyResult,
        DummyProvider(),
    )

    engine = EvidenceEngine(
        providers,
    )

    registry = engine.build(
        DummyResultCollection(),
    )

    assert registry.exists(
        "TEST001",
    )


def test_evidence_fields():

    providers = EvidenceProviderRegistry()

    providers.register(
        DummyResult,
        DummyProvider(),
    )

    engine = EvidenceEngine(
        providers,
    )

    registry = engine.build(
        DummyResultCollection(),
    )

    evidence = registry.get(
        "TEST001",
    )

    assert evidence.title == "Dummy Evidence"

    assert evidence.source is EvidenceSource.GREEKS

    assert evidence.direction is EvidenceDirection.BULLISH

    assert evidence.level is EvidenceLevel.STRONG

    assert evidence.score == 1.0

    assert evidence.confidence == 1.0


def test_empty_results():

    class EmptyResults:

        def __iter__(self):

            return iter(())

    providers = EvidenceProviderRegistry()

    engine = EvidenceEngine(
        providers,
    )

    registry = engine.build(
        EmptyResults(),
    )

    assert len(registry) == 0


def test_engine_is_deterministic():

    providers = EvidenceProviderRegistry()

    providers.register(
        DummyResult,
        DummyProvider(),
    )

    engine = EvidenceEngine(
        providers,
    )

    first = engine.build(
        DummyResultCollection(),
    )

    second = engine.build(
        DummyResultCollection(),
    )

    assert tuple(first) == tuple(second)