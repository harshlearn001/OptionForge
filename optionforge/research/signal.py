"""
==============================================================
OptionForge
research/signal.py
--------------------------------------------------------------
Professional Trading Signal Enum
==============================================================
"""

from enum import Enum


class Signal(Enum):
    """
    Professional research signal.

    Every strategy in OptionForge returns one of these
    values only.
    """

    BUY = "BUY"
    SELL = "SELL"
    WATCH = "WATCH"

    def __str__(self) -> str:
        return self.value
