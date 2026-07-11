"""
============================================================
OptionForge
PerformanceMetrics Tests
============================================================
"""

import pytest

from optionforge.analytics.performance_metrics import (
    PerformanceMetrics,
)


def metrics():

    return PerformanceMetrics(

        total_return=25.0,

        annual_return=18.0,

        cagr=17.5,

        volatility=12.0,

        max_drawdown=8.0,

        sharpe_ratio=1.80,

        sortino_ratio=2.30,

        calmar_ratio=2.20,

        win_rate=62.0,

        profit_factor=1.85,

        expectancy=0.42,

        recovery_factor=3.10,

    )


# ==========================================================
# Construction
# ==========================================================

def test_create():

    assert isinstance(

        metrics(),

        PerformanceMetrics,

    )


# ==========================================================
# Values
# ==========================================================

def test_total_return():

    assert metrics().total_return == 25.0


def test_sharpe():

    assert metrics().sharpe_ratio == 1.80


def test_profit_factor():

    assert metrics().profit_factor == 1.85


def test_expectancy():

    assert metrics().expectancy == 0.42


# ==========================================================
# Convenience
# ==========================================================

def test_profitable():

    assert metrics().is_profitable


def test_positive_expectancy():

    assert metrics().has_positive_expectancy


def test_low_risk():

    assert metrics().is_low_risk


# ==========================================================
# Validation
# ==========================================================

@pytest.mark.parametrize(

    "field,value",

    [

        ("win_rate", -1),

        ("win_rate", 101),

        ("max_drawdown", -1),

        ("max_drawdown", 101),

        ("volatility", -1),

        ("profit_factor", -1),

    ],

)

def test_validation(field, value):

    kwargs = dict(

        total_return=25.0,

        annual_return=18.0,

        cagr=17.5,

        volatility=12.0,

        max_drawdown=8.0,

        sharpe_ratio=1.80,

        sortino_ratio=2.30,

        calmar_ratio=2.20,

        win_rate=62.0,

        profit_factor=1.85,

        expectancy=0.42,

        recovery_factor=3.10,

    )

    kwargs[field] = value

    with pytest.raises(ValueError):

        PerformanceMetrics(**kwargs)


# ==========================================================
# Serialization
# ==========================================================

def test_to_dict():

    data = metrics().to_dict()

    assert data["total_return"] == 25.0

    assert data["sharpe_ratio"] == 1.80

    assert data["profit_factor"] == 1.85


# ==========================================================
# Representation
# ==========================================================

def test_str():

    assert "PerformanceMetrics" in str(metrics())


def test_repr():

    assert "PerformanceMetrics" in repr(metrics())