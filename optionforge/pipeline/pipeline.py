"""
==============================================================
OptionForge
pipeline/pipeline.py
--------------------------------------------------------------
Professional Pipeline Engine
==============================================================
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from optionforge.datasource import MarketData
from optionforge.storage.schema import OptionChainSchema


class OptionForgePipeline:
    """
    Professional OptionForge Pipeline

    Responsibilities
    ----------------
    1. Load Market Data
    2. Validate Schema
    3. Return Standardized DataFrame

    Future Versions

    v1.0
        Analytics

    v1.1
        Intelligence

    v1.2
        Strategy

    v1.3
        Scanner

    v1.4
        Dashboard

    v1.5
        Report
    """

    @staticmethod
    def run(csv_file: str | Path) -> pd.DataFrame:

        # --------------------------------------------------
        # Load Market Data
        # --------------------------------------------------

        dataframe = MarketData.from_csv(csv_file)

        # --------------------------------------------------
        # Validate Schema
        # --------------------------------------------------

        valid, missing = OptionChainSchema.validate(list(dataframe.columns))

        if not valid:

            raise ValueError(f"Missing required columns: {missing}")

        # --------------------------------------------------
        # Future Pipeline Stages
        # --------------------------------------------------

        return dataframe
