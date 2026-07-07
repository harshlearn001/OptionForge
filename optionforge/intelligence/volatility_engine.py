"""
==============================================================
OptionForge
Intelligence
Volatility Intelligence Engine
==============================================================

Interprets volatility analytics into an
institutional volatility assessment.

Version : 1.0
Author  : OptionForge
==============================================================
"""

from __future__ import annotations

from optionforge.intelligence.enums.volatility_state import (
    VolatilityState,
)

from optionforge.intelligence.models.volatility_intelligence import (
    VolatilityIntelligence,
)

from optionforge.models import (
    IVRankResult,
    IVPercentileResult,
    ExpectedMoveResult,
)


class VolatilityEngine:
    """
    Institutional Volatility Engine.

    Consumes volatility analytics and produces an
    institutional volatility interpretation.

    No analytics are calculated here.
    """

    @classmethod
    def evaluate(
        cls,
        *,
        iv_rank: IVRankResult,
        iv_percentile: IVPercentileResult,
        expected_move: ExpectedMoveResult,
    ) -> VolatilityIntelligence:

        evidence = (

            f"IV Rank = {iv_rank.iv_rank:.2f}",

            f"IV Percentile = {iv_percentile.iv_percentile:.2f}",

            f"Expected Move = {expected_move.expected_move:.2f}",

        )

        avg = (
            iv_rank.iv_rank +
            iv_percentile.iv_percentile
        ) / 2

        if avg <= 20:

            state = VolatilityState.VERY_CHEAP
            confidence = 95.0
            summary = (
                "Options appear exceptionally inexpensive."
            )

        elif avg <= 40:

            state = VolatilityState.CHEAP
            confidence = 88.0
            summary = (
                "Options appear relatively inexpensive."
            )

        elif avg <= 60:

            state = VolatilityState.FAIR
            confidence = 80.0
            summary = (
                "Volatility appears fairly priced."
            )

        elif avg <= 80:

            state = VolatilityState.EXPENSIVE
            confidence = 88.0
            summary = (
                "Options appear relatively expensive."
            )

        else:

            state = VolatilityState.VERY_EXPENSIVE
            confidence = 95.0
            summary = (
                "Options appear exceptionally expensive."
            )

        risks = (
            "Volatility regime may change rapidly.",
        )

        return VolatilityIntelligence(

            state=state,

            confidence=confidence,

            evidence=evidence,

            risks=risks,

            summary=summary,

        )