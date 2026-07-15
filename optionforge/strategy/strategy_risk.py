"""
============================================================
OptionForge
Strategy Risk
============================================================

Author      : OptionForge
Module      : strategy_risk.py
Purpose     : Institutional strategy risk classification.

StrategyRisk classifies the inherent risk profile of an
options strategy.

============================================================
"""

from __future__ import annotations

from enum import Enum, auto


class StrategyRisk(Enum):
    """
    Institutional strategy risk classification.
    """

    # -----------------------------------------------------
    # Risk Levels
    # -----------------------------------------------------

    VERY_LOW = auto()

    LOW = auto()

    MODERATE = auto()

    HIGH = auto()

    VERY_HIGH = auto()

    # -----------------------------------------------------
    # Convenience
    # -----------------------------------------------------

    @property
    def score(self) -> int:
        """
        Numerical risk score.
        """

        return {
            StrategyRisk.VERY_LOW: 1,
            StrategyRisk.LOW: 2,
            StrategyRisk.MODERATE: 3,
            StrategyRisk.HIGH: 4,
            StrategyRisk.VERY_HIGH: 5,
        }[self]

    @property
    def is_very_low(self) -> bool:
        """
        Returns True for VERY_LOW risk.
        """

        return self is StrategyRisk.VERY_LOW

    @property
    def is_low(self) -> bool:
        """
        Returns True for LOW risk.
        """

        return self is StrategyRisk.LOW

    @property
    def is_moderate(self) -> bool:
        """
        Returns True for MODERATE risk.
        """

        return self is StrategyRisk.MODERATE

    @property
    def is_high(self) -> bool:
        """
        Returns True for HIGH risk.
        """

        return self is StrategyRisk.HIGH

    @property
    def is_very_high(self) -> bool:
        """
        Returns True for VERY_HIGH risk.
        """

        return self is StrategyRisk.VERY_HIGH

    @property
    def is_conservative(self) -> bool:
        """
        Conservative institutional strategy.
        """

        return self in (
            StrategyRisk.VERY_LOW,
            StrategyRisk.LOW,
        )

    @property
    def is_aggressive(self) -> bool:
        """
        Aggressive institutional strategy.
        """

        return self in (
            StrategyRisk.HIGH,
            StrategyRisk.VERY_HIGH,
        )

    @property
    def requires_active_management(self) -> bool:
        """
        Strategies requiring active monitoring.
        """

        return self in (
            StrategyRisk.HIGH,
            StrategyRisk.VERY_HIGH,
        )

    @property
    def suitable_for_beginners(self) -> bool:
        """
        Educational convenience property.
        """

        return self in (
            StrategyRisk.VERY_LOW,
            StrategyRisk.LOW,
        )

    @classmethod
    def from_score(
        cls,
        score: int,
    ) -> "StrategyRisk":
        """
        Convert a numerical score into a StrategyRisk.
        """

        if score <= 1:

            return cls.VERY_LOW

        if score == 2:

            return cls.LOW

        if score == 3:

            return cls.MODERATE

        if score == 4:

            return cls.HIGH

        return cls.VERY_HIGH

    def __str__(self) -> str:
        """
        Human-readable representation.
        """

        return self.name.replace(
            "_",
            " ",
        ).title()
