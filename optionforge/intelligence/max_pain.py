"""
==============================================================
OptionForge
intelligence/max_pain.py
--------------------------------------------------------------
Professional Max Pain Engine
==============================================================
"""

from __future__ import annotations



from optionforge.models.max_pain_result import MaxPainResult
import pandas as pd

class MaxPain:

    @staticmethod
    def calculate(df: pd.DataFrame) -> MaxPainResult:

        strikes = sorted(df["STRIKE_PRICE"].unique())

        pain_rows = []

        for settlement in strikes:

            call_pain = 0.0
            put_pain = 0.0

            # -------------------------
            # Call Pain
            # -------------------------

            calls = df[df["OPTION_TYPE"] == "CE"]

            for _, row in calls.iterrows():

                if settlement > row["STRIKE_PRICE"]:

                    call_pain += (
                        settlement - row["STRIKE_PRICE"]
                    ) * row["OPEN_INTEREST"]       

            # -------------------------
            # Put Pain
            # -------------------------

            puts = df[df["OPTION_TYPE"] == "PE"]

            for _, row in puts.iterrows():

                if settlement < row["STRIKE_PRICE"]:

                    put_pain += (
                        row["STRIKE_PRICE"] - settlement
                    ) * row["OPEN_INTEREST"]

            total = call_pain + put_pain

            pain_rows.append(
                {
                    "STRIKE": settlement,
                    "CALL_PAIN": call_pain,
                    "PUT_PAIN": put_pain,
                    "TOTAL_PAIN": total,
                }
            )

        pain_table = pd.DataFrame(pain_rows)

        winner = pain_table.loc[
            pain_table["TOTAL_PAIN"].idxmin()
        ]

        # -----------------------------------
        # Highest OI Levels
        # -----------------------------------

        call_df = df[df["OPTION_TYPE"] == "CE"]

        put_df = df[df["OPTION_TYPE"] == "PE"]

        highest_call_oi = call_df.loc[
            call_df["OPEN_INTEREST"].idxmax(),
            "STRIKE_PRICE",
        ]

        highest_put_oi = put_df.loc[
            put_df["OPEN_INTEREST"].idxmax(),
            "STRIKE_PRICE",
        ]

        total_call_oi = int(call_df["OPEN_INTEREST"].sum())
        total_put_oi = int(put_df["OPEN_INTEREST"].sum())

        return MaxPainResult(

            max_pain=float(winner["STRIKE"]),

            total_pain=float(winner["TOTAL_PAIN"]),

            call_pain=float(winner["CALL_PAIN"]),

            put_pain=float(winner["PUT_PAIN"]),

            evaluated_strikes=len(strikes),

            support=float(highest_put_oi),

            resistance=float(highest_call_oi),

            highest_call_oi=float(highest_call_oi),

            highest_put_oi=float(highest_put_oi),

            total_call_oi=total_call_oi,

            total_put_oi=total_put_oi,

            pain_table=pain_table,

            interpretation=(
                "Maximum Pain is the strike where "
                "combined option writer payout is minimized."
            ),
        )
    