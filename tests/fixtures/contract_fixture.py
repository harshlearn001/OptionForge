"""
Reusable OptionContract fixture.

Used by all OptionForge tests.
"""

from __future__ import annotations

from optionforge.common.enums import OptionType
from optionforge.kernel.option_contract import OptionContract

from tests.fixtures.strike_fixture import build_strike


def build_contract(
    strike_price: int = 25000,
    option_type: OptionType = OptionType.CALL,
) -> OptionContract:
    """
    Build a reusable OptionContract.
    """

    return OptionContract(
        strike=build_strike(strike_price),
        option_type=option_type,
    )
