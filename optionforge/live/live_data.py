"""
==============================================================
OptionForge
live/live_data.py
--------------------------------------------------------------
Professional Live Data Loader
==============================================================
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd


class LiveData:
    """
    Professional Live Data Loader.

    Responsibilities
    ----------------
    1. Load today's option-chain CSV.
    2. Return a DataFrame.

    Future Versions
    ----------------
    - NSE Downloader
    - Broker APIs
    - Live Market Feed
    """

    @staticmethod
    def load(csv_file: str | Path) -> pd.DataFrame:

        csv_file = Path(csv_file)

        if not csv_file.exists():
            raise FileNotFoundError(
                f"Live data file not found: {csv_file}"
            )

        return pd.read_csv(csv_file)