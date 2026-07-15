"""
==============================================================
OptionForge
Intelligence
Market State
==============================================================

Institutional Market Regimes.

Author : OptionForge
==============================================================
"""

from __future__ import annotations

from enum import Enum, auto


class MarketState(Enum):
    """
    Institutional Market Regime.
    """

    BULLISH_TREND = auto()

    BEARISH_TREND = auto()

    RANGE_BOUND = auto()

    BREAKOUT = auto()

    TRANSITION = auto()
