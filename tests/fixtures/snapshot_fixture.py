"""
Reusable MarketSnapshot fixture.

Used by all OptionForge tests.
"""

from __future__ import annotations

from optionforge.common.enums import OptionType
from optionforge.market.market_snapshot import MarketSnapshot

from tests.fixtures.contract_fixture import (
    build_contract,
)


def build_snapshot(
    strike_price: int = 25000,
    option_type: OptionType = OptionType.CALL,
    open_interest: int = 1000,
    change_in_open_interest: int = 100,
    volume: int = 500,
    open: float = 100.0,
    high: float = 110.0,
    low: float = 95.0,
    close: float = 105.0,
) -> MarketSnapshot:
    """
    Build a reusable market snapshot.
    """

    return MarketSnapshot(
        contract=build_contract(
            strike_price=strike_price,
            option_type=option_type,
        ),
        open=open,
        high=high,
        low=low,
        close=close,
        volume=volume,
        open_interest=open_interest,
        change_in_open_interest=change_in_open_interest,
    )