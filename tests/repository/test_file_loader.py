"""
============================================================
OptionForge
File Loader Tests
============================================================
"""

from pathlib import Path

import pandas as pd

import pytest

from optionforge.repository import (
    FileLoader,
)

from optionforge.repository.repository_exception import (
    RepositoryValidationError,
)


# ==========================================================
# CSV
# ==========================================================

def test_load_csv(tmp_path):

    file = tmp_path / "demo.csv"

    pd.DataFrame(

        {

            "A": [1, 2],

            "B": [3, 4],

        }

    ).to_csv(

        file,

        index=False,

    )

    df = FileLoader.load(file)

    assert isinstance(df, pd.DataFrame)

    assert len(df) == 2


# ==========================================================
# Parquet
# ==========================================================

def test_load_parquet(tmp_path):

    file = tmp_path / "demo.parquet"

    pd.DataFrame(

        {

            "A": [10],

            "B": [20],

        }

    ).to_parquet(file)

    df = FileLoader.load(file)

    assert isinstance(df, pd.DataFrame)

    assert df.iloc[0]["A"] == 10


# ==========================================================
# Unsupported
# ==========================================================

def test_invalid_extension(tmp_path):

    file = tmp_path / "demo.xyz"

    file.write_text("test")

    with pytest.raises(

        RepositoryValidationError,

    ):

        FileLoader.load(file)


# ==========================================================
# Supported Formats
# ==========================================================

def test_supported_formats():

    formats = FileLoader.supported_formats()

    assert ".csv" in formats

    assert ".parquet" in formats


# ==========================================================
# Path Object
# ==========================================================

def test_accepts_path_object(tmp_path):

    file = Path(tmp_path / "sample.csv")

    pd.DataFrame(

        {

            "X": [5],

        }

    ).to_csv(

        file,

        index=False,

    )

    df = FileLoader.load(file)

    assert len(df) == 1