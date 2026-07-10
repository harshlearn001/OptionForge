"""
============================================================
OptionForge
Strategy Type
============================================================

Author      : OptionForge
Module      : strategy_type.py
Purpose     : Institutional options strategies.

StrategyType represents the executable options strategy
recommended by OptionForge.

============================================================
"""

from __future__ import annotations

from enum import Enum, auto


class StrategyType(Enum):
    """
    Institutional options strategies.
    """

    # -----------------------------------------------------
    # Bullish
    # -----------------------------------------------------

    LONG_CALL = auto()

    BULL_CALL_SPREAD = auto()

    BULL_PUT_SPREAD = auto()

    SYNTHETIC_LONG = auto()

    # -----------------------------------------------------
    # Bearish
    # -----------------------------------------------------

    LONG_PUT = auto()

    BEAR_PUT_SPREAD = auto()

    BEAR_CALL_SPREAD = auto()

    SYNTHETIC_SHORT = auto()

    # -----------------------------------------------------
    # Neutral
    # -----------------------------------------------------

    IRON_CONDOR = auto()

    IRON_BUTTERFLY = auto()

    SHORT_STRANGLE = auto()

    SHORT_STRADDLE = auto()

    CALENDAR_SPREAD = auto()

    DIAGONAL_SPREAD = auto()

    # -----------------------------------------------------
    # Volatility
    # -----------------------------------------------------

    LONG_STRADDLE = auto()

    LONG_STRANGLE = auto()

    RATIO_SPREAD = auto()

    BACKSPREAD = auto()

    # -----------------------------------------------------
    # Hedging
    # -----------------------------------------------------

    PROTECTIVE_PUT = auto()

    COVERED_CALL = auto()

    COLLAR = auto()

    DELTA_HEDGE = auto()

    # -----------------------------------------------------
    # Cash
    # -----------------------------------------------------

    CASH = auto()

    NO_POSITION = auto()

    # -----------------------------------------------------
    # Convenience
    # -----------------------------------------------------

    @property
    def is_bullish(self) -> bool:

        return self in (

            StrategyType.LONG_CALL,

            StrategyType.BULL_CALL_SPREAD,

            StrategyType.BULL_PUT_SPREAD,

            StrategyType.SYNTHETIC_LONG,

        )

    @property
    def is_bearish(self) -> bool:

        return self in (

            StrategyType.LONG_PUT,

            StrategyType.BEAR_PUT_SPREAD,

            StrategyType.BEAR_CALL_SPREAD,

            StrategyType.SYNTHETIC_SHORT,

        )

    @property
    def is_neutral(self) -> bool:

        return self in (

            StrategyType.IRON_CONDOR,

            StrategyType.IRON_BUTTERFLY,

            StrategyType.SHORT_STRANGLE,

            StrategyType.SHORT_STRADDLE,

            StrategyType.CALENDAR_SPREAD,

            StrategyType.DIAGONAL_SPREAD,

        )

    @property
    def is_volatility(self) -> bool:

        return self in (

            StrategyType.LONG_STRADDLE,

            StrategyType.LONG_STRANGLE,

            StrategyType.RATIO_SPREAD,

            StrategyType.BACKSPREAD,

        )

    @property
    def is_hedge(self) -> bool:

        return self in (

            StrategyType.PROTECTIVE_PUT,

            StrategyType.COVERED_CALL,

            StrategyType.COLLAR,

            StrategyType.DELTA_HEDGE,

        )

    @property
    def is_cash(self) -> bool:

        return self in (

            StrategyType.CASH,

            StrategyType.NO_POSITION,

        )

    def __str__(self) -> str:

        return self.name.replace(
            "_",
            " ",
        ).title()