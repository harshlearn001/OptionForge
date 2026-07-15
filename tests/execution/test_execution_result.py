"""
============================================================
OptionForge
ExecutionResult Tests
============================================================
"""

from optionforge.execution.execution_result import ExecutionResult
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


def execution_result():

    return ExecutionResult(
        trades=(trade(),),
    )


def test_trade_count():

    assert execution_result().trade_count == 1


def test_total_quantity():

    assert execution_result().total_quantity == 100


def test_total_notional():

    assert execution_result().total_notional == (trade().notional_value)


def test_average_execution_price():

    assert execution_result().average_execution_price == trade().average_price


def test_complete_trade_count():

    assert execution_result().complete_trade_count == 1


def test_partial_trade_count():

    assert execution_result().partial_trade_count == 0


def test_unfilled_trade_count():

    assert execution_result().unfilled_trade_count == 0


def test_empty_result():

    result = ExecutionResult()

    assert result.trade_count == 0

    assert result.total_quantity == 0

    assert result.total_notional == 0.0

    assert result.average_execution_price == 0.0


def test_to_dict():

    data = execution_result().to_dict()

    assert data["trade_count"] == 1

    assert data["total_quantity"] == 100

    assert data["complete_trade_count"] == 1


def test_str():

    assert "ExecutionResult" in str(execution_result())


def test_repr():

    assert "ExecutionResult" in repr(execution_result())
