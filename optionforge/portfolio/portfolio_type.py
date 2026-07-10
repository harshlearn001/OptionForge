"""
============================================================
OptionForge
Portfolio Type
============================================================

Author      : OptionForge
Module      : portfolio_type.py

Purpose
-------
Defines institutional portfolio classifications.

PortfolioType represents the primary objective of a
portfolio and guides capital allocation, diversification,
and risk management decisions.

============================================================
"""

from __future__ import annotations

from enum import Enum, auto


class PortfolioType(Enum):
    """
    Institutional portfolio classifications.
    """

    # -----------------------------------------------------
    # Directional
    # -----------------------------------------------------

    DIRECTIONAL = auto()

    # -----------------------------------------------------
    # Income
    # -----------------------------------------------------

    INCOME = auto()

    # -----------------------------------------------------
    # Volatility
    # -----------------------------------------------------

    VOLATILITY = auto()

    # -----------------------------------------------------
    # Hedging
    # -----------------------------------------------------

    HEDGING = auto()

    # -----------------------------------------------------
    # Market Neutral
    # -----------------------------------------------------

    MARKET_NEUTRAL = auto()

    # -----------------------------------------------------
    # Cash
    # -----------------------------------------------------

    CASH = auto()

    # -----------------------------------------------------
    # Convenience
    # -----------------------------------------------------

    @property
    def is_directional(self) -> bool:
        """
        Returns True for directional portfolios.
        """

        return self is PortfolioType.DIRECTIONAL

    @property
    def is_income(self) -> bool:
        """
        Returns True for income portfolios.
        """

        return self is PortfolioType.INCOME

    @property
    def is_volatility(self) -> bool:
        """
        Returns True for volatility portfolios.
        """

        return self is PortfolioType.VOLATILITY
    @property
    def is_hedging(self) -> bool:
        """
        Returns True for hedging portfolios.
        """

        return self is PortfolioType.HEDGING

    @property
    def is_market_neutral(self) -> bool:
        """
        Returns True for market-neutral portfolios.
        """

        return self is PortfolioType.MARKET_NEUTRAL

    @property
    def is_cash(self) -> bool:
        """
        Returns True for cash portfolios.
        """

        return self is PortfolioType.CASH

    @property
    def requires_active_management(self) -> bool:
        """
        Returns True when the portfolio requires
        active management.
        """

        return self in (

            PortfolioType.DIRECTIONAL,

            PortfolioType.VOLATILITY,

            PortfolioType.HEDGING,

        )

    @property
    def allows_leverage(self) -> bool:
        """
        Returns True when leverage may be used.
        """

        return self in (

            PortfolioType.DIRECTIONAL,

            PortfolioType.VOLATILITY,

        )

    @property
    def is_defensive(self) -> bool:
        """
        Returns True for defensive portfolio styles.
        """

        return self in (

            PortfolioType.INCOME,

            PortfolioType.HEDGING,

            PortfolioType.CASH,

        )

    def __str__(self) -> str:
        """
        Human-readable representation.
        """

        return self.name.replace(

            "_",

            " ",

        ).title()
    