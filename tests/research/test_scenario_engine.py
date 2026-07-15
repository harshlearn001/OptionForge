"""
============================================================
OptionForge
ScenarioEngine Tests
============================================================
"""

from optionforge.research.scenario_analysis import (
    ScenarioAnalysis,
)
from optionforge.research.scenario_engine import (
    ScenarioEngine,
)


def engine():

    return ScenarioEngine()


# ==========================================================
# Construction
# ==========================================================


def test_create():

    assert isinstance(
        engine(),
        ScenarioEngine,
    )


# ==========================================================
# Return Type
# ==========================================================


def test_result_type():

    result = engine().run(
        scenario_name="Bull Market",
        strategy_return=24.5,
        benchmark_return=16.2,
        win_rate=72.0,
        max_drawdown=8.4,
        sharpe_ratio=1.75,
    )

    assert isinstance(
        result,
        ScenarioAnalysis,
    )


# ==========================================================
# Pass
# ==========================================================


def test_pass():

    result = engine().run(
        "Bull Market",
        24.5,
        16.2,
        72.0,
        8.4,
        1.75,
    )

    assert result.passed


# ==========================================================
# Fail
# ==========================================================


def test_fail():

    result = engine().run(
        "Bear Market",
        -10.0,
        2.0,
        35.0,
        18.0,
        -0.5,
    )

    assert not result.passed


# ==========================================================
# Excess Return
# ==========================================================


def test_excess_return():

    result = engine().run(
        "Bull Market",
        24.5,
        16.2,
        72.0,
        8.4,
        1.75,
    )

    assert result.excess_return == 8.3


# ==========================================================
# Stored Values
# ==========================================================


def test_scenario_name():

    result = engine().run(
        "Bull Market",
        24.5,
        16.2,
        72.0,
        8.4,
        1.75,
    )

    assert result.scenario_name == "Bull Market"


def test_strategy_return():

    result = engine().run(
        "Bull Market",
        24.5,
        16.2,
        72.0,
        8.4,
        1.75,
    )

    assert result.strategy_return == 24.5


def test_benchmark_return():

    result = engine().run(
        "Bull Market",
        24.5,
        16.2,
        72.0,
        8.4,
        1.75,
    )

    assert result.benchmark_return == 16.2


def test_win_rate():

    result = engine().run(
        "Bull Market",
        24.5,
        16.2,
        72.0,
        8.4,
        1.75,
    )

    assert result.win_rate == 72.0


def test_drawdown():

    result = engine().run(
        "Bull Market",
        24.5,
        16.2,
        72.0,
        8.4,
        1.75,
    )

    assert result.max_drawdown == 8.4


def test_sharpe():

    result = engine().run(
        "Bull Market",
        24.5,
        16.2,
        72.0,
        8.4,
        1.75,
    )

    assert result.sharpe_ratio == 1.75


# ==========================================================
# Representation
# ==========================================================


def test_repr():

    assert "ScenarioEngine" in repr(
        engine(),
    )


def test_str():

    assert "ScenarioEngine" in str(
        engine(),
    )
