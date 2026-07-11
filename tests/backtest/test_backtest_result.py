"""
============================================================
OptionForge
BacktestResult Tests
============================================================
"""

from optionforge.backtest.backtest import Backtest
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


def result():

    return BacktestResult(

        backtests=(

            backtest(),

        ),

    )


def test_count():

    assert result().backtest_count == 1


def test_total_return():

    assert result().total_return == 20.0


def test_average_return():

    assert result().average_return == 20.0


def test_average_sharpe():

    assert result().average_sharpe == 1.5


def test_total_trades():

    assert result().total_trades == 100


def test_average_win_rate():

    assert result().average_win_rate == 60.0


def test_empty():

    r = BacktestResult()

    assert r.backtest_count == 0

    assert r.average_return == 0.0

    assert r.average_sharpe == 0.0


def test_to_dict():

    data = result().to_dict()

    assert data["backtest_count"] == 1

    assert data["total_return"] == 20.0

    assert data["total_trades"] == 100


def test_str():

    assert "BacktestResult" in str(result())


def test_repr():

    assert "BacktestResult" in repr(result())