"""
==============================================================
OptionForge
storage/reader.py
--------------------------------------------------------------
Historical Storage Reader
==============================================================
"""

from pathlib import Path

import pandas as pd


class StorageReader:

    @staticmethod
    def load(path: str) -> pd.DataFrame:

        return pd.read_parquet(Path(path))
