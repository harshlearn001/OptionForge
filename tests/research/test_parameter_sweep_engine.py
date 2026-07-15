"""
============================================================
OptionForge
ParameterSweepEngine Tests
============================================================
"""

import pytest

from optionforge.research.parameter_sweep import (
    ParameterSweep,
)
from optionforge.research.parameter_sweep_engine import (
    ParameterSweepEngine,
)


def engine():

    return ParameterSweepEngine()


# ==========================================================
# Construction
# ==========================================================


def test_create():

    assert isinstance(
        engine(),
        ParameterSweepEngine,
    )


# ==========================================================
# Empty
# ==========================================================


def test_empty():

    with pytest.raises(ValueError):

        engine().run(
            "RSI",
            [],
        )


# ==========================================================
# Return Type
# ==========================================================


def test_result():

    result = engine().run(
        "RSI Length",
        [
            84.2,
            86.5,
            91.3,
            88.7,
            85.9,
        ],
    )

    assert isinstance(
        result,
        ParameterSweep,
    )


# ==========================================================
# Values
# ==========================================================


def test_tested():

    result = engine().run(
        "RSI Length",
        [
            84.2,
            86.5,
            91.3,
            88.7,
            85.9,
        ],
    )

    assert result.tested_values == 5


def test_best():

    result = engine().run(
        "RSI Length",
        [
            84.2,
            86.5,
            91.3,
            88.7,
            85.9,
        ],
    )

    assert result.best_score == 91.3


def test_best_value():

    result = engine().run(
        "RSI Length",
        [
            84.2,
            86.5,
            91.3,
            88.7,
            85.9,
        ],
    )

    assert result.best_value == 3


def test_average():

    result = engine().run(
        "RSI Length",
        [
            84.2,
            86.5,
            91.3,
            88.7,
            85.9,
        ],
    )

    assert result.average_score == 87.32


def test_pass():

    result = engine().run(
        "RSI Length",
        [
            84.2,
            86.5,
            91.3,
            88.7,
            85.9,
        ],
    )

    assert result.passed


# ==========================================================
# Representation
# ==========================================================


def test_repr():

    assert "ParameterSweepEngine" in repr(
        engine(),
    )


def test_str():

    assert "ParameterSweepEngine" in str(
        engine(),
    )
