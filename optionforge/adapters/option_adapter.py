"""
==============================================================
OptionForge
Option Adapter
--------------------------------------------------------------
Professional Market Option Adapter
==============================================================
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd


class OptionAdapter:
    """
    Converts MarketForge Option data into
    OptionForge Standard Format.

    Supports
    --------
    • Index Options
    • Stock Options
    • Weekly Expiry
    • Monthly Expiry
    """

    COLUMN_MAPPING = {
        "TRADE_DATE": "TRADE_DATE",
        "EXP_DATE": "EXPIRY",
        "SYMBOL": "SYMBOL",
        "INSTRUMENT": "INSTRUMENT",
        "STRIKE_PRICE": "STRIKE",
        "OPT_TYPE": "OPT_TYPE",
        "OPEN_PRICE": "OPEN",
        "HI_PRICE": "HIGH",
        "LO_PRICE": "LOW",
        "CLOSE_PRICE": "CLOSE",
        "OPEN_INT": "OI",
        "TRD_QTY": "VOLUME",
        "NO_OF_CONT": "CONTRACTS",
        "NO_OF_TRADE": "TRADES",
        "NOTION_VAL": "NOTIONAL_VALUE",
        "PR_VAL": "PREMIUM_VALUE",
    }

    COLUMN_ORDER = [
        "TRADE_DATE",
        "EXPIRY",
        "SYMBOL",
        "INSTRUMENT",
        "STRIKE",
        "OPT_TYPE",
        "OPEN",
        "HIGH",
        "LOW",
        "CLOSE",
        "OI",
        "VOLUME",
        "CONTRACTS",
        "TRADES",
        "NOTIONAL_VALUE",
        "PREMIUM_VALUE",
    ]

    @classmethod
    def convert(cls, parquet_file: str | Path) -> pd.DataFrame:

        df = pd.read_parquet(parquet_file)

        # ----------------------------------
        # Rename columns
        # ----------------------------------

        df = df.rename(columns=cls.COLUMN_MAPPING)

        # ----------------------------------
        # Date columns
        # ----------------------------------

        df["TRADE_DATE"] = pd.to_datetime(df["TRADE_DATE"].astype(str), format="%Y%m%d")

        df["EXPIRY"] = pd.to_datetime(df["EXPIRY"].astype(str), format="%Y%m%d")

        # ----------------------------------
        # String columns
        # ----------------------------------

        string_cols = [
            "SYMBOL",
            "INSTRUMENT",
            "OPT_TYPE",
        ]

        for col in string_cols:
            df[col] = df[col].astype("string")

        # ----------------------------------
        # Float columns
        # ----------------------------------

        float_cols = [
            "OPEN",
            "HIGH",
            "LOW",
            "CLOSE",
            "PREMIUM_VALUE",
        ]

        for col in float_cols:
            df[col] = df[col].astype(float)

        # ----------------------------------
        # Integer columns
        # ----------------------------------

        int_cols = [
            "STRIKE",
            "OI",
            "VOLUME",
            "CONTRACTS",
            "TRADES",
            "NOTIONAL_VALUE",
        ]

        for col in int_cols:
            df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0).astype("int64")

        # ----------------------------------
        # Final order
        # ----------------------------------

        df = df[cls.COLUMN_ORDER]

        # ----------------------------------
        # Sort
        # ----------------------------------

        df = df.sort_values(
            [
                "TRADE_DATE",
                "EXPIRY",
                "STRIKE",
                "OPT_TYPE",
            ]
        ).reset_index(drop=True)

        return df
