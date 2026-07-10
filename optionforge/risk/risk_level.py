"""
============================================================
OptionForge
Risk Level
============================================================

Author      : OptionForge
Module      : risk_level.py

Purpose
-------
Institutional risk severity classification.

RiskLevel represents the severity of risk associated
with a portfolio independent of the approval decision.

============================================================
"""

from __future__ import annotations

from enum import Enum, auto


class RiskLevel(Enum):
    """
    Institutional risk severity.
    """

    # -----------------------------------------------------
    # Severity
    # -----------------------------------------------------

    VERY_LOW = auto()

    LOW = auto()

    MODERATE = auto()

    HIGH = auto()

    VERY_HIGH = auto()

    EXTREME = auto()

    # -----------------------------------------------------
    # Convenience
    # -----------------------------------------------------

    @property
    def score(self) -> int:
        """
        Numerical severity score.
        """

        return {

            RiskLevel.VERY_LOW: 1,

            RiskLevel.LOW: 2,

            RiskLevel.MODERATE: 3,

            RiskLevel.HIGH: 4,

            RiskLevel.VERY_HIGH: 5,

            RiskLevel.EXTREME: 6,

        }[self]

    @property
    def is_safe(self) -> bool:
        """
        Suitable for normal operation.
        """

        return self in (

            RiskLevel.VERY_LOW,

            RiskLevel.LOW,

        )

    @property
    def requires_attention(self) -> bool:
        """
        Elevated monitoring required.
        """

        return self in (

            RiskLevel.MODERATE,

            RiskLevel.HIGH,

        )

    @property
    def is_critical(self) -> bool:
        """
        Critical institutional risk.
        """

        return self in (

            RiskLevel.VERY_HIGH,

            RiskLevel.EXTREME,

        )
    @classmethod
    def from_score(
        cls,
        score: float,
    ) -> "RiskLevel":
        """
        Convert a numerical risk score (0-100)
        into a RiskLevel.
        """

        if score <= 10:

            return cls.VERY_LOW

        if score <= 25:

            return cls.LOW

        if score <= 45:

            return cls.MODERATE

        if score <= 65:

            return cls.HIGH

        if score <= 85:

            return cls.VERY_HIGH

        return cls.EXTREME

    def __str__(
        self,
    ) -> str:
        """
        Human-readable representation.
        """

        return self.name.replace(

            "_",

            " ",

        ).title()