"""
============================================================
OptionForge
MonteCarloEngine Tests
============================================================
"""

import pytest

from optionforge.research.monte_carlo import (
    MonteCarloSimulation,
)
from optionforge.research.monte_carlo_engine import (
    MonteCarloEngine,
)


def engine():
    return MonteCarloEngine()


def test_create():
    assert isinstance(
        engine(),
        MonteCarloEngine,
    )


def test_empty():

    with pytest.raises(ValueError):
        engine().run([])


def test_result_type():

    result = engine().run([100, -50, 80])

    assert isinstance(
        result,
        MonteCarloSimulation,
    )


def test_simulations():

    result = engine().run([100, -50, 80])

    assert result.simulations == 3


def test_best():

    result = engine().run([100, -50, 80])

    assert result.best_return == 100


def test_worst():

    result = engine().run([100, -50, 80])

    assert result.worst_return == -50


def test_average():

    result = engine().run([100, -50, 80])

    assert result.average_return == 43.3333333333


def test_profit_probability():

    result = engine().run([100, -50, 80])

    assert result.probability_of_profit == 66.6666666667


def test_loss_probability():

    result = engine().run([100, -50, 80])

    assert result.probability_of_loss == 33.3333333333


def test_repr():

    assert "MonteCarloEngine" in repr(
        engine(),
    )


def test_str():

    assert "MonteCarloEngine" in str(
        engine(),
    )
