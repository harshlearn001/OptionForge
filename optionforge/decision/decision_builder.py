"""
============================================================
OptionForge
Decision Builder
============================================================

Author      : OptionForge
Module      : decision_builder.py

Purpose
-------
Builds an immutable Decision from MarketDNA.

This is the ONLY component responsible for creating
Decision objects.

============================================================
"""

from __future__ import annotations

from optionforge.decision.confidence_level import (
    ConfidenceLevel,
)
from optionforge.decision.decision import Decision
from optionforge.decision.decision_type import (
    DecisionType,
)
from optionforge.decision.strategy_type import (
    StrategyType,
)
from optionforge.marketdna.market_dna import MarketDNA


class DecisionBuilder:
    """
    Builds institutional trading decisions.
    """

    def build(
        self,
        market_dna: MarketDNA,
    ) -> Decision:

        decision = self._decision_type(
            market_dna,
        )

        strategy = self._strategy(
            market_dna,
            decision,
        )

        confidence_level = (
            ConfidenceLevel.from_score(
                market_dna.confidence,
            )
        )

        recommendation = (
            strategy.name.replace(
                "_",
                " ",
            ).title()
        )

        rationale = self._rationale(
            market_dna,
        )

        return Decision(

            decision=decision,

            strategy=strategy,

            confidence_level=confidence_level,

            confidence=market_dna.confidence,

            market_dna=market_dna,

            recommendation=recommendation,

            rationale=rationale,

        )

    # -----------------------------------------------------

    @staticmethod
    def _decision_type(
        dna: MarketDNA,
    ) -> DecisionType:

        if dna.is_bullish:

            if dna.confidence >= 90:

                return DecisionType.STRONG_BUY

            if dna.confidence >= 75:

                return DecisionType.BUY

            return DecisionType.ACCUMULATE

        if dna.is_bearish:

            if dna.confidence >= 90:

                return DecisionType.STRONG_SELL

            return DecisionType.SELL

        return DecisionType.HOLD

    # -----------------------------------------------------

    @staticmethod
    def _strategy(
        dna: MarketDNA,
        decision: DecisionType,
    ) -> StrategyType:

        if decision.is_bullish:

            if dna.is_low_volatility:

                return StrategyType.LONG_CALL

            return StrategyType.BULL_CALL_SPREAD

        if decision.is_bearish:

            if dna.is_high_volatility:

                return StrategyType.LONG_PUT

            return StrategyType.BEAR_PUT_SPREAD

        return StrategyType.CASH

    # -----------------------------------------------------

    @staticmethod
    def _rationale(
        dna: MarketDNA,
    ) -> tuple[str, ...]:

        return (

            f"Market Regime: {dna.regime}",

            f"Trend: {dna.trend}",

            f"Volatility: {dna.volatility}",

            f"Liquidity: {dna.liquidity}",

            f"Dealer: {dna.dealer_position}",

            f"Confidence: {dna.confidence:.1f}%",

        )