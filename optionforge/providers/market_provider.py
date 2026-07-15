"""
============================================================
OptionForge
Market Provider
============================================================

Author      : OptionForge
Module      : market_provider.py

Purpose
-------
Base provider for all market data providers.

Responsibilities
----------------
✓ Access repositories
✓ Provide common query methods
✓ Never load files directly
✓ Never perform analytics

The Provider layer sits between the Repository layer
and higher-level business logic.

============================================================
"""

from __future__ import annotations

from abc import ABC

import pandas as pd

from optionforge.repository.market_repository import (
    MarketRepository,
)


class MarketProvider(ABC):
    """
    Base provider for market data.

    Providers expose business-oriented queries while
    delegating all data access to the Repository layer.
    """

    def __init__(
        self,
        repository: MarketRepository,
    ) -> None:

        self._repository = repository

    # =====================================================
    # Properties
    # =====================================================

    @property
    def repository(self) -> MarketRepository:
        """
        Underlying repository.
        """

        return self._repository

    # =====================================================
    # Common Queries
    # =====================================================

    def exists(
        self,
        symbol: str,
        **kwargs,
    ) -> bool:
        """
        Return True if data exists.
        """

        return self.repository.exists(
            symbol,
            **kwargs,
        )

    # -----------------------------------------------------

    def latest(
        self,
        symbol: str,
        **kwargs,
    ) -> pd.DataFrame:
        """
        Return latest available data.
        """

        return self.repository.latest(
            symbol,
            **kwargs,
        )

    # -----------------------------------------------------

    def history(
        self,
        symbol: str,
        **kwargs,
    ) -> pd.DataFrame:
        """
        Return historical dataset.
        """

        return self.repository.load(
            symbol,
            **kwargs,
        )

    # =====================================================
    # Representation
    # =====================================================

    def __repr__(self) -> str:

        return (
            f"{self.__class__.__name__}("
            f"repository={self.repository.__class__.__name__})"
        )

    __str__ = __repr__
