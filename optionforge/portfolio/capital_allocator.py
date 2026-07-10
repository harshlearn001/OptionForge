"""
============================================================
OptionForge
Capital Allocator
============================================================

Author      : OptionForge
Module      : capital_allocator.py

Purpose
-------
Institutional capital allocation engine.

CapitalAllocator determines how much capital should
be allocated to a Position based on the portfolio's
risk profile.

============================================================
"""

from __future__ import annotations

from optionforge.portfolio.allocation import (
    Allocation,
)
from optionforge.portfolio.portfolio_risk import (
    PortfolioRisk,
)
from optionforge.portfolio.position import (
    Position,
)


class CapitalAllocator:
    """
    Institutional capital allocation engine.
    """

    # =====================================================
    # Constructor
    # =====================================================

    def __init__(
        self,
        portfolio_risk: PortfolioRisk,
    ) -> None:

        self._portfolio_risk = portfolio_risk

    # =====================================================
    # Properties
    # =====================================================

    @property
    def portfolio_risk(
        self,
    ) -> PortfolioRisk:
        """
        Active portfolio risk profile.
        """

        return self._portfolio_risk

    # =====================================================
    # Public API
    # =====================================================

    def allocate(
        self,
        *,
        position: Position,
        portfolio_value: float,
    ) -> Allocation:
        """
        Allocate capital for a Position.
        """

        allocation = min(

            position.capital_used,

            portfolio_value
            * (
                self._portfolio_risk.max_capital_per_trade
                / 100.0
            ),

        )

        return Allocation(

            position=position,

            allocated_capital=allocation,

            available_capital=(

                portfolio_value

                - allocation

            ),

            portfolio_value=portfolio_value,

        )
        # =====================================================
    # Callable Interface
    # =====================================================

    def __call__(
        self,
        *,
        position: Position,
        portfolio_value: float,
    ) -> Allocation:
        """
        Callable shortcut.
        """

        return self.allocate(

            position=position,

            portfolio_value=portfolio_value,

        )

    # =====================================================
    # Validation
    # =====================================================

    def can_allocate(
        self,
        *,
        position: Position,
        portfolio_value: float,
    ) -> bool:
        """
        Returns True if the position can be
        allocated within the portfolio risk
        limits.
        """

        maximum = (

            portfolio_value

            * (

                self._portfolio_risk.max_capital_per_trade

                / 100.0

            )

        )

        return position.capital_used <= maximum

    def remaining_capacity(
        self,
        *,
        portfolio_value: float,
        allocated_capital: float,
    ) -> float:
        """
        Remaining allocatable capital.
        """

        return max(

            portfolio_value

            - allocated_capital,

            0.0,

        )

    # =====================================================
    # Representation
    # =====================================================

    def __repr__(
        self,
    ) -> str:

        return (

            f"{self.__class__.__name__}("

            f"portfolio_risk="

            f"{self._portfolio_risk.name})"

        )