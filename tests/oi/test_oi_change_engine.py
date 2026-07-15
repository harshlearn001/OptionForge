"""
==============================================================
Tests for OI Change Engine
==============================================================
"""

from optionforge.oi.oi_change_engine import OIChangeEngine
from tests.fixtures.option_chain_fixture import build_option_chain


def test_engine_creation():

    chain = build_option_chain()

    engine = OIChangeEngine(chain)

    assert engine.chain is chain


def test_calculate_returns_result():

    chain = build_option_chain()

    engine = OIChangeEngine(chain)

    result = engine.calculate()

    assert result is not None


def test_result_has_dataframe():

    chain = build_option_chain()

    engine = OIChangeEngine(chain)

    result = engine.calculate()

    assert hasattr(result, "to_dataframe")


def test_dataframe_not_empty():

    chain = build_option_chain()

    engine = OIChangeEngine(chain)

    result = engine.calculate()

    df = result.to_dataframe()

    assert len(df) > 0


def test_dataframe_columns():

    chain = build_option_chain()

    engine = OIChangeEngine(chain)

    result = engine.calculate()

    df = result.to_dataframe()

    expected = {
        "strike_price",
        "call_oi",
        "put_oi",
        "call_change",
        "put_change",
        "total_change",
        "call_volume",
        "put_volume",
        "pcr",
        "dominance",
        "buildup",
    }

    assert expected.issubset(df.columns)