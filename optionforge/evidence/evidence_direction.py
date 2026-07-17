"""
============================================================
OptionForge
Evidence Direction
============================================================

Author      : OptionForge
Module      : evidence_direction.py
Purpose     : Represents the directional interpretation
              of institutional evidence.

EvidenceDirection is independent from EvidenceLevel.

Example
-------
Direction : Bullish
Level     : Strong

============================================================
"""

from __future__ import annotations

from enum import IntEnum


class EvidenceDirection(IntEnum):
    """
    Direction implied by evidence.
    """

    VERY_BEARISH = -2

    BEARISH = -1

    NEUTRAL = 0

    BULLISH = 1

    VERY_BULLISH = 2

    @property
    def is_bullish(self) -> bool:
        """
        Returns True for bullish evidence.
        """
        return self > EvidenceDirection.NEUTRAL

    @property
    def is_bearish(self) -> bool:
        """
        Returns True for bearish evidence.
        """
        return self < EvidenceDirection.NEUTRAL

    @property
    def is_neutral(self) -> bool:
        """
        Returns True for neutral evidence.
        """
        return self is EvidenceDirection.NEUTRAL

    @property
    def intensity(self) -> int:
        """
        Absolute directional strength.

        VERY_BULLISH -> 2
        BULLISH      -> 1
        NEUTRAL      -> 0
        """
        return abs(int(self))

    @property
    def opposite(self) -> "EvidenceDirection":
        """
        Returns opposite direction.
        """
        return EvidenceDirection(-int(self))

    def __str__(self) -> str:
        """
        Human-readable representation.
        """
        return self.name.replace("_", " ").title()