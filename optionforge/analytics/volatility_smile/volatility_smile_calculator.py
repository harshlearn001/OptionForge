"""
============================================================
OptionForge
Volatility Smile Calculator
============================================================

Institutional Volatility Smile Calculator

============================================================
"""

from __future__ import annotations


class VolatilitySmileCalculator:
    """
    Prepare strike-IV pairs for smile analysis.
    """

    @staticmethod
    def calculate(
        *,
        strikes: list[float],
        ivs: list[float],
    ) -> list[tuple[float, float]]:

        if len(strikes) != len(ivs):
            raise ValueError(
                "strikes and ivs must have the same length."
            )

        if not strikes:
            return []

        return sorted(

            zip(strikes, ivs),

            key=lambda x: x[0],

        )

    def __repr__(self):

        return "VolatilitySmileCalculator()"

    __str__ = __repr__