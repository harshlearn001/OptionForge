"""
============================================================
OptionForge
Portfolio Risk
============================================================

Author      : OptionForge
Module      : portfolio_risk.py

Purpose
-------
Defines institutional portfolio risk classifications.

PortfolioRisk represents the overall risk appetite
for an investment portfolio and guides capital
allocation and exposure limits.

============================================================
"""

from __future__ import annotations

from enum import Enum, auto


class PortfolioRisk(Enum):
    """
    Institutional portfolio risk profile.
    """

    # -----------------------------------------------------
    # Risk Levels
    # -----------------------------------------------------

    CONSERVATIVE = auto()

    BALANCED = auto()

    AGGRESSIVE = auto()

    INSTITUTIONAL = auto()

    # -----------------------------------------------------
    # Risk Score
    # -----------------------------------------------------

    @property
    def score(self) -> int:
        """
        Numerical portfolio risk score.
        """

        return {

            PortfolioRisk.CONSERVATIVE: 1,

            PortfolioRisk.BALANCED: 2,

            PortfolioRisk.AGGRESSIVE: 3,

            PortfolioRisk.INSTITUTIONAL: 4,

        }[self]

    # -----------------------------------------------------
    # Convenience
    # -----------------------------------------------------

    @property
    def is_conservative(self) -> bool:
        """
        Returns True for conservative portfolios.
        """

        return self is PortfolioRisk.CONSERVATIVE

    @property
    def is_balanced(self) -> bool:
        """
        Returns True for balanced portfolios.
        """

        return self is PortfolioRisk.BALANCED

    @property
    def is_aggressive(self) -> bool:
        """
        Returns True for aggressive portfolios.
        """

        return self is PortfolioRisk.AGGRESSIVE
    @property
    def is_institutional(self) -> bool:
        """
        Returns True for institutional portfolios.
        """

        return self is PortfolioRisk.INSTITUTIONAL

    # -----------------------------------------------------
    # Capital Allocation
    # -----------------------------------------------------

    @property
    def max_capital_per_trade(self) -> float:
        """
        Suggested maximum capital allocation per trade
        as a percentage of the portfolio.
        """

        return {

            PortfolioRisk.CONSERVATIVE: 2.0,

            PortfolioRisk.BALANCED: 5.0,

            PortfolioRisk.AGGRESSIVE: 10.0,

            PortfolioRisk.INSTITUTIONAL: 20.0,

        }[self]

    @property
    def max_portfolio_exposure(self) -> float:
        """
        Suggested maximum total portfolio exposure
        as a percentage of capital.
        """

        return {

            PortfolioRisk.CONSERVATIVE: 40.0,

            PortfolioRisk.BALANCED: 70.0,

            PortfolioRisk.AGGRESSIVE: 90.0,

            PortfolioRisk.INSTITUTIONAL: 100.0,

        }[self]

    @property
    def allows_unlimited_risk(self) -> bool:
        """
        Returns True when undefined-risk strategies
        may be permitted.
        """

        return self is PortfolioRisk.INSTITUTIONAL

    @property
    def requires_diversification(self) -> bool:
        """
        Returns True when diversification is expected.
        """

        return self in (

            PortfolioRisk.CONSERVATIVE,

            PortfolioRisk.BALANCED,

        )

    # -----------------------------------------------------
    # Factory
    # -----------------------------------------------------

    @classmethod
    def from_score(
        cls,
        score: int,
    ) -> "PortfolioRisk":
        """
        Convert a numerical score into a PortfolioRisk.
        """

        if score <= 1:
            return cls.CONSERVATIVE

        if score == 2:
            return cls.BALANCED

        if score == 3:
            return cls.AGGRESSIVE

        return cls.INSTITUTIONAL

    # -----------------------------------------------------
    # Representation
    # -----------------------------------------------------

    def __str__(self) -> str:
        """
        Human-readable representation.
        """

        return self.name.replace(

            "_",

            " ",

        ).title()