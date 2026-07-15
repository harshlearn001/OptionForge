from unittest.mock import Mock

import pandas as pd

from optionforge.providers.market_provider import (
    MarketProvider,
)


class DummyProvider(MarketProvider):
    """
    Concrete provider for testing.
    """

    pass


def test_repository_property():

    repo = Mock()

    provider = DummyProvider(repo)

    assert provider.repository is repo


def test_exists():

    repo = Mock()

    repo.exists.return_value = True

    provider = DummyProvider(repo)

    assert provider.exists("NIFTY")

    repo.exists.assert_called_once()


def test_latest():

    df = pd.DataFrame({"A": [1]})

    repo = Mock()

    repo.latest.return_value = df

    provider = DummyProvider(repo)

    result = provider.latest("NIFTY")

    assert result.equals(df)


def test_history():

    df = pd.DataFrame({"A": [1]})

    repo = Mock()

    repo.load.return_value = df

    provider = DummyProvider(repo)

    result = provider.history("NIFTY")

    assert result.equals(df)


def test_repr():

    repo = Mock()

    provider = DummyProvider(repo)

    assert "DummyProvider" in repr(provider)
