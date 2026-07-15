"""
============================================================
OptionForge
IV Rank Calculator
============================================================

Institutional IV Rank Calculator

============================================================
"""

from __future__ import annotations


class IVRankCalculator:
    """
    Calculate IV Rank.

    Formula
    -------
    (Current IV - Lowest IV)
    ------------------------
    (Highest IV - Lowest IV)
    """

    @staticmethod
    def calculate(
        *,
        current_iv: float,
        lowest_iv: float,
        highest_iv: float,
    ) -> float:

        if highest_iv <= lowest_iv:
            return 0.0

        return ((current_iv - lowest_iv) / (highest_iv - lowest_iv)) * 100.0

    def __repr__(self):

        return "IVRankCalculator()"

    __str__ = __repr__
