"""
============================================================
OptionForge
BenchmarkEngine Tests
============================================================
"""

from optionforge.research.benchmark_engine import (
    BenchmarkEngine,
)
from optionforge.research.benchmark_comparison import (
    BenchmarkComparison,
)


def engine():

    return BenchmarkEngine()


# ==========================================================
# Construction
# ==========================================================


def test_create():

    assert isinstance(
        engine(),
        BenchmarkEngine,
    )


# ==========================================================
# Return Type
# ==========================================================


def test_result_type():

    result = engine().run(
        strategy_return=18.5,
        benchmark_name="NIFTY 50",
        benchmark_return=12.2,
    )

    assert isinstance(
        result,
        BenchmarkComparison,
    )


# ==========================================================
# Pass / Fail
# ==========================================================


def test_pass():

    result = engine().run(
        18.5,
        "NIFTY 50",
        12.2,
    )

    assert result.passed

    assert result.outperformed


def test_fail():

    result = engine().run(
        5.0,
        "NIFTY 50",
        12.2,
    )

    assert not result.passed

    assert not result.outperformed


# ==========================================================
# Calculated Values
# ==========================================================


def test_alpha():

    result = engine().run(
        18.5,
        "NIFTY 50",
        12.2,
    )

    assert result.alpha == 6.3


def test_excess_return():

    result = engine().run(
        18.5,
        "NIFTY 50",
        12.2,
    )

    assert result.excess_return == 6.3


def test_tracking_error():

    result = engine().run(
        18.5,
        "NIFTY 50",
        12.2,
    )

    assert result.tracking_error == 0.0


def test_information_ratio():

    result = engine().run(
        18.5,
        "NIFTY 50",
        12.2,
    )

    assert result.information_ratio == 0.0


# ==========================================================
# Stored Values
# ==========================================================


def test_benchmark_name():

    result = engine().run(
        18.5,
        "NIFTY 50",
        12.2,
    )

    assert result.benchmark_name == "NIFTY 50"


def test_strategy_return():

    result = engine().run(
        18.5,
        "NIFTY 50",
        12.2,
    )

    assert result.strategy_return == 18.5


def test_benchmark_return():

    result = engine().run(
        18.5,
        "NIFTY 50",
        12.2,
    )

    assert result.benchmark_return == 12.2


# ==========================================================
# Representation
# ==========================================================


def test_repr():

    assert "BenchmarkEngine" in repr(
        engine(),
    )


def test_str():

    assert "BenchmarkEngine" in str(
        engine(),
    )
