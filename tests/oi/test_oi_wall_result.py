"""
==============================================================
Tests for OIWallResult
==============================================================
"""

from __future__ import annotations

import pandas as pd

from optionforge.common.enums import WallType
from optionforge.oi.oi_wall_result import OIWallResult


def build_result() -> OIWallResult:

    df = pd.DataFrame(
        {
            "strike_price": [24800, 24850, 24900, 24950, 25000],

            "CALL_OI": [100, 500, 300, 900, 200],

            "PUT_OI": [900, 400, 800, 200, 100],

            "CALL_SHARE": [0.04, 0.20, 0.12, 0.36, 0.08],

            "PUT_SHARE": [0.36, 0.16, 0.32, 0.08, 0.04],

            "WALL": [
                WallType.PUT_WALL.value,
                WallType.CALL_WALL.value,
                WallType.PUT_WALL.value,
                WallType.CALL_WALL.value,
                WallType.BALANCED.value,
            ],
        }
    )

    return OIWallResult(df)


# ==========================================================
# DataFrame
# ==========================================================

def test_dataframe():

    result = build_result()

    assert len(result.dataframe()) == 5


# ==========================================================
# Filters
# ==========================================================

def test_call_wall():

    result = build_result()

    assert len(result.call_wall()) == 2


def test_put_wall():

    result = build_result()

    assert len(result.put_wall()) == 2


def test_balanced():

    result = build_result()

    assert len(result.balanced()) == 1


# ==========================================================
# Support / Resistance
# ==========================================================

def test_support():

    result = build_result()

    support = result.support()

    assert support["strike_price"] == 24800


def test_resistance():

    result = build_result()

    resistance = result.resistance()

    assert resistance["strike_price"] == 24950


# ==========================================================
# Top Walls
# ==========================================================

def test_top_call_walls():

    result = build_result()

    df = result.top_call_walls(2)

    assert len(df) == 2

    assert df.iloc[0]["CALL_OI"] == 900


def test_top_put_walls():

    result = build_result()

    df = result.top_put_walls(2)

    assert len(df) == 2

    assert df.iloc[0]["PUT_OI"] == 900


# ==========================================================
# Summary
# ==========================================================

def test_summary():

    result = build_result()

    summary = result.summary()

    assert summary[WallType.CALL_WALL.value] == 2

    assert summary[WallType.PUT_WALL.value] == 2

    assert summary[WallType.BALANCED.value] == 1


# ==========================================================
# Dictionary
# ==========================================================

def test_to_dict():

    result = build_result()

    d = result.to_dict()

    assert d["rows"] == 5

    assert d["support"] == 24800

    assert d["resistance"] == 24950

    assert "summary" in d


# ==========================================================
# Representation
# ==========================================================

def test_repr():

    result = build_result()

    assert "OIWallResult" in repr(result)