"""
============================================================
OptionForge
Repository Exceptions
============================================================

Author      : OptionForge
Module      : repository_exception.py

Purpose
-------
Repository layer exceptions.

These exceptions are raised only by the Repository
package and should never contain business logic.

============================================================
"""

from __future__ import annotations


class RepositoryError(Exception):
    """
    Base class for all repository errors.
    """

    pass


# ==========================================================
# Repository Configuration
# ==========================================================

class RepositoryConfigurationError(RepositoryError):
    """
    Repository configuration is invalid.
    """

    pass


# ==========================================================
# File Errors
# ==========================================================

class RepositoryFileNotFoundError(RepositoryError):
    """
    Repository file could not be located.
    """

    pass


class UnsupportedFileFormatError(RepositoryError):
    """
    Unsupported repository file format.
    """

    pass


# ==========================================================
# Data Errors
# ==========================================================

class RepositoryValidationError(RepositoryError):
    """
    Repository validation failed.
    """

    pass


class EmptyRepositoryDataError(RepositoryError):
    """
    Repository returned an empty DataFrame.
    """

    pass


# ==========================================================
# Cache Errors
# ==========================================================

class RepositoryNotFoundError(RepositoryError):
    """
    Repository file or symbol could not be located.
    """

    pass


# ==========================================================
# Symbol Errors
# ==========================================================

class UnknownSymbolError(RepositoryError):
    """
    Symbol does not exist in repository.
    """

    pass


# ==========================================================
# Data Type Errors
# ==========================================================

class UnsupportedRepositoryTypeError(RepositoryError):
    """
    Unknown repository data type.
    """

    pass
class RepositoryCacheError(RepositoryError):
    """
    Repository cache failure.
    """

    pass