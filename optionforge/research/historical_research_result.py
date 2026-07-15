"""
==============================================================
OptionForge
Historical Research Result
==============================================================

Author      : OptionForge Engineering Team

Purpose
-------
Immutable result produced by the Historical
Research Engine.

Represents statistical evidence gathered from
similar historical market observations.

This is NOT the final ResearchResult.

ResearchResult represents the complete institutional
research decision and should consume this object.

==============================================================
"""

from __future__ import annotations

from dataclasses import asdict
from dataclasses import dataclass

from optionforge.research.historical_match import (
    HistoricalMatch,
)


@dataclass(
    frozen=True,
    slots=True,
)
class HistoricalResearchResult:
    """
    Statistical result produced from
    historical similarity analysis.
    """

    matches: list[HistoricalMatch]

    win_rate: float

    average_return: float

    median_return: float

    average_drawdown: float

    average_runup: float

    expected_value: float

    @property
    def match_count(self) -> int:
        """
        Number of historical matches.
        """
        return len(self.matches)

    @property
    def confidence(self) -> float:
        """
        Simple confidence estimate based
        on sample size.

        Can later be replaced by a more
        sophisticated statistical model.
        """

        if self.match_count >= 100:
            return 1.0

        return round(self.match_count / 100.0, 2)

    def summary(self) -> dict:

        return {

            "match_count": self.match_count,

            "win_rate": self.win_rate,

            "average_return": self.average_return,

            "median_return": self.median_return,

            "average_drawdown": self.average_drawdown,

            "average_runup": self.average_runup,

            "expected_value": self.expected_value,

            "confidence": self.confidence,

        }

    def to_dict(self) -> dict:

        d = asdict(self)

        d["match_count"] = self.match_count

        d["confidence"] = self.confidence

        return d

    def __repr__(self) -> str:

        return (

            "HistoricalResearchResult("

            f"matches={self.match_count}, "

            f"win_rate={self.win_rate:.2f}, "

            f"expected_value={self.expected_value:.2f})"

        )