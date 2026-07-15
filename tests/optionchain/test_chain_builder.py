"""
Tests for optionforge.optionchain.chain_builder
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

from optionforge.optionchain.chain_builder import ChainBuilder

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


def build_symbol(
    ticker: str = "NIFTY",
) -> Symbol:
    return Symbol(
        ticker=ticker,
        exchange=Exchange.NSE,
        instrument_type=InstrumentType.INDEX,
        lot_size=75,
        tick_size=0.05,
        strike_interval=50,
        trading_session=build_session(),
    )


def build_expiry(
    ticker: str = "NIFTY",
    expiry_date: date = date(2026, 7, 2),
) -> Expiry:
    return Expiry(
        symbol=build_symbol(ticker),
        expiry_date=expiry_date,
        expiry_type=ExpiryType.WEEKLY,
    )


def build_contract(
    strike_price: int,
    option_type: OptionType,
    ticker: str = "NIFTY",
    expiry_date: date = date(2026, 7, 2),
) -> OptionContract:

    strike = Strike(
        expiry=build_expiry(
            ticker,
            expiry_date,
        ),
        strike_price=strike_price,
    )

    return OptionContract(
        strike=strike,
        option_type=option_type,
    )


def build_snapshot(
    strike_price: int,
    option_type: OptionType,
    ticker: str = "NIFTY",
    expiry_date: date = date(2026, 7, 2),
) -> MarketSnapshot:

    return MarketSnapshot(
        contract=build_contract(
            strike_price,
            option_type,
            ticker,
            expiry_date,
        ),
        open=100,
        high=120,
        low=90,
        close=110,
        volume=1000,
        open_interest=500,
        change_in_open_interest=50,
    )


# ==========================================================
# Success
# ==========================================================


def test_build_success():

    chain = ChainBuilder.build(
        [
            build_snapshot(25100, OptionType.CALL),
            build_snapshot(25100, OptionType.PUT),
            build_snapshot(25150, OptionType.CALL),
            build_snapshot(25150, OptionType.PUT),
        ]
    )

    assert isinstance(chain, OptionChain)
    assert chain.snapshot_count == 4


# ==========================================================
# Empty
# ==========================================================


def test_build_empty():

    with pytest.raises(ValueError):
        ChainBuilder.build([])


# ==========================================================
# Duplicate
# ==========================================================


def test_build_duplicate():

    snapshot = build_snapshot(
        25100,
        OptionType.CALL,
    )

    with pytest.raises(ValueError):
        ChainBuilder.build(
            [
                snapshot,
                snapshot,
            ]
        )


# ==========================================================
# Different Symbol
# ==========================================================


def test_build_different_symbol():

    with pytest.raises(ValueError):

        ChainBuilder.build(
            [
                build_snapshot(
                    25100,
                    OptionType.CALL,
                    ticker="NIFTY",
                ),
                build_snapshot(
                    25100,
                    OptionType.PUT,
                    ticker="BANKNIFTY",
                ),
            ]
        )


# ==========================================================
# Different Expiry
# ==========================================================


def test_build_different_expiry():

    with pytest.raises(ValueError):

        ChainBuilder.build(
            [
                build_snapshot(
                    25100,
                    OptionType.CALL,
                    expiry_date=date(2026, 7, 2),
                ),
                build_snapshot(
                    25100,
                    OptionType.PUT,
                    expiry_date=date(2026, 7, 9),
                ),
            ]
        )


# ==========================================================
# Iterable Input
# ==========================================================


def test_build_from_tuple():

    snapshots = (
        build_snapshot(25100, OptionType.CALL),
        build_snapshot(25100, OptionType.PUT),
    )

    chain = ChainBuilder.build(snapshots)

    assert isinstance(chain, OptionChain)
