"""
==============================================================
Tests for OIConcentrationEngine
==============================================================
"""

from __future__ import annotations

from optionforge.oi.oi_by_strike import OIByStrike
from optionforge.oi.oi_concentration_engine import (
    OIConcentrationEngine,
)
from optionforge.oi.oi_concentration_result import (
    OIConcentrationResult,
)

from tests.fixtures.option_chain_fixture import (
    build_option_chain,
)


def build_engine() -> OIConcentrationEngine:

    chain = build_option_chain()

    oi = OIByStrike(chain)

    return OIConcentrationEngine(oi)


# ==========================================================
# Result
# ==========================================================

def test_returns_result():

    result = build_engine().calculate()

    assert isinstance(result, OIConcentrationResult)


# ==========================================================
# DataFrame
# ==========================================================

def test_dataframe_exists():

    result = build_engine().calculate()

    assert not result.dataframe().empty


def test_concentration_column_exists():

    result = build_engine().calculate()

    assert "CONCENTRATION" in result.dataframe().columns


# ==========================================================
# Filters
# ==========================================================

def test_very_high():

    result = build_engine().calculate()

    result.very_high()


def test_high():

    result = build_engine().calculate()

    result.high()


def test_medium():

    result = build_engine().calculate()

    result.medium()


def test_low():

    result = build_engine().calculate()

    result.low()


def test_very_low():

    result = build_engine().calculate()

    result.very_low()


# ==========================================================
# Summary
# ==========================================================

def test_summary():

    result = build_engine().calculate()

    assert isinstance(result.summary(), dict)


# ==========================================================
# Representation
# ==========================================================

def test_repr():

    engine = build_engine()

    assert "OIConcentrationEngine" in repr(engine)