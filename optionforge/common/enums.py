"""
optionforge.common.enums
========================

Centralized enumerations used throughout the OptionForge framework.

This module defines the shared financial enumerations used across
OptionForge. Keeping them in one location ensures consistency,
type safety, readability, and prevents duplicate definitions.

Engineering Principles
----------------------
- One source of truth
- Explicit over implicit
- Strong typing
- No business logic

Author
------
OptionForge Engineering Team
"""

from __future__ import annotations

from enum import Enum, unique

@unique
class Exchange(str, Enum):
    """Supported stock exchanges."""

    NSE = "NSE"
    BSE = "BSE"

    def __str__(self) -> str:
        return self.value


@unique
class InstrumentType(str, Enum):
    """Supported financial instrument types."""

    EQUITY = "EQUITY"
    INDEX = "INDEX"
    FUTURE = "FUTURE"
    OPTION = "OPTION"

    def __str__(self) -> str:
        return self.value


@unique
class OptionType(str, Enum):
    """Option contract type."""

    CALL = "CALL"
    PUT = "PUT"

    def __str__(self) -> str:
        return self.value

    @property
    def short_name(self) -> str:
        """Return the exchange abbreviation."""
        return "CE" if self is OptionType.CALL else "PE"


@unique
class ExpiryType(str, Enum):
    """Expiry classification."""

    WEEKLY = "WEEKLY"
    MONTHLY = "MONTHLY"

    def __str__(self) -> str:
        return self.value


@unique
class MarketStatus(str, Enum):
    """Trading session status."""

    PRE_OPEN = "PRE_OPEN"
    OPEN = "OPEN"
    CLOSED = "CLOSED"
    POST_CLOSE = "POST_CLOSE"
    HOLIDAY = "HOLIDAY"

    def __str__(self) -> str:
        return self.value

@unique
class BuildUp(str, Enum):
    """Open Interest build-up classification."""

    LONG_BUILDUP = "LONG_BUILDUP"
    SHORT_BUILDUP = "SHORT_BUILDUP"
    SHORT_COVERING = "SHORT_COVERING"
    LONG_UNWINDING = "LONG_UNWINDING"
    NEUTRAL = "NEUTRAL"

    def __str__(self) -> str:
        return self.value

@unique
class WallType(str, Enum):
    """
    OI Wall classification.
    """

    CALL_WALL = "CALL_WALL"

    PUT_WALL = "PUT_WALL"

    BALANCED = "BALANCED"

    def __str__(self) -> str:
        return self.value  

__all__ = [
    "Exchange",
    "InstrumentType",
    "OptionType",
    "ExpiryType",
    "MarketStatus",
    "BuildUp",
    "WallType",
]

