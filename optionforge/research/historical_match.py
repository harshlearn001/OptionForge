"""
==============================================================
OptionForge
Historical Match
==============================================================

Represents one historical market observation that
matches a research query.

Author
------
OptionForge Engineering Team
==============================================================
"""

from __future__ import annotations

from dataclasses import asdict
from dataclasses import dataclass
from datetime import date


@dataclass(slots=True, frozen=True)
class HistoricalMatch:
    """
    One historical research match.
    """

    trading_date: date

    similarity: float

    return_1d: float

    return_5d: float

    return_10d: float

    max_drawdown: float

    max_runup: float

    def summary(self) -> dict:
        """
        Lightweight summary.
        """

        return {

            "date": self.trading_date.isoformat(),

            "similarity": self.similarity,

            "return_5d": self.return_5d,

        }

    def to_dict(self) -> dict:
        """
        Dictionary representation.
        """

        d = asdict(self)

        d["trading_date"] = self.trading_date.isoformat()

        return d

    def __repr__(self) -> str:

        return (

            "HistoricalMatch("

            f"{self.trading_date.isoformat()}, "

            f"similarity={self.similarity:.2f})"

        )