"""
==============================================================
OptionForge
intelligence/market_structure.py
--------------------------------------------------------------
Market Structure Intelligence Engine
==============================================================
"""

from __future__ import annotations

from optionforge.models import MarketStructureResult


class MarketStructure:
    """
    Professional Market Structure Intelligence Engine
    """

    @staticmethod
    def calculate(

        support_strength: float,
        resistance_strength: float,

        expected_move: float,

        iv_rank: float,
        iv_percentile: float,

        max_pain: float,

        oi_wall_score: float,
        oi_shift_score: float,
        oi_change_score: float,

    ) -> MarketStructureResult:

        # ======================================================
        # Weighted Score
        # ======================================================

        score = (

            support_strength * 0.15 +

            resistance_strength * 0.15 +

            expected_move * 0.10 +

            iv_rank * 0.10 +

            iv_percentile * 0.10 +

            max_pain * 0.15 +

            oi_wall_score * 0.10 +

            oi_shift_score * 0.10 +

            oi_change_score * 0.05

        )

        score = max(0.0, min(score, 100.0))

        # ======================================================
        # Bias
        # ======================================================

        if score >= 95:

            bias = "EXTREMELY BULLISH"

        elif score >= 85:

            bias = "STRONGLY BULLISH"

        elif score >= 70:

            bias = "BULLISH"

        elif score >= 55:

            bias = "NEUTRAL"

        elif score >= 40:

            bias = "BEARISH"

        elif score >= 20:

            bias = "STRONGLY BEARISH"

        else:

            bias = "EXTREMELY BEARISH"

        # ======================================================
        # Confidence
        # ======================================================

        if score >= 95:

            confidence = "VERY HIGH"
            stars = 5

        elif score >= 80:

            confidence = "HIGH"
            stars = 4

        elif score >= 60:

            confidence = "MEDIUM"
            stars = 3

        elif score >= 40:

            confidence = "LOW"
            stars = 2

        else:

            confidence = "VERY LOW"
            stars = 1

        # ======================================================
        # Recommendation
        # ======================================================

        if score >= 85:

            recommendation = (
                "High probability bullish market structure. "
                "Buying dips is preferred."
            )

        elif score >= 70:

            recommendation = (
                "Bullish market structure. "
                "Look for trend continuation."
            )

        elif score >= 55:

            recommendation = (
                "Neutral market. "
                "Wait for confirmation."
            )

        elif score >= 40:

            recommendation = (
                "Bearish market structure. "
                "Avoid aggressive longs."
            )

        else:

            recommendation = (
                "High probability bearish market. "
                "Selling rallies is preferred."
            )

        interpretation = (

            f"Overall Market Structure Score "
            f"is {score:.2f}/100."

        )

        return MarketStructureResult(

            score=round(score, 2),

            bias=bias,

            confidence=confidence,

            stars=stars,

            recommendation=recommendation,

            support_strength=support_strength,

            resistance_strength=resistance_strength,

            expected_move=expected_move,

            iv_rank=iv_rank,

            iv_percentile=iv_percentile,

            max_pain=max_pain,

            interpretation=interpretation,

        )