"""
============================================================
OptionForge
Risk Profile
============================================================

Author      : OptionForge
Module      : risk_profile.py
Purpose     : Defines institutional trading risk profiles.

RiskProfile determines the acceptable level of risk
used by the Strategy framework when selecting an
options strategy.

============================================================
"""

from __future__ import annotations

from enum import Enum, auto


class RiskProfile(Enum):
    """
    Institutional trading risk profile.
    """

    # -----------------------------------------------------
    # Profiles
    # -----------------------------------------------------

    CONSERVATIVE = auto()

    MODERATE = auto()

    AGGRESSIVE = auto()

    INSTITUTIONAL = auto()

    # -----------------------------------------------------
    # Capital Allocation
    # -----------------------------------------------------

    @property
    def max_position_size(self) -> float:
        """
        Suggested maximum position size as a
        percentage of portfolio capital.
        """

        return {

            RiskProfile.CONSERVATIVE: 2.0,

            RiskProfile.MODERATE: 5.0,

            RiskProfile.AGGRESSIVE: 10.0,

            RiskProfile.INSTITUTIONAL: 25.0,

        }[self]

    # -----------------------------------------------------
    # Probability Preference
    # -----------------------------------------------------

    @property
    def preferred_probability_of_profit(
        self,
    ) -> float:
        """
        Minimum preferred probability of profit.
        """

        return {

            RiskProfile.CONSERVATIVE: 75.0,

            RiskProfile.MODERATE: 65.0,

            RiskProfile.AGGRESSIVE: 55.0,

            RiskProfile.INSTITUTIONAL: 50.0,

        }[self]

    # -----------------------------------------------------
    # Behaviour
    # -----------------------------------------------------

    @property
    def prefers_defined_risk(self) -> bool:
        """
        Prefers defined-risk option structures.
        """

        return self in (

            RiskProfile.CONSERVATIVE,

            RiskProfile.MODERATE,

        )

    @property
    def allows_unlimited_risk(self) -> bool:
        """
        Allows unlimited-risk strategies.
        """

        return self is RiskProfile.INSTITUTIONAL

    @property
    def prefers_income(self) -> bool:
        """
        Prefers premium-selling strategies.
        """

        return self in (

            RiskProfile.CONSERVATIVE,

            RiskProfile.MODERATE,

        )

    @property
    def prefers_directional(self) -> bool:
        """
        Prefers directional strategies.
        """

        return self in (

            RiskProfile.AGGRESSIVE,

            RiskProfile.INSTITUTIONAL,

        )

    @property
    def prefers_volatility(self) -> bool:
        """
        Prefers long volatility opportunities.
        """

        return self in (

            RiskProfile.AGGRESSIVE,

            RiskProfile.INSTITUTIONAL,

        )

    @property
    def prefers_capital_preservation(self) -> bool:
        """
        Prefers capital preservation.
        """

        return self is RiskProfile.CONSERVATIVE

    # -----------------------------------------------------
    # Representation
    # -----------------------------------------------------

    def __str__(self) -> str:

        return self.name.replace(
            "_",
            " ",
        ).title()