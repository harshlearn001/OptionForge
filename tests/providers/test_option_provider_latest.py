"""
============================================================
OptionForge
Option Provider Latest Tests
============================================================

Tests automatic latest trade date and expiry discovery.

============================================================
"""

from pathlib import Path

from optionforge.repository.repository_context import (
    RepositoryContext,
)

from optionforge.repository.option_repository import (
    OptionRepository,
)

from optionforge.providers.option_provider import (
    OptionProvider,
)


# ============================================================
# Test Setup
# ============================================================

MARKETFORGE_ROOT = Path(r"H:\MarketForge")

context = RepositoryContext(

    marketforge_root=MARKETFORGE_ROOT,

    use_parquet=True,

    use_cache=True,

    validate_schema=True,

)

repository = OptionRepository(context)

provider = OptionProvider(repository)


# ============================================================
# Tests
# ============================================================

def test_trade_dates():
    """
    Provider should return sorted trade dates.
    """

    dates = provider.trade_dates("NIFTY")

    assert len(dates) > 0

    assert dates == sorted(dates)

    assert isinstance(dates[0], int)

    assert isinstance(dates[-1], int)


# ------------------------------------------------------------

def test_latest_trade_date():
    """
    Latest trade date should equal the maximum trade date.
    """

    dates = provider.trade_dates("NIFTY")

    latest = provider.latest_trade_date("NIFTY")

    assert latest == max(dates)


# ------------------------------------------------------------

def test_expiries():
    """
    Expiry list should be sorted.
    """

    latest = provider.latest_trade_date("NIFTY")

    expiries = provider.expiries(

        "NIFTY",

        latest,

    )

    assert len(expiries) > 0

    assert expiries == sorted(expiries)

    assert isinstance(expiries[0], int)

    assert isinstance(expiries[-1], int)


# ------------------------------------------------------------

def test_latest_expiry():
    """
    latest_expiry() should return the nearest expiry
    (first expiry in sorted order).
    """

    latest = provider.latest_trade_date("NIFTY")

    expiries = provider.expiries(

        "NIFTY",

        latest,

    )

    expiry = provider.latest_expiry(

        "NIFTY",

        latest,

    )

    assert expiry == expiries[0]


# ------------------------------------------------------------

def test_option_chain_latest():
    """
    Latest option chain should not be empty.
    """

    trade_date = provider.latest_trade_date("NIFTY")

    expiry = provider.latest_expiry(

        "NIFTY",

        trade_date,

    )

    chain = provider.option_chain(

        "NIFTY",

        trade_date,

        expiry,

    )

    assert len(chain) > 0

    assert "TRADE_DATE" in chain.columns

    assert "EXP_DATE" in chain.columns

    assert "OPEN_INT" in chain.columns

    assert "OPT_TYPE" in chain.columns


# ------------------------------------------------------------

def test_invalid_symbol():

    try:

        provider.trade_dates("INVALID_SYMBOL")

    except Exception:

        return

    assert False, "Expected an exception for invalid symbol."


# ------------------------------------------------------------

def test_repr():

    assert "OptionProvider" in repr(provider)