"""
==============================================================
Tests for HistoricalMatch
==============================================================
"""

from datetime import date

from optionforge.research.historical_match import (
    HistoricalMatch,
)


def build_match():

    return HistoricalMatch(

        trading_date=date(2025, 6, 12),

        similarity=0.93,

        return_1d=0.45,

        return_5d=2.18,

        return_10d=3.84,

        max_drawdown=-0.72,

        max_runup=4.25,

    )


def test_date():

    assert build_match().trading_date.year == 2025


def test_similarity():

    assert build_match().similarity == 0.93


def test_return_5d():

    assert build_match().return_5d == 2.18


def test_summary():

    assert isinstance(

        build_match().summary(),

        dict,

    )


def test_to_dict():

    d = build_match().to_dict()

    assert d["trading_date"] == "2025-06-12"


def test_repr():

    assert "HistoricalMatch" in repr(build_match())


def test_drawdown():

    assert build_match().max_drawdown == -0.72


def test_runup():

    assert build_match().max_runup == 4.25