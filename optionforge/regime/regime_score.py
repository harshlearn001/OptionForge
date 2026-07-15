"""
==============================================================
OptionForge
Market Regime Score
==============================================================

Computes confidence for the classified market regime.

Author
------
OptionForge Engineering Team
==============================================================
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class RegimeScore:
    """
    Computes normalized regime confidence.
    """

    institutional: float

    trend: float

    dealer: float

    volatility: float

    # ==========================================================
    # Weights
    # ==========================================================

    INSTITUTIONAL_WEIGHT = 0.35

    TREND_WEIGHT = 0.30

    DEALER_WEIGHT = 0.20

    VOLATILITY_WEIGHT = 0.15

    # ==========================================================
    # Calculate
    # ==========================================================

    def calculate(self) -> float:
        """
        Returns normalized confidence.

        Output:
            0.0 ... 1.0
        """

        score = (

            self.institutional * self.INSTITUTIONAL_WEIGHT +

            self.trend * self.TREND_WEIGHT +

            self.dealer * self.DEALER_WEIGHT +

            self.volatility * self.VOLATILITY_WEIGHT

        )

        score = max(0.0, min(1.0, score))

        return round(score, 4)

    def __float__(self):

        return self.calculate()

    def __repr__(self):

        return (
            "RegimeScore("
            f"{self.calculate():.4f})"
        )