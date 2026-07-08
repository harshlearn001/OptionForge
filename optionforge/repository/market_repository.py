"""
============================================================
OptionForge
Market Repository
============================================================

Author      : OptionForge
Module      : market_repository.py
Purpose     : Base repository interface.

============================================================
"""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod

import pandas as pd


class MarketRepository(ABC):
    """
    Base repository for all market data.
    """

    @abstractmethod
    def load(
        self,
        symbol: str,
        **kwargs,
    ) -> pd.DataFrame:
        """
        Load market data.
        """

    @abstractmethod
    def exists(
        self,
        symbol: str,
        **kwargs,
    ) -> bool:
        """
        Return True if data exists.
        """

    @abstractmethod
    def latest(
        self,
        symbol: str,
        **kwargs,
    ) -> pd.DataFrame:
        """
        Return latest available dataset.
        """