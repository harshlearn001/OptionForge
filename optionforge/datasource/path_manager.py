"""
==============================================================
OptionForge
Datasource
Path Manager
==============================================================

Centralized filesystem paths for MarketForge.

Responsibilities
----------------
- Locate MarketForge master data.
- Provide strongly typed paths.
- No file loading.
- No business logic.

Version : 2.0
Author  : OptionForge
==============================================================
"""

from __future__ import annotations

from pathlib import Path


class PathManager:
    """
    Centralized MarketForge path manager.
    """

    def __init__(self, marketforge_root: str | Path):

        self._root = Path(marketforge_root)

        self._master = self._root / "data" / "master"

    # ==========================================================
    # Spot Data
    # ==========================================================

    @property
    def equity_master(self) -> Path:
        return self._master / "Equity_master"

    @property
    def indices_master(self) -> Path:
        return self._master / "Indices_master"

    # ==========================================================
    # Futures
    # ==========================================================

    @property
    def futures_master(self) -> Path:
        return self._master / "Futures_master_three_expiries"

    @property
    def futidx(self) -> Path:
        return self.futures_master / "FUTIDX"

    @property
    def futstk(self) -> Path:
        return self.futures_master / "FUTSTK"

    # ==========================================================
    # Options
    # ==========================================================

    @property
    def options_master(self) -> Path:
        return self._master / "Options_master"

    @property
    def option_indices(self) -> Path:
        return self.options_master / "INDICES"

    @property
    def option_stocks(self) -> Path:
        return self.options_master / "STOCKS"

    # ==========================================================
    # Volatility
    # ==========================================================

    @property
    def vix(self) -> Path:
        return self.indices_master / "VIX.csv"