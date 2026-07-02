"""
Reusable Expiry fixture.

Used by all OptionForge tests.
"""

from __future__ import annotations

from datetime import date

from optionforge.common.enums import ExpiryType
from optionforge.kernel.expiry import Expiry

from tests.fixtures.symbol_fixture import (
    build_symbol,
)


def build_expiry() -> Expiry:
    """
    Build a reusable weekly expiry.
    """

    return Expiry(
        symbol=build_symbol(),
        expiry_date=date(2026, 7, 2),
        expiry_type=ExpiryType.WEEKLY,
    )