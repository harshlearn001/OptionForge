"""
============================================================
OptionForge
ScenarioAnalysis Tests
============================================================
"""

import pytest

from optionforge.research.scenario_analysis import (
    ScenarioAnalysis,
)


def analysis():

    return ScenarioAnalysis(

        scenario_name="Bull Market",

        strategy_return=28.5,

        benchmark_return=20.0,

        win_rate=72.0,

        max_drawdown=9.5,

        sharpe_ratio=1.85,

        passed=True,

    )


# ==========================================================
# Construction
# ==========================================================

def test_create():

    assert isinstance(

        analysis(),

        ScenarioAnalysis,

    )


# ==========================================================
# Values
# ==========================================================

def test_scenario():

    assert analysis().scenario_name == "Bull Market"


def test_strategy_return():

    assert analysis().strategy_return == 28.5


def test_benchmark_return():

    assert analysis().benchmark_return == 20.0


def test_win_rate():

    assert analysis().win_rate == 72.0


def test_drawdown():

    assert analysis().max_drawdown == 9.5


def test_sharpe():

    assert analysis().sharpe_ratio == 1.85


# ==========================================================
# Property
# ==========================================================

def test_excess_return():

    assert analysis().excess_return == 8.5


# ==========================================================
# Validation
# ==========================================================

def test_empty_name():

    with pytest.raises(ValueError):

        ScenarioAnalysis(

            scenario_name="",

            strategy_return=1,

            benchmark_return=1,

            win_rate=50,

            max_drawdown=5,

            sharpe_ratio=1,

            passed=True,

        )


@pytest.mark.parametrize(

    "rate",

    [-1, 101],

)

def test_invalid_win_rate(rate):

    with pytest.raises(ValueError):

        ScenarioAnalysis(

            scenario_name="Bull",

            strategy_return=1,

            benchmark_return=1,

            win_rate=rate,

            max_drawdown=5,

            sharpe_ratio=1,

            passed=True,

        )


def test_negative_drawdown():

    with pytest.raises(ValueError):

        ScenarioAnalysis(

            scenario_name="Bull",

            strategy_return=1,

            benchmark_return=1,

            win_rate=50,

            max_drawdown=-1,

            sharpe_ratio=1,

            passed=True,

        )


# ==========================================================
# Serialization
# ==========================================================

def test_to_dict():

    data = analysis().to_dict()

    assert data["scenario_name"] == "Bull Market"

    assert data["excess_return"] == 8.5


# ==========================================================
# Representation
# ==========================================================

def test_str():

    assert "ScenarioAnalysis" in str(

        analysis(),

    )


def test_repr():

    assert "ScenarioAnalysis" in repr(

        analysis(),

    )