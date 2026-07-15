"""
============================================================
OptionForge
IV Chain Result
============================================================

Immutable result object for an entire IV option chain.

============================================================
"""

from __future__ import annotations

from dataclasses import dataclass

import pandas as pd


@dataclass(
    frozen=True,
    slots=True,
)
class IVChainResult:
    """
    Entire option chain with calculated IV and Greeks.
    """

    symbol: str

    trade_date: int

    expiry: int

    spot: float

    chain: pd.DataFrame

    def __len__(self) -> int:

        return len(self.chain)

    @property
    def contracts(self) -> int:

        return len(self.chain)

    def __repr__(self) -> str:

        return (
            f"IVChainResult(" f"symbol={self.symbol}, " f"contracts={self.contracts})"
        )

    __str__ = __repr__
