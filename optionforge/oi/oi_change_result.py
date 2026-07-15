"""
==============================================================
OptionForge
OI Change Result
==============================================================
"""

from __future__ import annotations

from dataclasses import dataclass

import pandas as pd


# ==========================================================
# One Strike
# ==========================================================

@dataclass(frozen=True, slots=True)
class OIChangeRow:
    """
    One strike OI Change analytics.
    """

    strike_price: float

    call_oi: int
    put_oi: int

    call_change: int
    put_change: int

    total_change: int

    call_volume: int
    put_volume: int

    pcr: float

    dominance: str

    buildup: str


# ==========================================================
# Result Table
# ==========================================================

class OIChangeResult:
    """
    Collection of OI Change rows.
    """

    def __init__(self, dataframe: pd.DataFrame):

        self._df = dataframe.copy()

    # ------------------------------------------------------

    def to_dataframe(self) -> pd.DataFrame:

        return self._df.copy()

    dataframe = to_dataframe

    # ------------------------------------------------------

    def __len__(self):

        return len(self._df)

    # ------------------------------------------------------

    def __repr__(self):

        return (
            f"OIChangeResult("
            f"rows={len(self)}, "
            f"columns={len(self._df.columns)})"
        )