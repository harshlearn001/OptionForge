"""
==============================================================
Tests for OITrendEngine
==============================================================
"""

from __future__ import annotations

import pytest

from optionforge.oi.oi_by_strike import OIByStrike
from optionforge.oi.oi_trend_engine import OITrendEngine
from optionforge.oi.oi_trend_result import OITrendResult

from tests.fixtures.option_chain_fixture import (
    build_option_chain,
)


# ==========================================================
# Helpers
# ==========================================================


def build_history() -> tuple[OIByStrike, ...]:
    """
    Build sample history.
    """

    return (
        OIByStrike(build_option_chain()),
        OIByStrike(build_option_chain()),
        OIByStrike(build_option_chain()),
    )


def build_engine() -> OITrendEngine:
    """
    Build reusable engine.
    """

    return OITrendEngine(build_history())


# ==========================================================
# Constructor
# ==========================================================


def test_requires_at_least_two_snapshots():

    history = (
        OIByStrike(build_option_chain()),
    )

    with pytest.raises(ValueError):

        OITrendEngine(history)


# ==========================================================
# Result
# ==========================================================


def test_returns_result():

    result = build_engine().calculate()

    assert isinstance(result, OITrendResult)


# ==========================================================
# DataFrame
# ==========================================================


def test_dataframe_exists():

    result = build_engine().calculate()

    assert not result.dataframe().empty


def test_trend_score_column_exists():

    result = build_engine().calculate()

    assert "TREND_SCORE" in result.dataframe().columns


def test_trend_column_exists():

    result = build_engine().calculate()

    assert "TREND" in result.dataframe().columns


# ==========================================================
# Summary
# ==========================================================


def test_summary():

    result = build_engine().calculate()

    assert isinstance(result.summary(), dict)


# ==========================================================
# Filters
# ==========================================================


def test_strong_bullish():

    result = build_engine().calculate()

    result.strong_bullish()


def test_strong_bearish():

    result = build_engine().calculate()

    result.strong_bearish()


# ==========================================================
# Ranking
# ==========================================================


def test_top_bullish():

    result = build_engine().calculate()

    result.top_bullish()


def test_top_bearish():

    result = build_engine().calculate()

    result.top_bearish()


# ==========================================================
# Representation
# ==========================================================


def test_repr():

    engine = build_engine()

    assert "OITrendEngine" in repr(engine)