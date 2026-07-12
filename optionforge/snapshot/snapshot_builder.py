"""
============================================================
OptionForge
Snapshot Builder
============================================================

Author      : OptionForge
Module      : snapshot_builder.py

Purpose
-------
Build immutable InstitutionalSnapshot objects from
Provider layer components.

Responsibilities
----------------
✓ Coordinate Providers
✓ Assemble InstitutionalSnapshot
✓ Never perform analytics
✓ Never read files
✓ Never validate CSVs

============================================================
"""

from __future__ import annotations

from optionforge.providers.option_provider import (
    OptionProvider,
)
from optionforge.providers.spot_provider import (
    SpotProvider,
)
from optionforge.snapshot.institutional_snapshot import (
    InstitutionalSnapshot,
)


class SnapshotBuilder:
    """
    Builder for InstitutionalSnapshot.
    """

    def __init__(
        self,
        option_provider: OptionProvider,
        spot_provider: SpotProvider,
    ) -> None:

        self._option_provider = option_provider
        self._spot_provider = spot_provider

    # =====================================================

    @property
    def option_provider(self) -> OptionProvider:

        return self._option_provider

    @property
    def spot_provider(self) -> SpotProvider:

        return self._spot_provider

    # =====================================================

    def build(
        self,
        symbol: str,
        trade_date,
        expiry,
    ) -> InstitutionalSnapshot:
        """
        Build an immutable market snapshot.
        """

        option_chain = self.option_provider.option_chain(
            symbol=symbol,
            trade_date=trade_date,
            expiry=expiry,
        )

        spot = self.spot_provider.latest(symbol)

        return InstitutionalSnapshot(

            symbol=symbol,

            trade_date=trade_date,

            expiry=expiry,

            spot=spot,

            option_chain=option_chain,

        )

    # =====================================================

    def __repr__(self) -> str:

        return (
            f"{self.__class__.__name__}("
            f"option_provider={self.option_provider.__class__.__name__}, "
            f"spot_provider={self.spot_provider.__class__.__name__})"
        )

    __str__ = __repr__