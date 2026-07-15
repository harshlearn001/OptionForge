"""
============================================================
OptionForge
Modified PCR Engine
============================================================

Author      : OptionForge
Module      : modified_pcr.py

Purpose
-------
Calculate the basic Put-Call Ratio (PCR) from an
InstitutionalSnapshot.

This is Version 1 of the engine. More advanced weighted
and institutional PCR calculations will be added later.

============================================================
"""

from __future__ import annotations

from dataclasses import dataclass

from optionforge.analytics.base_engine import AnalyticsEngine
from optionforge.snapshot.institutional_snapshot import (
    InstitutionalSnapshot,
)


@dataclass(frozen=True)
class ModifiedPCRResult:
    """
    Result returned by ModifiedPCREngine.
    """

    symbol: str

    trade_date: object

    expiry: object

    call_oi: float

    put_oi: float

    pcr: float

    contracts: int


class ModifiedPCREngine(AnalyticsEngine):
    """
    Version-1 Modified PCR Engine.
    """

    def calculate(
        self,
        snapshot: InstitutionalSnapshot,
    ) -> ModifiedPCRResult:

        df = snapshot.option_chain

        call_oi = float(
            df.loc[
                df["OPT_TYPE"] == "CE",
                "OPEN_INT",
            ].sum()
        )

        put_oi = float(
            df.loc[
                df["OPT_TYPE"] == "PE",
                "OPEN_INT",
            ].sum()
        )

        if call_oi == 0:
            pcr = 0.0
        else:
            pcr = round(
                put_oi / call_oi,
                4,
            )

        return ModifiedPCRResult(
            symbol=snapshot.symbol,
            trade_date=snapshot.trade_date,
            expiry=snapshot.expiry,
            call_oi=call_oi,
            put_oi=put_oi,
            pcr=pcr,
            contracts=len(df),
        )
