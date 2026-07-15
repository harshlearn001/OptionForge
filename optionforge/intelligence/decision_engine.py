"""
==============================================================
OptionForge
Intelligence
Institutional Decision Engine
==============================================================

Combines multiple intelligence engines into one
institutional decision.

Version : 1.0
Author  : OptionForge
==============================================================
"""

from __future__ import annotations

from optionforge.intelligence.enums.dealer_state import DealerState
from optionforge.intelligence.enums.market_state import MarketState
from optionforge.intelligence.enums.institutional_state import (
    InstitutionalState,
)

from optionforge.intelligence.models.dealer_intelligence import (
    DealerIntelligence,
)
from optionforge.intelligence.models.market_intelligence import (
    MarketIntelligence,
)
from optionforge.intelligence.models.institutional_decision import (
    InstitutionalDecision,
)


class DecisionEngine:
    """
    Institutional Decision Engine.

    Combines Dealer Intelligence and Market Intelligence
    into a single institutional opinion.

    This engine performs NO analytics.

    It only interprets existing intelligence.
    """

    # ---------------------------------------------------------
    # Decision Matrix
    # ---------------------------------------------------------

    DECISION_MATRIX = {
        (
            DealerState.LONG_GAMMA,
            MarketState.BULLISH_TREND,
        ): InstitutionalState.STRONGLY_BULLISH,
        (
            DealerState.LONG_GAMMA,
            MarketState.BREAKOUT,
        ): InstitutionalState.BULLISH,
        (
            DealerState.LONG_GAMMA,
            MarketState.RANGE_BOUND,
        ): InstitutionalState.BULLISH,
        (
            DealerState.TRANSITION,
            MarketState.TRANSITION,
        ): InstitutionalState.NEUTRAL,
        (
            DealerState.SHORT_GAMMA,
            MarketState.BEARISH_TREND,
        ): InstitutionalState.STRONGLY_BEARISH,
        (
            DealerState.SHORT_GAMMA,
            MarketState.RANGE_BOUND,
        ): InstitutionalState.BEARISH,
    }

    @classmethod
    def evaluate(
        cls,
        *,
        dealer: DealerIntelligence,
        market: MarketIntelligence,
    ) -> InstitutionalDecision:

        state = cls.DECISION_MATRIX.get(
            (dealer.state, market.state),
            InstitutionalState.NEUTRAL,
        )

        evidence = (
            f"Dealer = {dealer.state.name}",
            f"Market = {market.state.name}",
        )

        confidence = round(
            (dealer.confidence + market.confidence) / 2,
            1,
        )

        risks = ("Monitor for changing market conditions.",)

        summary = f"Institutional assessment is " f"{state.name.replace('_', ' ')}."

        return InstitutionalDecision(
            state=state,
            confidence=confidence,
            evidence=evidence,
            risks=risks,
            summary=summary,
        )
