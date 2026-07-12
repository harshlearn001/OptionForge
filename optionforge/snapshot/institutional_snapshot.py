"""
============================================================
OptionForge
Institutional Snapshot
============================================================

Author      : OptionForge
Module      : institutional_snapshot.py

Purpose
-------
Immutable market snapshot consumed by every analytics
engine inside OptionForge.

Responsibilities
----------------
✓ Hold market state
✓ Immutable
✓ No analytics
✓ No repository logic
✓ No provider logic
✓ No file loading

============================================================
"""

from __future__ import annotations

from dataclasses import dataclass

import pandas as pd


@dataclass(frozen=True, slots=True)
class InstitutionalSnapshot:
    """
    Immutable market snapshot.

    Every analytics engine should consume this object
    instead of directly accessing repositories or
    providers.
    """

    # =====================================================
    # Identity
    # =====================================================

    symbol: str

    trade_date: object

    expiry: object

    # =====================================================
    # Market Data
    # =====================================================

    spot: pd.DataFrame

    option_chain: pd.DataFrame

    vix: pd.DataFrame | None = None

    # =====================================================
    # Metadata
    # =====================================================

    days_to_expiry: int | None = None

    source: str = "MarketForge"

    version: str = "0.4.0"

    # =====================================================

    @property
    def has_vix(self) -> bool:
        """
        Returns True if VIX data is available.
        """

        return self.vix is not None

    # =====================================================

    @property
    def strike_count(self) -> int:
        """
        Number of unique strikes.
        """

        if self.option_chain.empty:
            return 0

        return int(
            self.option_chain[
                "STRIKE_PRICE"
            ]
            .nunique()
        )

    # =====================================================

    @property
    def contract_count(self) -> int:
        """
        Number of option contracts.
        """

        return len(self.option_chain)

    # =====================================================

    def __repr__(self) -> str:

        return (
            f"{self.__class__.__name__}("
            f"symbol={self.symbol!r}, "
            f"trade_date={self.trade_date!r}, "
            f"expiry={self.expiry!r}, "
            f"contracts={self.contract_count})"
        )

    __str__ = __repr__