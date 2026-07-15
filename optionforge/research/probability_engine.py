"""
==============================================================
OptionForge
Probability Engine
==============================================================

Computes historical probabilities from similar
market observations.

Author
------
OptionForge Engineering Team
==============================================================
"""

from __future__ import annotations

from statistics import mean
from statistics import median

from optionforge.research.historical_match import (
    HistoricalMatch,
)


class ProbabilityEngine:
    """
    Historical probability calculator.
    """

    def __init__(
        self,
        matches: list[HistoricalMatch],
    ) -> None:

        self._matches = matches

    def count(self) -> int:

        return len(self._matches)

    def win_rate(self) -> float:

        if not self._matches:
            return 0.0

        wins = sum(
            m.return_5d > 0
            for m in self._matches
        )

        return wins / len(self._matches)

    def average_return(self) -> float:

        if not self._matches:
            return 0.0

        return mean(
            m.return_5d
            for m in self._matches
        )

    def median_return(self) -> float:

        if not self._matches:
            return 0.0

        return median(
            m.return_5d
            for m in self._matches
        )

    def average_drawdown(self) -> float:

        if not self._matches:
            return 0.0

        return mean(
            m.max_drawdown
            for m in self._matches
        )

    def average_runup(self) -> float:

        if not self._matches:
            return 0.0

        return mean(
            m.max_runup
            for m in self._matches
        )

    def expected_value(self) -> float:
        """
        Historical expected return.
        """

        return self.average_return()

    def summary(self) -> dict:

        return {

            "count": self.count(),

            "win_rate": self.win_rate(),

            "average_return": self.average_return(),

            "median_return": self.median_return(),

            "average_drawdown": self.average_drawdown(),

            "average_runup": self.average_runup(),

            "expected_value": self.expected_value(),

        }

    def __repr__(self) -> str:

        return (
            f"ProbabilityEngine("
            f"matches={self.count()})"
        )