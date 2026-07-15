"""
============================================================
OptionForge
Snapshot Builder
============================================================

Author      : OptionForge
Module      : snapshot_builder.py
Purpose     : Build synchronized MarketSnapshot objects.

============================================================
"""

from __future__ import annotations

from optionforge.market_snapshot.market_snapshot import (
    MarketSnapshot,
)

from optionforge.utils.loader import (
    Loader,
)


class SnapshotBuilder:
    """
    Builds immutable MarketSnapshot objects.
    """

    def __init__(
        self,
        loader: Loader,
    ) -> None:

        self._loader = loader

    # -----------------------------------------------------

    def build(
        self,
        symbol: str,
    ) -> MarketSnapshot:
        """
        Build synchronized snapshot.
        """

        market = self._loader.load(symbol)

        return MarketSnapshot(
            symbol=symbol,
            option=market.option,
            future=market.future,
            spot=market.spot,
        )
