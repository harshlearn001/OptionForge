"""
==============================================================
OptionForge
research/exit_reason.py
--------------------------------------------------------------
Professional Trade Exit Reasons
==============================================================
"""

from enum import Enum


class ExitReason(Enum):
    """
    Professional trade exit reason.
    """

    TARGET = "TARGET"
    STOP = "STOP"
    TIME = "TIME"
    MANUAL = "MANUAL"

    def __str__(self) -> str:
        return self.value