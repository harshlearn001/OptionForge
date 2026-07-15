"""
Tests for optionforge.market.option_chain
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
from optionforge.kernel.expiry import Expiry
from optionforge.kernel.option_contract import OptionContract
from optionforge.kernel.strike import Strike
from optionforge.kernel.symbol import Symbol
from optionforge.kernel.trading_session import TradingSession

from optionforge.market.market_snapshot import MarketSnapshot
from optionforge.market.option_chain import OptionChain

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


def build_contract(
    strike_price: int,
    option_type: OptionType,
) -> OptionContract:

    strike = Strike(
        expiry=build_expiry(),
        strike_price=strike_price,
    )

    return OptionContract(
        strike=strike,
        option_type=option_type,
    )


def build_snapshot(
    strike_price: int,
    option_type: OptionType,
) -> MarketSnapshot:

    return MarketSnapshot(
        contract=build_contract(
            strike_price,
            option_type,
        ),
        open=100,
        high=120,
        low=95,
        close=110,
        volume=100000,
        open_interest=50000,
        change_in_open_interest=1000,
    )


def build_chain() -> OptionChain:

    return OptionChain(
        [
            build_snapshot(25100, OptionType.CALL),
            build_snapshot(25100, OptionType.PUT),
            build_snapshot(25150, OptionType.CALL),
            build_snapshot(25150, OptionType.PUT),
        ]
    )


# ==========================================================
# Creation
# ==========================================================


def test_creation():

    chain = build_chain()

    assert chain.snapshot_count == 4


# ==========================================================
# Identity
# ==========================================================


def test_symbol():

    assert build_chain().symbol.ticker == "NIFTY"


def test_exchange():

    assert build_chain().exchange is Exchange.NSE


def test_expiry():

    assert build_chain().expiry.expiry_date == date(2026, 7, 2)


def test_trading_date():

    assert build_chain().trading_date == date(2026, 7, 1)


# ==========================================================
# Collection
# ==========================================================


def test_len():

    assert len(build_chain()) == 4


def test_iteration():

    assert sum(1 for _ in build_chain()) == 4


def test_contains():

    chain = build_chain()

    snapshot = build_snapshot(
        25100,
        OptionType.CALL,
    )

    assert snapshot in chain


# ==========================================================
# Lookup
# ==========================================================


def test_get():

    chain = build_chain()

    contract = build_contract(
        25100,
        OptionType.CALL,
    )

    assert chain.get(contract) is not None


def test_exists():

    chain = build_chain()

    contract = build_contract(
        25100,
        OptionType.CALL,
    )

    assert chain.exists(contract)


# ==========================================================
# Serialization
# ==========================================================


def test_to_dict():

    data = build_chain().to_dict()

    assert data["symbol"] == "NIFTY"
    assert data["snapshot_count"] == 4


def test_to_list():

    data = build_chain().to_list()

    assert len(data) == 4


# ==========================================================
# Representation
# ==========================================================


def test_str():

    assert "NIFTY" in str(build_chain())


def test_repr():

    assert "OptionChain" in repr(build_chain())


# ==========================================================
# Validation
# ==========================================================


def test_empty_chain():

    with pytest.raises(ValueError):
        OptionChain([])


def test_duplicate_contract():

    snapshot = build_snapshot(
        25100,
        OptionType.CALL,
    )

    with pytest.raises(ValueError):
        OptionChain(
            [
                snapshot,
                snapshot,
            ]
        )


# ==========================================================
# Frozen
# ==========================================================


def test_frozen():

    chain = build_chain()

    with pytest.raises(FrozenInstanceError):
        chain.snapshots = ()
