"""
============================================================
OptionForge
Rule Result Tests
============================================================
"""

import pytest

from optionforge.risk.rule_result import (
    RuleResult,
)

# ==========================================================
# Helper
# ==========================================================


def result() -> RuleResult:

    return RuleResult(
        rule_name="CapitalRule",
        score=15.0,
        passed=True,
        warnings=("Capital approaching limit",),
        reasons=("Capital utilization acceptable",),
    )


# ==========================================================
# Construction
# ==========================================================


def test_returns_rule_result():

    assert isinstance(
        result(),
        RuleResult,
    )


def test_values():

    r = result()

    assert r.rule_name == "CapitalRule"

    assert r.score == 15.0

    assert r.passed is True


# ==========================================================
# Validation
# ==========================================================


def test_invalid_score():

    with pytest.raises(
        ValueError,
    ):

        RuleResult(
            rule_name="CapitalRule",
            score=150.0,
            passed=False,
        )


# ==========================================================
# Counts
# ==========================================================


def test_warning_count():

    assert result().warning_count == 1


def test_reason_count():

    assert result().reason_count == 1


# ==========================================================
# Serialization
# ==========================================================


def test_to_dict():

    data = result().to_dict()

    assert isinstance(
        data,
        dict,
    )

    assert data["rule_name"] == "CapitalRule"

    assert data["score"] == 15.0

    assert data["passed"] is True

    assert data["warnings"] == [
        "Capital approaching limit",
    ]

    assert data["reasons"] == [
        "Capital utilization acceptable",
    ]


# ==========================================================
# Representation
# ==========================================================


def test_str():

    assert "CapitalRule" in str(
        result(),
    )


def test_repr():

    assert "RuleResult" in repr(
        result(),
    )


# ==========================================================
# Equality
# ==========================================================


def test_equality():

    assert result() == result()


# ==========================================================
# Immutability
# ==========================================================


def test_immutable():

    import dataclasses

    with pytest.raises(
        dataclasses.FrozenInstanceError,
    ):

        result().score = 25.0
