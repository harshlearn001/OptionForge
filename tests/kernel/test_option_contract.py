"""
Tests for optionforge.kernel.option_contract
"""

from dataclasses import FrozenInstanceError
from datetime import date, time

import pytest

from optionforge.common.enums import (
    Exchange,
    InstrumentType,
    MarketStatus,
    ExpiryType,
    OptionType,
)
from optionforge.kernel.trading_session import TradingSession
from optionforge.kernel.symbol import Symbol
from optionforge.kernel.expiry import Expiry
from optionforge.kernel.strike import Strike
from optionforge.kernel.option_contract import OptionContract

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


def build_call_contract() -> OptionContract:
    return OptionContract(
        strike=build_strike(),
        option_type=OptionType.CALL,
    )


def build_put_contract() -> OptionContract:
    return OptionContract(
        strike=build_strike(),
        option_type=OptionType.PUT,
    )


# ==========================================================
# Creation
# ==========================================================


def test_contract_creation():
    contract = build_call_contract()

    assert contract.symbol.ticker == "NIFTY"
    assert contract.strike_price == 25150
    assert contract.option_type is OptionType.CALL


# ==========================================================
# Properties
# ==========================================================


def test_exchange_property():
    assert build_call_contract().exchange is Exchange.NSE


def test_expiry_property():
    assert build_call_contract().expiry.expiry_type is ExpiryType.WEEKLY


def test_strike_property():
    assert build_call_contract().strike.strike_price == 25150


def test_is_call():
    assert build_call_contract().is_call is True


def test_is_put():
    assert build_put_contract().is_put is True


# ==========================================================
# Contract ID
# ==========================================================


def test_contract_id():
    contract = build_call_contract()

    assert contract.contract_id == "NSE:NIFTY:20260702:25150:CE"


# ==========================================================
# Serialization
# ==========================================================


def test_to_dict():
    data = build_call_contract().to_dict()

    assert data["symbol"] == "NIFTY"
    assert data["exchange"] == "NSE"
    assert data["strike_price"] == 25150
    assert data["option_type"] == "CALL"


# ==========================================================
# String Representation
# ==========================================================


def test_string_representation():
    contract = build_call_contract()

    assert str(contract) == "NIFTY 2026-07-02 25150 CE"


def test_repr():
    contract = build_call_contract()

    assert "OptionContract(" in repr(contract)


# ==========================================================
# Immutability
# ==========================================================


def test_frozen_dataclass():
    contract = build_call_contract()

    with pytest.raises(FrozenInstanceError):
        contract.option_type = OptionType.PUT
