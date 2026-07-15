"""
==============================================================
Tests for OIConcentrationResult
==============================================================
"""

from __future__ import annotations

import pandas as pd

from optionforge.common.enums import ConcentrationLevel
from optionforge.oi.oi_concentration_result import (
    OIConcentrationResult,
)


def build_result() -> OIConcentrationResult:
    """
    Build reusable concentration result.
    """

    df = pd.DataFrame(
        {
            "strike_price": [
                24800,
                24850,
                24900,
                24950,
                25000,
            ],
            "OI_SHARE": [
                0.24,
                0.17,
                0.12,
                0.07,
                0.03,
            ],
            "CONCENTRATION": [
                ConcentrationLevel.VERY_HIGH.value,
                ConcentrationLevel.HIGH.value,
                ConcentrationLevel.MEDIUM.value,
                ConcentrationLevel.LOW.value,
                ConcentrationLevel.VERY_LOW.value,
            ],
        }
    )

    return OIConcentrationResult(df)


# ==========================================================
# DataFrame
# ==========================================================


def test_dataframe():

    result = build_result()

    assert len(result.dataframe()) == 5


def test_dataframe_returns_copy():

    result = build_result()

    df = result.dataframe()

    df.loc[0, "OI_SHARE"] = 999

    assert result.dataframe().iloc[0]["OI_SHARE"] == 0.24


# ==========================================================
# Filters
# ==========================================================


def test_very_high():

    result = build_result()

    assert len(result.very_high()) == 1


def test_high():

    result = build_result()

    assert len(result.high()) == 1


def test_medium():

    result = build_result()

    assert len(result.medium()) == 1


def test_low():

    result = build_result()

    assert len(result.low()) == 1


def test_very_low():

    result = build_result()

    assert len(result.very_low()) == 1


# ==========================================================
# Ranking
# ==========================================================


def test_top_concentration():

    result = build_result()

    df = result.top_concentration(2)

    assert len(df) == 2

    assert df.iloc[0]["OI_SHARE"] == 0.24


# ==========================================================
# Summary
# ==========================================================


def test_summary():

    result = build_result()

    summary = result.summary()

    assert summary[ConcentrationLevel.VERY_HIGH.value] == 1

    assert summary[ConcentrationLevel.HIGH.value] == 1

    assert summary[ConcentrationLevel.MEDIUM.value] == 1

    assert summary[ConcentrationLevel.LOW.value] == 1

    assert summary[ConcentrationLevel.VERY_LOW.value] == 1


# ==========================================================
# Dictionary
# ==========================================================


def test_to_dict():

    result = build_result()

    d = result.to_dict()

    assert d["rows"] == 5

    assert d["highest_concentration"] == 24800

    assert "summary" in d


# ==========================================================
# Representation
# ==========================================================


def test_repr():

    result = build_result()

    assert "OIConcentrationResult" in repr(result)