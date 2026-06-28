"""
==============================================================
OptionForge
session/market_session.py
--------------------------------------------------------------
Professional Market Session
==============================================================
"""

from __future__ import annotations

from pathlib import Path
import pandas as pd

from optionforge.workflow import WorkflowEngine


class MarketSession:
    """
    Professional Market Session

    Responsibilities
    ----------------
    1. Load market data
    2. Execute workflow
    3. Return standardized dataframe

    Future Versions
    ----------------
    Analytics
    Strategy
    Scanner
    Dashboard
    Report
    """

    @staticmethod
    def run(csv_file: str | Path) -> pd.DataFrame:

        dataframe = WorkflowEngine.run(csv_file)

        return dataframe