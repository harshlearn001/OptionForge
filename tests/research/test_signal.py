"""
==============================================================
OptionForge
tests/research/test_signal.py
==============================================================
"""

from optionforge.research.signal import Signal


def test_buy():
    assert Signal.BUY.value == "BUY"


def test_sell():
    assert Signal.SELL.value == "SELL"


def test_watch():
    assert Signal.WATCH.value == "WATCH"


def test_string():
    assert str(Signal.BUY) == "BUY"
    assert str(Signal.SELL) == "SELL"
    assert str(Signal.WATCH) == "WATCH"
