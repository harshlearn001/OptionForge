from optionforge.evidence.evidence_level import (
    EvidenceLevel,
)


def test_ordering():

    assert (
        EvidenceLevel.VERY_WEAK
        < EvidenceLevel.WEAK
        < EvidenceLevel.MODERATE
        < EvidenceLevel.STRONG
        < EvidenceLevel.VERY_STRONG
    )


def test_is_strong():

    assert EvidenceLevel.STRONG.is_strong

    assert EvidenceLevel.VERY_STRONG.is_strong

    assert not EvidenceLevel.MODERATE.is_strong


def test_is_weak():

    assert EvidenceLevel.WEAK.is_weak

    assert EvidenceLevel.VERY_WEAK.is_weak

    assert not EvidenceLevel.STRONG.is_weak


def test_is_moderate():

    assert EvidenceLevel.MODERATE.is_moderate

    assert not EvidenceLevel.WEAK.is_moderate


def test_integer_values():

    assert int(EvidenceLevel.VERY_WEAK) == 1

    assert int(EvidenceLevel.WEAK) == 2

    assert int(EvidenceLevel.MODERATE) == 3

    assert int(EvidenceLevel.STRONG) == 4

    assert int(EvidenceLevel.VERY_STRONG) == 5


def test_string_representation():

    assert str(EvidenceLevel.VERY_WEAK) == "Very Weak"

    assert str(EvidenceLevel.VERY_STRONG) == "Very Strong"