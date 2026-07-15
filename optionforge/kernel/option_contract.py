"""
optionforge.kernel.option_contract
==================================

Option Contract domain model.

Represents one immutable option contract.

An OptionContract belongs to one Strike and
is identified by its OptionType (CALL or PUT).

It intentionally contains NO market data.

Market information such as LTP, Bid, Ask,
Open Interest and Volume belong to the
MarketSnapshot model.

Engineering Principles
----------------------
- Immutable domain object
- One responsibility
- Identity only
- Financially correct
- Fully testable

Author
------
OptionForge Engineering Team
"""

from __future__ import annotations

from dataclasses import dataclass

from optionforge.common.enums import OptionType
from optionforge.kernel.expiry import Expiry
from optionforge.kernel.strike import Strike
from optionforge.kernel.symbol import Symbol


@dataclass(frozen=True, slots=True)
class OptionContract:
    """
    Represents one immutable option contract.
    """

    strike: Strike

    option_type: OptionType

    @property
    def symbol(self) -> Symbol:
        """
        Returns underlying symbol.
        """
        return self.strike.symbol

    @property
    def exchange(self):
        """
        Returns underlying exchange.
        """
        return self.symbol.exchange

    @property
    def expiry(self) -> Expiry:
        """
        Returns expiry.
        """
        return self.strike.expiry

    @property
    def strike_price(self) -> int:
        """
        Returns strike price.
        """
        return self.strike.strike_price

    @property
    def contract_id(self) -> str:
        """
        Returns globally unique contract identifier.

        Example
        -------
        NSE:NIFTY:20260702:25150:CE
        """

        return (
            f"{self.exchange.value}:"
            f"{self.symbol.ticker}:"
            f"{self.expiry.expiry_date:%Y%m%d}:"
            f"{self.strike_price}:"
            f"{self.option_type.short_name}"
        )

    @property
    def is_call(self) -> bool:
        """
        Returns True if Call option.
        """
        return self.option_type is OptionType.CALL

    @property
    def is_put(self) -> bool:
        """
        Returns True if Put option.
        """
        return self.option_type is OptionType.PUT

    def to_dict(self) -> dict:
        """
        Convert contract to dictionary.
        """

        return {
            "contract_id": self.contract_id,
            "symbol": self.symbol.ticker,
            "exchange": self.exchange.value,
            "expiry_date": self.expiry.expiry_date.isoformat(),
            "expiry_type": self.expiry.expiry_type.value,
            "strike_price": self.strike_price,
            "option_type": self.option_type.value,
        }

    def __str__(self) -> str:
        """
        Human-readable representation.
        """

        return (
            f"{self.symbol.ticker} "
            f"{self.expiry.expiry_date.isoformat()} "
            f"{self.strike_price} "
            f"{self.option_type.short_name}"
        )

    def __repr__(self) -> str:
        """
        Developer-friendly representation.
        """

        return (
            "OptionContract("
            f"symbol='{self.symbol.ticker}', "
            f"expiry_date={self.expiry.expiry_date.isoformat()}, "
            f"strike_price={self.strike_price}, "
            f"option_type={self.option_type.value})"
        )
