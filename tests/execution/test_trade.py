"""
============================================================
OptionForge
Trade Tests
============================================================
"""

import pytest

from optionforge.execution.fill import Fill
from optionforge.execution.fill_status import FillStatus
from optionforge.execution.order import Order
from optionforge.execution.order_side import OrderSide
from optionforge.execution.order_status import OrderStatus
from optionforge.execution.order_type import OrderType
from optionforge.execution.trade import Trade


def order():

    return Order(

        symbol="NIFTY",

        side=OrderSide.BUY,

        order_type=OrderType.MARKET,

        status=OrderStatus.PENDING,

        quantity=100,

        price=250.0,

    )


def fill1():

    return Fill(

        order=order(),

        quantity=40,

        price=250.0,

        status=FillStatus.PARTIAL,

    )


def fill2():

    return Fill(

        order=order(),

        quantity=60,

        price=251.0,

        status=FillStatus.COMPLETE,

    )


def trade():

    return Trade(

        order=order(),

        fills=(

            fill1(),

            fill2(),

        ),

    )


def test_order():

    assert trade().order.symbol == "NIFTY"


def test_fill_count():

    assert trade().fill_count == 2


def test_total_quantity():

    assert trade().total_quantity == 100


def test_remaining_quantity():

    assert trade().remaining_quantity == 0


def test_notional_value():

    assert trade().notional_value == (

        fill1().notional_value

        + fill2().notional_value

    )


def test_average_price():

    expected = (

        (40 * 250.0)

        + (60 * 251.0)

    ) / 100

    assert trade().average_price == expected


def test_complete():

    assert trade().is_complete

    assert not trade().is_partial


def test_partial():

    partial = Trade(

        order=order(),

        fills=(

            fill1(),

        ),

    )

    assert partial.is_partial

    assert not partial.is_complete


def test_unfilled():

    empty = Trade(

        order=order(),

        fills=(),

    )

    assert empty.is_unfilled

    assert empty.total_quantity == 0

    assert empty.average_price == 0.0


def test_validation():

    with pytest.raises(ValueError):

        Trade(

            order=order(),

            fills=(

                Fill(

                    order=order(),

                    quantity=70,

                    price=250,

                    status=FillStatus.PARTIAL,

                ),

                Fill(

                    order=order(),

                    quantity=40,

                    price=250,

                    status=FillStatus.PARTIAL,

                ),

            ),

        )


def test_to_dict():

    data = trade().to_dict()

    assert data["fill_count"] == 2

    assert data["total_quantity"] == 100

    assert data["is_complete"] is True


def test_str():

    assert "Trade" in str(trade())


def test_repr():

    assert "Trade" in repr(trade())