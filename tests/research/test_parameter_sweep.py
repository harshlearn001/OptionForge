"""
============================================================
OptionForge
ParameterSweep Tests
============================================================
"""

import pytest

from optionforge.research.parameter_sweep import (
    ParameterSweep,
)


def sweep():

    return ParameterSweep(

        parameter_name="RSI Length",

        tested_values=15,

        best_value=14,

        best_score=92.5,

        average_score=87.0,

        stability_score=91.0,

        passed=True,

    )


# ==========================================================
# Construction
# ==========================================================

def test_create():

    assert isinstance(

        sweep(),

        ParameterSweep,

    )


# ==========================================================
# Values
# ==========================================================

def test_parameter():

    assert sweep().parameter_name == "RSI Length"


def test_tested_values():

    assert sweep().tested_values == 15


def test_best_value():

    assert sweep().best_value == 14


def test_best_score():

    assert sweep().best_score == 92.5


def test_average_score():

    assert sweep().average_score == 87.0


def test_stability():

    assert sweep().stability_score == 91.0


# ==========================================================
# Property
# ==========================================================

def test_difference():

    assert sweep().score_difference == 5.5


# ==========================================================
# Validation
# ==========================================================

def test_empty_name():

    with pytest.raises(ValueError):

        ParameterSweep(

            parameter_name="",

            tested_values=1,

            best_value=1,

            best_score=1,

            average_score=1,

            stability_score=50,

            passed=True,

        )


def test_invalid_count():

    with pytest.raises(ValueError):

        ParameterSweep(

            parameter_name="RSI",

            tested_values=0,

            best_value=1,

            best_score=1,

            average_score=1,

            stability_score=50,

            passed=True,

        )


@pytest.mark.parametrize(

    "score",

    [

        -1,

        101,

    ],

)

def test_invalid_stability(score):

    with pytest.raises(ValueError):

        ParameterSweep(

            parameter_name="RSI",

            tested_values=10,

            best_value=1,

            best_score=1,

            average_score=1,

            stability_score=score,

            passed=True,

        )


# ==========================================================
# Serialization
# ==========================================================

def test_to_dict():

    data = sweep().to_dict()

    assert data["parameter_name"] == "RSI Length"

    assert data["score_difference"] == 5.5


# ==========================================================
# Representation
# ==========================================================

def test_str():

    assert "ParameterSweep" in str(

        sweep(),

    )


def test_repr():

    assert "ParameterSweep" in repr(

        sweep(),

    )