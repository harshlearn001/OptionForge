"""
============================================================
OptionForge
MarketForge Loader
============================================================

Author      : OptionForge
Module      : marketforge_loader.py

Purpose
-------
Loads a MarketForge CSV and validates it before it enters
OptionForge.

============================================================
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from optionforge.integration.csv_validator import CSVValidator


class MarketForgeLoader:
    """
    Loads MarketForge CSV files.
    """

    def __init__(self):

        self.validator = CSVValidator()

    def load(
        self,
        filepath: str | Path,
    ) -> pd.DataFrame:
        """
        Load and validate MarketForge CSV.
        """

        filepath = Path(filepath)

        if not filepath.exists():

            raise FileNotFoundError(filepath)

        dataframe = pd.read_csv(filepath)

        self.validator.validate(dataframe)

        return dataframe

    def __repr__(self):

        return "MarketForgeLoader()"

    __str__ = __repr__