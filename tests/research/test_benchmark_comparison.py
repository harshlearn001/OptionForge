"""
============================================================
OptionForge
BenchmarkComparison Tests
============================================================
"""

import pytest

from optionforge.research.benchmark_comparison import (
    BenchmarkComparison,
)


def comparison():

    return BenchmarkComparison(
        benchmark_name="NIFTY 50",
        strategy_return=24.5,
        benchmark_return=18.2,
        alpha=6.3,
        tracking_error=4.5,
        information_ratio=1.40,
        outperformed=True,
        passed=True,
    )


# ==========================================================
# Construction
# ==========================================================


def test_create():

    assert isinstance(
        comparison(),
        BenchmarkComparison,
    )


# ==========================================================
# Values
# ==========================================================


def test_benchmark():

    assert comparison().benchmark_name == "NIFTY 50"


def test_strategy_return():

    assert comparison().strategy_return == 24.5


def test_benchmark_return():

    assert comparison().benchmark_return == 18.2


def test_alpha():

    assert comparison().alpha == 6.3


# ==========================================================
# Property
# ==========================================================


def test_excess_return():

    assert comparison().excess_return == 6.3


# ==========================================================
# Validation
# ==========================================================


def test_empty_name():

    with pytest.raises(ValueError):

        BenchmarkComparison(
            benchmark_name="",
            strategy_return=1,
            benchmark_return=1,
            alpha=0,
            tracking_error=1,
            information_ratio=0,
            outperformed=False,
            passed=False,
        )


def test_tracking_error():

    with pytest.raises(ValueError):

        BenchmarkComparison(
            benchmark_name="NIFTY",
            strategy_return=1,
            benchmark_return=1,
            alpha=0,
            tracking_error=-1,
            information_ratio=0,
            outperformed=False,
            passed=False,
        )


# ==========================================================
# Serialization
# ==========================================================


def test_to_dict():

    data = comparison().to_dict()

    assert data["benchmark_name"] == "NIFTY 50"

    assert data["alpha"] == 6.3

    assert data["excess_return"] == 6.3


# ==========================================================
# Representation
# ==========================================================


def test_str():

    assert "BenchmarkComparison" in str(
        comparison(),
    )


def test_repr():

    assert "BenchmarkComparison" in repr(
        comparison(),
    )
