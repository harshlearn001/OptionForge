"""
==============================================================
OptionForge
OI Trend Result
--------------------------------------------------------------
Immutable result object for OI Trend analytics.
==============================================================
"""

from __future__ import annotations

from dataclasses import dataclass

import pandas as pd

from optionforge.common.enums import TrendDirection


@dataclass(frozen=True, slots=True)
class OITrendResult:
    """
    Immutable result object for OI Trend analytics.
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

    def strong_bullish(self) -> pd.DataFrame:

        return (
            self.df[
                self.df["TREND"]
                == TrendDirection.STRONG_BULLISH.value
            ]
            .copy()
            .reset_index(drop=True)
        )

    def bullish(self) -> pd.DataFrame:

        return (
            self.df[
                self.df["TREND"]
                == TrendDirection.BULLISH.value
            ]
            .copy()
            .reset_index(drop=True)
        )

    def sideways(self) -> pd.DataFrame:

        return (
            self.df[
                self.df["TREND"]
                == TrendDirection.SIDEWAYS.value
            ]
            .copy()
            .reset_index(drop=True)
        )

    def bearish(self) -> pd.DataFrame:

        return (
            self.df[
                self.df["TREND"]
                == TrendDirection.BEARISH.value
            ]
            .copy()
            .reset_index(drop=True)
        )

    def strong_bearish(self) -> pd.DataFrame:

        return (
            self.df[
                self.df["TREND"]
                == TrendDirection.STRONG_BEARISH.value
            ]
            .copy()
            .reset_index(drop=True)
        )

    # ==========================================================
    # Ranking
    # ==========================================================

    def top_bullish(
        self,
        n: int = 5,
    ) -> pd.DataFrame:

        return (
            self.df
            .nlargest(n, "TREND_SCORE")
            .reset_index(drop=True)
        )

    def top_bearish(
        self,
        n: int = 5,
    ) -> pd.DataFrame:

        return (
            self.df
            .nsmallest(n, "TREND_SCORE")
            .reset_index(drop=True)
        )

    # ==========================================================
    # Summary
    # ==========================================================

    def summary(self) -> dict[str, int]:

        counts = (
            self.df["TREND"]
            .value_counts()
            .to_dict()
        )

        return {
            TrendDirection.STRONG_BULLISH.value:
                counts.get(
                    TrendDirection.STRONG_BULLISH.value,
                    0,
                ),
            TrendDirection.BULLISH.value:
                counts.get(
                    TrendDirection.BULLISH.value,
                    0,
                ),
            TrendDirection.SIDEWAYS.value:
                counts.get(
                    TrendDirection.SIDEWAYS.value,
                    0,
                ),
            TrendDirection.BEARISH.value:
                counts.get(
                    TrendDirection.BEARISH.value,
                    0,
                ),
            TrendDirection.STRONG_BEARISH.value:
                counts.get(
                    TrendDirection.STRONG_BEARISH.value,
                    0,
                ),
        }

    # ==========================================================
    # Dictionary
    # ==========================================================

    def to_dict(self) -> dict:

        return {
            "rows": len(self.df),
            "summary": self.summary(),
            "strongest_bullish":
                self.top_bullish(1).iloc[0]["strike_price"],
            "strongest_bearish":
                self.top_bearish(1).iloc[0]["strike_price"],
        }

    # ==========================================================
    # Representation
    # ==========================================================

    def __repr__(self) -> str:

        return (
            "OITrendResult("
            f"rows={len(self.df)})"
        )