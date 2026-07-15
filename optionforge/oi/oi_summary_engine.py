"""
==============================================================
OptionForge
Institutional OI Summary Engine
==============================================================
"""

from __future__ import annotations

from optionforge.oi.oi_by_strike import OIByStrike
from optionforge.oi.oi_summary_result import OISummaryResult


class OISummaryEngine:
    """
    Institutional Open Interest Summary.

    Produces a high-level summary of an option chain using the
    OIByStrike master analytics table.
    """

    @staticmethod
    def calculate(
        oi: OIByStrike,
    ) -> OISummaryResult:

        df = oi.dataframe()

        call_oi = int(df["CALL_OI"].sum())
        put_oi = int(df["PUT_OI"].sum())

        total_oi = call_oi + put_oi

        call_volume = int(df["CALL_VOLUME"].sum())
        put_volume = int(df["PUT_VOLUME"].sum())

        total_volume = call_volume + put_volume

        call_share = call_oi / total_oi if total_oi > 0 else 0.0

        put_share = put_oi / total_oi if total_oi > 0 else 0.0

        pcr = put_oi / call_oi if call_oi > 0 else 0.0

        if put_oi > call_oi:
            dominant = "PUT"

        elif call_oi > put_oi:
            dominant = "CALL"

        else:
            dominant = "BALANCED"

        return OISummaryResult(
            call_oi=call_oi,
            put_oi=put_oi,
            total_oi=total_oi,
            call_volume=call_volume,
            put_volume=put_volume,
            total_volume=total_volume,
            call_share=round(call_share, 4),
            put_share=round(put_share, 4),
            pcr=round(pcr, 4),
            strikes=len(df),
            dominant_side=dominant,
        )
