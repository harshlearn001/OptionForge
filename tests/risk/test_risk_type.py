"""
============================================================
OptionForge
Risk Type Tests
============================================================
"""

from optionforge.risk.risk_type import (
    RiskType,
)


# ==========================================================
# Enum
# ==========================================================

def test_enum_members():

    assert RiskType.APPROVED.name == "APPROVED"

    assert RiskType.REVIEW.name == "REVIEW"

    assert RiskType.REJECTED.name == "REJECTED"


# ==========================================================
# Approved
# ==========================================================

def test_is_approved():

    assert RiskType.APPROVED.is_approved

    assert not RiskType.REVIEW.is_approved

    assert not RiskType.REJECTED.is_approved


# ==========================================================
# Review
# ==========================================================

def test_requires_review():

    assert RiskType.REVIEW.requires_review

    assert not RiskType.APPROVED.requires_review

    assert not RiskType.REJECTED.requires_review


# ==========================================================
# Rejected
# ==========================================================

def test_is_rejected():

    assert RiskType.REJECTED.is_rejected

    assert not RiskType.APPROVED.is_rejected

    assert not RiskType.REVIEW.is_rejected

# ==========================================================
# From Score
# ==========================================================

def test_from_score_approved():

    assert (

        RiskType.from_score(

            0,

        )

        is RiskType.APPROVED

    )

    assert (

        RiskType.from_score(

            30,

        )

        is RiskType.APPROVED

    )


def test_from_score_review():

    assert (

        RiskType.from_score(

            31,

        )

        is RiskType.REVIEW

    )

    assert (

        RiskType.from_score(

            70,

        )

        is RiskType.REVIEW

    )


def test_from_score_rejected():

    assert (

        RiskType.from_score(

            71,

        )

        is RiskType.REJECTED

    )

    assert (

        RiskType.from_score(

            100,

        )

        is RiskType.REJECTED

    )


# ==========================================================
# String
# ==========================================================

def test_str():

    assert (

        str(

            RiskType.APPROVED,

        )

        == "Approved"

    )

    assert (

        str(

            RiskType.REVIEW,

        )

        == "Review"

    )

    assert (

        str(

            RiskType.REJECTED,

        )

        == "Rejected"

    )