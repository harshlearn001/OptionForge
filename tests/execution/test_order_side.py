"""
============================================================
OptionForge
OrderSide Tests
============================================================
"""

from optionforge.execution.order_side import OrderSide


def test_buy():

    assert OrderSide.BUY.is_buy

    assert not OrderSide.BUY.is_sell


def test_sell():

    assert OrderSide.SELL.is_sell

    assert not OrderSide.SELL.is_buy


def test_str():

    assert str(OrderSide.BUY) == "Buy"

    assert str(OrderSide.SELL) == "Sell"