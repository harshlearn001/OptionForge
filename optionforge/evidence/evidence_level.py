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


class EvidenceLevel(Enum):
    """
    Institutional evidence strength.
    """

    # -----------------------------------------------------
    # Weak Evidence
    # -----------------------------------------------------

    VERY_WEAK = auto()

    WEAK = auto()

    # -----------------------------------------------------
    # Neutral
    # -----------------------------------------------------

    MODERATE = auto()

    # -----------------------------------------------------
    # Strong Evidence
    # -----------------------------------------------------

    STRONG = auto()

    VERY_STRONG = auto()

    @property
    def rank(self) -> int:
        """
        Numerical ranking for comparisons.
        """

        return {
            EvidenceLevel.VERY_WEAK: 1,
            EvidenceLevel.WEAK: 2,
            EvidenceLevel.MODERATE: 3,
            EvidenceLevel.STRONG: 4,
            EvidenceLevel.VERY_STRONG: 5,
        }[self]

    @property
    def is_strong(self) -> bool:
        """
        Returns True for strong evidence.
        """

        return self in (
            EvidenceLevel.STRONG,
            EvidenceLevel.VERY_STRONG,
        )

    @property
    def is_weak(self) -> bool:
        """
        Returns True for weak evidence.
        """

        return self in (
            EvidenceLevel.VERY_WEAK,
            EvidenceLevel.WEAK,
        )

    @property
    def is_moderate(self) -> bool:
        """
        Returns True for moderate evidence.
        """

        return self is EvidenceLevel.MODERATE

    def __str__(self) -> str:
        """
        Human-readable representation.
        """

        return self.name.replace("_", " ").title()
