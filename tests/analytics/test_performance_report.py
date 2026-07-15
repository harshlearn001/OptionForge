"""
============================================================
OptionForge
PerformanceReport Tests
============================================================
"""

from optionforge.analytics.drawdown_analysis import (
    DrawdownAnalysis,
)
from optionforge.analytics.equity_curve import (
    EquityCurve,
)
from optionforge.analytics.performance_metrics import (
    PerformanceMetrics,
)
from optionforge.analytics.performance_report import (
    PerformanceReport,
)
from optionforge.analytics.trade_statistics import (
    TradeStatistics,
)
from optionforge.backtest.backtest import (
    Backtest,
)
from optionforge.backtest.backtest_result import (
    BacktestResult,
)


def report():

    curve = EquityCurve(
        values=(100000, 102000, 105000),
    )

    backtest = Backtest(
        total_return=5,
        annual_return=5,
        max_drawdown=2,
        sharpe_ratio=1.5,
        sortino_ratio=2,
        win_rate=60,
        total_trades=20,
        profitable_trades=12,
        losing_trades=8,
    )

    result = BacktestResult(
        backtests=(backtest,),
    )

    drawdown = DrawdownAnalysis(
        equity_curve=curve,
        max_drawdown=2,
        current_drawdown=0,
        peak_equity=105000,
        lowest_equity=100000,
        recovered=True,
    )

    metrics = PerformanceMetrics(
        total_return=5,
        annual_return=5,
        cagr=5,
        volatility=8,
        max_drawdown=2,
        sharpe_ratio=1.5,
        sortino_ratio=2,
        calmar_ratio=2.5,
        win_rate=60,
        profit_factor=1.8,
        expectancy=250,
        recovery_factor=2.5,
    )

    trades = TradeStatistics(
        total_trades=20,
        winning_trades=12,
        losing_trades=8,
        average_win=300,
        average_loss=-150,
        largest_win=1000,
        largest_loss=-500,
        profit_factor=1.8,
        expectancy=250,
        longest_winning_streak=4,
        longest_losing_streak=2,
    )

    return PerformanceReport(
        backtest_result=result,
        equity_curve=curve,
        drawdown_analysis=drawdown,
        performance_metrics=metrics,
        trade_statistics=trades,
        summary="Institutional report",
    )


def test_create():

    assert isinstance(
        report(),
        PerformanceReport,
    )


def test_profitable():

    assert report().is_profitable


def test_trade_count():

    assert report().trade_count == 20


def test_total_return():

    assert report().total_return == 5


def test_summary():

    assert report().summary == "Institutional report"


def test_to_dict():

    data = report().to_dict()

    assert "performance_metrics" in data

    assert "trade_statistics" in data

    assert data["summary"] == "Institutional report"


def test_str():

    assert "PerformanceReport" in str(report())


def test_repr():

    assert "PerformanceReport" in repr(report())
