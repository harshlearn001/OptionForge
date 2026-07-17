from optionforge.evidence.evidence_direction import (
    EvidenceDirection,
)


def test_bullish():

    assert EvidenceDirection.BULLISH.is_bullish
    assert not EvidenceDirection.BULLISH.is_bearish


def test_bearish():

    assert EvidenceDirection.BEARISH.is_bearish
    assert not EvidenceDirection.BEARISH.is_bullish


def test_neutral():

    assert EvidenceDirection.NEUTRAL.is_neutral


def test_opposite():

    assert (
        EvidenceDirection.BULLISH.opposite
        is EvidenceDirection.BEARISH
    )

    assert (
        EvidenceDirection.VERY_BULLISH.opposite
        is EvidenceDirection.VERY_BEARISH
    )


def test_intensity():

    assert (
        EvidenceDirection.VERY_BULLISH.intensity == 2
    )

    assert (
        EvidenceDirection.BULLISH.intensity == 1
    )

    assert (
        EvidenceDirection.NEUTRAL.intensity == 0
    )