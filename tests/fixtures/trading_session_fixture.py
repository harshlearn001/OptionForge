"""
Reusable TradingSession fixture.

Used by all OptionForge tests.
"""

from __future__ import annotations

from datetime import date

from optionforge.kernel.trading_session import TradingSession


def build_trading_session() -> TradingSession:
    """
    Build a reusable trading session for tests.
    """

    return TradingSession(
        trading_date=date(2026, 7, 1),
    )