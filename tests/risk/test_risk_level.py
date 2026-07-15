"""
============================================================
OptionForge
Risk Level Tests
============================================================
"""

from optionforge.risk.risk_level import (
    RiskLevel,
)

# ==========================================================
# Enum
# ==========================================================


def test_enum_members():

    assert RiskLevel.VERY_LOW.name == "VERY_LOW"

    assert RiskLevel.LOW.name == "LOW"

    assert RiskLevel.MODERATE.name == "MODERATE"

    assert RiskLevel.HIGH.name == "HIGH"

    assert RiskLevel.VERY_HIGH.name == "VERY_HIGH"

    assert RiskLevel.EXTREME.name == "EXTREME"


# ==========================================================
# Score
# ==========================================================


def test_score():

    assert RiskLevel.VERY_LOW.score == 1

    assert RiskLevel.LOW.score == 2

    assert RiskLevel.MODERATE.score == 3

    assert RiskLevel.HIGH.score == 4

    assert RiskLevel.VERY_HIGH.score == 5

    assert RiskLevel.EXTREME.score == 6


# ==========================================================
# Safe
# ==========================================================


def test_is_safe():

    assert RiskLevel.VERY_LOW.is_safe

    assert RiskLevel.LOW.is_safe

    assert not RiskLevel.MODERATE.is_safe

    assert not RiskLevel.HIGH.is_safe

    assert not RiskLevel.VERY_HIGH.is_safe

    assert not RiskLevel.EXTREME.is_safe


# ==========================================================
# Attention
# ==========================================================


def test_requires_attention():

    assert RiskLevel.MODERATE.requires_attention

    assert RiskLevel.HIGH.requires_attention

    assert not RiskLevel.VERY_LOW.requires_attention

    assert not RiskLevel.LOW.requires_attention

    assert not RiskLevel.VERY_HIGH.requires_attention

    assert not RiskLevel.EXTREME.requires_attention


# ==========================================================
# Critical
# ==========================================================


def test_is_critical():

    assert RiskLevel.VERY_HIGH.is_critical

    assert RiskLevel.EXTREME.is_critical

    assert not RiskLevel.VERY_LOW.is_critical

    assert not RiskLevel.LOW.is_critical

    assert not RiskLevel.MODERATE.is_critical

    assert not RiskLevel.HIGH.is_critical


# ==========================================================
# From Score
# ==========================================================


def test_from_score():

    assert RiskLevel.from_score(0) is RiskLevel.VERY_LOW

    assert RiskLevel.from_score(10) is RiskLevel.VERY_LOW

    assert RiskLevel.from_score(11) is RiskLevel.LOW

    assert RiskLevel.from_score(25) is RiskLevel.LOW

    assert RiskLevel.from_score(26) is RiskLevel.MODERATE

    assert RiskLevel.from_score(45) is RiskLevel.MODERATE

    assert RiskLevel.from_score(46) is RiskLevel.HIGH

    assert RiskLevel.from_score(65) is RiskLevel.HIGH

    assert RiskLevel.from_score(66) is RiskLevel.VERY_HIGH

    assert RiskLevel.from_score(85) is RiskLevel.VERY_HIGH

    assert RiskLevel.from_score(86) is RiskLevel.EXTREME

    assert RiskLevel.from_score(100) is RiskLevel.EXTREME


# ==========================================================
# String
# ==========================================================


def test_str():

    assert (
        str(
            RiskLevel.VERY_LOW,
        )
        == "Very Low"
    )

    assert (
        str(
            RiskLevel.LOW,
        )
        == "Low"
    )

    assert (
        str(
            RiskLevel.MODERATE,
        )
        == "Moderate"
    )

    assert (
        str(
            RiskLevel.HIGH,
        )
        == "High"
    )

    assert (
        str(
            RiskLevel.VERY_HIGH,
        )
        == "Very High"
    )

    assert (
        str(
            RiskLevel.EXTREME,
        )
        == "Extreme"
    )
