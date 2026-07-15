"""
Tests for OIBuildupResult.
"""

from __future__ import annotations

import pandas as pd

from optionforge.common.enums import BuildUp
from optionforge.oi.oi_buildup_result import OIBuildupResult


def build_result() -> OIBuildupResult:

    df = pd.DataFrame(
        {
            "strike_price": [24900, 24950, 25000, 25050, 25100],
            "BUILDUP": [
                BuildUp.LONG_BUILDUP.value,
                BuildUp.SHORT_BUILDUP.value,
                BuildUp.SHORT_COVERING.value,
                BuildUp.LONG_UNWINDING.value,
                BuildUp.NEUTRAL.value,
            ],
        }
    )

    return OIBuildupResult(df)


# ==========================================================
# dataframe
# ==========================================================

def test_dataframe():

    result = build_result()

    assert len(result.dataframe()) == 5


# ==========================================================
# filters
# ==========================================================

def test_long_buildup():

    result = build_result()

    assert len(result.long_buildup()) == 1


def test_short_buildup():

    result = build_result()

    assert len(result.short_buildup()) == 1


def test_short_covering():

    result = build_result()

    assert len(result.short_covering()) == 1


def test_long_unwinding():

    result = build_result()

    assert len(result.long_unwinding()) == 1


def test_neutral():

    result = build_result()

    assert len(result.neutral()) == 1


# ==========================================================
# summary
# ==========================================================

def test_summary():

    result = build_result()

    summary = result.summary()

    assert summary[BuildUp.LONG_BUILDUP.value] == 1

    assert summary[BuildUp.SHORT_BUILDUP.value] == 1

    assert summary[BuildUp.SHORT_COVERING.value] == 1

    assert summary[BuildUp.LONG_UNWINDING.value] == 1

    assert summary[BuildUp.NEUTRAL.value] == 1


# ==========================================================
# dict
# ==========================================================

def test_to_dict():

    result = build_result()

    d = result.to_dict()

    assert d["rows"] == 5

    assert "summary" in d


# ==========================================================
# repr
# ==========================================================

def test_repr():

    result = build_result()

    assert "OIBuildupResult" in repr(result)