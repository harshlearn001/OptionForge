"""
Tests for OIWallEngine.
"""

from optionforge.oi.oi_by_strike import OIByStrike
from optionforge.oi.oi_wall_engine import OIWallEngine
from optionforge.oi.oi_wall_result import OIWallResult

from tests.fixtures.option_chain_fixture import build_option_chain


def build_engine():

    chain = build_option_chain()

    oi = OIByStrike(chain)

    return OIWallEngine(oi)


# ==========================================================
# Result
# ==========================================================

def test_returns_result():

    result = build_engine().calculate()

    assert isinstance(result, OIWallResult)


# ==========================================================
# DataFrame
# ==========================================================

def test_dataframe_exists():

    result = build_engine().calculate()

    assert not result.dataframe().empty


def test_wall_column_exists():

    result = build_engine().calculate()

    assert "WALL" in result.dataframe().columns


# ==========================================================
# Summary
# ==========================================================

def test_summary():

    result = build_engine().calculate()

    assert isinstance(result.summary(), dict)


# ==========================================================
# Filters
# ==========================================================

def test_call_wall():

    result = build_engine().calculate()

    result.call_wall()


def test_put_wall():

    result = build_engine().calculate()

    result.put_wall()


# ==========================================================
# Support / Resistance
# ==========================================================

def test_support():

    result = build_engine().calculate()

    assert result.support() is not None


def test_resistance():

    result = build_engine().calculate()

    assert result.resistance() is not None


# ==========================================================
# Representation
# ==========================================================

def test_repr():

    engine = build_engine()

    assert "OIWallEngine" in repr(engine)