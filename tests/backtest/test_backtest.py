"""
============================================================
OptionForge
Backtest Tests
============================================================
"""

import pytest

from optionforge.backtest.backtest import Backtest


def backtest():

    return Backtest(

        total_return=25.0,

        annual_return=18.5,

        max_drawdown=8.2,

        sharpe_ratio=1.75,

        sortino_ratio=2.30,

        win_rate=62.5,

        total_trades=100,

        profitable_trades=63,

        losing_trades=37,

    )


# ==========================================================
# Construction
# ==========================================================

def test_create():

    assert isinstance(

        backtest(),

        Backtest,

    )


# ==========================================================
# Values
# ==========================================================

def test_total_return():

    assert backtest().total_return == 25.0


def test_annual_return():

    assert backtest().annual_return == 18.5


def test_drawdown():

    assert backtest().max_drawdown == 8.2


def test_sharpe():

    assert backtest().sharpe_ratio == 1.75


def test_sortino():

    assert backtest().sortino_ratio == 2.30


def test_win_rate():

    assert backtest().win_rate == 62.5


def test_trade_counts():

    bt = backtest()

    assert bt.total_trades == 100

    assert bt.profitable_trades == 63

    assert bt.losing_trades == 37


# ==========================================================
# Convenience
# ==========================================================

def test_expectancy():

    assert backtest().expectancy == 0.25


def test_profitable():

    assert backtest().is_profitable


def test_has_drawdown():

    assert backtest().has_drawdown


# ==========================================================
# Validation
# ==========================================================

@pytest.mark.parametrize(

    "field,value",

    [

        ("win_rate", -1),

        ("win_rate", 101),

        ("total_trades", -1),

        ("profitable_trades", -1),

        ("losing_trades", -1),

    ],

)

def test_validation(field, value):

    kwargs = dict(

        total_return=25.0,

        annual_return=18.5,

        max_drawdown=8.2,

        sharpe_ratio=1.75,

        sortino_ratio=2.30,

        win_rate=62.5,

        total_trades=100,

        profitable_trades=63,

        losing_trades=37,

    )

    kwargs[field] = value

    with pytest.raises(ValueError):

        Backtest(**kwargs)


# ==========================================================
# Serialization
# ==========================================================

def test_to_dict():

    data = backtest().to_dict()

    assert data["total_return"] == 25.0

    assert data["annual_return"] == 18.5

    assert data["total_trades"] == 100

    assert data["expectancy"] == 0.25


# ==========================================================
# Representation
# ==========================================================

def test_str():

    assert "Backtest" in str(backtest())


def test_repr():

    assert "Backtest" in repr(backtest())