"""
optionforge.market.market_snapshot
==================================

Daily Market Snapshot domain model.

Represents one immutable end-of-day market snapshot
for an option contract.

This class stores only observed market data.

Engineering Principles
----------------------
- Immutable domain object
- One responsibility
- Daily timeframe
- Financially correct
- Fully testable

Author
------
OptionForge Engineering Team
"""

from __future__ import annotations

from dataclasses import dataclass


from optionforge.kernel.expiry import Expiry
from optionforge.kernel.option_contract import OptionContract
from optionforge.kernel.strike import Strike
from optionforge.kernel.symbol import Symbol


@dataclass(frozen=True, slots=True)
class MarketSnapshot:
    """
    Represents one immutable daily market snapshot.
    """

    contract: OptionContract

    open: float
    high: float
    low: float
    close: float

    volume: int

    open_interest: int

    change_in_open_interest: int

    def __post_init__(self) -> None:
        """
        Validate market data.
        """

        if self.open <= 0:
            raise ValueError("Open price must be positive.")

        if self.high <= 0:
            raise ValueError("High price must be positive.")

        if self.low <= 0:
            raise ValueError("Low price must be positive.")

        if self.close <= 0:
            raise ValueError("Close price must be positive.")

        if self.volume < 0:
            raise ValueError("Volume cannot be negative.")

        if self.open_interest < 0:
            raise ValueError("Open interest cannot be negative.")

        if self.high < self.low:
            raise ValueError("High price cannot be less than low price.")

        if not (self.low <= self.open <= self.high):
            raise ValueError("Open price must lie within High-Low range.")

        if not (self.low <= self.close <= self.high):
            raise ValueError("Close price must lie within High-Low range.")

    # =====================================================
    # Identity
    # =====================================================

    @property
    def symbol(self) -> Symbol:
        """
        Returns underlying symbol.
        """
        return self.contract.symbol

    @property
    def exchange(self):
        """
        Returns exchange.
        """
        return self.contract.exchange

    @property
    def expiry(self) -> Expiry:
        """
        Returns expiry.
        """
        return self.contract.expiry

    @property
    def strike(self) -> Strike:
        """
        Returns strike.
        """
        return self.contract.strike

    @property
    def option_type(self) -> OptionType:
        """
        Returns option type.
        """
        return self.contract.option_type

    @property
    def contract_id(self) -> str:
        """
        Returns unique contract identifier.
        """
        return self.contract.contract_id

    @property
    def trading_date(self):
        """
        Returns trading date.
        """
        return self.symbol.trading_session.trading_date

    # =====================================================
    # Price Statistics
    # =====================================================

    @property
    def is_bullish(self) -> bool:
        """
        Returns True if Close > Open.
        """
        return self.close > self.open

    @property
    def is_bearish(self) -> bool:
        """
        Returns True if Close < Open.
        """
        return self.close < self.open

    @property
    def is_doji(self) -> bool:
        """
        Returns True if Open == Close.
        """
        return self.open == self.close

    @property
    def price_range(self) -> float:
        """
        Returns High - Low.
        """
        return self.high - self.low

    @property
    def body_size(self) -> float:
        """
        Returns candle body size.
        """
        return abs(self.close - self.open)

    @property
    def upper_shadow(self) -> float:
        """
        Returns upper wick length.
        """
        return self.high - max(self.open, self.close)

    @property
    def lower_shadow(self) -> float:
        """
        Returns lower wick length.
        """
        return min(self.open, self.close) - self.low

    # =====================================================
    # Serialization
    # =====================================================

    def to_dict(self) -> dict:
        """
        Convert MarketSnapshot to dictionary.
        """

        return {
            "contract_id": self.contract_id,
            "symbol": self.symbol.ticker,
            "exchange": self.exchange.value,
            "trading_date": self.trading_date.isoformat(),
            "expiry_date": self.expiry.expiry_date.isoformat(),
            "strike_price": self.contract.strike_price,
            "option_type": self.option_type.value,
            "open": self.open,
            "high": self.high,
            "low": self.low,
            "close": self.close,
            "volume": self.volume,
            "open_interest": self.open_interest,
            "change_in_open_interest": self.change_in_open_interest,
        }

    # =====================================================
    # Representation
    # =====================================================

    def __str__(self) -> str:
        """
        Human-readable representation.
        """

        return (
            f"{self.contract} | "
            f"O:{self.open:.2f} "
            f"H:{self.high:.2f} "
            f"L:{self.low:.2f} "
            f"C:{self.close:.2f}"
        )

    def __repr__(self) -> str:
        """
        Developer-friendly representation.
        """

        return (
            "MarketSnapshot("
            f"contract='{self.contract_id}', "
            f"close={self.close}, "
            f"oi={self.open_interest})"
        )
