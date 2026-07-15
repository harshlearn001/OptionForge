"""
==============================================================
OptionForge
OI Trend Engine
--------------------------------------------------------------
Institutional OI Trend Analytics Engine.

Computes trend score across multiple OIByStrike snapshots.

Returns an immutable OITrendResult.
==============================================================
"""

from __future__ import annotations

import pandas as pd

from optionforge.oi.oi_by_strike import OIByStrike
from optionforge.oi.oi_trend_result import OITrendResult
from optionforge.oi.trend_classifier import TrendClassifier


class OITrendEngine:
    """
    Institutional OI Trend Engine.
    """

    def __init__(
        self,
        history: tuple[OIByStrike, ...],
    ) -> None:

        if len(history) < 2:
            raise ValueError(
                "Trend engine requires at least two snapshots."
            )

        self.history = history

    # ==========================================================
    # Calculate
    # ==========================================================

    def calculate(
        self,
    ) -> OITrendResult:

        first = (
            self.history[0]
            .dataframe()[["strike_price", "OI_SHARE"]]
            .rename(
                columns={
                    "OI_SHARE": "FIRST_OI_SHARE",
                }
            )
        )

        last = (
            self.history[-1]
            .dataframe()
            .copy()
        )

        df = pd.merge(
            last,
            first,
            on="strike_price",
            how="left",
        )

        df["FIRST_OI_SHARE"] = (
            df["FIRST_OI_SHARE"]
            .fillna(0.0)
        )

        df["TREND_SCORE"] = (
            df["OI_SHARE"]
            - df["FIRST_OI_SHARE"]
        )

        df["TREND"] = (
            df["TREND_SCORE"]
            .apply(
                lambda x:
                TrendClassifier.classify(x).value
            )
        )

        return OITrendResult(df)

    # ==========================================================
    # Representation
    # ==========================================================

    def __repr__(self) -> str:

        return (
            "OITrendEngine("
            f"history={len(self.history)})"
        )