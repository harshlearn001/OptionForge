"""
============================================================
OptionForge
Decision Type
============================================================

Author      : OptionForge
Module      : decision_type.py
Purpose     : High-level institutional trading decisions.

DecisionType represents the action selected after
evaluating MarketDNA.

It is intentionally strategy-independent.

============================================================
"""

from __future__ import annotations

from enum import Enum, auto


class DecisionType(Enum):
    """
    High-level institutional decision.
    """

    # -----------------------------------------------------
    # Directional
    # -----------------------------------------------------

    STRONG_BUY = auto()

    BUY = auto()

    ACCUMULATE = auto()

    HOLD = auto()

    REDUCE = auto()

    SELL = auto()

    STRONG_SELL = auto()

    # -----------------------------------------------------
    # Risk
    # -----------------------------------------------------

    HEDGE = auto()

    EXIT = auto()

    NO_ACTION = auto()

    # -----------------------------------------------------
    # Convenience
    # -----------------------------------------------------

    @property
    def is_bullish(self) -> bool:
        """
        Returns True for bullish decisions.
        """

        return self in (
            DecisionType.STRONG_BUY,
            DecisionType.BUY,
            DecisionType.ACCUMULATE,
        )

    @property
    def is_bearish(self) -> bool:
        """
        Returns True for bearish decisions.
        """

        return self in (
            DecisionType.SELL,
            DecisionType.STRONG_SELL,
        )

    @property
    def is_neutral(self) -> bool:
        """
        Returns True for neutral decisions.
        """

        return self in (
            DecisionType.HOLD,
            DecisionType.NO_ACTION,
        )

    @property
    def is_risk_action(self) -> bool:
        """
        Returns True for risk-management actions.
        """

        return self in (
            DecisionType.HEDGE,
            DecisionType.EXIT,
            DecisionType.REDUCE,
        )

    @property
    def score(self) -> int:
        """
        Numerical decision strength.
        """

        return {
            DecisionType.STRONG_SELL: -3,
            DecisionType.SELL: -2,
            DecisionType.REDUCE: -1,
            DecisionType.NO_ACTION: 0,
            DecisionType.HOLD: 0,
            DecisionType.ACCUMULATE: 1,
            DecisionType.BUY: 2,
            DecisionType.STRONG_BUY: 3,
            DecisionType.HEDGE: -4,
            DecisionType.EXIT: -5,
        }[self]

    def __str__(self) -> str:
        """
        Human-readable representation.
        """

        return self.name.replace("_", " ").title()
