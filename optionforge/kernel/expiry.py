"""
=========================================================
OptionForge
Expiry
=========================================================

Represents one option expiry for an underlying symbol.

An Expiry belongs to exactly one Symbol and contains
metadata about the expiry. It does NOT contain option
contracts directly.

Author : OptionForge
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from enum import Enum


class ExpiryType(Enum):
    """Supported expiry types."""

    WEEKLY = "WEEKLY"
    MONTHLY = "MONTHLY"


@dataclass(frozen=True, slots=True)
class Expiry:
    """
    Represents one option expiry.

    Parameters
    ----------
    expiry_date : date
        Expiry date.

    expiry_type : ExpiryType
        Weekly or Monthly expiry.

    trading_date : date
        Current trading date.

    symbol : str
        Underlying symbol.
    """

    symbol: str
    trading_date: date
    expiry_date: date
    expiry_type: ExpiryType

    def __post_init__(self) -> None:

        object.__setattr__(self, "symbol", self.symbol.upper().strip())

        if not self.symbol:
            raise ValueError("Symbol cannot be empty.")

        if self.expiry_date < self.trading_date:
            raise ValueError(
                "Expiry date cannot be before trading date."
            )

    @property
    def dte(self) -> int:
        """
        Days to Expiry.
        """
        return (self.expiry_date - self.trading_date).days

    @property
    def is_expiry_day(self) -> bool:
        """
        Returns True if trading date equals expiry date.
        """
        return self.trading_date == self.expiry_date

    @property
    def is_weekly(self) -> bool:
        return self.expiry_type is ExpiryType.WEEKLY

    @property
    def is_monthly(self) -> bool:
        return self.expiry_type is ExpiryType.MONTHLY

    @property
    def expiry_id(self) -> str:
        """
        Unique expiry identifier.
        """
        return (
            f"{self.symbol}_"
            f"{self.expiry_date:%Y%m%d}_"
            f"{self.expiry_type.value}"
        )

    def to_dict(self) -> dict:
        """
        Convert Expiry to dictionary.
        """
        return {
            "expiry_id": self.expiry_id,
            "symbol": self.symbol,
            "trading_date": self.trading_date.isoformat(),
            "expiry_date": self.expiry_date.isoformat(),
            "expiry_type": self.expiry_type.value,
            "dte": self.dte,
            "is_expiry_day": self.is_expiry_day,
        }

    def __str__(self) -> str:
        return (
            f"{self.symbol} "
            f"{self.expiry_date.isoformat()} "
            f"[{self.expiry_type.value}]"
        )