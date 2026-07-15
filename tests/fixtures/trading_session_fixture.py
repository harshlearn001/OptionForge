"""
Reusable TradingSession fixture.

Used by all OptionForge tests.
"""

from __future__ import annotations

from datetime import date, time

from optionforge.common.enums import Exchange, MarketStatus
from optionforge.kernel.trading_session import TradingSession


def build_trading_session() -> TradingSession:
    """
    Build a reusable trading session for tests.
    """

    return TradingSession(
        exchange=Exchange.NSE,
        trading_date=date(2026, 7, 1),
        market_status=MarketStatus.OPEN,
        session_start=time(9, 15),
        session_end=time(15, 30),
    )
