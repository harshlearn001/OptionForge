"""
Tests for optionforge.optionchain.strike_selector
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

from optionforge.optionchain.strike_selector import StrikeSelector

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
            build_snapshot(25150, OptionType.CALL),
            build_snapshot(25150, OptionType.PUT),
        )
    )


# ==========================================================
# Exact Strike
# ==========================================================


def test_exact():

    result = StrikeSelector.exact(
        build_chain(),
        25050,
    )

    assert len(result) == 2

    assert all(s.contract.strike_price == 25050 for s in result)


# ==========================================================
# Between
# ==========================================================


def test_between():

    result = StrikeSelector.between(
        build_chain(),
        25050,
        25100,
    )

    assert len(result) == 4

    assert all(25050 <= s.contract.strike_price <= 25100 for s in result)


# ==========================================================
# Around
# ==========================================================


def test_around():

    result = StrikeSelector.around(
        build_chain(),
        center=25060,
        width=1,
    )

    strikes = {s.contract.strike_price for s in result}

    assert strikes == {
        25000,
        25050,
        25100,
    }


# ==========================================================
# Exact Not Found
# ==========================================================


def test_exact_not_found():

    result = StrikeSelector.exact(
        build_chain(),
        26000,
    )

    assert result == ()


# ==========================================================
# Invalid Range
# ==========================================================


def test_invalid_range():

    with pytest.raises(ValueError):

        StrikeSelector.between(
            build_chain(),
            25100,
            25000,
        )


# ==========================================================
# Negative Width
# ==========================================================


def test_negative_width():

    with pytest.raises(ValueError):

        StrikeSelector.around(
            build_chain(),
            center=25050,
            width=-1,
        )


# ==========================================================
# Width Zero
# ==========================================================


def test_zero_width():

    result = StrikeSelector.around(
        build_chain(),
        center=25050,
        width=0,
    )

    assert len(result) == 2

    assert all(s.contract.strike_price == 25050 for s in result)
