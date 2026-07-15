"""
optionforge.kernel.trading_session
==================================

Trading session domain model.

A TradingSession represents one complete trading session for an exchange.
It contains only session-related information and does not depend on
symbols, option chains, or market data.

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
from datetime import date, time, timedelta

from optionforge.common.enums import Exchange, MarketStatus
from optionforge.common.exceptions import InvalidTradingSessionError


@dataclass(frozen=True, slots=True)
class TradingSession:
    """
    Represents a single exchange trading session.
    """

    exchange: Exchange
    trading_date: date
    market_status: MarketStatus
    session_start: time
    session_end: time

    def __post_init__(self) -> None:
        """
        Validate trading session times.
        """
        if self.session_end <= self.session_start:
            raise InvalidTradingSessionError(
                "session_end must be later than session_start."
            )

    def is_open(self) -> bool:
        """
        Returns True if the market is currently open.
        """
        return self.market_status is MarketStatus.OPEN

    def is_closed(self) -> bool:
        """
        Returns True if the market is closed.
        """
        return not self.is_open()

    @property
    def session_duration(self) -> timedelta:
        """
        Returns the total trading session duration.
        """

        start = (
            self.session_start.hour * 3600
            + self.session_start.minute * 60
            + self.session_start.second
        )

        end = (
            self.session_end.hour * 3600
            + self.session_end.minute * 60
            + self.session_end.second
        )

        return timedelta(seconds=end - start)
