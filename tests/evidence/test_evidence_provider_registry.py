from optionforge.evidence.evidence_provider_registry import (
    EvidenceProviderRegistry,
)


class DummyResult:
    pass


class DummyProvider:
    pass


def test_register():

    registry = EvidenceProviderRegistry()

    provider = DummyProvider()

    registry.register(
        DummyResult,
        provider,
    )

    assert registry.exists(
        DummyResult,
    )

    assert len(registry) == 1


def test_resolve():

    registry = EvidenceProviderRegistry()

    provider = DummyProvider()

    registry.register(
        DummyResult,
        provider,
    )

    assert (
        registry.resolve(
            DummyResult(),
        )
        is provider
    )