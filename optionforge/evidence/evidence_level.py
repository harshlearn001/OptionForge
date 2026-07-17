"""
============================================================
OptionForge
Evidence Level
============================================================

Author      : OptionForge
Module      : evidence_level.py
Purpose     : Represents the strength of institutional
              evidence.

EvidenceLevel is a qualitative classification derived
from quantitative evidence scores.

============================================================
"""

from __future__ import annotations

from enum import Enum, auto


from enum import IntEnum


class EvidenceLevel(IntEnum):

    VERY_WEAK = 1
    WEAK = 2
    MODERATE = 3
    STRONG = 4
    VERY_STRONG = 5

    @property
    def is_strong(self) -> bool:
        return self >= EvidenceLevel.STRONG

    @property
    def is_weak(self) -> bool:
        return self <= EvidenceLevel.WEAK

    @property
    def is_moderate(self) -> bool:
        return self is EvidenceLevel.MODERATE

    def __str__(self) -> str:
        return self.name.replace("_", " ").title()