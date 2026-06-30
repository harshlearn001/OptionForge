"""
optionforge.kernel.expiry
=========================

Expiry domain model.

An Expiry represents one option expiry belonging to a Symbol.

It contains expiry metadata only.
It does NOT contain strikes, contracts, Greeks,
volatility, pricing or option chain data.

Engineering Principles
----------------------
- Immutable domain object
- One responsibility
- Financially correct
- Fully testable

Author
------
OptionForge Engineering Team
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date

from optionforge.common.enums import ExpiryType
from optionforge.common.exceptions import InvalidExpiryError
from optionforge.kernel.symbol import Symbol


@dataclass(frozen=True, slots=True)
class Expiry:
    """
    Represents one option expiry for one Symbol.
    """

    symbol: Symbol

    expiry_date: date

    expiry_type: ExpiryType

    def __post_init__(self) -> None:
        """
        Validate Expiry.
        """

        if self.expiry_date < self.symbol.trading_session.trading_date:
            raise InvalidExpiryError(
                "Expiry date cannot be before trading date."
            )

    @property
    def expiry_id(self) -> str:
        """
        Returns unique expiry identifier.
        """

        return (
            f"{self.symbol.ticker}_"
            f"{self.expiry_date:%Y%m%d}_"
            f"{self.expiry_type.value}"
        )

    @property
    def is_weekly(self) -> bool:
        """
        Returns True if expiry is weekly.
        """
        return self.expiry_type is ExpiryType.WEEKLY

    @property
    def is_monthly(self) -> bool:
        """
        Returns True if expiry is monthly.
        """
        return self.expiry_type is ExpiryType.MONTHLY

    def days_to_expiry(
        self,
        reference_date: date,
    ) -> int:
        """
        Returns days to expiry.
        """

        return (
            self.expiry_date -
            reference_date
        ).days

    def is_expired(
        self,
        reference_date: date,
    ) -> bool:
        """
        Returns True if already expired.
        """

        return reference_date > self.expiry_date
    
    
    def is_expiry_day(
        self,
        reference_date: date,
    ) -> bool:
        """
        Returns True if the supplied reference date
        is the expiry date.
        """

        return reference_date == self.expiry_date

    def to_dict(self) -> dict:
        """
        Convert Expiry to a serializable dictionary.
        """

        return {
            "expiry_id": self.expiry_id,
            "symbol": self.symbol.ticker,
            "exchange": self.symbol.exchange.value,
            "instrument_type": self.symbol.instrument_type.value,
            "expiry_date": self.expiry_date.isoformat(),
            "expiry_type": self.expiry_type.value,
            "days_to_expiry": self.days_to_expiry(
                self.symbol.trading_session.trading_date
            ),
            "is_weekly": self.is_weekly,
            "is_monthly": self.is_monthly,
            "is_expiry_day": self.is_expiry_day(
        self.symbol.trading_session.trading_date
            ),
        }

    def __str__(self) -> str:
        """
        Human-readable representation.
        """

        return (
            f"{self.symbol.ticker} "
            f"{self.expiry_date.isoformat()} "
            f"[{self.expiry_type.value}]"
        )

    def __repr__(self) -> str:
        """
        Developer-friendly representation.
        """

        return (
            "Expiry("
            f"symbol='{self.symbol.ticker}', "
            f"expiry_date={self.expiry_date.isoformat()}, "
            f"expiry_type={self.expiry_type.value})"
        )