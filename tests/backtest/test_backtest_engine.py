"""
============================================================
OptionForge
BacktestEngine Tests
============================================================
"""

from optionforge.backtest.backtest import Backtest
from optionforge.backtest.backtest_builder import BacktestBuilder
from optionforge.backtest.backtest_engine import BacktestEngine
from optionforge.backtest.backtest_registry import BacktestRegistry
from optionforge.backtest.backtest_result import BacktestResult


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


def engine():

    return BacktestEngine()


def test_registry():

    assert isinstance(

        engine().registry,

        BacktestRegistry,

    )


def test_execute_returns_result():

    result = engine().execute(

        backtests=(backtest(),),

    )

    assert isinstance(

        result,

        BacktestResult,

    )


def test_backtest_count():

    result = engine().execute(

        backtests=(backtest(),),

    )

    assert result.backtest_count == 1


def test_total_return():

    result = engine().execute(

        backtests=(backtest(),),

    )

    assert result.total_return == 20.0


def test_total_trades():

    result = engine().execute(

        backtests=(backtest(),),

    )

    assert result.total_trades == 100


def test_empty():

    result = engine().execute()

    assert result.backtest_count == 0


def test_builder_type():

    builder = engine().registry.get_builder()

    assert isinstance(

        builder,

        BacktestBuilder,

    )


def test_repr():

    assert (

        "BacktestEngine"

        in repr(

            engine(),

        )

    )