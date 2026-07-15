"""
==============================================================
Tests for RegimeResult
==============================================================
"""

from optionforge.regime.enums.regime_state import (
    RegimeState,
)

from optionforge.regime.regime_result import (
    RegimeResult,
)


def build_result():

    return RegimeResult(

        regime=RegimeState.STRONG_UPTREND,

        confidence=0.91,

    )


# ==========================================================
# Values
# ==========================================================

def test_regime():

    assert (

        build_result().regime

        is RegimeState.STRONG_UPTREND

    )


def test_confidence():

    assert build_result().confidence == 0.91


# ==========================================================
# Helpers
# ==========================================================

def test_trending():

    assert build_result().is_trending()


def test_bullish():

    assert build_result().is_bullish()


def test_not_bearish():

    assert not build_result().is_bearish()


def test_not_ranging():

    assert not build_result().is_ranging()


def test_not_expansion():

    assert not build_result().is_volatility_expansion()


def test_not_compression():

    assert not build_result().is_volatility_compression()


# ==========================================================
# Summary
# ==========================================================

def test_summary():

    summary = build_result().summary()

    assert summary["regime"] == "STRONG_UPTREND"

    assert summary["confidence"] == 0.91


# ==========================================================
# Dictionary
# ==========================================================

def test_dict():

    d = build_result().to_dict()

    assert d["regime"] == "STRONG_UPTREND"


# ==========================================================
# Repr
# ==========================================================

def test_repr():

    assert (

        "RegimeResult"

        in repr(build_result())

    )