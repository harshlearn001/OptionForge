"""
==============================================================
Tests for RegimeState
==============================================================
"""

from optionforge.regime.enums.regime_state import (
    RegimeState,
)


def test_unique_members():

    assert len(RegimeState) == 7


def test_string():

    assert (
        str(RegimeState.UPTREND)
        == "UPTREND"
    )


def test_strong_uptrend():

    assert (
        RegimeState.STRONG_UPTREND.name
        == "STRONG_UPTREND"
    )


def test_uptrend():

    assert (
        RegimeState.UPTREND.name
        == "UPTREND"
    )


def test_range():

    assert (
        RegimeState.RANGE_BOUND.name
        == "RANGE_BOUND"
    )


def test_downtrend():

    assert (
        RegimeState.DOWNTREND.name
        == "DOWNTREND"
    )


def test_strong_downtrend():

    assert (
        RegimeState.STRONG_DOWNTREND.name
        == "STRONG_DOWNTREND"
    )


def test_volatility_expansion():

    assert (
        RegimeState.VOLATILITY_EXPANSION.name
        == "VOLATILITY_EXPANSION"
    )


def test_volatility_compression():

    assert (
        RegimeState.VOLATILITY_COMPRESSION.name
        == "VOLATILITY_COMPRESSION"
    )