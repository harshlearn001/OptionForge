"""
Tests for optionforge.kernel.strike
"""

from dataclasses import FrozenInstanceError
from datetime import date, time

import pytest

from optionforge.common.enums import (
    Exchange,
    InstrumentType,
    MarketStatus,
    ExpiryType,
)
from optionforge.common.exceptions import InvalidStrikeError
from optionforge.kernel.trading_session import TradingSession
from optionforge.kernel.symbol import Symbol
from optionforge.kernel.expiry import Expiry
from optionforge.kernel.strike import Strike


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


def build_strike() -> Strike:
    return Strike(
        expiry=build_expiry(),
        strike_price=25150,
    )


# ==========================================================
# Creation
# ==========================================================

def test_strike_creation():
    strike = build_strike()

    assert strike.strike_price == 25150
    assert strike.symbol.ticker == "NIFTY"


# ==========================================================
# Validation
# ==========================================================

def test_zero_strike():
    with pytest.raises(
        InvalidStrikeError,
        match="Strike price must be positive.",
    ):
        Strike(
            expiry=build_expiry(),
            strike_price=0,
        )


def test_negative_strike():
    with pytest.raises(
        InvalidStrikeError,
        match="Strike price must be positive.",
    ):
        Strike(
            expiry=build_expiry(),
            strike_price=-100,
        )


# ==========================================================
# Properties
# ==========================================================

def test_symbol_property():
    strike = build_strike()

    assert strike.symbol.ticker == "NIFTY"


def test_expiry_reference():
    strike = build_strike()

    assert strike.expiry.expiry_type is ExpiryType.WEEKLY


def test_strike_id():
    strike = build_strike()

    assert (
        strike.strike_id
        == "NIFTY_20260702_25150"
    )


# ==========================================================
# Serialization
# ==========================================================

def test_to_dict():
    data = build_strike().to_dict()

    assert data["symbol"] == "NIFTY"
    assert data["exchange"] == "NSE"
    assert data["strike_price"] == 25150


# ==========================================================
# String Representation
# ==========================================================

def test_string_representation():
    strike = build_strike()

    assert str(strike) == "NIFTY 2026-07-02 25150"


def test_repr():
    strike = build_strike()

    assert "Strike(" in repr(strike)


# ==========================================================
# Immutability
# ==========================================================

def test_frozen_dataclass():
    strike = build_strike()

    with pytest.raises(FrozenInstanceError):
        strike.strike_price = 25200