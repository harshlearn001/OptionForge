"""
==============================================================
OptionForge
OI Summary
--------------------------------------------------------------
Professional Open Interest Summary
==============================================================
"""

from __future__ import annotations

import pandas as pd

from .helpers import (
    total_call_oi,
    total_put_oi,
    total_call_volume,
    total_put_volume,
    total_contracts,
    total_trades,
    pcr,
)


class OISummary:
    """
    Professional Open Interest Summary.
    """

    def __init__(self, df: pd.DataFrame):

        self.df = df

    # ---------------------------------------------------------

    @property
    def call_oi(self) -> int:

        return total_call_oi(self.df)

    @property
    def put_oi(self) -> int:

        return total_put_oi(self.df)

    @property
    def total_oi(self) -> int:

        return self.call_oi + self.put_oi

    # ---------------------------------------------------------

    @property
    def call_volume(self) -> int:

        return total_call_volume(self.df)

    @property
    def put_volume(self) -> int:

        return total_put_volume(self.df)

    @property
    def total_volume(self) -> int:

        return self.call_volume + self.put_volume

    # ---------------------------------------------------------

    @property
    def contracts(self) -> int:

        return total_contracts(self.df)

    @property
    def trades(self) -> int:

        return total_trades(self.df)

    # ---------------------------------------------------------

    @property
    def pcr(self) -> float:

        return pcr(self.df)

    # ---------------------------------------------------------

    def to_dict(self) -> dict:

        return {
            "CALL_OI": self.call_oi,
            "PUT_OI": self.put_oi,
            "TOTAL_OI": self.total_oi,
            "CALL_VOLUME": self.call_volume,
            "PUT_VOLUME": self.put_volume,
            "TOTAL_VOLUME": self.total_volume,
            "CONTRACTS": self.contracts,
            "TRADES": self.trades,
            "PCR": self.pcr,
        }

    # ---------------------------------------------------------

    def __repr__(self):

        return (
            f"OISummary("
            f"PCR={self.pcr}, "
            f"CALL_OI={self.call_oi:,}, "
            f"PUT_OI={self.put_oi:,})"
        )
