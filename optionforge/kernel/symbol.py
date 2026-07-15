"""
optionforge.kernel.symbol
=========================

Symbol domain model.

A Symbol represents one tradable underlying instrument
such as an Index, Equity or Future.

It contains only identity and contract specification.
It does NOT contain option chain, Greeks, volatility,
pricing, or market data.

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

from optionforge.common.enums import (
    Exchange,
    InstrumentType,
)
from optionforge.common.exceptions import (
    InvalidSymbolError,
)
from optionforge.kernel.trading_session import (
    TradingSession,
)


@dataclass(frozen=True, slots=True)
class Symbol:
    """
    Represents one tradable underlying instrument.

    Parameters
    ----------
    ticker
        Trading symbol.
        Example:
            NIFTY
            BANKNIFTY
            RELIANCE

    exchange
        Exchange where instrument trades.

    instrument_type
        Type of financial instrument.

    lot_size
        Exchange lot size.

    tick_size
        Minimum price movement.

    strike_interval
        Standard option strike spacing.

    trading_session
        Trading session associated with the symbol.

    isin
        Optional ISIN code.

    sector
        Optional business sector.
    """

    ticker: str

    exchange: Exchange

    instrument_type: InstrumentType

    lot_size: int

    tick_size: float

    strike_interval: int

    trading_session: TradingSession

    isin: str | None = None

    sector: str | None = None

    def __post_init__(self) -> None:
        """
        Validate Symbol.
        """

        object.__setattr__(
            self,
            "ticker",
            self.ticker.strip().upper(),
        )

        if not self.ticker:
            raise InvalidSymbolError("Ticker cannot be empty.")

        if self.lot_size <= 0:
            raise InvalidSymbolError("Lot size must be positive.")

        if self.tick_size <= 0:
            raise InvalidSymbolError("Tick size must be positive.")

        if self.strike_interval <= 0:
            raise InvalidSymbolError("Strike interval must be positive.")

    @property
    def symbol_id(self) -> str:
        """
        Returns a unique symbol identifier.

        Example
        -------
        NSE:NIFTY
        """
        return f"{self.exchange}:{self.ticker}"

    @property
    def is_index(self) -> bool:
        """
        Returns True if this symbol represents an index.
        """
        return self.instrument_type is InstrumentType.INDEX

    @property
    def is_equity(self) -> bool:
        """
        Returns True if this symbol represents an equity.
        """
        return self.instrument_type is InstrumentType.EQUITY

    @property
    def is_future(self) -> bool:
        """
        Returns True if this symbol represents a futures contract.
        """
        return self.instrument_type is InstrumentType.FUTURE

    @property
    def is_option(self) -> bool:
        """
        Returns True if this symbol represents an option.
        """
        return self.instrument_type is InstrumentType.OPTION

    def to_dict(self) -> dict:
        """
        Convert Symbol to a serializable dictionary.
        """

        return {
            "symbol_id": self.symbol_id,
            "ticker": self.ticker,
            "exchange": self.exchange.value,
            "instrument_type": self.instrument_type.value,
            "lot_size": self.lot_size,
            "tick_size": self.tick_size,
            "strike_interval": self.strike_interval,
            "isin": self.isin,
            "sector": self.sector,
        }

    def __str__(self) -> str:
        """
        Human-readable representation.
        """
        return self.symbol_id

    def __repr__(self) -> str:
        """
        Developer-friendly representation.
        """
        return (
            "Symbol("
            f"ticker='{self.ticker}', "
            f"exchange={self.exchange.value}, "
            f"instrument_type={self.instrument_type.value})"
        )
