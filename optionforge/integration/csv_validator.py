"""
============================================================
OptionForge
CSV Validator
============================================================

Author      : OptionForge
Module      : csv_validator.py

Purpose
-------
Validates MarketForge CSV before integration.

============================================================
"""

from __future__ import annotations

import pandas as pd

from optionforge.integration.schema import (
    REQUIRED_COLUMNS,
    NUMERIC_COLUMNS,
)

from optionforge.integration.exceptions import (
    EmptyCSVError,
    MissingColumnError,
    DuplicateRowError,
    InvalidDataTypeError,
)


class CSVValidator:
    """
    Validates MarketForge CSV files.
    """

    def validate(
        self,
        dataframe: pd.DataFrame,
    ) -> bool:
        """
        Validate dataframe.
        """

        if dataframe.empty:
            raise EmptyCSVError("CSV contains no rows.")

        missing = [
            column for column in REQUIRED_COLUMNS if column not in dataframe.columns
        ]

        if missing:

            raise MissingColumnError(f"Missing columns: {missing}")

        duplicates = dataframe.duplicated().sum()

        if duplicates:

            raise DuplicateRowError(f"{duplicates} duplicate rows found.")

        for column in NUMERIC_COLUMNS:

            if not pd.api.types.is_numeric_dtype(dataframe[column]):

                raise InvalidDataTypeError(f"{column} must be numeric.")

        return True

    def __repr__(self):

        return "CSVValidator()"

    __str__ = __repr__
