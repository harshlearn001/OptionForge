from optionforge.evidence.evidence import Evidence
from optionforge.evidence.evidence_collection import (
    EvidenceCollection,
)
from optionforge.evidence.evidence_direction import (
    EvidenceDirection,
)
from optionforge.evidence.evidence_level import (
    EvidenceLevel,
)
from optionforge.evidence.evidence_source import (
    EvidenceSource,
)


def make_evidence(
    source,
    direction,
    level,
):

    return Evidence(
        id=f"{source.name}",
        title=source.value,
        source=source,
        direction=direction,
        level=level,
        score=1.0,
        confidence=0.90,
        description="Test",
    )


def test_collection():

    collection = EvidenceCollection()

    collection = collection.add(
        make_evidence(
            EvidenceSource.GREEKS,
            EvidenceDirection.BULLISH,
            EvidenceLevel.STRONG,
        )
    )

    collection = collection.add(
        make_evidence(
            EvidenceSource.SMART_PCR,
            EvidenceDirection.BEARISH,
            EvidenceLevel.MODERATE,
        )
    )

    assert len(collection) == 2

    assert len(collection.bullish) == 1

    assert len(collection.bearish) == 1

    assert len(collection.strong) == 1

    assert len(
        collection.by_source(
            EvidenceSource.GREEKS,
        )
    ) == 1

    assert len(
        collection.by_direction(
            EvidenceDirection.BEARISH,
        )
    ) == 1