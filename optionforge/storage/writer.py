"""
==============================================================
OptionForge
storage/writer.py
--------------------------------------------------------------
Historical Storage Writer
==============================================================
"""

from pathlib import Path

import pandas as pd

from optionforge.storage.schema import OptionChainSchema


class StorageWriter:

    @staticmethod
    def save_daily_chain(
        dataframe,
        folder,
        filename,
    ):

        # ---------------------------------------------
        # Convert Legacy Names
        # ---------------------------------------------

        COLUMN_MAPPING = {
            "EXPIRY_DATE": "EXPIRY",
            "STRIKE_PRICE": "STRIKE",
            "OPTION_CLOSE": "LTP",
            "SPOT_CLOSE": "SPOT",
            "OPEN_INTEREST": "OI",
            "OPTION_VOLUME": "VOLUME",
        }

        dataframe = dataframe.rename(columns=COLUMN_MAPPING)

        # ---------------------------------------------
        # Validate Schema
        # ---------------------------------------------

        valid, missing = OptionChainSchema.validate(dataframe.columns)

        if not valid:
            raise ValueError(f"Missing columns : {missing}")

        ...
        missing = [
            c for c in OptionChainSchema.REQUIRED_COLUMNS if c not in dataframe.columns
        ]

        if missing:
            raise ValueError(f"Missing columns : {missing}")

        output_folder = Path(folder)

        output_folder.mkdir(
            parents=True,
            exist_ok=True,
        )

        output_file = output_folder / filename

        dataframe.to_parquet(
            output_file,
            index=False,
        )

        return output_file
