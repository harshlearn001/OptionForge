"""
==============================================================
OptionForge
datasource/market_data.py
--------------------------------------------------------------
Professional Market Data Loader
==============================================================
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd


class MarketData:
    """
    Professional Market Data Loader
    """

    @staticmethod
    def from_csv(file_path: str | Path) -> pd.DataFrame:
        """
        Load option chain data from a CSV file.
        """

        file_path = Path(file_path)

        if not file_path.exists():
            raise FileNotFoundError(
                f"CSV file not found: {file_path}"
            )

        # Read CSV
        df = pd.read_csv(
            file_path,
            encoding="utf-8-sig",
        )

        # Normalize column names
        df.columns = (
            df.columns
            .str.replace("\ufeff", "", regex=False)
            .str.strip()
            .str.upper()
        )

        

        return df