"""
============================================================
OptionForge
IntegrationResult Tests
============================================================
"""

from optionforge.integration.integration_result import (
    IntegrationResult,
)


def result():

    return IntegrationResult(
        success=True,
        filepath="marketforge.csv",
        rows=500,
        columns=42,
        warnings=(),
        errors=(),
    )


# ==========================================================
# Construction
# ==========================================================


def test_create():

    assert isinstance(
        result(),
        IntegrationResult,
    )


# ==========================================================
# Stored Values
# ==========================================================


def test_success():

    assert result().success


def test_filepath():

    assert result().filepath == "marketforge.csv"


def test_rows():

    assert result().rows == 500


def test_columns():

    assert result().columns == 42


# ==========================================================
# Properties
# ==========================================================


def test_warning_count():

    assert result().warning_count == 0


def test_error_count():

    assert result().error_count == 0


def test_has_warnings():

    assert not result().has_warnings


def test_has_errors():

    assert not result().has_errors


def test_is_valid():

    assert result().is_valid


# ==========================================================
# Dictionary
# ==========================================================


def test_to_dict():

    data = result().to_dict()

    assert data["success"]

    assert data["rows"] == 500

    assert data["columns"] == 42


# ==========================================================
# Representation
# ==========================================================


def test_repr():

    assert "IntegrationResult" in repr(
        result(),
    )


def test_str():

    assert "IntegrationResult" in str(
        result(),
    )
