"""
==============================================================
OptionForge
Similarity Engine
==============================================================

Ranks historical observations by similarity to the
current ResearchQuery.

Author
------
OptionForge Engineering Team
==============================================================
"""

from __future__ import annotations

from typing import Iterable

from optionforge.research.historical_match import HistoricalMatch


class SimilarityEngine:
    """
    Ranks historical matches.
    """

    def __init__(
        self,
        matches: Iterable[HistoricalMatch],
    ) -> None:

        self._matches = list(matches)

    def rank(self) -> list[HistoricalMatch]:
        """
        Return matches sorted by similarity.
        """

        return sorted(
            self._matches,
            key=lambda x: x.similarity,
            reverse=True,
        )

    def best_match(self) -> HistoricalMatch | None:
        """
        Highest similarity match.
        """

        ranked = self.rank()

        if not ranked:
            return None

        return ranked[0]

    def top(
        self,
        n: int = 10,
    ) -> list[HistoricalMatch]:
        """
        Return top-N matches.
        """

        return self.rank()[:n]

    def __len__(self) -> int:

        return len(self._matches)

    def __repr__(self) -> str:

        return (
            f"SimilarityEngine("
            f"matches={len(self)})"
        )