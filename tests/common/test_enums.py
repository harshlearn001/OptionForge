"""
Tests for optionforge.common.enums
"""

from optionforge.common.enums import (
    Exchange,
    ExpiryType,
    InstrumentType,
    MarketStatus,
    OptionType,
)


def test_exchange_values():
    assert Exchange.NSE.value == "NSE"
    assert Exchange.BSE.value == "BSE"


def test_instrument_type_values():
    assert InstrumentType.EQUITY.value == "EQUITY"
    assert InstrumentType.INDEX.value == "INDEX"
    assert InstrumentType.FUTURE.value == "FUTURE"
    assert InstrumentType.OPTION.value == "OPTION"


def test_option_type_values():
    assert OptionType.CALL.value == "CALL"
    assert OptionType.PUT.value == "PUT"


def test_option_type_short_name():
    assert OptionType.CALL.short_name == "CE"
    assert OptionType.PUT.short_name == "PE"


def test_expiry_type_values():
    assert ExpiryType.WEEKLY.value == "WEEKLY"
    assert ExpiryType.MONTHLY.value == "MONTHLY"


def test_market_status_values():
    assert MarketStatus.PRE_OPEN.value == "PRE_OPEN"
    assert MarketStatus.OPEN.value == "OPEN"
    assert MarketStatus.CLOSED.value == "CLOSED"
    assert MarketStatus.POST_CLOSE.value == "POST_CLOSE"
    assert MarketStatus.HOLIDAY.value == "HOLIDAY"


def test_enum_string_behavior():
    assert str(Exchange.NSE) == "NSE"
    assert str(OptionType.CALL) == "CALL"
    assert str(MarketStatus.OPEN) == "OPEN"


def test_enum_uniqueness():
    assert Exchange.NSE != Exchange.BSE
    assert OptionType.CALL != OptionType.PUT
