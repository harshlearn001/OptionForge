"""
Tests for optionforge.optionchain.chain_validator
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
from optionforge.optionchain.chain_validator import ChainValidator

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


def test_validate_success():

    snapshots = [
        build_snapshot(25100, OptionType.CALL),
        build_snapshot(25100, OptionType.PUT),
        build_snapshot(25150, OptionType.CALL),
        build_snapshot(25150, OptionType.PUT),
    ]

    validated = ChainValidator.validate(snapshots)

    assert len(validated) == 4


# ==========================================================
# Empty
# ==========================================================


def test_empty():

    with pytest.raises(ValueError):
        ChainValidator.validate([])


# ==========================================================
# Invalid Type
# ==========================================================


def test_invalid_object():

    with pytest.raises(TypeError):
        ChainValidator.validate(
            [
                build_snapshot(
                    25100,
                    OptionType.CALL,
                ),
                object(),
            ]
        )


# ==========================================================
# Duplicate
# ==========================================================


def test_duplicate_contract():

    snapshot = build_snapshot(
        25100,
        OptionType.CALL,
    )

    with pytest.raises(ValueError):
        ChainValidator.validate(
            [
                snapshot,
                snapshot,
            ]
        )


# ==========================================================
# Different Symbol
# ==========================================================


def test_different_symbol():

    with pytest.raises(ValueError):

        ChainValidator.validate(
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


def test_different_expiry():

    with pytest.raises(ValueError):

        ChainValidator.validate(
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
# Returns Tuple
# ==========================================================


def test_returns_tuple():

    validated = ChainValidator.validate(
        [
            build_snapshot(
                25100,
                OptionType.CALL,
            )
        ]
    )

    assert isinstance(validated, tuple)
