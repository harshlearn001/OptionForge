"""
============================================================
OptionForge
OrderType Tests
============================================================
"""

from optionforge.execution.order_type import OrderType


def test_market():

    assert OrderType.MARKET.is_market


def test_limit():

    assert OrderType.LIMIT.is_limit


def test_stop():

    assert OrderType.STOP.is_stop


def test_stop_limit():

    assert OrderType.STOP_LIMIT.is_stop_limit


def test_str():

    assert str(OrderType.STOP_LIMIT) == "Stop Limit"