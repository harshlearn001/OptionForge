"""
============================================================
OptionForge
Integration Exceptions
============================================================

Author      : OptionForge
Module      : exceptions.py

Purpose
-------
Custom exceptions used throughout the OptionForge
Integration Layer.

Shared by:

    • FileResolver
    • MarketValidator
    • MarketRepository
    • MarketProvider
    • SnapshotBuilder

============================================================
"""

from __future__ import annotations


# ============================================================
# Base Exceptions
# ============================================================

class IntegrationError(Exception):
    """
    Base exception for the Integration Layer.
    """
    pass


# ============================================================
# Repository Exceptions
# ============================================================

class RepositoryError(IntegrationError):
    """
    Base repository exception.
    """
    pass


class RepositoryNotConfiguredError(RepositoryError):
    """
    Raised when an optional repository
    has not been configured.
    """
    pass


class RepositoryNotFoundError(RepositoryError):
    """
    Raised when a repository directory
    does not exist.
    """
    pass


class FileNotFoundInRepository(RepositoryError):
    """
    Raised when a symbol file cannot
    be located inside the repository.
    """
    pass


class UnsupportedFileFormatError(RepositoryError):
    """
    Raised when the repository contains
    an unsupported file extension.
    """
    pass


# ============================================================
# Validation Exceptions
# ============================================================

class ValidationError(IntegrationError):
    """
    Base validation exception.
    """
    pass


class InvalidCSVError(ValidationError):
    """
    Raised when the CSV/Parquet file
    cannot be validated.
    """
    pass


class EmptyDataFrameError(ValidationError):
    """
    Raised when a DataFrame contains
    zero rows.
    """
    pass


class MissingColumnError(ValidationError):
    """
    Raised when one or more required
    columns are missing.
    """
    pass


class DuplicateColumnError(ValidationError):
    """
    Raised when duplicate column names
    are detected.
    """
    pass


class DuplicateRowError(ValidationError):
    """
    Raised when duplicate rows
    are detected.
    """
    pass


class InvalidColumnTypeError(ValidationError):
    """
    Raised when a column has an
    unexpected datatype.
    """
    pass


class MissingValueError(ValidationError):
    """
    Raised when required columns
    contain missing values.
    """
    pass


class InvalidDateColumnError(ValidationError):
    """
    Raised when a date column
    cannot be parsed.
    """
    pass


class UnsupportedSchemaError(ValidationError):
    """
    Raised when the MarketForge
    schema is unsupported.
    """
    pass


# ============================================================
# Snapshot Exceptions
# ============================================================

class SnapshotError(IntegrationError):
    """
    Base snapshot exception.
    """
    pass


class SnapshotBuildError(SnapshotError):
    """
    Raised when an InstitutionalSnapshot
    cannot be created.
    """
    pass


class SpotDataNotFoundError(SnapshotError):
    """
    Raised when spot history
    is unavailable.
    """
    pass


class OptionDataNotFoundError(SnapshotError):
    """
    Raised when option history
    is unavailable.
    """
    pass


class ExpiryNotFoundError(SnapshotError):
    """
    Raised when expiry cannot
    be determined.
    """
    pass


class ATMStrikeNotFoundError(SnapshotError):
    """
    Raised when the ATM strike
    cannot be determined.
    """
    pass


# ============================================================
# Provider Exceptions
# ============================================================

class ProviderError(IntegrationError):
    """
    Base provider exception.
    """
    pass


class InvalidTradeDateError(ProviderError):
    """
    Raised when an invalid trade date
    is requested.
    """
    pass


class InvalidSymbolError(ProviderError):
    """
    Raised when an unknown symbol
    is requested.
    """
    pass
# ============================================================
# Backward Compatibility
# ============================================================

# Old names kept for existing modules

EmptyCSVError = EmptyDataFrameError

InvalidDataTypeError = InvalidColumnTypeError