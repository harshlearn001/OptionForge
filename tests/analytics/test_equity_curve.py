"""
============================================================
OptionForge
EquityCurve Tests
============================================================
"""

import pytest

from optionforge.analytics.equity_curve import (
    EquityCurve,
)


def curve():

    return EquityCurve(

        values=(

            100000,

            102000,

            101500,

            104000,

            108000,

        ),

    )


# ==========================================================
# Construction
# ==========================================================

def test_create():

    assert isinstance(

        curve(),

        EquityCurve,

    )


# ==========================================================
# Values
# ==========================================================

def test_length():

    assert curve().length == 5


def test_start():

    assert curve().start_value == 100000


def test_end():

    assert curve().end_value == 108000


def test_high():

    assert curve().highest_value == 108000


def test_low():

    assert curve().lowest_value == 100000


def test_return():

    assert curve().total_return == 8.0


# ==========================================================
# Validation
# ==========================================================

def test_empty():

    with pytest.raises(

        ValueError,

    ):

        EquityCurve(

            values=(),

        )


def test_negative():

    with pytest.raises(

        ValueError,

    ):

        EquityCurve(

            values=(

                100,

                -50,

            ),

        )


# ==========================================================
# Serialization
# ==========================================================

def test_to_dict():

    data = curve().to_dict()

    assert data["length"] == 5

    assert data["end_value"] == 108000

    assert data["total_return"] == 8.0


# ==========================================================
# Representation
# ==========================================================

def test_str():

    assert "EquityCurve" in str(

        curve(),

    )


def test_repr():

    assert "EquityCurve" in repr(

        curve(),

    )