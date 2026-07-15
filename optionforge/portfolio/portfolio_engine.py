"""
============================================================
OptionForge
Portfolio Engine
============================================================

Author      : OptionForge
Module      : portfolio_engine.py

Purpose
-------
Institutional orchestration engine for Portfolio.

Coordinates:

    Position(s)
          ↓
    CapitalAllocator
          ↓
    PortfolioBuilder
          ↓
    Portfolio
          ↓
    PortfolioResult

Contains NO portfolio business logic.

============================================================
"""

from __future__ import annotations

from optionforge.portfolio.capital_allocator import (
    CapitalAllocator,
)
from optionforge.portfolio.portfolio import (
    Portfolio,
)
from optionforge.portfolio.portfolio_builder import (
    PortfolioBuilder,
)
from optionforge.portfolio.portfolio_result import (
    PortfolioResult,
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


class PortfolioEngine:
    """
    Institutional Portfolio Engine.
    """

    # =====================================================
    # Constructor
    # =====================================================

    def __init__(
        self,
        *,
        portfolio_risk: PortfolioRisk,
        allocator: CapitalAllocator | None = None,
        builder: PortfolioBuilder | None = None,
    ) -> None:

        self._allocator = (
            allocator
            if allocator is not None
            else CapitalAllocator(
                portfolio_risk,
            )
        )

        self._builder = builder if builder is not None else PortfolioBuilder()
        # =====================================================

    # Public API
    # =====================================================

    def build(
        self,
        *,
        name: str,
        portfolio_type: PortfolioType,
        positions: tuple[Position, ...],
        total_capital: float,
    ) -> PortfolioResult:
        """
        Build an institutional PortfolioResult.
        """

        allocations = tuple(
            self._allocator.allocate(
                position=position,
                portfolio_value=total_capital,
            )
            for position in positions
        )

        portfolio = self._builder.build(
            name=name,
            portfolio_type=portfolio_type,
            portfolio_risk=(self._allocator.portfolio_risk),
            positions=positions,
            allocations=allocations,
            total_capital=total_capital,
        )

        return PortfolioResult(
            portfolio=portfolio,
        )

    # =====================================================
    # Callable Interface
    # =====================================================

    def __call__(
        self,
        *,
        name: str,
        portfolio_type: PortfolioType,
        positions: tuple[Position, ...],
        total_capital: float,
    ) -> PortfolioResult:
        """
        Callable shortcut.
        """

        return self.build(
            name=name,
            portfolio_type=portfolio_type,
            positions=positions,
            total_capital=total_capital,
        )
        # =====================================================

    # Convenience
    # =====================================================

    @property
    def allocator(
        self,
    ) -> CapitalAllocator:
        """
        Capital allocator.
        """

        return self._allocator

    @property
    def builder(
        self,
    ) -> PortfolioBuilder:
        """
        Portfolio builder.
        """

        return self._builder

    # =====================================================
    # Representation
    # =====================================================

    def __repr__(
        self,
    ) -> str:

        return (
            f"{self.__class__.__name__}("
            f"portfolio_risk="
            f"{self.allocator.portfolio_risk.name})"
        )
