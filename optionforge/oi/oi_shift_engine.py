"""
==============================================================
OptionForge
OI Shift Engine
--------------------------------------------------------------
Institutional OI Shift Analytics Engine.

Compares two OIByStrike datasets and detects
Open Interest migration between snapshots.

Returns an immutable OIShiftResult.
==============================================================
"""

from __future__ import annotations

import pandas as pd

from optionforge.oi.oi_by_strike import OIByStrike
from optionforge.oi.shift_classifier import ShiftClassifier
from optionforge.oi.oi_shift_result import OIShiftResult


class OIShiftEngine:
    """
    Institutional OI Shift Engine.
    """

    def __init__(
        self,
        previous: OIByStrike,
        current: OIByStrike,
    ) -> None:

        self.previous = previous
        self.current = current

    # ==========================================================
    # Calculate
    # ==========================================================

    def calculate(
        self,
    ) -> OIShiftResult:
        """
        Calculate OI Shift analytics.
        """

        previous = (
            self.previous.dataframe()
            .loc[:, ["strike_price", "OI_SHARE"]]
            .rename(
                columns={
                    "OI_SHARE": "PREVIOUS_OI_SHARE",
                }
            )
        )

        current = self.current.dataframe().copy()

        df = pd.merge(
            current,
            previous,
            on="strike_price",
            how="left",
        )

        df["PREVIOUS_OI_SHARE"] = (
            df["PREVIOUS_OI_SHARE"]
            .fillna(0.0)
        )

        df["SHIFT"] = (
            df["OI_SHARE"]
            - df["PREVIOUS_OI_SHARE"]
        )

        df["SHIFT_DIRECTION"] = (
            df["SHIFT"]
            .apply(
                lambda x:
                ShiftClassifier.classify(x).value
            )
        )

        return OIShiftResult(df)

    # ==========================================================
    # Representation
    # ==========================================================

    def __repr__(self) -> str:

        return (
            "OIShiftEngine("
            f"rows={len(self.current.dataframe())})"
        )