"""
==============================================================
OptionForge
analytics/max_pain/engine.py
--------------------------------------------------------------
Professional Max Pain Engine
==============================================================
"""

from __future__ import annotations

import pandas as pd

from optionforge.market.option_chain import OptionChain
from optionforge.models.max_pain_result import MaxPainResult
from optionforge.optionchain.filters import ChainFilters

class MaxPainEngine:
    """
    Professional Max Pain Engine.
    """

    @staticmethod
    def calculate(
        chain: OptionChain,
    ) -> MaxPainResult:
        """
        Calculate Maximum Pain.
        """

        calls = ChainFilters.calls(chain)
        puts = ChainFilters.puts(chain)

        strikes = sorted(
            {
                snapshot.contract.strike_price
                for snapshot in chain
            }
        )

        pain_rows: list[
            tuple[
                float,
                float,
                float,
                float,
            ]
        ] = []

        for settlement in strikes:

            call_pain = 0.0
            put_pain = 0.0

            # ----------------------------------
            # Call Pain
            # ----------------------------------

            for snapshot in calls:

                strike = snapshot.contract.strike_price
                oi = snapshot.open_interest

                if settlement > strike:

                    call_pain += (
                        settlement - strike
                    ) * oi

            # ----------------------------------
            # Put Pain
            # ----------------------------------

            for snapshot in puts:

                strike = snapshot.contract.strike_price
                oi = snapshot.open_interest

                if settlement < strike:

                    put_pain += (
                        strike - settlement
                    ) * oi

            # ----------------------------------
            # Total Pain
            # ----------------------------------

            total_pain = (
                call_pain +
                put_pain
            )

            pain_rows.append(
                (
                    settlement,
                    call_pain,
                    put_pain,
                    total_pain,
                )
            )

        # Remaining migration:
        #   • Find minimum total pain
        #   • Calculate highest OI levels
        #   • Populate MaxPainResult
        winner = min(
            pain_rows,
            key=lambda row: row[3],  # total_pain
        )

        max_pain = winner[0]
        call_pain = winner[1]
        put_pain = winner[2]
        total_pain = winner[3]
        highest_call = max(
            calls,
            key=lambda snapshot: snapshot.open_interest,
        )

        highest_put = max(
            puts,
            key=lambda snapshot: snapshot.open_interest,
        )

        total_call_oi = sum(
            snapshot.open_interest
            for snapshot in calls
        )

        total_put_oi = sum(
            snapshot.open_interest
            for snapshot in puts
        )

        pain_table = pd.DataFrame(
            pain_rows,
            columns=[
                "STRIKE",
                "CALL_PAIN",
                "PUT_PAIN",
                "TOTAL_PAIN",
            ],
        )

        total_put_oi = sum(
            snapshot.open_interest
            for snapshot in puts
        )

        pain_table = pd.DataFrame(
    pain_rows,
    columns=[
        "STRIKE",
        "CALL_PAIN",
        "PUT_PAIN",
        "TOTAL_PAIN",
    ],
)
        return MaxPainResult(

            max_pain=float(max_pain),

            total_pain=float(total_pain),

            call_pain=float(call_pain),

            put_pain=float(put_pain),

            evaluated_strikes=len(strikes),

            support=float(
                highest_put.contract.strike_price
            ),

            resistance=float(
                highest_call.contract.strike_price
            ),

            highest_call_oi=float(
                highest_call.contract.strike_price
            ),

            highest_put_oi=float(
                highest_put.contract.strike_price
            ),

            total_call_oi=int(total_call_oi),

            total_put_oi=int(total_put_oi),

            pain_table=pain_table,

            interpretation=(
                "Maximum Pain is the strike where "
                "combined option writer payout is minimized."
            ),
        )