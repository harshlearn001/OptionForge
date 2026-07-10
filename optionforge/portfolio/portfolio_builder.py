"""
============================================================
OptionForge
Portfolio Builder
============================================================

Author      : OptionForge
Module      : portfolio_builder.py

Purpose
-------
Construct immutable Portfolio objects from positions,
allocations and portfolio configuration.

Contains NO portfolio management logic.

============================================================
"""

from __future__ import annotations

from optionforge.portfolio.allocation import (
    Allocation,
)
from optionforge.portfolio.portfolio import (
    Portfolio,
)
from optionforge.portfolio.portfolio_risk import (
    PortfolioRisk,
)
from optionforge.portfolio.portfolio_type import (
    PortfolioType,
)
from optionforge.portfolio.position import (
    Position,
)


class PortfolioBuilder:
    """
    Institutional Portfolio Builder.
    """

    # =====================================================
    # Public API
    # =====================================================

    def build(
        self,
        *,
        name: str,
        portfolio_type: PortfolioType,
        portfolio_risk: PortfolioRisk,
        positions: tuple[Position, ...] = (),
        allocations: tuple[Allocation, ...] = (),
        total_capital: float = 0.0,
    ) -> Portfolio:
        """
        Build an immutable Portfolio.
        """

        return Portfolio(

            name=name,

            portfolio_type=portfolio_type,

            portfolio_risk=portfolio_risk,

            positions=positions,

            allocations=allocations,

            total_capital=total_capital,

        )
        # =====================================================
    # Convenience
    # =====================================================

    def empty(
        self,
        *,
        name: str,
        portfolio_type: PortfolioType,
        portfolio_risk: PortfolioRisk,
        total_capital: float,
    ) -> Portfolio:
        """
        Build an empty Portfolio.
        """

        return self.build(

            name=name,

            portfolio_type=portfolio_type,

            portfolio_risk=portfolio_risk,

            positions=(),

            allocations=(),

            total_capital=total_capital,

        )

    def from_positions(
        self,
        *,
        name: str,
        portfolio_type: PortfolioType,
        portfolio_risk: PortfolioRisk,
        positions: tuple[Position, ...],
        allocations: tuple[Allocation, ...],
        total_capital: float,
    ) -> Portfolio:
        """
        Build a Portfolio from existing
        positions and allocations.
        """

        return self.build(

            name=name,

            portfolio_type=portfolio_type,

            portfolio_risk=portfolio_risk,

            positions=positions,

            allocations=allocations,

            total_capital=total_capital,

        )

    # =====================================================
    # Callable Interface
    # =====================================================

    def __call__(
        self,
        **kwargs,
    ) -> Portfolio:
        """
        Callable shortcut.
        """

        return self.build(

            **kwargs,

        )

    # =====================================================
    # Representation
    # =====================================================

    def __repr__(
        self,
    ) -> str:

        return (

            f"{self.__class__.__name__}()"

        )