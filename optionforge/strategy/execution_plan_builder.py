"""
============================================================
OptionForge
Execution Plan Builder
============================================================

Author      : OptionForge
Module      : execution_plan_builder.py

Purpose
-------
Build immutable ExecutionPlan objects.

ExecutionPlanBuilder is the ONLY component responsible
for constructing ExecutionPlan instances.

Contains NO business logic related to market analysis.

============================================================
"""

from __future__ import annotations

from optionforge.strategy.execution_plan import (
    ExecutionPlan,
)
from optionforge.strategy.strategy import (
    Strategy,
)


class ExecutionPlanBuilder:
    """
    Builds immutable ExecutionPlan objects.
    """

    # =====================================================
    # Public API
    # =====================================================

    def build(
        self,
        strategy: Strategy,
    ) -> ExecutionPlan:
        """
        Build an ExecutionPlan from Strategy.
        """

        return ExecutionPlan(

            strategy=strategy,

            entry_rule=self._entry_rule(
                strategy,
            ),

            entry_price=self._entry_price(
                strategy,
            ),

            target_rule=self._target_rule(
                strategy,
            ),

            stop_loss_rule=self._stop_loss(
                strategy,
            ),

            position_size=self._position_size(
                strategy,
            ),

            max_capital=self._max_capital(
                strategy,
            ),

            max_risk=self._max_risk(
                strategy,
            ),

            expected_reward=self._expected_reward(
                strategy,
            ),

            notes=self._notes(
                strategy,
            ),

            metadata={

                "builder":
                    "ExecutionPlanBuilder",

                "strategy":
                    strategy.type.name,

            },

        )

    # =====================================================
    # Entry
    # =====================================================

    @staticmethod
    def _entry_rule(
        strategy: Strategy,
    ) -> str:

        if strategy.is_cash:

            return "No trade."

        return "Enter after confirmation candle."

    @staticmethod
    def _entry_price(
        strategy: Strategy,
    ) -> str:

        if strategy.is_cash:

            return "N/A"

        return "Market"
    
        # =====================================================
    # Target
    # =====================================================

    @staticmethod
    def _target_rule(
        strategy: Strategy,
    ) -> str:

        if strategy.is_cash:

            return "N/A"

        if strategy.is_hedge:

            return "Maintain protection."

        if strategy.is_volatility:

            return "Exit after volatility expansion."

        return "Trail profits using swing highs/lows."

    # =====================================================
    # Stop Loss
    # =====================================================

    @staticmethod
    def _stop_loss(
        strategy: Strategy,
    ) -> str:

        if strategy.is_cash:

            return "N/A"

        if strategy.is_hedge:

            return "Portfolio risk threshold."

        return "Exit at predefined premium loss."

    # =====================================================
    # Position Sizing
    # =====================================================

    @staticmethod
    def _position_size(
        strategy: Strategy,
    ) -> str:

        if strategy.is_cash:

            return "0 Lots"

        if strategy.risk.is_low:

            return "1 Lot"

        if strategy.risk.is_moderate:

            return "2 Lots"

        if strategy.risk.is_high:

            return "3 Lots"

        return "Institutional Size"

    # =====================================================
    # Capital
    # =====================================================

    @staticmethod
    def _max_capital(
        strategy: Strategy,
    ) -> str:

        return f"₹{strategy.capital_required:,.0f}"

    @staticmethod
    def _max_risk(
        strategy: Strategy,
    ) -> str:

        if strategy.is_cash:

            return "₹0"

        if strategy.risk.is_low:

            return "1% Portfolio"

        if strategy.risk.is_moderate:

            return "2% Portfolio"

        if strategy.risk.is_high:

            return "3% Portfolio"

        return "Defined by Risk Desk"
    

        # =====================================================
    # Expected Reward
    # =====================================================

    @staticmethod
    def _expected_reward(
        strategy: Strategy,
    ) -> str:

        if strategy.is_cash:

            return "None"

        if strategy.is_hedge:

            return "Capital Protection"

        if strategy.is_volatility:

            return "Depends on Volatility Expansion"

        return strategy.max_profit

    # =====================================================
    # Notes
    # =====================================================

    @staticmethod
    def _notes(
        strategy: Strategy,
    ) -> tuple[str, ...]:

        notes = [

            f"Strategy: {strategy.title}",

            f"Risk: {strategy.risk.name}",

            f"Confidence: {strategy.confidence:.1f}%",

        ]

        if strategy.is_cash:

            notes.append(

                "No trade recommended."

            )

        elif strategy.is_hedge:

            notes.append(

                "Portfolio protection strategy."

            )

        elif strategy.is_volatility:

            notes.append(

                "Monitor implied volatility closely."

            )

        else:

            notes.append(

                "Follow institutional risk management."

            )

        return tuple(notes)

    # =====================================================
    # Representation
    # =====================================================

    def __repr__(
        self,
    ) -> str:

        return (

            f"{self.__class__.__name__}()"

        )
    
