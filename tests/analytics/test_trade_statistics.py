"""
============================================================
OptionForge
TradeStatistics Tests
============================================================
"""

import pytest

from optionforge.analytics.trade_statistics import (
    TradeStatistics,
)


def stats():

    return TradeStatistics(

        total_trades=100,

        winning_trades=60,

        losing_trades=40,

        average_win=1250.0,

        average_loss=-700.0,

        largest_win=5200.0,

        largest_loss=-2400.0,

        profit_factor=1.80,

        expectancy=320.0,

        longest_winning_streak=8,

        longest_losing_streak=4,

    )


# ==========================================================
# Construction
# ==========================================================

def test_create():

    assert isinstance(

        stats(),

        TradeStatistics,

    )


# ==========================================================
# Values
# ==========================================================

def test_counts():

    s = stats()

    assert s.total_trades == 100

    assert s.winning_trades == 60

    assert s.losing_trades == 40


def test_win_rate():

    assert stats().win_rate == 60.0


def test_loss_rate():

    assert stats().loss_rate == 40.0


def test_profit_factor():

    assert stats().profit_factor == 1.80


def test_expectancy():

    assert stats().expectancy == 320.0


# ==========================================================
# Convenience
# ==========================================================

def test_profitable():

    assert stats().is_profitable


# ==========================================================
# Validation
# ==========================================================

@pytest.mark.parametrize(

    "field,value",

    [

        ("total_trades", -1),

        ("winning_trades", -1),

        ("losing_trades", -1),

        ("profit_factor", -1),

    ],

)

def test_validation(field, value):

    kwargs = dict(

        total_trades=100,

        winning_trades=60,

        losing_trades=40,

        average_win=1250.0,

        average_loss=-700.0,

        largest_win=5200.0,

        largest_loss=-2400.0,

        profit_factor=1.80,

        expectancy=320.0,

        longest_winning_streak=8,

        longest_losing_streak=4,

    )

    kwargs[field] = value

    with pytest.raises(ValueError):

        TradeStatistics(**kwargs)


def test_invalid_trade_count():

    with pytest.raises(ValueError):

        TradeStatistics(

            total_trades=10,

            winning_trades=8,

            losing_trades=5,

            average_win=100,

            average_loss=-50,

            largest_win=500,

            largest_loss=-200,

            profit_factor=2,

            expectancy=20,

            longest_winning_streak=3,

            longest_losing_streak=2,

        )


# ==========================================================
# Serialization
# ==========================================================

def test_to_dict():

    data = stats().to_dict()

    assert data["win_rate"] == 60.0

    assert data["loss_rate"] == 40.0

    assert data["profit_factor"] == 1.80


# ==========================================================
# Representation
# ==========================================================

def test_str():

    assert "TradeStatistics" in str(stats())


def test_repr():

    assert "TradeStatistics" in repr(stats())