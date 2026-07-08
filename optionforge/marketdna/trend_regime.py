"""
============================================================
OptionForge
Trend Regime
============================================================

Author      : OptionForge
Module      : trend_regime.py
Purpose     : Defines the institutional market trend.

The TrendRegime represents the directional structure
of the market after evaluating institutional evidence.

============================================================
"""

from __future__ import annotations

from enum import Enum, auto


class TrendRegime(Enum):
    """
    Institutional trend classification.
    """

    # -----------------------------------------------------
    # Bullish Trend
    # -----------------------------------------------------

    STRONG_UPTREND = auto()

    UPTREND = auto()

    WEAK_UPTREND = auto()

    # -----------------------------------------------------
    # Neutral
    # -----------------------------------------------------

    SIDEWAYS = auto()

    TRANSITION = auto()

    # -----------------------------------------------------
    # Bearish Trend
    # -----------------------------------------------------

    WEAK_DOWNTREND = auto()

    DOWNTREND = auto()

    STRONG_DOWNTREND = auto()

    # -----------------------------------------------------
    # Convenience
    # -----------------------------------------------------

    @property
    def is_bullish(self) -> bool:
        """
        Returns True for bullish trends.
        """

        return self in (
            TrendRegime.STRONG_UPTREND,
            TrendRegime.UPTREND,
            TrendRegime.WEAK_UPTREND,
        )

    @property
    def is_bearish(self) -> bool:
        """
        Returns True for bearish trends.
        """

        return self in (
            TrendRegime.STRONG_DOWNTREND,
            TrendRegime.DOWNTREND,
            TrendRegime.WEAK_DOWNTREND,
        )

    @property
    def is_sideways(self) -> bool:
        """
        Returns True for sideways markets.
        """

        return self is TrendRegime.SIDEWAYS

    @property
    def is_transition(self) -> bool:
        """
        Returns True during trend transitions.
        """

        return self is TrendRegime.TRANSITION

    @property
    def strength(self) -> int:
        """
        Numerical trend strength.
        """

        return {
            TrendRegime.STRONG_DOWNTREND: -3,
            TrendRegime.DOWNTREND: -2,
            TrendRegime.WEAK_DOWNTREND: -1,
            TrendRegime.SIDEWAYS: 0,
            TrendRegime.TRANSITION: 0,
            TrendRegime.WEAK_UPTREND: 1,
            TrendRegime.UPTREND: 2,
            TrendRegime.STRONG_UPTREND: 3,
        }[self]

    def __str__(self) -> str:
        """
        Human-readable representation.
        """

        return self.name.replace("_", " ").title()