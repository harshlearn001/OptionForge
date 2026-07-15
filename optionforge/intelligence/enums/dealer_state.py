"""
==============================================================
Dealer State
==============================================================
"""

from enum import Enum, auto


class DealerState(Enum):
    """
    Institutional dealer positioning.
    """

    LONG_GAMMA = auto()

    SHORT_GAMMA = auto()

    NEUTRAL = auto()

    TRANSITION = auto()

    UNKNOWN = auto()
