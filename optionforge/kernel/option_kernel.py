"""
=========================================================
OptionForge
Trading Session
=========================================================

Represents one exchange trading session.

A TradingSession contains only information about a
single trading day. It intentionally does NOT contain
symbols, option chains, Greeks or analytics.

Author : OptionForge
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date, time, timedelta
from typing import Optional


@dataclass(frozen=True, slots=True)
class TradingSession:
    """
    Represents one trading session for an exchange.

    Parameters
    ----------
    trading_date : date
        Trading date.

    exchange : str
        Exchange name (e.g. "NSE").

    market_open : time
        Market opening time.

    market_close : time
        Market closing time.

    is_holiday : bool
        True if exchange is closed.

    holiday_name : Optional[str]
        Holiday description.
    """

    trading_date: date
    exchange: str
    market_open: time
    market_close: time
    is_holiday: bool = False
    holiday_name: Optional[str] = None

    def __post_init__(self) -> None:

        if not self.exchange.strip():
            raise ValueError("Exchange cannot be empty.")

        if self.market_open >= self.market_close:
            raise ValueError("Market open time must be before market close.")

        if self.is_holiday and not self.holiday_name:
            raise ValueError("Holiday name must be provided when is_holiday=True.")

        if not self.is_holiday and self.holiday_name:
            raise ValueError("holiday_name should be None when is_holiday=False.")

    @property
    def session_id(self) -> str:
        """
        Unique session identifier.
        """
        return f"{self.exchange}_{self.trading_date:%Y%m%d}"

    @property
    def weekday(self) -> str:
        """
        Trading day name.
        """
        return self.trading_date.strftime("%A")

    def market_duration(self) -> timedelta:
        """
        Returns total market duration.
        """
        open_dt = timedelta(
            hours=self.market_open.hour,
            minutes=self.market_open.minute,
            seconds=self.market_open.second,
        )

        close_dt = timedelta(
            hours=self.market_close.hour,
            minutes=self.market_close.minute,
            seconds=self.market_close.second,
        )

        return close_dt - open_dt

    def to_dict(self) -> dict:
        """
        Convert object to dictionary.
        """
        return {
            "session_id": self.session_id,
            "trading_date": self.trading_date.isoformat(),
            "exchange": self.exchange,
            "market_open": self.market_open.isoformat(),
            "market_close": self.market_close.isoformat(),
            "weekday": self.weekday,
            "is_holiday": self.is_holiday,
            "holiday_name": self.holiday_name,
        }

    def __str__(self) -> str:
        return (
            f"{self.exchange} " f"{self.trading_date.isoformat()} " f"({self.weekday})"
        )
