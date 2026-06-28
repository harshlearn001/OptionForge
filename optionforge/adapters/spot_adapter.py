"""
==============================================================
OptionForge
adapters/spot_adapter.py
--------------------------------------------------------------
Professional Spot Adapter
==============================================================
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd


class SpotAdapter:
    """
    MarketForge Spot Adapter

    Supports
    --------
    • Equity Spot
    • Index Spot

    Responsibilities
    ----------------
    • Load CSV
    • Standardize column names
    • Convert dates
    • Return clean DataFrame
    """

    # ------------------------------------------
    # Column Mapping
    # ------------------------------------------

    COLUMN_MAP = {

        "DATE": "TRADE_DATE",

        "TOTTRDQTY": "VOLUME",

        "TOTTRDVAL": "VALUE",

        "TOTALTRADES": "TRADES",

    }

    @staticmethod
    def convert(csv_file: str | Path) -> pd.DataFrame:

        csv_file = Path(csv_file)

        if not csv_file.exists():

            raise FileNotFoundError(csv_file)

        # ------------------------------------------
        # Read CSV
        # ------------------------------------------

        df = pd.read_csv(csv_file)

        # ------------------------------------------
        # Normalize Columns
        # ------------------------------------------

        df.columns = (
            df.columns
            .str.strip()
            .str.upper()
        )

        # ------------------------------------------
        # Rename
        # ------------------------------------------

        df = df.rename(
            columns=SpotAdapter.COLUMN_MAP
        )

        # ------------------------------------------
        # Convert Date
        # ------------------------------------------

        if "TRADE_DATE" in df.columns:

            if pd.api.types.is_integer_dtype(df["TRADE_DATE"]):

                df["TRADE_DATE"] = pd.to_datetime(

                    df["TRADE_DATE"].astype(str),

                    format="%Y%m%d"

                )

            else:

                df["TRADE_DATE"] = pd.to_datetime(

                    df["TRADE_DATE"]

                )

        # ------------------------------------------
        # Sort
        # ------------------------------------------

        if "TRADE_DATE" in df.columns:

            df = df.sort_values(

                "TRADE_DATE"

            ).reset_index(drop=True)

        return df