from optionforge.evidence.evidence import (
    Evidence,
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


def test_evidence():

    evidence = Evidence(

        id="PCR001",

        title="Institutional PCR",

        source=EvidenceSource.SMART_PCR,

        direction=EvidenceDirection.BEARISH,

        level=EvidenceLevel.STRONG,

        score=0.74,

        confidence=0.91,

        description="Weighted PCR indicates bearish positioning.",

        metadata={
            "atm": 25100,
        },
    )

    assert evidence.id == "PCR001"

    assert evidence.title == "Institutional PCR"

    assert evidence.is_bearish

    assert not evidence.is_bullish

    assert evidence.confidence_percent == 91.0

    assert evidence.metadata["atm"] == 25100


def test_invalid_confidence():

    try:

        Evidence(

            id="A",

            title="B",

            source=EvidenceSource.GREEKS,

            direction=EvidenceDirection.NEUTRAL,

            level=EvidenceLevel.MODERATE,

            score=0.0,

            confidence=1.5,

            description="Invalid",

        )

        assert False

    except ValueError:

        pass