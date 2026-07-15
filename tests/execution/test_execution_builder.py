"""
============================================================
OptionForge
ExecutionBuilder Tests
============================================================
"""

from optionforge.execution.execution_builder import (
    ExecutionBuilder,
)
from optionforge.execution.execution_result import (
    ExecutionResult,
)
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


def trade():

    fill = Fill(
        order=order(),
        quantity=100,
        price=250.0,
        status=FillStatus.COMPLETE,
    )

    return Trade(
        order=order(),
        fills=(fill,),
    )


def test_builder_returns_execution_result():

    result = ExecutionBuilder().build(
        trades=(trade(),),
    )

    assert isinstance(
        result,
        ExecutionResult,
    )


def test_trade_count():

    result = ExecutionBuilder().build(
        trades=(trade(),),
    )

    assert result.trade_count == 1


def test_empty():

    result = ExecutionBuilder().build()

    assert result.trade_count == 0


def test_quantity():

    result = ExecutionBuilder().build(
        trades=(trade(),),
    )

    assert result.total_quantity == 100


def test_notional():

    result = ExecutionBuilder().build(
        trades=(trade(),),
    )

    assert result.total_notional == 25000.0


def test_repr():

    result = ExecutionBuilder().build()

    assert "ExecutionResult" in repr(result)
