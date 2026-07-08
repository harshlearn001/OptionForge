"""
============================================================
OptionForge
Risk Profile
============================================================

Author      : OptionForge
Module      : risk_profile.py
Purpose     : Defines institutional risk profiles.

RiskProfile determines the acceptable level of risk
used by the Strategy Engine when selecting an options
strategy.

============================================================
"""

from __future__ import annotations

from enum import Enum, auto


class RiskProfile(Enum):
    """
    Institutional trading risk profile.
    """

    # -----------------------------------------------------
    # Conservative
    # -----------------------------------------------------

    CONSERVATIVE = auto()

    # -----------------------------------------------------
    # Balanced
    # -----------------------------------------------------

    MODERATE = auto()

    # -----------------------------------------------------
    # Aggressive
    # -----------------------------------------------------

    AGGRESSIVE = auto()

    # -----------------------------------------------------
    # Professional
    # -----------------------------------------------------

    INSTITUTIONAL = auto()

    # -----------------------------------------------------
    # Convenience
    # -----------------------------------------------------

    @property
    def allows_unlimited_risk(self) -> bool:
        """
        Returns True if unlimited-risk strategies
        may be selected.
        """

        return self is RiskProfile.INSTITUTIONAL

    @property
    def prefers_defined_risk(self) -> bool:
        """
        Returns True if defined-risk strategies
        are preferred.
        """

        return self in (
            RiskProfile.CONSERVATIVE,
            RiskProfile.MODERATE,
        )

    @property
    def max_position_size(self) -> float:
        """
        Suggested maximum position size as a
        percentage of portfolio.
        """

        return {

            RiskProfile.CONSERVATIVE: 2.0,

            RiskProfile.MODERATE: 5.0,

            RiskProfile.AGGRESSIVE: 10.0,

            RiskProfile.INSTITUTIONAL: 25.0,

        }[self]

    @property
    def preferred_probability_of_profit(self) -> float:
        """
        Minimum preferred probability of profit.
        """

        return {

            RiskProfile.CONSERVATIVE: 75.0,

            RiskProfile.MODERATE: 65.0,

            RiskProfile.AGGRESSIVE: 55.0,

            RiskProfile.INSTITUTIONAL: 50.0,

        }[self]

    @property
    def prefers_income(self) -> bool:
        """
        Returns True for profiles that generally
        favor premium-selling strategies.
        """

        return self in (
            RiskProfile.CONSERVATIVE,
            RiskProfile.MODERATE,
        )

    @property
    def prefers_directional(self) -> bool:
        """
        Returns True for profiles that generally
        favor directional trades.
        """

        return self in (
            RiskProfile.AGGRESSIVE,
            RiskProfile.INSTITUTIONAL,
        )

    def __str__(self) -> str:
        """
        Human-readable representation.
        """

        return self.name.replace("_", " ").title()