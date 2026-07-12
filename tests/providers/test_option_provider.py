from unittest.mock import Mock

import pandas as pd

from optionforge.providers.option_provider import (
    OptionProvider,
)


def sample_df():

    return pd.DataFrame(
        {
            "TRADE_DATE": [
                20260101,
                20260101,
                20260102,
            ],
            "EXP_DATE": [
                20260129,
                20260226,
                20260129,
            ],
            "STRIKE_PRICE": [
                25000,
                25000,
                25100,
            ],
        }
    )


# ==========================================================
# Discovery
# ==========================================================


def test_available_trade_dates():

    repo = Mock()

    repo.load.return_value = sample_df()

    provider = OptionProvider(repo)

    dates = provider.available_trade_dates(
        "NIFTY"
    )

    assert dates == [
        20260101,
        20260102,
    ]


def test_expiry_list():

    repo = Mock()

    repo.load.return_value = sample_df()

    provider = OptionProvider(repo)

    expiries = provider.expiry_list(
        "NIFTY"
    )

    assert expiries == [
        20260129,
        20260226,
    ]


# ==========================================================
# Option Chain
# ==========================================================


def test_option_chain_trade_date():

    repo = Mock()

    repo.load.return_value = sample_df()

    provider = OptionProvider(repo)

    chain = provider.option_chain(
        "NIFTY",
        20260101,
    )

    assert len(chain) == 2


def test_option_chain_expiry():

    repo = Mock()

    repo.load.return_value = sample_df()

    provider = OptionProvider(repo)

    chain = provider.option_chain(
        "NIFTY",
        20260101,
        20260129,
    )

    assert len(chain) == 1


def test_option_chain_empty():

    repo = Mock()

    repo.load.return_value = sample_df()

    provider = OptionProvider(repo)

    chain = provider.option_chain(
        "NIFTY",
        20300101,
    )

    assert chain.empty


def test_option_chain_columns():

    repo = Mock()

    repo.load.return_value = sample_df()

    provider = OptionProvider(repo)

    chain = provider.option_chain(
        "NIFTY",
        20260101,
    )

    assert "STRIKE_PRICE" in chain.columns


# ==========================================================
# Misc
# ==========================================================


def test_repository_property():

    repo = Mock()

    provider = OptionProvider(repo)

    assert provider.repository is repo


def test_repr():

    repo = Mock()

    provider = OptionProvider(repo)

    assert "OptionProvider" in repr(provider)

# ==========================================================
# Strike Discovery
# ==========================================================


def test_strikes():

    repo = Mock()

    repo.load.return_value = sample_df()

    provider = OptionProvider(repo)

    strikes = provider.strikes(
        "NIFTY",
        20260101,
        20260129,
    )

    assert strikes == [25000]


def test_strikes_empty():

    repo = Mock()

    repo.load.return_value = sample_df()

    provider = OptionProvider(repo)

    strikes = provider.strikes(
        "NIFTY",
        20300101,
        20300129,
    )

    assert strikes == []