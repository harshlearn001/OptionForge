"""
============================================================
OptionForge
OrderStatus Tests
============================================================
"""

from optionforge.execution.order_status import OrderStatus


def test_pending():

    assert OrderStatus.PENDING.is_open


def test_filled():

    assert OrderStatus.FILLED.is_closed

    assert OrderStatus.FILLED.is_filled


def test_cancelled():

    assert OrderStatus.CANCELLED.is_cancelled


def test_rejected():

    assert OrderStatus.REJECTED.is_rejected


def test_str():

    assert str(

        OrderStatus.PARTIALLY_FILLED

    ) == "Partially Filled"