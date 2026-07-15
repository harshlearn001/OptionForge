"""
==============================================================
Tests for OIShiftEngine
==============================================================
"""

from __future__ import annotations

from optionforge.oi.oi_by_strike import OIByStrike
from optionforge.oi.oi_shift_engine import OIShiftEngine
from optionforge.oi.oi_shift_result import OIShiftResult

from tests.fixtures.option_chain_fixture import (
    build_option_chain,
)


def build_engine() -> OIShiftEngine:

    previous = OIByStrike(build_option_chain())

    current = OIByStrike(build_option_chain())

    return OIShiftEngine(
        previous=previous,
        current=current,
    )


# ==========================================================
# Result
# ==========================================================

def test_returns_result():

    result = build_engine().calculate()

    assert isinstance(result, OIShiftResult)


# ==========================================================
# DataFrame
# ==========================================================

def test_dataframe_exists():

    result = build_engine().calculate()

    assert not result.dataframe().empty


def test_shift_column_exists():

    result = build_engine().calculate()

    assert "SHIFT" in result.dataframe().columns


def test_shift_direction_column_exists():

    result = build_engine().calculate()

    assert "SHIFT_DIRECTION" in result.dataframe().columns


# ==========================================================
# Filters
# ==========================================================

def test_strong_up():

    build_engine().calculate().strong_up()


def test_strong_down():

    build_engine().calculate().strong_down()


# ==========================================================
# Summary
# ==========================================================

def test_summary():

    summary = build_engine().calculate().summary()

    assert isinstance(summary, dict)


# ==========================================================
# Ranking
# ==========================================================

def test_top_upward_shift():

    build_engine().calculate().top_upward_shift()


def test_top_downward_shift():

    build_engine().calculate().top_downward_shift()


# ==========================================================
# Representation
# ==========================================================

def test_repr():

    engine = build_engine()

    assert "OIShiftEngine" in repr(engine)