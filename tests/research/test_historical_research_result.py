"""
==============================================================
Tests for Historical ResearchResult
==============================================================
"""

from datetime import date

from optionforge.research.historical_match import (
    HistoricalMatch,
)

from optionforge.research.historical_research_result import (
    HistoricalResearchResult,
)


def build_match():

    return HistoricalMatch(

        trading_date=date(2025, 6, 10),

        similarity=0.95,

        return_1d=0.5,

        return_5d=2.0,

        return_10d=3.2,

        max_drawdown=-1.0,

        max_runup=4.5,

    )


def build_result():

    return HistoricalResearchResult(

        matches=[

            build_match(),

            build_match(),

            build_match(),

        ],

        win_rate=0.75,

        average_return=2.15,

        median_return=2.0,

        average_drawdown=-0.82,

        average_runup=4.10,

        expected_value=2.15,

    )


def test_match_count():

    assert build_result().match_count == 3


def test_confidence():

    assert build_result().confidence == 0.03


def test_summary():

    assert isinstance(
        build_result().summary(),
        dict,
    )


def test_dict():

    assert isinstance(
        build_result().to_dict(),
        dict,
    )


def test_repr():

    assert (
        "ResearchResult"
        in repr(build_result())
    )


def test_average_return():

    assert build_result().average_return == 2.15


def test_expected_value():

    assert build_result().expected_value == 2.15


def test_win_rate():

    assert build_result().win_rate == 0.75


def test_matches():

    assert len(
        build_result().matches
    ) == 3