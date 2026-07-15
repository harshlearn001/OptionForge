"""
Tests for optionforge.optionchain.filters
"""

from datetime import date, time

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

from optionforge.optionchain.filters import ChainFilters

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
    strike: int,
    option_type: OptionType,
) -> OptionContract:

    return OptionContract(
        strike=Strike(
            expiry=build_expiry(),
            strike_price=strike,
        ),
        option_type=option_type,
    )


def build_snapshot(
    strike: int,
    option_type: OptionType,
    oi: int,
    volume: int,
) -> MarketSnapshot:

    return MarketSnapshot(
        contract=build_contract(
            strike,
            option_type,
        ),
        open=100,
        high=120,
        low=90,
        close=110,
        volume=volume,
        open_interest=oi,
        change_in_open_interest=100,
    )


def build_chain() -> OptionChain:

    return OptionChain(
        (
            build_snapshot(25100, OptionType.CALL, 1000, 500),
            build_snapshot(25100, OptionType.PUT, 2000, 800),
            build_snapshot(25150, OptionType.CALL, 3000, 1000),
            build_snapshot(25150, OptionType.PUT, 4000, 1200),
        )
    )


# ==========================================================
# Calls
# ==========================================================


def test_calls():

    chain = build_chain()

    result = ChainFilters.calls(chain)

    assert len(result) == 2

    assert all(s.option_type is OptionType.CALL for s in result)


# ==========================================================
# Puts
# ==========================================================


def test_puts():

    chain = build_chain()

    result = ChainFilters.puts(chain)

    assert len(result) == 2

    assert all(s.option_type is OptionType.PUT for s in result)


# ==========================================================
# Strike
# ==========================================================


def test_by_strike():

    chain = build_chain()

    result = ChainFilters.by_strike(
        chain,
        25100,
    )

    assert len(result) == 2

    assert all(s.contract.strike_price == 25100 for s in result)


# ==========================================================
# Option Type
# ==========================================================


def test_by_option_type():

    chain = build_chain()

    result = ChainFilters.by_option_type(
        chain,
        OptionType.PUT,
    )

    assert len(result) == 2

    assert all(s.option_type is OptionType.PUT for s in result)


# ==========================================================
# Open Interest
# ==========================================================


def test_by_open_interest():

    chain = build_chain()

    result = ChainFilters.by_open_interest(
        chain,
        minimum=2500,
    )

    assert len(result) == 2

    assert all(s.open_interest >= 2500 for s in result)


# ==========================================================
# Volume
# ==========================================================


def test_by_volume():

    chain = build_chain()

    result = ChainFilters.by_volume(
        chain,
        minimum=900,
    )

    assert len(result) == 2

    assert all(s.volume >= 900 for s in result)


# ==========================================================
# Empty Result
# ==========================================================


def test_empty_result():

    chain = build_chain()

    result = ChainFilters.by_strike(
        chain,
        26000,
    )

    assert result == ()
