"""
==============================================================
OptionForge
intelligence/resistance_strength.py
--------------------------------------------------------------
Resistance Strength Intelligence Engine
==============================================================
"""

from __future__ import annotations

from optionforge.models import ResistanceStrengthResult


class ResistanceStrength:
    """
    Calculates Resistance Strength Score
    """

    @staticmethod
    def calculate(
        resistance: float,
        resistance_oi: int,
        max_call_oi: int,
        spot_price: float,
    ) -> ResistanceStrengthResult:

        # --------------------------------------------------
        # 1. Call OI Strength (0-40)
        # --------------------------------------------------

        oi_ratio = resistance_oi / max(max_call_oi, 1)

        oi_score = min(oi_ratio * 40, 40)

        # --------------------------------------------------
        # 2. OI Dominance (0-20)
        # --------------------------------------------------

        dominance_score = min(oi_ratio * 20, 20)

        # --------------------------------------------------
        # 3. Distance from Spot (0-20)
        # --------------------------------------------------

        distance = abs(resistance - spot_price)

        distance_pct = distance / max(spot_price, 1)

        distance_score = max(20 * (1 - distance_pct), 0)

        # --------------------------------------------------
        # 4. Strike Quality (0-20)
        # --------------------------------------------------

        strike_score = 20

        # --------------------------------------------------
        # Final Score
        # --------------------------------------------------

        score = oi_score + dominance_score + distance_score + strike_score

        score = min(score, 100)

        # --------------------------------------------------
        # Rating
        # --------------------------------------------------

        if score >= 90:

            rating = "VERY STRONG"
            stars = 5

        elif score >= 75:

            rating = "STRONG"
            stars = 4

        elif score >= 60:

            rating = "MODERATE"
            stars = 3

        elif score >= 40:

            rating = "WEAK"
            stars = 2

        else:

            rating = "VERY WEAK"
            stars = 1

        interpretation = (
            f"Resistance at {resistance:.0f} " f"is classified as {rating}."
        )

        return ResistanceStrengthResult(
            resistance=float(resistance),
            resistance_oi=int(resistance_oi),
            score=round(score, 2),
            stars=stars,
            rating=rating,
            interpretation=interpretation,
        )
