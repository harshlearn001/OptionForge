"""
============================================================
OptionForge
Market Regime
============================================================

Author      : OptionForge
Module      : market_regime.py
Purpose     : Defines the overall institutional market
              regime.

The MarketRegime represents the highest-level
classification of the market after evaluating all
available evidence.

============================================================
"""

from __future__ import annotations

from enum import Enum, auto


class MarketRegime(Enum):
    """
    Institutional market regime.
    """

    # -----------------------------------------------------
    # Directional Regimes
    # -----------------------------------------------------

    STRONGLY_BULLISH = auto()

    BULLISH = auto()

    NEUTRAL = auto()

    BEARISH = auto()

    STRONGLY_BEARISH = auto()

    # -----------------------------------------------------
    # Transitional Regime
    # -----------------------------------------------------

    TRANSITION = auto()

    # -----------------------------------------------------
    # Trading Environment
    # -----------------------------------------------------

    RANGE_BOUND = auto()

    TRENDING = auto()

    HIGH_VOLATILITY = auto()

    LOW_VOLATILITY = auto()

    @property
    def is_bullish(self) -> bool:
        """
        Returns True for bullish regimes.
        """

        return self in (
            MarketRegime.BULLISH,
            MarketRegime.STRONGLY_BULLISH,
        )

    @property
    def is_bearish(self) -> bool:
        """
        Returns True for bearish regimes.
        """

        return self in (
            MarketRegime.BEARISH,
            MarketRegime.STRONGLY_BEARISH,
        )

    @property
    def is_neutral(self) -> bool:
        """
        Returns True for neutral market.
        """

        return self is MarketRegime.NEUTRAL

    @property
    def is_trending(self) -> bool:
        """
        Returns True for trending environments.
        """

        return self is MarketRegime.TRENDING

    @property
    def is_range_bound(self) -> bool:
        """
        Returns True for range-bound markets.
        """

        return self is MarketRegime.RANGE_BOUND

    def __str__(self) -> str:
        """
        Human-readable representation.
        """

        return self.name.replace("_", " ").title()
