"""
============================================================
OptionForge
Market Snapshot
============================================================

Author      : OptionForge
Module      : market_snapshot.py
Purpose     : Immutable synchronized market datasets.

============================================================
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC, datetime

import pandas as pd


@dataclass(
    frozen=True,
    slots=True,
)
class MarketSnapshot:
    """
    Immutable synchronized market datasets.
    """

    symbol: str

    option: pd.DataFrame

    future: pd.DataFrame

    spot: pd.DataFrame

    timestamp: datetime = datetime.now(UTC)

    @property
    def option_rows(self) -> int:

        return len(self.option)

    @property
    def future_rows(self) -> int:

        return len(self.future)

    @property
    def spot_rows(self) -> int:

        return len(self.spot)

    @property
    def total_rows(self) -> int:

        return (

            self.option_rows

            + self.future_rows

            + self.spot_rows

        )

    def to_dict(self):

        return {

            "symbol": self.symbol,

            "option_rows": self.option_rows,

            "future_rows": self.future_rows,

            "spot_rows": self.spot_rows,

            "total_rows": self.total_rows,

            "timestamp": self.timestamp.isoformat(),

        }