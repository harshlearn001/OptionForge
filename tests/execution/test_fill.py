"""
============================================================
OptionForge
Fill Tests
============================================================
"""

import pytest

from optionforge.execution.fill import Fill
from optionforge.execution.fill_status import FillStatus
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
        quantity=100,
        price=250.0,
    )


def fill():

    return Fill(
        order=order(),
        quantity=40,
        price=251.0,
        status=FillStatus.PARTIAL,
    )


def test_parent_order():

    assert fill().order.symbol == "NIFTY"


def test_quantity():

    assert fill().quantity == 40


def test_price():

    assert fill().price == 251.0


def test_notional_value():

    assert fill().notional_value == 10040.0


def test_remaining_quantity():

    assert fill().remaining_quantity == 60


def test_partial():

    assert fill().is_partial

    assert not fill().is_complete


def test_complete():

    complete_fill = Fill(
        order=order(),
        quantity=100,
        price=250.0,
        status=FillStatus.COMPLETE,
    )

    assert complete_fill.is_complete


def test_to_dict():

    data = fill().to_dict()

    assert data["quantity"] == 40

    assert data["price"] == 251.0

    assert data["status"] == "PARTIAL"


def test_negative_price():

    with pytest.raises(ValueError):

        Fill(
            order=order(),
            quantity=10,
            price=-1.0,
            status=FillStatus.PARTIAL,
        )


def test_zero_quantity():

    with pytest.raises(ValueError):

        Fill(
            order=order(),
            quantity=0,
            price=250.0,
            status=FillStatus.PARTIAL,
        )


def test_quantity_exceeds_order():

    with pytest.raises(ValueError):

        Fill(
            order=order(),
            quantity=101,
            price=250.0,
            status=FillStatus.PARTIAL,
        )


def test_str():

    assert "Fill" in str(fill())


def test_repr():

    assert "Fill" in repr(fill())
