"""
============================================================
OptionForge
Confidence Level
============================================================

Author      : OptionForge
Module      : confidence_level.py
Purpose     : Institutional decision confidence.

ConfidenceLevel classifies how strongly OptionForge
believes its decision based on MarketDNA and Evidence.

============================================================
"""

from __future__ import annotations

from enum import Enum, auto


class ConfidenceLevel(Enum):
    """
    Institutional confidence classification.
    """

    # -----------------------------------------------------
    # Highest
    # -----------------------------------------------------

    VERY_HIGH = auto()

    HIGH = auto()

    MODERATE = auto()

    LOW = auto()

    VERY_LOW = auto()

    # -----------------------------------------------------
    # Convenience
    # -----------------------------------------------------

    @property
    def minimum_score(self) -> float:
        """
        Minimum confidence percentage.
        """

        return {

            ConfidenceLevel.VERY_HIGH: 90.0,

            ConfidenceLevel.HIGH: 75.0,

            ConfidenceLevel.MODERATE: 60.0,

            ConfidenceLevel.LOW: 40.0,

            ConfidenceLevel.VERY_LOW: 0.0,

        }[self]

    @property
    def is_tradeable(self) -> bool:
        """
        Returns True if confidence is sufficient
        for institutional trading.
        """

        return self in (

            ConfidenceLevel.VERY_HIGH,

            ConfidenceLevel.HIGH,

        )

    @property
    def requires_confirmation(self) -> bool:
        """
        Returns True if additional confirmation
        is recommended.
        """

        return self is ConfidenceLevel.MODERATE

    @property
    def avoid_new_positions(self) -> bool:
        """
        Returns True if confidence is too low
        to justify initiating new positions.
        """

        return self in (

            ConfidenceLevel.LOW,

            ConfidenceLevel.VERY_LOW,

        )

    def __str__(self) -> str:
        """
        Human-readable representation.
        """

        return self.name.replace("_", " ").title()

    @classmethod
    def from_score(
        cls,
        confidence: float,
    ) -> "ConfidenceLevel":
        """
        Convert numerical confidence into a
        ConfidenceLevel.
        """

        if confidence >= 90:

            return cls.VERY_HIGH

        if confidence >= 75:

            return cls.HIGH

        if confidence >= 60:

            return cls.MODERATE

        if confidence >= 40:

            return cls.LOW

        return cls.VERY_LOW