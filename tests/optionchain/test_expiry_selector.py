"""
Tests for optionforge.optionchain.expiry_selector
"""

from datetime import date, time

import pytest

from optionforge.common.enums import (
    Exchange,
    ExpiryType,
    InstrumentType,
    MarketStatus,
    OptionType,
)

from optionforge.kernel.expiry import Expiry
from optionforge.kernel.option_contract import OptionContract
from optionforge.kernel.strike import Strike
from optionforge.kernel.symbol import Symbol
from optionforge.kernel.trading_session import TradingSession

from optionforge.market.market_snapshot import MarketSnapshot
from optionforge.market.option_chain import OptionChain

from optionforge.optionchain.expiry_selector import ExpirySelector

# ==========================================================
# Builders
# ==========================================================


def build_session() -> TradingSession:
    return TradingSession(
        exchange=Exchange.NSE,
        trading_date=date(2026, 7, 1),
        market_status=MarketStatus.OPEN,
        session_start=time(9, 15),
        session_end=time(15, 30),
    )


def build_symbol() -> Symbol:
    return Symbol(
        ticker="NIFTY",
        exchange=Exchange.NSE,
        instrument_type=InstrumentType.INDEX,
        lot_size=75,
        tick_size=0.05,
        strike_interval=50,
        trading_session=build_session(),
    )


def build_chain(
    expiry_date: date,
    expiry_type: ExpiryType,
) -> OptionChain:

    expiry = Expiry(
        symbol=build_symbol(),
        expiry_date=expiry_date,
        expiry_type=expiry_type,
    )

    contract = OptionContract(
        strike=Strike(
            expiry=expiry,
            strike_price=25000,
        ),
        option_type=OptionType.CALL,
    )

    snapshot = MarketSnapshot(
        contract=contract,
        open=100,
        high=120,
        low=90,
        close=110,
        volume=1000,
        open_interest=500,
        change_in_open_interest=50,
    )

    return OptionChain((snapshot,))


def build_chains():

    weekly1 = build_chain(
        date(2026, 7, 2),
        ExpiryType.WEEKLY,
    )

    weekly2 = build_chain(
        date(2026, 7, 9),
        ExpiryType.WEEKLY,
    )

    monthly = build_chain(
        date(2026, 7, 30),
        ExpiryType.MONTHLY,
    )

    return (
        weekly1,
        weekly2,
        monthly,
    )


# ==========================================================
# Exact
# ==========================================================


def test_exact():

    chains = build_chains()

    expiry = chains[1].expiry

    result = ExpirySelector.exact(
        chains,
        expiry,
    )

    assert result.expiry == expiry


# ==========================================================
# Nearest
# ==========================================================


def test_nearest():

    chain = ExpirySelector.nearest(
        build_chains(),
    )

    assert chain.expiry.expiry_date == date(2026, 7, 2)


# ==========================================================
# Weekly
# ==========================================================


def test_weekly():

    result = ExpirySelector.weekly(
        build_chains(),
    )

    assert len(result) == 2

    assert all(chain.expiry.is_weekly for chain in result)


# ==========================================================
# Monthly
# ==========================================================


def test_monthly():

    result = ExpirySelector.monthly(
        build_chains(),
    )

    assert len(result) == 1

    assert result[0].expiry.is_monthly


# ==========================================================
# Unknown Expiry
# ==========================================================


def test_unknown_expiry():

    chains = build_chains()

    unknown = Expiry(
        symbol=build_symbol(),
        expiry_date=date(2026, 8, 27),
        expiry_type=ExpiryType.MONTHLY,
    )

    with pytest.raises(LookupError):
        ExpirySelector.exact(
            chains,
            unknown,
        )


# ==========================================================
# Empty Chains
# ==========================================================


def test_empty():

    with pytest.raises(ValueError):
        ExpirySelector.nearest(())
