"""
optionforge.common.enums
========================

Centralized enumerations used throughout the OptionForge framework.

This module contains all shared enumerations that define the financial
language of the project. Keeping them in one location ensures consistency,
type safety, readability, and prevents duplicate definitions across modules.

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

from enum import Enum


class Exchange(str, Enum):
    """
    Supported exchanges.

    Attributes
    ----------
    NSE
        National Stock Exchange of India.

    BSE
        Bombay Stock Exchange.
    """

    NSE = "NSE"
    BSE = "BSE"


class InstrumentType(str, Enum):
    """
    Supported financial instrument types.
    """

    EQUITY = "EQUITY"
    INDEX = "INDEX"
    FUTURE = "FUTURE"
    OPTION = "OPTION"


class OptionType(str, Enum):
    """
    Option contract type.
    """

    CALL = "CALL"
    PUT = "PUT"

    @property
    def short_name(self) -> str:
        """Return exchange representation."""
        return "CE" if self is OptionType.CALL else "PE"


class ExpiryType(str, Enum):
    """
    Expiry classification.
    """

    WEEKLY = "WEEKLY"
    MONTHLY = "MONTHLY"


class MarketStatus(str, Enum):
    """
    Trading session status.
    """

    PRE_OPEN = "PRE_OPEN"
    OPEN = "OPEN"
    CLOSED = "CLOSED"
    POST_CLOSE = "POST_CLOSE"
    HOLIDAY = "HOLIDAY"