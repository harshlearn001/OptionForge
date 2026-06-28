"""
==============================================================
OptionForge
NSE Adapter
--------------------------------------------------------------
Converts NSE Option Chain data into the
OptionForge Standard Schema
==============================================================
"""

from __future__ import annotations

import pandas as pd


class NSEAdapter:
    """
    Converts NSE Option Chain columns into
    the OptionForge Standard Schema.
    """

    COLUMN_MAPPING = {

        # Symbol
        "SYMBOL": "SYMBOL",
        "SYM": "SYMBOL",

        # Expiry
        "EXPIRY": "EXPIRY",
        "EXPIRY DATE": "EXPIRY",
        "EXPIRY_DATE": "EXPIRY",

        # Strike
        "STRIKE": "STRIKE",
        "STRIKE PRICE": "STRIKE",
        "STRIKE_PRICE": "STRIKE",

        # Option Type
        "OPTION_TYPE": "OPTION_TYPE",
        "OPTION TYPE": "OPTION_TYPE",

        # Price
        "LTP": "LTP",
        "LAST_PRICE": "LTP",
        "OPTION_CLOSE": "LTP",

        # IV
        "IV": "IV",
        "IMPLIED_VOLATILITY": "IV",

        # OI
        "OI": "OI",
        "OPEN_INTEREST": "OI",

        # Change in OI
        "CHANGE_IN_OI": "CHANGE_IN_OI",
        "CHANGE IN OI": "CHANGE_IN_OI",

        # Volume
        "VOLUME": "VOLUME",
        "OPTION_VOLUME": "VOLUME",

        # Spot
        "SPOT": "SPOT",
        "SPOT_CLOSE": "SPOT",
    }
    @classmethod
    def convert(cls, dataframe: pd.DataFrame) -> pd.DataFrame:
        """
        Convert NSE dataframe to OptionForge schema.
        """

        dataframe = dataframe.rename(columns=cls.COLUMN_MAPPING)

        return dataframe