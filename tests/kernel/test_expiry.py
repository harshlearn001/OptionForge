"""
Tests for optionforge.kernel.expiry
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
from optionforge.common.exceptions import InvalidExpiryError
from optionforge.kernel.trading_session import TradingSession
from optionforge.kernel.symbol import Symbol
from optionforge.kernel.expiry import Expiry

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


# ==========================================================
# Creation
# ==========================================================


def test_expiry_creation():
    expiry = build_expiry()

    assert expiry.symbol.ticker == "NIFTY"
    assert expiry.expiry_date == date(2026, 7, 2)
    assert expiry.expiry_type is ExpiryType.WEEKLY


# ==========================================================
# Validation
# ==========================================================


def test_invalid_expiry_date():
    with pytest.raises(
        InvalidExpiryError,
        match="Expiry date cannot be before trading date.",
    ):
        Expiry(
            symbol=build_symbol(),
            expiry_date=date(2026, 6, 30),
            expiry_type=ExpiryType.WEEKLY,
        )


# ==========================================================
# Date Logic
# ==========================================================


def test_days_to_expiry():
    expiry = build_expiry()

    assert expiry.days_to_expiry(date(2026, 7, 1)) == 1


def test_expired():
    expiry = build_expiry()

    assert expiry.is_expired(date(2026, 7, 3)) is True


def test_not_expired():
    expiry = build_expiry()

    assert expiry.is_expired(date(2026, 7, 1)) is False


def test_is_expiry_day():
    expiry = build_expiry()

    assert expiry.is_expiry_day(date(2026, 7, 2)) is True


# ==========================================================
# Properties
# ==========================================================


def test_weekly():
    assert build_expiry().is_weekly is True


def test_monthly():
    expiry = Expiry(
        symbol=build_symbol(),
        expiry_date=date(2026, 7, 30),
        expiry_type=ExpiryType.MONTHLY,
    )

    assert expiry.is_monthly is True


def test_expiry_id():
    expiry = build_expiry()

    assert expiry.expiry_id == "NIFTY_20260702_WEEKLY"


# ==========================================================
# Serialization
# ==========================================================


def test_to_dict():
    data = build_expiry().to_dict()

    assert data["symbol"] == "NIFTY"
    assert data["exchange"] == "NSE"
    assert data["instrument_type"] == "INDEX"
    assert data["expiry_type"] == "WEEKLY"


# ==========================================================
# String Representation
# ==========================================================


def test_string_representation():
    expiry = build_expiry()

    assert str(expiry) == "NIFTY 2026-07-02 [WEEKLY]"


# ==========================================================
# Immutability
# ==========================================================


def test_frozen_dataclass():
    expiry = build_expiry()

    with pytest.raises(FrozenInstanceError):
        expiry.expiry_date = date(2026, 7, 9)
