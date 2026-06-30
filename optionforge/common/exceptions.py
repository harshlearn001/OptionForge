"""
optionforge.common.exceptions
=============================

Custom exception hierarchy for the OptionForge framework.

Every exception raised by OptionForge should inherit from
OptionForgeError. This provides a single base class that users
can catch when handling framework-specific errors.

Engineering Principles
----------------------
- One root exception
- Clear hierarchy
- Meaningful names
- No business logic

Author
------
OptionForge Engineering Team
"""

from __future__ import annotations

__all__ = [
    "OptionForgeError",
    "ValidationError",
    "InvalidSymbolError",
    "InvalidExpiryError",
    "InvalidStrikeError",
    "InvalidContractError",
    "MarketError",
    "MarketClosedError",
    "InvalidTradingSessionError",
    "PricingError",
]


class OptionForgeError(Exception):
    """Base exception for the OptionForge framework."""


# ---------------------------------------------------------------------
# Validation Errors
# ---------------------------------------------------------------------


class ValidationError(OptionForgeError):
    """Base class for validation-related exceptions."""


class InvalidSymbolError(ValidationError):
    """Raised when a symbol is invalid."""


class InvalidExpiryError(ValidationError):
    """Raised when an expiry is invalid."""


class InvalidStrikeError(ValidationError):
    """Raised when a strike price is invalid."""


class InvalidContractError(ValidationError):
    """Raised when an option contract is invalid."""


# ---------------------------------------------------------------------
# Market Errors
# ---------------------------------------------------------------------


class MarketError(OptionForgeError):
    """Base class for market-related exceptions."""


class MarketClosedError(MarketError):
    """Raised when an operation requires an open market."""


class InvalidTradingSessionError(MarketError):
    """Raised when the trading session is invalid."""


# ---------------------------------------------------------------------
# Pricing Errors
# ---------------------------------------------------------------------


class PricingError(OptionForgeError):
    """Raised when an option pricing calculation fails."""