"""
Reusable Strike fixture.

Used by all OptionForge tests.
"""

from __future__ import annotations

from optionforge.kernel.strike import Strike

from tests.fixtures.expiry_fixture import (
    build_expiry,
)


def build_strike(
    strike_price: int = 25000,
) -> Strike:
    """
    Build a reusable strike.
    """

    return Strike(
        expiry=build_expiry(),
        strike_price=strike_price,
    )