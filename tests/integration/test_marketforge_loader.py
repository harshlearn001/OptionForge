"""
============================================================
OptionForge
MarketForgeLoader Tests
============================================================
"""


import pandas as pd
import pytest

from optionforge.integration.marketforge_loader import (
    MarketForgeLoader,
)

from optionforge.integration.schema import (
    REQUIRED_COLUMNS,
)


def loader():

    return MarketForgeLoader()


def create_csv(tmp_path):

    data = {}

    for column in REQUIRED_COLUMNS:

        if column == "Date":

            data[column] = ["2026-07-01"]

        elif column == "Symbol":

            data[column] = ["NIFTY"]

        else:

            data[column] = [1.0]

    df = pd.DataFrame(data)

    file = tmp_path / "marketforge.csv"

    df.to_csv(file, index=False)

    return file


# ==========================================================
# Construction
# ==========================================================


def test_create():

    assert isinstance(
        loader(),
        MarketForgeLoader,
    )


# ==========================================================
# Load
# ==========================================================


def test_load(tmp_path):

    file = create_csv(tmp_path)

    df = loader().load(file)

    assert len(df) == 1


def test_columns(tmp_path):

    file = create_csv(tmp_path)

    df = loader().load(file)

    assert "Symbol" in df.columns


def test_missing_file():

    with pytest.raises(FileNotFoundError):

        loader().load("does_not_exist.csv")


# ==========================================================
# Representation
# ==========================================================


def test_repr():

    assert "MarketForgeLoader" in repr(
        loader(),
    )


def test_str():

    assert "MarketForgeLoader" in str(
        loader(),
    )
