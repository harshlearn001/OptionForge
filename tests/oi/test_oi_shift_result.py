"""
==============================================================
Tests for OIShiftResult
==============================================================
"""

from __future__ import annotations

import pandas as pd

from optionforge.common.enums import ShiftDirection
from optionforge.oi.oi_shift_result import OIShiftResult


def build_result() -> OIShiftResult:

    df = pd.DataFrame(
        {
            "strike_price": [
                24800,
                24850,
                24900,
                24950,
                25000,
            ],
            "SHIFT": [
                0.40,
                0.15,
                0.00,
                -0.15,
                -0.40,
            ],
            "SHIFT_DIRECTION": [
                ShiftDirection.STRONG_UP.value,
                ShiftDirection.UP.value,
                ShiftDirection.NEUTRAL.value,
                ShiftDirection.DOWN.value,
                ShiftDirection.STRONG_DOWN.value,
            ],
        }
    )

    return OIShiftResult(df)


# ==========================================================
# DataFrame
# ==========================================================

def test_dataframe():

    result = build_result()

    assert len(result.dataframe()) == 5


def test_dataframe_returns_copy():

    result = build_result()

    df = result.dataframe()

    df.loc[0, "SHIFT"] = 999

    assert result.dataframe().iloc[0]["SHIFT"] == 0.40


# ==========================================================
# Filters
# ==========================================================

def test_strong_up():
    assert len(build_result().strong_up()) == 1


def test_up():
    assert len(build_result().up()) == 1


def test_neutral():
    assert len(build_result().neutral()) == 1


def test_down():
    assert len(build_result().down()) == 1


def test_strong_down():
    assert len(build_result().strong_down()) == 1


# ==========================================================
# Ranking
# ==========================================================

def test_top_upward_shift():

    df = build_result().top_upward_shift(2)

    assert len(df) == 2

    assert df.iloc[0]["SHIFT"] == 0.40


def test_top_downward_shift():

    df = build_result().top_downward_shift(2)

    assert len(df) == 2

    assert df.iloc[0]["SHIFT"] == -0.40


# ==========================================================
# Summary
# ==========================================================

def test_summary():

    summary = build_result().summary()

    assert summary[ShiftDirection.STRONG_UP.value] == 1
    assert summary[ShiftDirection.UP.value] == 1
    assert summary[ShiftDirection.NEUTRAL.value] == 1
    assert summary[ShiftDirection.DOWN.value] == 1
    assert summary[ShiftDirection.STRONG_DOWN.value] == 1


# ==========================================================
# Dictionary
# ==========================================================

def test_to_dict():

    d = build_result().to_dict()

    assert d["rows"] == 5

    assert d["largest_upward_shift"] == 24800

    assert d["largest_downward_shift"] == 25000


# ==========================================================
# Representation
# ==========================================================

def test_repr():

    assert "OIShiftResult" in repr(build_result())