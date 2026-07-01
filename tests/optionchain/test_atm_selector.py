"""
Tests for optionforge.optionchain.atm_selector
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

from optionforge.optionchain.atm_selector import ATMSelector


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


def build_expiry() -> Expiry:
    return Expiry(
        symbol=build_symbol(),
        expiry_date=date(2026, 7, 2),
        expiry_type=ExpiryType.WEEKLY,
    )


def build_snapshot(
    strike_price: int,
    option_type: OptionType,
) -> MarketSnapshot:

    contract = OptionContract(
        strike=Strike(
            expiry=build_expiry(),
            strike_price=strike_price,
        ),
        option_type=option_type,
    )

    return MarketSnapshot(
        contract=contract,
        open=100,
        high=120,
        low=90,
        close=110,
        volume=1000,
        open_interest=500,
        change_in_open_interest=50,
    )


def build_chain() -> OptionChain:

    return OptionChain(
        (
            build_snapshot(25000, OptionType.CALL),
            build_snapshot(25000, OptionType.PUT),
            build_snapshot(25050, OptionType.CALL),
            build_snapshot(25050, OptionType.PUT),
            build_snapshot(25100, OptionType.CALL),
            build_snapshot(25100, OptionType.PUT),
        )
    )


# ==========================================================
# Exact ATM
# ==========================================================

def test_exact_atm():

    result = ATMSelector.select(
        build_chain(),
        25050,
    )

    assert len(result) == 2

    assert all(
        s.contract.strike_price == 25050
        for s in result
    )


# ==========================================================
# Nearest Lower
# ==========================================================

def test_nearest_lower():

    result = ATMSelector.select(
        build_chain(),
        25038,
    )

    assert len(result) == 2

    assert all(
        s.contract.strike_price == 25050
        for s in result
    )


# ==========================================================
# Nearest Higher
# ==========================================================

def test_nearest_higher():

    result = ATMSelector.select(
        build_chain(),
        25088,
    )

    assert len(result) == 2

    assert all(
        s.contract.strike_price == 25100
        for s in result
    )


# ==========================================================
# Below Lowest Strike
# ==========================================================

def test_below_lowest():

    result = ATMSelector.select(
        build_chain(),
        24000,
    )

    assert len(result) == 2

    assert all(
        s.contract.strike_price == 25000
        for s in result
    )


# ==========================================================
# Above Highest Strike
# ==========================================================

def test_above_highest():

    result = ATMSelector.select(
        build_chain(),
        26000,
    )

    assert len(result) == 2

    assert all(
        s.contract.strike_price == 25100
        for s in result
    )


# ==========================================================
# Empty Chain
# ==========================================================

def test_empty_chain():

    with pytest.raises(ValueError):
        ATMSelector.select(
            OptionChain(()),
            25000,
        )