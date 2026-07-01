"""
Tests for optionforge.market.market_snapshot
"""

from dataclasses import FrozenInstanceError
from datetime import date, time

import pytest

from optionforge.common.enums import (
    Exchange,
    ExpiryType,
    InstrumentType,
    MarketStatus,
    OptionType,
)
from optionforge.market.market_snapshot import MarketSnapshot
from optionforge.kernel.expiry import Expiry
from optionforge.kernel.option_contract import OptionContract
from optionforge.kernel.strike import Strike
from optionforge.kernel.symbol import Symbol
from optionforge.kernel.trading_session import TradingSession


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


def build_contract() -> OptionContract:
    return OptionContract(
        strike=build_strike(),
        option_type=OptionType.CALL,
    )


def build_snapshot() -> MarketSnapshot:
    return MarketSnapshot(
        contract=build_contract(),
        open=100.0,
        high=120.0,
        low=95.0,
        close=110.0,
        volume=250000,
        open_interest=150000,
        change_in_open_interest=5000,
    )


# ==========================================================
# Creation
# ==========================================================

def test_creation():
    snapshot = build_snapshot()

    assert snapshot.symbol.ticker == "NIFTY"
    assert snapshot.contract.option_type is OptionType.CALL


# ==========================================================
# Identity
# ==========================================================

def test_exchange():
    assert build_snapshot().exchange is Exchange.NSE


def test_option_type():
    assert build_snapshot().option_type is OptionType.CALL


def test_contract_id():
    assert (
        build_snapshot().contract_id
        == "NSE:NIFTY:20260702:25150:CE"
    )


# ==========================================================
# Candle Properties
# ==========================================================

def test_is_bullish():
    assert build_snapshot().is_bullish is True


def test_is_bearish():
    assert build_snapshot().is_bearish is False


def test_price_range():
    assert build_snapshot().price_range == 25.0


def test_body_size():
    assert build_snapshot().body_size == 10.0


def test_upper_shadow():
    assert build_snapshot().upper_shadow == 10.0


def test_lower_shadow():
    assert build_snapshot().lower_shadow == 5.0


# ==========================================================
# Serialization
# ==========================================================

def test_to_dict():
    data = build_snapshot().to_dict()

    assert data["symbol"] == "NIFTY"
    assert data["exchange"] == "NSE"
    assert data["option_type"] == "CALL"
    assert data["volume"] == 250000


# ==========================================================
# String Representation
# ==========================================================

def test_str():
    assert "NIFTY" in str(build_snapshot())


def test_repr():
    assert "MarketSnapshot(" in repr(build_snapshot())


# ==========================================================
# Immutability
# ==========================================================

def test_frozen():
    snapshot = build_snapshot()

    with pytest.raises(FrozenInstanceError):
        snapshot.volume = 1


# ==========================================================
# Validation
# ==========================================================

def test_invalid_high_low():
    with pytest.raises(ValueError):
        MarketSnapshot(
            contract=build_contract(),
            open=100,
            high=90,
            low=95,
            close=100,
            volume=1,
            open_interest=1,
            change_in_open_interest=0,
        )


def test_invalid_volume():
    with pytest.raises(ValueError):
        MarketSnapshot(
            contract=build_contract(),
            open=100,
            high=120,
            low=90,
            close=100,
            volume=-1,
            open_interest=1,
            change_in_open_interest=0,
        )