"""
============================================================
OptionForge
ExecutionEngine Tests
============================================================
"""

from optionforge.execution.execution_builder import (
    ExecutionBuilder,
)
from optionforge.execution.execution_engine import (
    ExecutionEngine,
)
from optionforge.execution.execution_registry import (
    ExecutionRegistry,
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


def engine():

    return ExecutionEngine()


def test_registry():

    assert isinstance(

        engine().registry,

        ExecutionRegistry,

    )


def test_execute_returns_result():

    result = engine().execute(

        trades=(trade(),),

    )

    assert isinstance(

        result,

        ExecutionResult,

    )


def test_trade_count():

    result = engine().execute(

        trades=(trade(),),

    )

    assert result.trade_count == 1


def test_quantity():

    result = engine().execute(

        trades=(trade(),),

    )

    assert result.total_quantity == 100


def test_notional():

    result = engine().execute(

        trades=(trade(),),

    )

    assert result.total_notional == 25000.0


def test_empty():

    result = engine().execute()

    assert result.trade_count == 0


def test_builder_type():

    builder = engine().registry.get_builder()

    assert isinstance(

        builder,

        ExecutionBuilder,

    )


def test_repr():

    assert (

        "ExecutionEngine"

        in repr(

            engine(),

        )

    )