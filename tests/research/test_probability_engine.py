"""
==============================================================
Tests for ProbabilityEngine
==============================================================
"""

from datetime import date

from optionforge.research.historical_match import (
    HistoricalMatch,
)

from optionforge.research.probability_engine import (
    ProbabilityEngine,
)


def build_engine():

    matches = [

        HistoricalMatch(
            trading_date=date(2024, 1, 10),
            similarity=0.90,
            return_1d=0.5,
            return_5d=2.0,
            return_10d=3.0,
            max_drawdown=-1.0,
            max_runup=4.0,
        ),

        HistoricalMatch(
            trading_date=date(2024, 2, 10),
            similarity=0.88,
            return_1d=-0.2,
            return_5d=-1.0,
            return_10d=-0.5,
            max_drawdown=-2.0,
            max_runup=1.5,
        ),

        HistoricalMatch(
            trading_date=date(2024, 3, 10),
            similarity=0.95,
            return_1d=0.8,
            return_5d=3.0,
            return_10d=5.0,
            max_drawdown=-0.5,
            max_runup=6.0,
        ),

    ]

    return ProbabilityEngine(matches)


def test_count():

    assert build_engine().count() == 3


def test_win_rate():

    assert build_engine().win_rate() == 2 / 3


def test_average_return():

    assert build_engine().average_return() == (2.0 - 1.0 + 3.0) / 3


def test_median_return():

    assert build_engine().median_return() == 2.0


def test_average_drawdown():

    assert build_engine().average_drawdown() == (-1.0 - 2.0 - 0.5) / 3


def test_average_runup():

    assert build_engine().average_runup() == (4.0 + 1.5 + 6.0) / 3


def test_expected_value():

    assert (
        build_engine().expected_value()
        ==
        build_engine().average_return()
    )


def test_summary():

    assert isinstance(
        build_engine().summary(),
        dict,
    )


def test_repr():

    assert (
        "ProbabilityEngine"
        in repr(build_engine())
    )


def test_empty():

    engine = ProbabilityEngine([])

    assert engine.count() == 0

    assert engine.win_rate() == 0.0

    assert engine.average_return() == 0.0