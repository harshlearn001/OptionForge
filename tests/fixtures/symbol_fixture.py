"""
Reusable Symbol fixture.

Used by all OptionForge tests.
"""

from __future__ import annotations

from optionforge.common.enums import (
    Exchange,
    InstrumentType,
)
from optionforge.kernel.symbol import Symbol

from tests.fixtures.trading_session_fixture import (
    build_trading_session,
)


def build_symbol() -> Symbol:
    """
    Build a reusable NIFTY symbol.
    """

    return Symbol(
        ticker="NIFTY",
        exchange=Exchange.NSE,
        instrument_type=InstrumentType.INDEX,
        lot_size=75,
        tick_size=0.05,
        strike_interval=50,
        trading_session=build_trading_session(),
    )