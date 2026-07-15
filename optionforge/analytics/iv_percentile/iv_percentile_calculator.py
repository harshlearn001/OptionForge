"""
============================================================
OptionForge
IV Percentile Calculator
============================================================

Institutional IV Percentile Calculator

============================================================
"""

from __future__ import annotations


class IVPercentileCalculator:
    """
    Calculate IV Percentile.

    Percentage of historical IV values
    below the current IV.
    """

    @staticmethod
    def calculate(
        *,
        current_iv: float,
        historical_iv: list[float],
    ) -> float:

        if not historical_iv:
            return 0.0

        below = sum(iv < current_iv for iv in historical_iv)

        return (below / len(historical_iv)) * 100.0

    def __repr__(self):

        return "IVPercentileCalculator()"

    __str__ = __repr__
