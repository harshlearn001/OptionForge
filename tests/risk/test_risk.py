"""
============================================================
OptionForge
Risk Tests
============================================================
"""

import pytest

from optionforge.risk.risk import (
    Risk,
)
from optionforge.risk.risk_level import (
    RiskLevel,
)
from optionforge.risk.risk_type import (
    RiskType,
)


# ==========================================================
# Helper
# ==========================================================

def risk() -> Risk:

    return Risk(

        risk_score=22.5,

        risk_level=RiskLevel.LOW,

        risk_type=RiskType.APPROVED,

        approved=True,

        warnings=(

            "No issues",

        ),

        reasons=(

            "Capital within limits",

            "Liquidity acceptable",

        ),

        recommended_position_size=5.0,

        max_capital_allocation=10.0,

    )


# ==========================================================
# Construction
# ==========================================================

def test_returns_risk():

    result = risk()

    assert isinstance(

        result,

        Risk,

    )


def test_values():

    result = risk()

    assert result.risk_score == 22.5

    assert result.risk_level is RiskLevel.LOW

    assert result.risk_type is RiskType.APPROVED

    assert result.approved


# ==========================================================
# Validation
# ==========================================================

def test_invalid_score():

    with pytest.raises(

        ValueError,

    ):

        Risk(

            risk_score=120.0,

            risk_level=RiskLevel.LOW,

            risk_type=RiskType.APPROVED,

            approved=True,

        )


def test_invalid_position_size():

    with pytest.raises(

        ValueError,

    ):

        Risk(

            risk_score=20.0,

            risk_level=RiskLevel.LOW,

            risk_type=RiskType.APPROVED,

            approved=True,

            recommended_position_size=150.0,

        )


def test_invalid_capital_allocation():

    with pytest.raises(

        ValueError,

    ):

        Risk(

            risk_score=20.0,

            risk_level=RiskLevel.LOW,

            risk_type=RiskType.APPROVED,

            approved=True,

            max_capital_allocation=150.0,

        )
# ==========================================================
# Convenience
# ==========================================================

def test_requires_review():

    result = Risk(

        risk_score=45.0,

        risk_level=RiskLevel.MODERATE,

        risk_type=RiskType.REVIEW,

        approved=False,

    )

    assert result.requires_review


def test_is_rejected():

    result = Risk(

        risk_score=90.0,

        risk_level=RiskLevel.EXTREME,

        risk_type=RiskType.REJECTED,

        approved=False,

    )

    assert result.is_rejected


def test_is_safe():

    assert risk().is_safe


def test_warning_count():

    assert risk().warning_count == 1


def test_reason_count():

    assert risk().reason_count == 2


# ==========================================================
# Serialization
# ==========================================================

def test_to_dict():

    data = risk().to_dict()

    assert isinstance(

        data,

        dict,

    )

    assert data["risk_score"] == 22.5

    assert data["risk_level"] == "LOW"

    assert data["risk_type"] == "APPROVED"

    assert data["approved"] is True

    assert data["recommended_position_size"] == 5.0

    assert data["max_capital_allocation"] == 10.0


# ==========================================================
# Representation
# ==========================================================

def test_str():

    assert (

        "Risk("

        in str(

            risk(),

        )

    )


def test_repr():

    assert (

        "Risk("

        in repr(

            risk(),

        )

    )


# ==========================================================
# Equality
# ==========================================================

def test_equality():

    assert risk() == risk()


# ==========================================================
# Immutability
# ==========================================================

def test_immutable():

    import dataclasses

    with pytest.raises(

        dataclasses.FrozenInstanceError,

    ):

        risk().approved = False