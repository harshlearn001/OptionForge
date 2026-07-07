"""
==============================================================
OptionForge
Intelligence
Volatility State
==============================================================
"""

from __future__ import annotations

from enum import Enum, auto


class VolatilityState(Enum):
    """
    Institutional volatility regime.
    """

    VERY_CHEAP = auto()

    CHEAP = auto()

    FAIR = auto()

    EXPENSIVE = auto()

    VERY_EXPENSIVE = auto()