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

from optionforge.storage.schema import REQUIRED_COLUMNS


class StorageWriter:

    @staticmethod
    def save_daily_chain(
        dataframe: pd.DataFrame,
        folder: str,
        filename: str,
    ) -> Path:

        missing = [
            c
            for c in REQUIRED_COLUMNS
            if c not in dataframe.columns
        ]

        if missing:
            raise ValueError(
                f"Missing columns : {missing}"
            )

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