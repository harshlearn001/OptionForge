"""
============================================================
OptionForge
Repository Exception
============================================================

Author      : OptionForge
Module      : repository_exception.py
Purpose     : Repository-specific exceptions.

============================================================
"""

from __future__ import annotations


class RepositoryError(Exception):
    """
    Base repository exception.
    """


class RepositoryNotFoundError(RepositoryError):
    """
    Raised when a requested market dataset
    cannot be located.
    """


class RepositoryValidationError(RepositoryError):
    """
    Raised when repository validation fails.
    """


class RepositoryConfigurationError(RepositoryError):
    """
    Raised when repository configuration
    is invalid.
    """