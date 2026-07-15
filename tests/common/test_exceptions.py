"""
Tests for optionforge.common.exceptions
"""

import pytest

from optionforge.common.exceptions import (
    InvalidContractError,
    InvalidExpiryError,
    InvalidStrikeError,
    InvalidSymbolError,
    InvalidTradingSessionError,
    MarketClosedError,
    MarketError,
    OptionForgeError,
    PricingError,
    ValidationError,
)


def test_exception_hierarchy():
    """Verify exception inheritance."""

    assert issubclass(ValidationError, OptionForgeError)
    assert issubclass(MarketError, OptionForgeError)

    assert issubclass(InvalidSymbolError, ValidationError)
    assert issubclass(InvalidExpiryError, ValidationError)
    assert issubclass(InvalidStrikeError, ValidationError)
    assert issubclass(InvalidContractError, ValidationError)

    assert issubclass(MarketClosedError, MarketError)
    assert issubclass(InvalidTradingSessionError, MarketError)

    assert issubclass(PricingError, OptionForgeError)


@pytest.mark.parametrize(
    "exception_cls",
    [
        InvalidSymbolError,
        InvalidExpiryError,
        InvalidStrikeError,
        InvalidContractError,
        MarketClosedError,
        InvalidTradingSessionError,
        PricingError,
    ],
)
def test_exception_messages(exception_cls):
    """Verify exception message is preserved."""

    message = "Test Error"

    with pytest.raises(exception_cls, match=message):
        raise exception_cls(message)
