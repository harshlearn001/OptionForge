"""
============================================================
OptionForge
Core Exceptions
============================================================
"""

from __future__ import annotations


class OptionForgeError(Exception):
    """Base exception for OptionForge."""


class ValidationError(OptionForgeError):
    """Input validation failed."""


class ProviderError(OptionForgeError):
    """Base provider exception."""


class ProviderExecutionError(ProviderError):
    """
    Raised when a provider fails during execution.
    """

    def __init__(
        self,
        provider: str,
        message: str,
    ) -> None:

        super().__init__(f"{provider}: {message}")

        self.provider = provider
        self.message = message


class DuplicateFeatureError(ProviderError):
    """
    Raised when multiple providers produce
    the same FeatureId.
    """


class MissingFeatureError(ProviderError):
    """
    Raised when a required feature
    is missing after registry build.
    """


class RegistryError(OptionForgeError):
    """Registry operation failed."""
