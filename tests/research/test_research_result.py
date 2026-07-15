"""
============================================================
OptionForge
ResearchResult Tests
============================================================
"""

import pytest

from optionforge.analytics.drawdown_analysis import DrawdownAnalysis
from optionforge.analytics.equity_curve import EquityCurve
from optionforge.analytics.performance_metrics import PerformanceMetrics
from optionforge.analytics.performance_report import PerformanceReport
from optionforge.analytics.trade_statistics import TradeStatistics
from optionforge.backtest.backtest import Backtest
from optionforge.backtest.backtest_result import BacktestResult
from optionforge.research.research import Research
from optionforge.research.research_result import ResearchResult


def result():

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

    report = PerformanceReport(
        backtest_result=bt_result,
        equity_curve=curve,
        drawdown_analysis=drawdown,
        performance_metrics=metrics,
        trade_statistics=trades,
    )

    research = Research(
        name="Walk Forward",
        strategy_name="Modified PCR",
    )

    return ResearchResult(
        research=research,
        performance_report=report,
        research_score=91.5,
        approved=True,
        recommendation="APPROVED",
    )


def test_create():

    assert isinstance(
        result(),
        ResearchResult,
    )


def test_score():

    assert result().research_score == 91.5


def test_approved():

    assert result().is_approved


def test_return():

    assert result().total_return == 5


def test_trade_count():

    assert result().trade_count == 20


def test_to_dict():

    data = result().to_dict()

    assert data["approved"] is True

    assert data["research_score"] == 91.5


@pytest.mark.parametrize(
    "score",
    [
        -1,
        101,
    ],
)
def test_validation(score):

    kwargs = result().to_dict()

    kwargs["research"] = result().research

    kwargs["performance_report"] = result().performance_report

    kwargs["research_score"] = score

    kwargs.pop("metadata", None)

    with pytest.raises(ValueError):

        ResearchResult(**kwargs)


def test_str():

    assert "ResearchResult" in str(result())


def test_repr():

    assert "ResearchResult" in repr(result())
