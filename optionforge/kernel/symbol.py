"""
=========================================================
OptionForge
Symbol
=========================================================

Represents an underlying trading instrument.

A Symbol is the underlying asset (Index, Equity, ETF, etc.).
It does NOT contain option chain, Greeks, IV or Open Interest.

Author : OptionForge
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Optional


class InstrumentType(Enum):
    """Supported underlying instrument types."""

    INDEX = "INDEX"
    EQUITY = "EQUITY"
    ETF = "ETF"


@dataclass(frozen=True, slots=True)
class Symbol:
    """
    Represents one underlying trading instrument.

    Parameters
    ----------
    name : str
        Trading symbol (e.g. NIFTY, RELIANCE).

    exchange : str
        Exchange name (e.g. NSE).

    instrument_type : InstrumentType
        Type of underlying.

    lot_size : int
        Exchange lot size.

    tick_size : float
        Minimum price movement.

    strike_interval : int
        Strike spacing for options.

    isin : str | None
        ISIN code (optional).

    sector : str | None
        Business sector (optional).
    """

    name: str
    exchange: str
    instrument_type: InstrumentType

    lot_size: int
    tick_size: float
    strike_interval: int

    isin: Optional[str] = None
    sector: Optional[str] = None

    def __post_init__(self) -> None:

        object.__setattr__(self, "name", self.name.upper().strip())
        object.__setattr__(self, "exchange", self.exchange.upper().strip())

        if not self.name:
            raise ValueError("Symbol name cannot be empty.")

        if not self.exchange:
            raise ValueError("Exchange cannot be empty.")

        if self.lot_size <= 0:
            raise ValueError("Lot size must be positive.")

        if self.tick_size <= 0:
            raise ValueError("Tick size must be positive.")

        if self.strike_interval <= 0:
            raise ValueError("Strike interval must be positive.")

    @property
    def symbol_id(self) -> str:
        """Unique symbol identifier."""
        return f"{self.exchange}:{self.name}"

    def is_index(self) -> bool:
        """Returns True if symbol is an index."""
        return self.instrument_type is InstrumentType.INDEX

    def is_equity(self) -> bool:
        """Returns True if symbol is an equity."""
        return self.instrument_type is InstrumentType.EQUITY

    def is_etf(self) -> bool:
        """Returns True if symbol is an ETF."""
        return self.instrument_type is InstrumentType.ETF

    def to_dict(self) -> dict:
        """Convert Symbol to dictionary."""

        return {
            "symbol_id": self.symbol_id,
            "name": self.name,
            "exchange": self.exchange,
            "instrument_type": self.instrument_type.value,
            "lot_size": self.lot_size,
            "tick_size": self.tick_size,
            "strike_interval": self.strike_interval,
            "isin": self.isin,
            "sector": self.sector,
        }

    def __str__(self) -> str:
        return self.symbol_id