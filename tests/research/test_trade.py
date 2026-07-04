from uuid import uuid4
from datetime import date

from optionforge.research.signal import Signal
from optionforge.research.trade import Trade


def create_trade():
    return Trade(
        trade_id=uuid4(),
        strategy_id="OF001",
        strategy_version="1.0.0",
        symbol="RELIANCE",
        signal=Signal.BUY,
        signal_date=date(2026, 7, 3),
        entry_date=date(2026, 7, 6),
        exit_date=date(2026, 7, 7),
        entry_price=1520.50,
        exit_price=1545.20,
        return_pct=1.62,
        holding_days=1,
    )


def test_trade_creation():
    trade = create_trade()

    assert trade.symbol == "RELIANCE"
    assert trade.signal == Signal.BUY


def test_prices():
    trade = create_trade()

    assert trade.entry_price == 1520.50
    assert trade.exit_price == 1545.20


def test_return():
    trade = create_trade()

    assert trade.return_pct == 1.62


def test_holding_days():
    trade = create_trade()

    assert trade.holding_days == 1