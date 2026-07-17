from optionforge.evidence.evidence_source import (
    EvidenceSource,
)


def test_string_values():

    assert str(EvidenceSource.GREEKS) == "Greeks"

    assert str(EvidenceSource.SMART_PCR) == "Smart PCR"


def test_unique_sources():

    values = {source.value for source in EvidenceSource}

    assert len(values) == len(EvidenceSource)


def test_membership():

    assert EvidenceSource.GAMMA_EXPOSURE in EvidenceSource

    assert EvidenceSource.MAX_PAIN in EvidenceSource