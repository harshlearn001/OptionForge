"""
============================================================
OptionForge
WalkForwardAnalysis Tests
============================================================
"""

import pytest

from optionforge.research.walk_forward import (
    WalkForwardAnalysis,
)


def analysis():

    return WalkForwardAnalysis(

        windows=10,

        successful_windows=8,

        failed_windows=2,

        stability_score=92.5,

        passed=True,

    )


# ==========================================================
# Construction
# ==========================================================

def test_create():

    assert isinstance(

        analysis(),

        WalkForwardAnalysis,

    )


# ==========================================================
# Values
# ==========================================================

def test_windows():

    assert analysis().windows == 10


def test_successful():

    assert analysis().successful_windows == 8


def test_failed():

    assert analysis().failed_windows == 2


def test_score():

    assert analysis().stability_score == 92.5


# ==========================================================
# Properties
# ==========================================================

def test_success_rate():

    assert analysis().success_rate == 80.0


def test_passed():

    assert analysis().passed


# ==========================================================
# Validation
# ==========================================================

@pytest.mark.parametrize(

    "field,value",

    [

        ("windows", 0),

        ("successful_windows", -1),

        ("failed_windows", -1),

        ("stability_score", -1),

        ("stability_score", 101),

    ],

)

def test_validation(

    field,

    value,

):

    kwargs = dict(

        windows=10,

        successful_windows=8,

        failed_windows=2,

        stability_score=92.5,

        passed=True,

    )

    kwargs[field] = value

    with pytest.raises(ValueError):

        WalkForwardAnalysis(

            **kwargs,

        )


def test_invalid_window_counts():

    with pytest.raises(ValueError):

        WalkForwardAnalysis(

            windows=10,

            successful_windows=9,

            failed_windows=2,

            stability_score=90,

            passed=True,

        )


# ==========================================================
# Serialization
# ==========================================================

def test_to_dict():

    data = analysis().to_dict()

    assert data["windows"] == 10

    assert data["successful_windows"] == 8

    assert data["success_rate"] == 80.0


# ==========================================================
# Representation
# ==========================================================

def test_str():

    assert "WalkForwardAnalysis" in str(

        analysis(),

    )


def test_repr():

    assert "WalkForwardAnalysis" in repr(

        analysis(),

    )