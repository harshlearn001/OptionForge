"""
==============================================================
OptionForge
datasource/market_data.py
--------------------------------------------------------------
Professional Market Data Loader
==============================================================
"""

from __future__ import annotations

import pandas as pd
from pathlib import Path


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

        return pd.read_csv(file_path)