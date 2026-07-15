"""
============================================================
OptionForge
CSVValidator Tests
============================================================
"""

import pandas as pd
import pytest

from optionforge.integration.csv_validator import (
    CSVValidator,
)

from optionforge.integration.schema import (
    REQUIRED_COLUMNS,
)

from optionforge.integration.exceptions import (
    EmptyCSVError,
    MissingColumnError,
    DuplicateRowError,
    InvalidDataTypeError,
)


def validator():

    return CSVValidator()


def dataframe():

    data = {}

    for column in REQUIRED_COLUMNS:

        if column == "Date":

            data[column] = ["2026-07-01"]

        elif column == "Symbol":

            data[column] = ["NIFTY"]

        else:

            data[column] = [1.0]

    return pd.DataFrame(data)


# ==========================================================
# Construction
# ==========================================================


def test_create():

    assert isinstance(
        validator(),
        CSVValidator,
    )


# ==========================================================
# Valid
# ==========================================================


def test_valid():

    assert validator().validate(dataframe())


# ==========================================================
# Empty
# ==========================================================


def test_empty():

    with pytest.raises(EmptyCSVError):

        validator().validate(pd.DataFrame())


# ==========================================================
# Missing Column
# ==========================================================


def test_missing_column():

    df = dataframe().drop(columns=["PCR"])

    with pytest.raises(MissingColumnError):

        validator().validate(df)


# ==========================================================
# Duplicate Row
# ==========================================================


def test_duplicate():

    df = pd.concat(
        [
            dataframe(),
            dataframe(),
        ],
        ignore_index=True,
    )

    with pytest.raises(DuplicateRowError):

        validator().validate(df)


# ==========================================================
# Invalid Numeric
# ==========================================================


def test_invalid_numeric():

    df = dataframe()

    df["Spot"] = ["ABC"]

    with pytest.raises(InvalidDataTypeError):

        validator().validate(df)


# ==========================================================
# Representation
# ==========================================================


def test_repr():

    assert "CSVValidator" in repr(
        validator(),
    )


def test_str():

    assert "CSVValidator" in str(
        validator(),
    )
