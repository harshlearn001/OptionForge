"""
Tests for optionforge.kernel.symbol
"""

from dataclasses import FrozenInstanceError
from datetime import date, time

import pytest

from optionforge.common.enums import (
    Exchange,
    InstrumentType,
    MarketStatus,
)
from optionforge.common.exceptions import (
    InvalidSymbolError,
)
from optionforge.kernel.symbol import Symbol
from optionforge.kernel.trading_session import TradingSession


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


# -------------------------------------------------------
# Creation
# -------------------------------------------------------

def test_symbol_creation():
    symbol = build_symbol()

    assert symbol.ticker == "NIFTY"
    assert symbol.exchange is Exchange.NSE
    assert symbol.instrument_type is InstrumentType.INDEX


# -------------------------------------------------------
# Validation
# -------------------------------------------------------

def test_empty_ticker():
    with pytest.raises(
        InvalidSymbolError,
        match="Ticker cannot be empty.",
    ):
        Symbol(
            ticker="",
            exchange=Exchange.NSE,
            instrument_type=InstrumentType.INDEX,
            lot_size=75,
            tick_size=0.05,
            strike_interval=50,
            trading_session=build_session(),
        )


def test_blank_ticker():
    with pytest.raises(
        InvalidSymbolError,
        match="Ticker cannot be empty.",
    ):
        Symbol(
            ticker="     ",
            exchange=Exchange.NSE,
            instrument_type=InstrumentType.INDEX,
            lot_size=75,
            tick_size=0.05,
            strike_interval=50,
            trading_session=build_session(),
        )


def test_invalid_lot_size():
    with pytest.raises(
        InvalidSymbolError,
        match="Lot size must be positive.",
    ):
        Symbol(
            ticker="NIFTY",
            exchange=Exchange.NSE,
            instrument_type=InstrumentType.INDEX,
            lot_size=0,
            tick_size=0.05,
            strike_interval=50,
            trading_session=build_session(),
        )


def test_invalid_tick_size():
    with pytest.raises(
        InvalidSymbolError,
        match="Tick size must be positive.",
    ):
        Symbol(
            ticker="NIFTY",
            exchange=Exchange.NSE,
            instrument_type=InstrumentType.INDEX,
            lot_size=75,
            tick_size=0,
            strike_interval=50,
            trading_session=build_session(),
        )


def test_invalid_strike_interval():
    with pytest.raises(
        InvalidSymbolError,
        match="Strike interval must be positive.",
    ):
        Symbol(
            ticker="NIFTY",
            exchange=Exchange.NSE,
            instrument_type=InstrumentType.INDEX,
            lot_size=75,
            tick_size=0.05,
            strike_interval=0,
            trading_session=build_session(),
        )


# -------------------------------------------------------
# Properties
# -------------------------------------------------------

def test_symbol_id():
    assert build_symbol().symbol_id == "NSE:NIFTY"


def test_is_index():
    assert build_symbol().is_index is True


def test_is_equity():
    symbol = Symbol(
        ticker="RELIANCE",
        exchange=Exchange.NSE,
        instrument_type=InstrumentType.EQUITY,
        lot_size=1,
        tick_size=0.05,
        strike_interval=1,
        trading_session=build_session(),
    )

    assert symbol.is_equity is True


def test_is_future():
    symbol = Symbol(
        ticker="NIFTY",
        exchange=Exchange.NSE,
        instrument_type=InstrumentType.FUTURE,
        lot_size=75,
        tick_size=0.05,
        strike_interval=50,
        trading_session=build_session(),
    )

    assert symbol.is_future is True


def test_is_option():
    symbol = Symbol(
        ticker="NIFTY",
        exchange=Exchange.NSE,
        instrument_type=InstrumentType.OPTION,
        lot_size=75,
        tick_size=0.05,
        strike_interval=50,
        trading_session=build_session(),
    )

    assert symbol.is_option is True


# -------------------------------------------------------
# Serialization
# -------------------------------------------------------

def test_to_dict():
    data = build_symbol().to_dict()

    assert data["ticker"] == "NIFTY"
    assert data["exchange"] == "NSE"
    assert data["instrument_type"] == "INDEX"


# -------------------------------------------------------
# Immutability
# -------------------------------------------------------

def test_frozen_dataclass():
    symbol = build_symbol()

    with pytest.raises(FrozenInstanceError):
        symbol.ticker = "BANKNIFTY"