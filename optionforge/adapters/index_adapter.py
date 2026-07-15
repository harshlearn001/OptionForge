"""
==============================================================
OptionForge
Index Adapter
--------------------------------------------------------------
Professional Market Index Adapter
==============================================================
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd


class IndexAdapter:
    """
    Converts MarketForge Index data into
    OptionForge Standard Format.
    """

    COLUMN_MAPPING = {
        "TRADE_DATE": "TRADE_DATE",
        "SYMBOL": "SYMBOL",
        "OPEN": "OPEN",
        "HIGH": "HIGH",
        "LOW": "LOW",
        "CLOSE": "CLOSE",
    }

    COLUMN_ORDER = [
        "TRADE_DATE",
        "SYMBOL",
        "OPEN",
        "HIGH",
        "LOW",
        "CLOSE",
    ]

    @classmethod
    def convert(cls, csv_file: str | Path) -> pd.DataFrame:

        df = pd.read_csv(csv_file)

        # -----------------------------
        # Rename columns
        # -----------------------------

        df = df.rename(columns=cls.COLUMN_MAPPING)

        # -----------------------------
        # Date
        # -----------------------------

        df["TRADE_DATE"] = pd.to_datetime(df["TRADE_DATE"].astype(str), format="%Y%m%d")

        # -----------------------------
        # String columns
        # -----------------------------

        df["SYMBOL"] = df["SYMBOL"].astype("string")

        # -----------------------------
        # Float columns
        # -----------------------------

        float_cols = [
            "OPEN",
            "HIGH",
            "LOW",
            "CLOSE",
        ]

        for col in float_cols:
            df[col] = df[col].astype(float)

        # -----------------------------
        # Final Order
        # -----------------------------

        df = df[cls.COLUMN_ORDER]

        return df
