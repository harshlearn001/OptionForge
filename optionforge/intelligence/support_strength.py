"""
==============================================================
OptionForge
intelligence/support_strength.py
--------------------------------------------------------------
Support Strength Intelligence Engine
==============================================================
"""

from __future__ import annotations

from optionforge.models import SupportStrengthResult


class SupportStrength:
    """
    Calculates Support Strength Score
    """

    @staticmethod
    def calculate(

        support: float,
        support_oi: int,
        max_put_oi: int,
        spot_price: float,

    ) -> SupportStrengthResult:

        # --------------------------------------------------
        # 1. Put OI Strength (0-40)
        # --------------------------------------------------

        oi_ratio = support_oi / max(max_put_oi, 1)

        oi_score = min(oi_ratio * 40, 40)

        # --------------------------------------------------
        # 2. OI Dominance (0-20)
        # --------------------------------------------------

        dominance_score = min(oi_ratio * 20, 20)

        # --------------------------------------------------
        # 3. Distance from Spot (0-20)
        # --------------------------------------------------

        distance = abs(spot_price - support)

        distance_pct = distance / max(spot_price, 1)

        distance_score = max(20 * (1 - distance_pct), 0)

        # --------------------------------------------------
        # 4. Strike Quality (Fixed 20)
        # (Future versions will improve this.)
        # --------------------------------------------------

        strike_score = 20

        # --------------------------------------------------
        # Final Score
        # --------------------------------------------------

        score = (

            oi_score
            + dominance_score
            + distance_score
            + strike_score

        )

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

            f"Support at {support:.0f} "
            f"is classified as {rating}."

        )

        return SupportStrengthResult(

            support=float(support),

            support_oi=int(support_oi),

            score=round(score, 2),

            stars=stars,

            rating=rating,

            interpretation=interpretation,

        )