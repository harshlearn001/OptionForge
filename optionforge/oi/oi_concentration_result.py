"""
==============================================================
OptionForge
OI Concentration Result
--------------------------------------------------------------
Immutable result object for OI Concentration analytics.
==============================================================
"""

from __future__ import annotations

from dataclasses import dataclass

import pandas as pd

from optionforge.common.enums import ConcentrationLevel


@dataclass(frozen=True, slots=True)
class OIConcentrationResult:
    """
    Immutable result object for OI Concentration analytics.
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

    def very_high(self) -> pd.DataFrame:

        return (
            self.df[
                self.df["CONCENTRATION"]
                == ConcentrationLevel.VERY_HIGH.value
            ]
            .copy()
            .reset_index(drop=True)
        )

    def high(self) -> pd.DataFrame:

        return (
            self.df[
                self.df["CONCENTRATION"]
                == ConcentrationLevel.HIGH.value
            ]
            .copy()
            .reset_index(drop=True)
        )

    def medium(self) -> pd.DataFrame:

        return (
            self.df[
                self.df["CONCENTRATION"]
                == ConcentrationLevel.MEDIUM.value
            ]
            .copy()
            .reset_index(drop=True)
        )

    def low(self) -> pd.DataFrame:

        return (
            self.df[
                self.df["CONCENTRATION"]
                == ConcentrationLevel.LOW.value
            ]
            .copy()
            .reset_index(drop=True)
        )

    def very_low(self) -> pd.DataFrame:

        return (
            self.df[
                self.df["CONCENTRATION"]
                == ConcentrationLevel.VERY_LOW.value
            ]
            .copy()
            .reset_index(drop=True)
        )

    # ==========================================================
    # Ranking
    # ==========================================================

    def top_concentration(
        self,
        n: int = 5,
    ) -> pd.DataFrame:

        return (
            self.df
            .nlargest(n, "OI_SHARE")
            .reset_index(drop=True)
        )

    # ==========================================================
    # Summary
    # ==========================================================

    def summary(self) -> dict[str, int]:

        counts = (
            self.df["CONCENTRATION"]
            .value_counts()
            .to_dict()
        )

        return {
            ConcentrationLevel.VERY_HIGH.value:
                counts.get(
                    ConcentrationLevel.VERY_HIGH.value,
                    0,
                ),

            ConcentrationLevel.HIGH.value:
                counts.get(
                    ConcentrationLevel.HIGH.value,
                    0,
                ),

            ConcentrationLevel.MEDIUM.value:
                counts.get(
                    ConcentrationLevel.MEDIUM.value,
                    0,
                ),

            ConcentrationLevel.LOW.value:
                counts.get(
                    ConcentrationLevel.LOW.value,
                    0,
                ),

            ConcentrationLevel.VERY_LOW.value:
                counts.get(
                    ConcentrationLevel.VERY_LOW.value,
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

            "highest_concentration":
                self.top_concentration(1)
                .iloc[0]["strike_price"],
        }

    # ==========================================================
    # Representation
    # ==========================================================

    def __repr__(self) -> str:

        return (
            "OIConcentrationResult("
            f"rows={len(self.df)})"
        )