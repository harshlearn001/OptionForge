"""
==============================================================
Tests for SimilarityEngine
==============================================================
"""

from datetime import date

from optionforge.research.historical_match import (
    HistoricalMatch,
)

from optionforge.research.similarity_engine import (
    SimilarityEngine,
)


def build_matches():

    return [

        HistoricalMatch(
            trading_date=date(2024, 1, 10),
            similarity=0.62,
            return_1d=0.2,
            return_5d=1.1,
            return_10d=1.8,
            max_drawdown=-0.4,
            max_runup=2.1,
        ),

        HistoricalMatch(
            trading_date=date(2024, 2, 12),
            similarity=0.95,
            return_1d=0.8,
            return_5d=2.4,
            return_10d=3.8,
            max_drawdown=-0.5,
            max_runup=4.0,
        ),

        HistoricalMatch(
            trading_date=date(2024, 3, 14),
            similarity=0.81,
            return_1d=0.5,
            return_5d=1.8,
            return_10d=2.7,
            max_drawdown=-0.6,
            max_runup=3.3,
        ),

    ]


def build_engine():

    return SimilarityEngine(
        build_matches(),
    )


def test_length():

    assert len(build_engine()) == 3


def test_rank():

    ranked = build_engine().rank()

    assert ranked[0].similarity == 0.95

    assert ranked[-1].similarity == 0.62


def test_best_match():

    assert (
        build_engine()
        .best_match()
        .similarity
        == 0.95
    )


def test_top():

    assert len(
        build_engine().top(2)
    ) == 2


def test_top_default():

    assert len(
        build_engine().top()
    ) == 3


def test_empty():

    engine = SimilarityEngine([])

    assert engine.best_match() is None


def test_repr():

    assert (
        "SimilarityEngine"
        in repr(build_engine())
    )