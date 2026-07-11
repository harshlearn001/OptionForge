"""
============================================================
OptionForge
ResearchEngine Tests
============================================================
"""

from optionforge.analytics.drawdown_analysis import DrawdownAnalysis
from optionforge.analytics.equity_curve import EquityCurve
from optionforge.analytics.performance_metrics import PerformanceMetrics
from optionforge.analytics.performance_report import PerformanceReport
from optionforge.analytics.trade_statistics import TradeStatistics
from optionforge.backtest.backtest import Backtest
from optionforge.backtest.backtest_result import BacktestResult
from optionforge.research.research import Research
from optionforge.research.research_engine import ResearchEngine
from optionforge.research.research_registry import ResearchRegistry
from optionforge.research.research_result import ResearchResult


def engine():

    return ResearchEngine()


def performance_report():

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

    bt_result = BacktestResult(
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
        calmar_ratio=2,
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
        backtest_result=bt_result,
        equity_curve=curve,
        drawdown_analysis=drawdown,
        performance_metrics=metrics,
        trade_statistics=trades,
    )


def research():

    return Research(
        name="Walk Forward",
        strategy_name="Modified PCR",
    )


def test_registry():

    assert isinstance(
        engine().registry,
        ResearchRegistry,
    )


def test_evaluate():

    result = engine().evaluate(
        research=research(),
        performance_report=performance_report(),
        research_score=91.5,
        approved=True,
        recommendation="APPROVED",
    )

    assert isinstance(
        result,
        ResearchResult,
    )


def test_score():

    result = engine().evaluate(
        research=research(),
        performance_report=performance_report(),
        research_score=91.5,
        approved=True,
    )

    assert result.research_score == 91.5


def test_approved():

    result = engine().evaluate(
        research=research(),
        performance_report=performance_report(),
        research_score=91.5,
        approved=True,
    )

    assert result.approved


def test_trade_count():

    result = engine().evaluate(
        research=research(),
        performance_report=performance_report(),
        research_score=91.5,
        approved=True,
    )

    assert result.trade_count == 20


def test_return():

    result = engine().evaluate(
        research=research(),
        performance_report=performance_report(),
        research_score=91.5,
        approved=True,
    )

    assert result.total_return == 5


def test_repr():

    assert "ResearchEngine" in repr(engine())


def test_registry_identity():

    e = engine()

    assert e.registry is e.registry