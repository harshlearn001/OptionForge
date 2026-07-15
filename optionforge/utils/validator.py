"""
OptionForge
engine/validator.py
"""

import pandas as pd


class Validator:

    REQUIRED_COLUMNS = [
        "TRADE_DATE",
        "SYMBOL",
        "EXPIRY_DATE",
        "STRIKE_PRICE",
        "OPTION_TYPE",
        "SPOT_CLOSE",
        "FUTURE_CLOSE",
        "OPTION_CLOSE",
        "OPEN_INTEREST",
        "CHANGE_IN_OI",
        "OPTION_VOLUME",
    ]

    @classmethod
    def validate(cls, df: pd.DataFrame):

        missing = []

        for col in cls.REQUIRED_COLUMNS:

            if col not in df.columns:
                missing.append(col)

        if missing:
            raise ValueError(f"Missing Columns : {missing}")

        if df.empty:
            raise ValueError("Empty DataFrame.")

        return True
