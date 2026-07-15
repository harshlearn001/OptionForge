"""
==============================================================
Tests for OITrendResult
==============================================================
"""

from __future__ import annotations

import pandas as pd

from optionforge.common.enums import TrendDirection
from optionforge.oi.oi_trend_result import OITrendResult


def build_result() -> OITrendResult:

    df = pd.DataFrame(
        {
            "strike_price": [
                24800,
                24850,
                24900,
                24950,
                25000,
            ],
            "TREND_SCORE": [
                0.80,
                0.35,
                0.00,
                -0.35,
                -0.80,
            ],
            "TREND": [
                TrendDirection.STRONG_BULLISH.value,
                TrendDirection.BULLISH.value,
                TrendDirection.SIDEWAYS.value,
                TrendDirection.BEARISH.value,
                TrendDirection.STRONG_BEARISH.value,
            ],
        }
    )

    return OITrendResult(df)


def test_dataframe():
    assert len(build_result().dataframe()) == 5


def test_dataframe_returns_copy():
    df = build_result().dataframe()
    df.loc[0, "TREND_SCORE"] = 999
    assert build_result().dataframe().iloc[0]["TREND_SCORE"] == 0.80


def test_strong_bullish():
    assert len(build_result().strong_bullish()) == 1


def test_bullish():
    assert len(build_result().bullish()) == 1


def test_sideways():
    assert len(build_result().sideways()) == 1


def test_bearish():
    assert len(build_result().bearish()) == 1


def test_strong_bearish():
    assert len(build_result().strong_bearish()) == 1


def test_top_bullish():
    df = build_result().top_bullish(2)
    assert len(df) == 2
    assert df.iloc[0]["TREND_SCORE"] == 0.80


def test_top_bearish():
    df = build_result().top_bearish(2)
    assert len(df) == 2
    assert df.iloc[0]["TREND_SCORE"] == -0.80


def test_summary():

    summary = build_result().summary()

    assert summary[TrendDirection.STRONG_BULLISH.value] == 1
    assert summary[TrendDirection.BULLISH.value] == 1
    assert summary[TrendDirection.SIDEWAYS.value] == 1
    assert summary[TrendDirection.BEARISH.value] == 1
    assert summary[TrendDirection.STRONG_BEARISH.value] == 1


def test_to_dict():

    d = build_result().to_dict()

    assert d["rows"] == 5
    assert d["strongest_bullish"] == 24800
    assert d["strongest_bearish"] == 25000


def test_repr():

    assert "OITrendResult" in repr(build_result())