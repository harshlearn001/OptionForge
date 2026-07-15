"""
==============================================================
OptionForge
OI Shift Result
--------------------------------------------------------------
Immutable result object for OI Shift analytics.
==============================================================
"""

from __future__ import annotations

from dataclasses import dataclass

import pandas as pd

from optionforge.common.enums import ShiftDirection


@dataclass(frozen=True, slots=True)
class OIShiftResult:
    """
    Immutable result object for OI Shift analytics.
    """

    df: pd.DataFrame

    # ==========================================================
    # Data
    # ==========================================================

    def dataframe(self) -> pd.DataFrame:
        """
        Return a copy of the analytics table.
        """
        return self.df.copy()

    # ==========================================================
    # Filters
    # ==========================================================

    def strong_up(self) -> pd.DataFrame:

        return (
            self.df[
                self.df["SHIFT_DIRECTION"]
                == ShiftDirection.STRONG_UP.value
            ]
            .copy()
            .reset_index(drop=True)
        )

    def up(self) -> pd.DataFrame:

        return (
            self.df[
                self.df["SHIFT_DIRECTION"]
                == ShiftDirection.UP.value
            ]
            .copy()
            .reset_index(drop=True)
        )

    def neutral(self) -> pd.DataFrame:

        return (
            self.df[
                self.df["SHIFT_DIRECTION"]
                == ShiftDirection.NEUTRAL.value
            ]
            .copy()
            .reset_index(drop=True)
        )

    def down(self) -> pd.DataFrame:

        return (
            self.df[
                self.df["SHIFT_DIRECTION"]
                == ShiftDirection.DOWN.value
            ]
            .copy()
            .reset_index(drop=True)
        )

    def strong_down(self) -> pd.DataFrame:

        return (
            self.df[
                self.df["SHIFT_DIRECTION"]
                == ShiftDirection.STRONG_DOWN.value
            ]
            .copy()
            .reset_index(drop=True)
        )

    # ==========================================================
    # Ranking
    # ==========================================================

    def top_upward_shift(
        self,
        n: int = 5,
    ) -> pd.DataFrame:

        return (
            self.df
            .nlargest(n, "SHIFT")
            .reset_index(drop=True)
        )

    def top_downward_shift(
        self,
        n: int = 5,
    ) -> pd.DataFrame:

        return (
            self.df
            .nsmallest(n, "SHIFT")
            .reset_index(drop=True)
        )

    # ==========================================================
    # Summary
    # ==========================================================

    def summary(self) -> dict[str, int]:

        counts = (
            self.df["SHIFT_DIRECTION"]
            .value_counts()
            .to_dict()
        )

        return {
            ShiftDirection.STRONG_UP.value:
                counts.get(ShiftDirection.STRONG_UP.value, 0),

            ShiftDirection.UP.value:
                counts.get(ShiftDirection.UP.value, 0),

            ShiftDirection.NEUTRAL.value:
                counts.get(ShiftDirection.NEUTRAL.value, 0),

            ShiftDirection.DOWN.value:
                counts.get(ShiftDirection.DOWN.value, 0),

            ShiftDirection.STRONG_DOWN.value:
                counts.get(ShiftDirection.STRONG_DOWN.value, 0),
        }

    # ==========================================================
    # Dictionary
    # ==========================================================

    def to_dict(self) -> dict:

        return {

            "rows": len(self.df),

            "summary": self.summary(),

            "largest_upward_shift":
                self.top_upward_shift(1)
                .iloc[0]["strike_price"],

            "largest_downward_shift":
                self.top_downward_shift(1)
                .iloc[0]["strike_price"],
        }

    # ==========================================================
    # Representation
    # ==========================================================

    def __repr__(self) -> str:

        return (
            "OIShiftResult("
            f"rows={len(self.df)})"
        )