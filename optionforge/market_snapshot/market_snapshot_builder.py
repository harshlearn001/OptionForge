"""
============================================================
OptionForge
Market Snapshot Builder
============================================================

Author      : OptionForge
Module      : market_snapshot_builder.py
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


class MarketSnapshotBuilder:
    """
    Builds immutable MarketSnapshot objects.

    Responsibilities
    ----------------
    ✓ Load synchronized market datasets
    ✓ Build immutable MarketSnapshot
    ✓ No analytics
    ✓ No business logic
    """

    def __init__(
        self,
        loader: Loader,
    ) -> None:

        self._loader = loader

    @property
    def loader(self) -> Loader:
        """
        Returns the configured loader.
        """
        return self._loader

    # -----------------------------------------------------

    def build(
        self,
        symbol: str,
    ) -> MarketSnapshot:
        """
        Build synchronized MarketSnapshot.
        """

        market = self.loader.load(symbol)

        return MarketSnapshot(
            symbol=symbol,
            option=market.option,
            future=market.future,
            spot=market.spot,
        )

    # -----------------------------------------------------

    def __repr__(self) -> str:

        return (
            f"{self.__class__.__name__}("
            f"loader={self.loader.__class__.__name__})"
        )

    __str__ = __repr__


# ==========================================================
# Backward Compatibility
# ==========================================================

# Existing code importing SnapshotBuilder will continue
# to work during the migration.
SnapshotBuilder = MarketSnapshotBuilder