"""
==============================================================
OptionForge
Research Filter
==============================================================

Determines whether a historical observation satisfies
a ResearchQuery.

Author
------
OptionForge Engineering Team
==============================================================
"""

from __future__ import annotations

from optionforge.research.research_query import ResearchQuery


class ResearchFilter:
    """
    Filters historical observations.
    """

    @staticmethod
    def matches(
        query: ResearchQuery,
        candidate: ResearchQuery,
    ) -> bool:
        """
        Returns True if candidate satisfies the query.
        """

        if query.symbol != candidate.symbol:
            return False

        if query.regime != candidate.regime:
            return False

        if (
            query.institutional_state
            != candidate.institutional_state
        ):
            return False

        if query.dealer_state != candidate.dealer_state:
            return False

        return True

    def __repr__(self) -> str:

        return "ResearchFilter()"