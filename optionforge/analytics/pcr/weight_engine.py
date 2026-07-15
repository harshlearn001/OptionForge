"""
============================================================
OptionForge
Weight Engine
============================================================

Provides strike weights for institutional analytics.

============================================================
"""

from __future__ import annotations


class WeightEngine:

    def __init__(
        self,
        strike_interval: int = 50,
    ) -> None:

        self.strike_interval = strike_interval

    # -----------------------------------------------------

    def distance(
        self,
        strike: int,
        atm: int,
    ) -> int:

        return abs(strike - atm)

    # -----------------------------------------------------

    def levels_from_atm(
        self,
        strike: int,
        atm: int,
    ) -> int:

        return int(
            self.distance(
                strike,
                atm,
            )
            / self.strike_interval
        )

    # -----------------------------------------------------

    def weight(
        self,
        strike: int,
        atm: int,
    ) -> float:

        level = self.levels_from_atm(
            strike,
            atm,
        )

        table = {
            0: 1.00,
            1: 0.95,
            2: 0.90,
            3: 0.85,
            4: 0.80,
            5: 0.75,
        }

        return table.get(
            level,
            0.50,
        )

    # -----------------------------------------------------

    def __repr__(self):

        return f"WeightEngine(" f"interval={self.strike_interval})"

    __str__ = __repr__
