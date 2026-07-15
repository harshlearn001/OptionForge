"""
============================================================
OptionForge
Volatility Surface Calculator
============================================================

Institutional Volatility Surface Calculator

============================================================
"""

from __future__ import annotations


class VolatilitySurfaceCalculator:
    """
    Build a volatility surface from
    strike, expiry and IV values.
    """

    @staticmethod
    def calculate(
        *,
        strikes: list[float],
        expiries: list[int],
        ivs: list[float],
    ) -> list[tuple[int, float, float]]:

        if not (len(strikes) == len(expiries) == len(ivs)):
            raise ValueError("Input lists must have the same length.")

        if not strikes:
            return []

        surface = list(
            zip(
                expiries,
                strikes,
                ivs,
            )
        )

        surface.sort(
            key=lambda row: (
                row[0],
                row[1],
            )
        )

        return surface

    def __repr__(self):

        return "VolatilitySurfaceCalculator()"

    __str__ = __repr__
