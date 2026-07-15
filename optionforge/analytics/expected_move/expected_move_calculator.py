"""
============================================================
OptionForge
Expected Move Calculator
============================================================

Institutional Expected Move Calculator

============================================================
"""

from __future__ import annotations

import math


class ExpectedMoveCalculator:
    """
    Calculate expected move from spot, IV and time.
    """

    @staticmethod
    def calculate(
        *,
        spot: float,
        volatility: float,
        time: float,
    ) -> float:

        if spot <= 0:
            raise ValueError("spot must be positive.")

        if volatility < 0:
            raise ValueError("volatility cannot be negative.")

        if time < 0:
            raise ValueError("time cannot be negative.")

        return spot * volatility * math.sqrt(time)

    def __repr__(self):

        return "ExpectedMoveCalculator()"

    __str__ = __repr__
