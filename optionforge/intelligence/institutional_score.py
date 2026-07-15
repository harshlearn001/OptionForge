"""
==============================================================
OptionForge
Institutional Score
--------------------------------------------------------------

Computes a normalized institutional score from the
individual analytics engines.

Output Range
------------
-1.0 .............................. +1.0

==============================================================
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class InstitutionalScore:
    """
    Weighted institutional score calculator.
    """

    summary: float
    change: float
    buildup: float
    wall: float
    concentration: float
    shift: float
    trend: float

    # ==========================================================
    # Weights
    # ==========================================================

    SUMMARY_WEIGHT = 0.05

    CHANGE_WEIGHT = 0.10

    BUILDUP_WEIGHT = 0.20

    WALL_WEIGHT = 0.20

    CONCENTRATION_WEIGHT = 0.15

    SHIFT_WEIGHT = 0.15

    TREND_WEIGHT = 0.15

    # ==========================================================
    # Score
    # ==========================================================

    def calculate(self) -> float:
        """
        Return normalized institutional score.
        """

        score = (

            self.summary * self.SUMMARY_WEIGHT +

            self.change * self.CHANGE_WEIGHT +

            self.buildup * self.BUILDUP_WEIGHT +

            self.wall * self.WALL_WEIGHT +

            self.concentration * self.CONCENTRATION_WEIGHT +

            self.shift * self.SHIFT_WEIGHT +

            self.trend * self.TREND_WEIGHT

        )

        score = max(-1.0, min(1.0, score))

        return round(score, 4)

    # ==========================================================
    # Representation
    # ==========================================================

    def __float__(self) -> float:

        return self.calculate()

    def __repr__(self) -> str:

        return (
            "InstitutionalScore("
            f"{self.calculate():.4f})"
        )