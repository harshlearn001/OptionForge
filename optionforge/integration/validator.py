"""
============================================================
OptionForge
Market Validator
============================================================

Author      : OptionForge
Module      : validator.py

Purpose
-------
Validate all MarketForge DataFrames before they
enter the OptionForge Integration Layer.

Responsibilities
----------------
✓ Required columns
✓ Empty DataFrames
✓ Duplicate columns
✓ Missing values
✓ Numeric datatypes
✓ Date columns
✓ Schema integrity

This module NEVER reads files.

============================================================
"""

from __future__ import annotations

from typing import Iterable

import pandas as pd
from pandas.api.types import (
    is_datetime64_any_dtype,
    is_numeric_dtype,
)

from .exceptions import (
    EmptyDataFrameError,
    MissingColumnError,
    DuplicateColumnError,
    InvalidColumnTypeError,
    MissingValueError,
)

from optionforge.contracts.option_contract import OPTION_COLUMNS
from optionforge.contracts.spot_contract import (
    INDEX_SPOT_COLUMNS,
    EQUITY_SPOT_COLUMNS,
)
from optionforge.contracts.future_contract import FUTURE_COLUMNS
from optionforge.contracts.delivery_contract import DELIVERY_COLUMNS


class MarketValidator:
    """
    Production Market Validator.

    All MarketForge data must pass through
    this validator before entering OptionForge.
    """

    # ======================================================
    # Public API
    # ======================================================

    def validate_option(
        self,
        df: pd.DataFrame,
    ) -> None:

        self._validate_dataframe(df)

        self._validate_required_columns(
            df,
            OPTION_COLUMNS,
        )

    # ------------------------------------------------------

    def validate_index_spot(
        self,
        df: pd.DataFrame,
    ) -> None:

        self._validate_dataframe(df)

        self._validate_required_columns(
            df,
            INDEX_SPOT_COLUMNS,
        )

    # ------------------------------------------------------

    def validate_equity_spot(
        self,
        df: pd.DataFrame,
    ) -> None:

        self._validate_dataframe(df)

        self._validate_required_columns(
            df,
            EQUITY_SPOT_COLUMNS,
        )

    # ------------------------------------------------------

    def validate_future(
        self,
        df: pd.DataFrame,
    ) -> None:

        self._validate_dataframe(df)

        self._validate_required_columns(
            df,
            FUTURE_COLUMNS,
        )

    # ------------------------------------------------------

    def validate_delivery(
        self,
        df: pd.DataFrame,
    ) -> None:

        self._validate_dataframe(df)

        self._validate_required_columns(
            df,
            DELIVERY_COLUMNS,
        )

    # ======================================================
    # Core Validation
    # ======================================================

    def _validate_dataframe(
        self,
        df: pd.DataFrame,
    ) -> None:

        self._validate_empty_dataframe(df)

        self._validate_duplicate_columns(df)

    # ------------------------------------------------------

    def _validate_required_columns(
        self,
        df: pd.DataFrame,
        required_columns: Iterable[str],
    ) -> None:

        missing = [
            column
            for column in required_columns
            if column not in df.columns
        ]

        if missing:

            raise MissingColumnError(
                "Missing required columns:\n"
                + "\n".join(missing)
            )
        # ------------------------------------------------------

    @staticmethod
    def _validate_empty_dataframe(
        df: pd.DataFrame,
    ) -> None:
        """
        Ensure DataFrame contains data.
        """

        if df.empty:
            raise EmptyDataFrameError(
                "The DataFrame contains no rows."
            )

    # ------------------------------------------------------

    @staticmethod
    def _validate_duplicate_columns(
        df: pd.DataFrame,
    ) -> None:
        """
        Detect duplicate column names.
        """

        duplicates = df.columns[df.columns.duplicated()]

        if len(duplicates):

            duplicate_names = "\n".join(
                duplicates.astype(str)
            )

            raise DuplicateColumnError(
                "Duplicate columns detected:\n"
                f"{duplicate_names}"
            )

    # ------------------------------------------------------

    @staticmethod
    def _validate_missing_values(
        df: pd.DataFrame,
        columns: Iterable[str],
    ) -> None:
        """
        Validate required columns contain no missing values.
        """

        invalid = []

        for column in columns:

            if df[column].isna().any():

                invalid.append(column)

        if invalid:

            raise MissingValueError(
                "Missing values detected:\n"
                + "\n".join(invalid)
            )

    # ------------------------------------------------------

    @staticmethod
    def _validate_numeric_columns(
        df: pd.DataFrame,
        columns: Iterable[str],
    ) -> None:
        """
        Validate numeric columns.
        """

        invalid = []

        for column in columns:

            if not is_numeric_dtype(df[column]):

                invalid.append(column)

        if invalid:

            raise InvalidColumnTypeError(
                "Expected numeric columns:\n"
                + "\n".join(invalid)
            )

    # ------------------------------------------------------

    @staticmethod
    def _validate_datetime_columns(
        df: pd.DataFrame,
        columns: Iterable[str],
    ) -> None:
        """
        Validate datetime columns.

        Integer date formats
        (example: 20240125)
        are accepted.
        """

        invalid = []

        for column in columns:

            if is_datetime64_any_dtype(df[column]):
                continue

            try:

                pd.to_datetime(
                    df[column],
                    errors="raise",
                )

            except Exception:

                invalid.append(column)

        if invalid:

            raise InvalidColumnTypeError(
                "Invalid datetime columns:\n"
                + "\n".join(invalid)
            )

    # ------------------------------------------------------

    @staticmethod
    def validation_report(
        df: pd.DataFrame,
    ) -> dict:
        """
        Return a validation summary.
        """

        return {

            "rows": len(df),

            "columns": len(df.columns),

            "memory_mb": round(

                df.memory_usage(
                    deep=True,
                ).sum()
                / 1024**2,

                2,

            ),

            "missing_values": int(

                df.isna().sum().sum()

            ),

            "duplicate_rows": int(

                df.duplicated().sum()

            ),

        }

    # ------------------------------------------------------

    @classmethod
    def print_report(
        cls,
        df: pd.DataFrame,
    ) -> None:
        """
        Print validation summary.
        """

        report = cls.validation_report(df)

        print("=" * 60)
        print("OPTIONFORGE VALIDATION REPORT")
        print("=" * 60)

        for key, value in report.items():

            print(f"{key:<20}: {value}")

        print("=" * 60)

    # ------------------------------------------------------

    def __repr__(self) -> str:

        return (
            f"{self.__class__.__name__}()"
        )