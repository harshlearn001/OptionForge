"""
============================================================
OptionForge
Spot Provider
============================================================

Author      : OptionForge
Module      : spot_provider.py

Purpose
-------
Business access layer for spot market data.

Responsibilities
----------------
✓ Provide spot history
✓ Provide latest market data
✓ Never read files
✓ Never validate data
✓ Never perform analytics
============================================================
"""

from __future__ import annotations

import pandas as pd

from optionforge.repository.spot_repository import SpotRepository


class SpotProvider:
    """
    Business provider for spot market data.
    """

    def __init__(
        self,
        repository: SpotRepository,
    ) -> None:

        self._repository = repository

    @property
    def repository(self) -> SpotRepository:
        return self._repository

    # -----------------------------------------------------

    def history(
        self,
        symbol: str,
    ) -> pd.DataFrame:
        """
        Return complete spot history.
        """

        return self.repository.load(symbol)

    # -----------------------------------------------------

    def latest(
        self,
        symbol: str,
    ) -> pd.DataFrame:
        """
        Return latest available row.
        """

        return self.repository.latest(symbol)

    # -----------------------------------------------------

    def __repr__(self) -> str:

        return (
            f"{self.__class__.__name__}("
            f"repository={self.repository.__class__.__name__})"
        )

    __str__ = __repr__
