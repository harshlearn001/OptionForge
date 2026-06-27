"""
==============================================================
OptionForge
intelligence/oi_wall.py
--------------------------------------------------------------
Open Interest Wall Intelligence Engine
==============================================================
"""

from __future__ import annotations

import pandas as pd

from optionforge.models import OIWallResult


class OIWall:
    """
    Open Interest Wall Analysis
    """

    @staticmethod
    def calculate(df: pd.DataFrame) -> OIWallResult:

        required = {
            "STRIKE_PRICE",
            "OPTION_TYPE",
            "OPEN_INTEREST",
        }

        missing = required - set(df.columns)

        if missing:
            raise ValueError(
                f"Missing columns: {missing}"
            )

        # ----------------------------------------
        # Separate Calls and Puts
        # ----------------------------------------

        calls = df[df["OPTION_TYPE"] == "CE"]

        puts = df[df["OPTION_TYPE"] == "PE"]

        # ----------------------------------------
        # Highest Call OI
        # ----------------------------------------

        call_row = calls.loc[
            calls["OPEN_INTEREST"].idxmax()
        ]

        resistance = float(call_row["STRIKE_PRICE"])

        resistance_oi = int(call_row["OPEN_INTEREST"])

        # ----------------------------------------
        # Highest Put OI
        # ----------------------------------------

        put_row = puts.loc[
            puts["OPEN_INTEREST"].idxmax()
        ]

        support = float(put_row["STRIKE_PRICE"])

        support_oi = int(put_row["OPEN_INTEREST"])

        # ----------------------------------------
        # Totals
        # ----------------------------------------

        total_call_oi = int(
            calls["OPEN_INTEREST"].sum()
        )

        total_put_oi = int(
            puts["OPEN_INTEREST"].sum()
        )

        if total_call_oi == 0:
            pcr = 0.0
        else:
            pcr = total_put_oi / total_call_oi

        # ----------------------------------------
        # Market Bias
        # ----------------------------------------

        if pcr > 1.20:
            bias = "Bullish"

        elif pcr < 0.80:
            bias = "Bearish"

        else:
            bias = "Neutral"

        # ----------------------------------------
        # Interpretation
        # ----------------------------------------

        interpretation = (
            f"Support near {support:.0f}, "
            f"Resistance near {resistance:.0f}. "
            f"PCR = {pcr:.2f}. "
            f"Overall market bias: {bias}."
        )

        return OIWallResult(

            strongest_support=support,

            strongest_resistance=resistance,

            support_oi=support_oi,

            resistance_oi=resistance_oi,

            total_put_oi=total_put_oi,

            total_call_oi=total_call_oi,

            put_call_ratio=round(pcr, 3),

            market_bias=bias,

            interpretation=interpretation,

        )