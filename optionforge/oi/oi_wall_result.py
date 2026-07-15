"""
==============================================================
OptionForge
OI Wall Result
--------------------------------------------------------------
Immutable result object for OI Wall analytics.
==============================================================
"""

from __future__ import annotations

from dataclasses import dataclass

import pandas as pd

from optionforge.common.enums import WallType


@dataclass(frozen=True, slots=True)
class OIWallResult:
    """
    Immutable result object for OI Wall analytics.
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
    # Wall Filters
    # ==========================================================

    def call_wall(self) -> pd.DataFrame:

        return (
            self.df[
                self.df["WALL"] == WallType.CALL_WALL.value
            ]
            .copy()
            .reset_index(drop=True)
        )

    def put_wall(self) -> pd.DataFrame:

        return (
            self.df[
                self.df["WALL"] == WallType.PUT_WALL.value
            ]
            .copy()
            .reset_index(drop=True)
        )

    def balanced(self) -> pd.DataFrame:

        return (
            self.df[
                self.df["WALL"] == WallType.BALANCED.value
            ]
            .copy()
            .reset_index(drop=True)
        )

    # ==========================================================
    # Support / Resistance
    # ==========================================================

    def support(self) -> pd.Series:
        """
        Highest Put OI strike.
        """

        return (
            self.df
            .sort_values("PUT_OI", ascending=False)
            .iloc[0]
        )

    def resistance(self) -> pd.Series:
        """
        Highest Call OI strike.
        """

        return (
            self.df
            .sort_values("CALL_OI", ascending=False)
            .iloc[0]
        )

    # ==========================================================
    # Top Walls
    # ==========================================================

    def top_call_walls(
        self,
        n: int = 5,
    ) -> pd.DataFrame:

        return (
            self.df
            .nlargest(n, "CALL_OI")
            .reset_index(drop=True)
        )

    def top_put_walls(
        self,
        n: int = 5,
    ) -> pd.DataFrame:

        return (
            self.df
            .nlargest(n, "PUT_OI")
            .reset_index(drop=True)
        )

    # ==========================================================
    # Summary
    # ==========================================================

    def summary(self) -> dict[str, int]:

        counts = (
            self.df["WALL"]
            .value_counts()
            .to_dict()
        )

        return {
            WallType.CALL_WALL.value:
                counts.get(WallType.CALL_WALL.value, 0),

            WallType.PUT_WALL.value:
                counts.get(WallType.PUT_WALL.value, 0),

            WallType.BALANCED.value:
                counts.get(WallType.BALANCED.value, 0),
        }

    # ==========================================================
    # Dictionary
    # ==========================================================

    def to_dict(self) -> dict:

        return {

            "rows": len(self.df),

            "summary": self.summary(),

            "support":
                self.support()["strike_price"],

            "resistance":
                self.resistance()["strike_price"],
        }

    # ==========================================================
    # Representation
    # ==========================================================

    def __repr__(self) -> str:

        s = self.summary()

        return (
            "OIWallResult("
            f"rows={len(self.df)}, "
            f"CALL_WALL={s[WallType.CALL_WALL.value]}, "
            f"PUT_WALL={s[WallType.PUT_WALL.value]}, "
            f"BALANCED={s[WallType.BALANCED.value]})"
        )