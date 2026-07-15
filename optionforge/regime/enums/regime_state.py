"""
==============================================================
OptionForge
Market Regime State
==============================================================

Market regime classification used by the Regime Engine.

A regime represents the overall behavior of the market,
rather than a directional trading signal.

Author
------
OptionForge Engineering Team
==============================================================
"""

from __future__ import annotations

from enum import Enum, auto, unique


@unique
class RegimeState(Enum):
    """
    Market regime classification.
    """

    STRONG_UPTREND = auto()

    UPTREND = auto()

    RANGE_BOUND = auto()

    DOWNTREND = auto()

    STRONG_DOWNTREND = auto()

    VOLATILITY_EXPANSION = auto()

    VOLATILITY_COMPRESSION = auto()

    def __str__(self) -> str:
        return self.name