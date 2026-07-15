"""
optionforge.kernel.strike
=========================

Strike domain model.

A Strike represents one strike level belonging to
an Expiry.

It contains only strike identity and metadata.

It does NOT contain option contracts, Greeks,
implied volatility, pricing or market data.

Engineering Principles
----------------------
- Immutable domain object
- One responsibility
- Strong validation
- Financially correct
- Fully testable

Author
------
OptionForge Engineering Team
"""

from __future__ import annotations

from dataclasses import dataclass

from optionforge.common.exceptions import InvalidStrikeError
from optionforge.kernel.expiry import Expiry
from optionforge.kernel.symbol import Symbol


@dataclass(frozen=True, slots=True)
class Strike:
    """
    Represents one strike level.
    """

    expiry: Expiry

    strike_price: int

    def __post_init__(self) -> None:
        """
        Validate Strike.
        """

        if self.strike_price <= 0:
            raise InvalidStrikeError("Strike price must be positive.")

    @property
    def symbol(self) -> Symbol:
        """
        Returns the underlying Symbol.
        """

        return self.expiry.symbol

    @property
    def strike_id(self) -> str:
        """
        Returns a unique strike identifier.

        Example
        -------
        NIFTY_20260702_25150
        """

        return (
            f"{self.symbol.ticker}_"
            f"{self.expiry.expiry_date:%Y%m%d}_"
            f"{self.strike_price}"
        )

    def to_dict(self) -> dict:
        """
        Convert Strike to a serializable dictionary.
        """

        return {
            "strike_id": self.strike_id,
            "symbol": self.symbol.ticker,
            "exchange": self.symbol.exchange.value,
            "expiry_date": self.expiry.expiry_date.isoformat(),
            "expiry_type": self.expiry.expiry_type.value,
            "strike_price": self.strike_price,
        }

    def __str__(self) -> str:
        """
        Human-readable representation.
        """

        return (
            f"{self.symbol.ticker} "
            f"{self.expiry.expiry_date.isoformat()} "
            f"{self.strike_price}"
        )

    def __repr__(self) -> str:
        """
        Developer-friendly representation.
        """

        return (
            "Strike("
            f"symbol='{self.symbol.ticker}', "
            f"expiry_date={self.expiry.expiry_date.isoformat()}, "
            f"strike_price={self.strike_price})"
        )
