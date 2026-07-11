"""
============================================================
OptionForge
Order Tests
============================================================
"""

import pytest

from optionforge.execution.order import Order
from optionforge.execution.order_side import OrderSide
from optionforge.execution.order_status import OrderStatus
from optionforge.execution.order_type import OrderType


def order():

    return Order(

        symbol="NIFTY",

        side=OrderSide.BUY,

        order_type=OrderType.MARKET,

        status=OrderStatus.PENDING,

        quantity=50,

        price=250.0,

    )


def test_symbol():

    assert order().symbol == "NIFTY"


def test_buy():

    assert order().is_buy


def test_market():

    assert order().is_market


def test_open():

    assert order().is_open


def test_notional():

    assert order().notional_value == 12500.0


def test_to_dict():

    data = order().to_dict()

    assert data["symbol"] == "NIFTY"

    assert data["quantity"] == 50


def test_empty_symbol():

    with pytest.raises(ValueError):

        Order(

            symbol="",

            side=OrderSide.BUY,

            order_type=OrderType.MARKET,

            status=OrderStatus.PENDING,

            quantity=1,

            price=1.0,

        )


def test_negative_price():

    with pytest.raises(ValueError):

        Order(

            symbol="ABC",

            side=OrderSide.BUY,

            order_type=OrderType.MARKET,

            status=OrderStatus.PENDING,

            quantity=1,

            price=-1,

        )


def test_zero_quantity():

    with pytest.raises(ValueError):

        Order(

            symbol="ABC",

            side=OrderSide.BUY,

            order_type=OrderType.MARKET,

            status=OrderStatus.PENDING,

            quantity=0,

            price=100,

        )


def test_str():

    assert "Order" in str(order())


def test_repr():

    assert "Order" in repr(order())