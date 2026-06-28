"""
==============================================================
OptionForge
workflow/workflow.py
--------------------------------------------------------------
Professional Workflow Engine
==============================================================
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from optionforge.datasource import MarketData
from optionforge.adapters import NSEAdapter
from optionforge.pipeline import OptionForgePipeline


class WorkflowEngine:
    """
    Professional Workflow Engine

    Responsibilities
    ----------------
    1. Load market data
    2. Standardize schema
    3. Execute pipeline

    Future Versions
    ----------------
    - Analytics
    - Intelligence
    - Strategy
    - Scanner
    - Dashboard
    - Report
    """

    @staticmethod
    def run(csv_file: str | Path) -> pd.DataFrame:

        # --------------------------------------------------
        # Load raw market data
        # --------------------------------------------------

        dataframe = MarketData.from_csv(csv_file)

        # --------------------------------------------------
        # Standardize schema
        # --------------------------------------------------

        dataframe = NSEAdapter.convert(dataframe)

        # --------------------------------------------------
        # Save temporary standardized data
        # --------------------------------------------------

        temp_file = Path("output") / "workflow_input.csv"
        temp_file.parent.mkdir(parents=True, exist_ok=True)

        dataframe.to_csv(temp_file, index=False)

        # --------------------------------------------------
        # Execute pipeline
        # --------------------------------------------------

        result = OptionForgePipeline.run(temp_file)

        return result