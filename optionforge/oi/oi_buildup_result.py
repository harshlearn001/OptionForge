"""
==============================================================
OptionForge
OI Build-up Result
--------------------------------------------------------------
Immutable result object for OI Build-up analytics.
==============================================================
"""

from __future__ import annotations

from dataclasses import dataclass

import pandas as pd

from optionforge.common.enums import BuildUp


@dataclass(frozen=True, slots=True)
class OIBuildupResult:
    """
    Immutable result of the OI Build-up Engine.
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

    def long_buildup(self) -> pd.DataFrame:

        return (
            self.df[
                self.df["BUILDUP"] == BuildUp.LONG_BUILDUP.value
            ]
            .copy()
            .reset_index(drop=True)
        )

    def short_buildup(self) -> pd.DataFrame:

        return (
            self.df[
                self.df["BUILDUP"] == BuildUp.SHORT_BUILDUP.value
            ]
            .copy()
            .reset_index(drop=True)
        )

    def short_covering(self) -> pd.DataFrame:

        return (
            self.df[
                self.df["BUILDUP"] == BuildUp.SHORT_COVERING.value
            ]
            .copy()
            .reset_index(drop=True)
        )

    def long_unwinding(self) -> pd.DataFrame:

        return (
            self.df[
                self.df["BUILDUP"] == BuildUp.LONG_UNWINDING.value
            ]
            .copy()
            .reset_index(drop=True)
        )

    def neutral(self) -> pd.DataFrame:

        return (
            self.df[
                self.df["BUILDUP"] == BuildUp.NEUTRAL.value
            ]
            .copy()
            .reset_index(drop=True)
        )

    # ==========================================================
    # Summary
    # ==========================================================

    def summary(self) -> dict[str, int]:
        """
        Build-up counts.
        """

        counts = (
            self.df["BUILDUP"]
            .value_counts()
            .to_dict()
        )

        return {
            BuildUp.LONG_BUILDUP.value:
                counts.get(BuildUp.LONG_BUILDUP.value, 0),

            BuildUp.SHORT_BUILDUP.value:
                counts.get(BuildUp.SHORT_BUILDUP.value, 0),

            BuildUp.SHORT_COVERING.value:
                counts.get(BuildUp.SHORT_COVERING.value, 0),

            BuildUp.LONG_UNWINDING.value:
                counts.get(BuildUp.LONG_UNWINDING.value, 0),

            BuildUp.NEUTRAL.value:
                counts.get(BuildUp.NEUTRAL.value, 0),
        }

    # ==========================================================
    # Dictionary
    # ==========================================================

    def to_dict(self) -> dict:

        return {
            "summary": self.summary(),
            "rows": len(self.df),
        }

    # ==========================================================
    # Representation
    # ==========================================================

    def __repr__(self) -> str:

        s = self.summary()

        return (
            "OIBuildupResult("
            f"rows={len(self.df)}, "
            f"LONG={s[BuildUp.LONG_BUILDUP.value]}, "
            f"SHORT={s[BuildUp.SHORT_BUILDUP.value]}, "
            f"COVERING={s[BuildUp.SHORT_COVERING.value]}, "
            f"UNWINDING={s[BuildUp.LONG_UNWINDING.value]}, "
            f"NEUTRAL={s[BuildUp.NEUTRAL.value]})"
        )