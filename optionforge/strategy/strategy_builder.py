"""
============================================================
OptionForge
Strategy Builder
============================================================

Author      : OptionForge
Module      : strategy_builder.py
Purpose     : Builds immutable Strategy objects.

StrategyBuilder is the ONLY component responsible for
constructing Strategy instances.

============================================================
"""

from __future__ import annotations

from optionforge.decision.decision import Decision

from optionforge.strategy.strategy import Strategy
from optionforge.strategy.strategy_selector import (
    StrategySelector,
)


class StrategyBuilder:
    """
    Builds immutable Strategy objects.
    """

    def __init__(
        self,
        selector: StrategySelector | None = None,
    ) -> None:

        self._selector = (
            selector
            if selector is not None
            else StrategySelector()
        )

    # -----------------------------------------------------

    def build(
        self,
        decision: Decision,
    ) -> Strategy:
        """
        Build Strategy from Decision.
        """

        strategy_type = self._selector.select(
            decision,
        )

        return Strategy(

            type=strategy_type,

            title=self._title(strategy_type),

            summary=self._summary(strategy_type),

            direction=self._direction(strategy_type),

            volatility_view=self._volatility(strategy_type),

            market_environment=str(
                decision.market_dna.regime
            ),

            max_profit=self._max_profit(strategy_type),

            max_loss=self._max_loss(strategy_type),

            probability_of_profit=self._pop(
                strategy_type,
            ),

            risk_reward=self._risk_reward(
                strategy_type,
            ),

            confidence=decision.confidence,

        )

    # -----------------------------------------------------
    # Private Helpers
    # -----------------------------------------------------

    @staticmethod
    def _title(strategy) -> str:

        return strategy.name.replace(
            "_",
            " ",
        ).title()

    # -----------------------------------------------------

    @staticmethod
    def _summary(strategy) -> str:

        return (

            f"Institutional "

            f"{strategy.name.replace('_', ' ').title()} "

            f"strategy."

        )

    # -----------------------------------------------------

    @staticmethod
    def _direction(strategy) -> str:

        if strategy.is_bullish:
            return "Bullish"

        if strategy.is_bearish:
            return "Bearish"

        if strategy.is_neutral:
            return "Neutral"

        if strategy.is_volatility:
            return "Volatility"

        if strategy.is_hedge:
            return "Hedging"

        return "Cash"

    # -----------------------------------------------------

    @staticmethod
    def _volatility(strategy) -> str:

        if strategy.is_volatility:
            return "High"

        return "Normal"

    # -----------------------------------------------------

    @staticmethod
    def _max_profit(strategy) -> str:

        if strategy.is_cash:
            return "None"

        if strategy.is_hedge:
            return "Protection"

        if strategy.is_volatility:
            return "Variable"

        return "Defined"

    # -----------------------------------------------------

    @staticmethod
    def _max_loss(strategy) -> str:

        if strategy.is_cash:
            return "None"

        return "Defined"

    # -----------------------------------------------------

    @staticmethod
    def _pop(strategy) -> float:

        probabilities = {

            strategy.LONG_CALL: 45.0,

            strategy.BULL_CALL_SPREAD: 65.0,

            strategy.BULL_PUT_SPREAD: 72.0,

            strategy.LONG_PUT: 45.0,

            strategy.BEAR_PUT_SPREAD: 65.0,

            strategy.BEAR_CALL_SPREAD: 72.0,

            strategy.IRON_CONDOR: 70.0,

            strategy.IRON_BUTTERFLY: 68.0,

            strategy.LONG_STRADDLE: 42.0,

            strategy.LONG_STRANGLE: 40.0,

        }

        return probabilities.get(

            strategy,

            50.0,

        )

    # -----------------------------------------------------

    @staticmethod
    def _risk_reward(strategy) -> str:

        if strategy.is_cash:

            return "N/A"

        if strategy.is_hedge:

            return "Capital Protection"

        if strategy.is_volatility:

            return "Variable"

        return "1:2"