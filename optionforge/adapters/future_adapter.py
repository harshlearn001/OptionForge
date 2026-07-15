"""
==============================================================
OptionForge
adapters/future_adapter.py
--------------------------------------------------------------
Professional Future Adapter
==============================================================
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd


class FutureAdapter:
    """
    Professional Future Adapter

    Supports
    --------
    • FUTIDX
    • FUTSTK

    Responsibilities
    ----------------
    • Load MarketForge Futures
    • Normalize columns
    • Convert dates
    • Return standardized dataframe
    """

    COLUMN_MAP = {
        "EXP_DATE": "EXPIRY",
        "OPEN_PRICE": "OPEN",
        "HI_PRICE": "HIGH",
        "LO_PRICE": "LOW",
        "CLOSE_PRICE": "CLOSE",
        "OPEN_INT": "OI",
        "TRD_QTY": "VOLUME",
        "TRD_VAL": "VALUE",
        "NO_OF_CONT": "CONTRACTS",
        "NO_OF_TRADE": "TRADES",
    }

    FINAL_COLUMNS = [
        "TRADE_DATE",
        "SYMBOL",
        "INSTRUMENT",
        "EXPIRY",
        "EXPIRY_TYPE",
        "OPEN",
        "HIGH",
        "LOW",
        "CLOSE",
        "OI",
        "VOLUME",
        "VALUE",
        "CONTRACTS",
        "TRADES",
    ]

    @staticmethod
    def convert(csv_file: str | Path) -> pd.DataFrame:

        csv_file = Path(csv_file)

        if not csv_file.exists():

            raise FileNotFoundError(csv_file)

        # ---------------------------------------------
        # Read
        # ---------------------------------------------

        df = pd.read_csv(csv_file)

        # ---------------------------------------------
        # Normalize Columns
        # ---------------------------------------------

        df.columns = df.columns.str.strip().str.upper()

        # ---------------------------------------------
        # Rename
        # ---------------------------------------------

        df = df.rename(columns=FutureAdapter.COLUMN_MAP)

        # ---------------------------------------------
        # Convert Dates
        # ---------------------------------------------

        if "TRADE_DATE" in df.columns:

            df["TRADE_DATE"] = pd.to_datetime(
                df["TRADE_DATE"].astype(str), format="%Y%m%d"
            )

        if "EXPIRY" in df.columns:

            df["EXPIRY"] = pd.to_datetime(df["EXPIRY"].astype(str), format="%Y%m%d")

        # ---------------------------------------------
        # Sort
        # ---------------------------------------------

        df = df.sort_values("TRADE_DATE").reset_index(drop=True)

        # ---------------------------------------------
        # Column Order
        # ---------------------------------------------

        df = df[FutureAdapter.FINAL_COLUMNS]

        return df
