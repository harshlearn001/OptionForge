"""
============================================================
OptionForge
BacktestBuilder Tests
============================================================
"""

from optionforge.backtest.backtest import Backtest
from optionforge.backtest.backtest_builder import (
    BacktestBuilder,
)
from optionforge.backtest.backtest_result import (
    BacktestResult,
)


def backtest():

    return Backtest(

        total_return=20.0,

        annual_return=15.0,

        max_drawdown=6.0,

        sharpe_ratio=1.5,

        sortino_ratio=2.0,

        win_rate=60.0,

        total_trades=100,

        profitable_trades=60,

        losing_trades=40,

    )


def builder():

    return BacktestBuilder()


def test_returns_result():

    result = builder().build(

        backtests=(backtest(),),

    )

    assert isinstance(

        result,

        BacktestResult,

    )


def test_count():

    result = builder().build(

        backtests=(backtest(),),

    )

    assert result.backtest_count == 1


def test_total_return():

    result = builder().build(

        backtests=(backtest(),),

    )

    assert result.total_return == 20.0


def test_total_trades():

    result = builder().build(

        backtests=(backtest(),),

    )

    assert result.total_trades == 100


def test_empty():

    result = builder().build()

    assert result.backtest_count == 0


def test_repr():

    result = builder().build()

    assert "BacktestResult" in repr(result)