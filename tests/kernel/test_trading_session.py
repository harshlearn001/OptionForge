"""
Tests for optionforge.kernel.trading_session
"""

from dataclasses import FrozenInstanceError
from datetime import date, time, timedelta

import pytest

from optionforge.common.enums import Exchange, MarketStatus
from optionforge.common.exceptions import InvalidTradingSessionError
from optionforge.kernel.trading_session import TradingSession


def build_session() -> TradingSession:
    return TradingSession(
        exchange=Exchange.NSE,
        trading_date=date(2026, 7, 1),
        market_status=MarketStatus.OPEN,
        session_start=time(9, 15),
        session_end=time(15, 30),
    )


def test_is_open():
    assert build_session().is_open() is True


def test_is_closed():
    session = TradingSession(
        exchange=Exchange.NSE,
        trading_date=date(2026, 7, 1),
        market_status=MarketStatus.CLOSED,
        session_start=time(9, 15),
        session_end=time(15, 30),
    )

    assert session.is_closed() is True


def test_session_duration():
    assert build_session().session_duration == timedelta(
        hours=6,
        minutes=15,
    )


def test_exchange():
    assert build_session().exchange is Exchange.NSE


def test_market_status():
    assert build_session().market_status is MarketStatus.OPEN


def test_invalid_session_times():
    with pytest.raises(
        InvalidTradingSessionError,
        match="session_end must be later than session_start.",
    ):
        TradingSession(
            exchange=Exchange.NSE,
            trading_date=date(2026, 7, 1),
            market_status=MarketStatus.OPEN,
            session_start=time(15, 30),
            session_end=time(9, 15),
        )


def test_frozen_dataclass():
    session = build_session()

    with pytest.raises(FrozenInstanceError):
        session.exchange = Exchange.BSE