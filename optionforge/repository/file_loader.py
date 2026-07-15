"""
============================================================
OptionForge
Repository
File Loader
============================================================

Author      : OptionForge
Module      : file_loader.py
Purpose     : Centralized file loading utility.

Responsibilities
----------------
- Read CSV files
- Read Parquet files
- Validate supported formats

Contains NO business logic.

============================================================
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from optionforge.repository.repository_exception import (
    RepositoryValidationError,
)


class FileLoader:
    """
    Centralized repository file loader.
    """

    _SUPPORTED = {
        ".csv": pd.read_csv,
        ".parquet": pd.read_parquet,
    }

    @classmethod
    def load(
        cls,
        path: str | Path,
    ) -> pd.DataFrame:
        """
        Load a dataset based on file extension.
        """

        path = Path(path)

        suffix = path.suffix.lower()

        reader = cls._SUPPORTED.get(suffix)

        if reader is None:

            raise RepositoryValidationError(f"Unsupported file format: {suffix}")

        return reader(path)

    @classmethod
    def supported_formats(
        cls,
    ) -> tuple[str, ...]:
        """
        Return supported file formats.
        """

        return tuple(cls._SUPPORTED.keys())
