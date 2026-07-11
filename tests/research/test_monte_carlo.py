"""
============================================================
OptionForge
MonteCarloSimulation Tests
============================================================
"""

import pytest

from optionforge.research.monte_carlo import (
    MonteCarloSimulation,
)


def simulation():

    return MonteCarloSimulation(

        simulations=10000,

        average_return=18.5,

        best_return=52.3,

        worst_return=-21.7,

        probability_of_profit=78.5,

        probability_of_loss=21.5,

        probability_of_ruin=1.2,

        max_drawdown=18.6,

        passed=True,

    )


# ==========================================================
# Construction
# ==========================================================

def test_create():

    assert isinstance(

        simulation(),

        MonteCarloSimulation,

    )


# ==========================================================
# Values
# ==========================================================

def test_simulations():

    assert simulation().simulations == 10000


def test_average_return():

    assert simulation().average_return == 18.5


def test_best_return():

    assert simulation().best_return == 52.3


def test_worst_return():

    assert simulation().worst_return == -21.7


# ==========================================================
# Probabilities
# ==========================================================

def test_profit_probability():

    assert simulation().probability_of_profit == 78.5


def test_loss_probability():

    assert simulation().probability_of_loss == 21.5


def test_ruin_probability():

    assert simulation().probability_of_ruin == 1.2


def test_survival_rate():

    assert simulation().expected_survival_rate == 98.8


# ==========================================================
# Validation
# ==========================================================

@pytest.mark.parametrize(

    "field,value",

    [

        ("simulations", 0),

        ("probability_of_profit", -1),

        ("probability_of_profit", 101),

        ("probability_of_loss", -1),

        ("probability_of_loss", 101),

        ("probability_of_ruin", -1),

        ("probability_of_ruin", 101),

        ("max_drawdown", -1),

        ("max_drawdown", 101),

    ],

)

def test_validation(

    field,

    value,

):

    kwargs = dict(

        simulations=10000,

        average_return=18.5,

        best_return=52.3,

        worst_return=-21.7,

        probability_of_profit=78.5,

        probability_of_loss=21.5,

        probability_of_ruin=1.2,

        max_drawdown=18.6,

        passed=True,

    )

    kwargs[field] = value

    with pytest.raises(ValueError):

        MonteCarloSimulation(

            **kwargs,

        )


# ==========================================================
# Serialization
# ==========================================================

def test_to_dict():

    data = simulation().to_dict()

    assert data["simulations"] == 10000

    assert data["expected_survival_rate"] == 98.8

    assert data["probability_of_ruin"] == 1.2


# ==========================================================
# Representation
# ==========================================================

def test_str():

    assert "MonteCarloSimulation" in str(

        simulation(),

    )


def test_repr():

    assert "MonteCarloSimulation" in repr(

        simulation(),

    )