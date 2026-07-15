from unittest.mock import Mock

import pandas as pd

from optionforge.providers.spot_provider import SpotProvider


def sample_df():

    return pd.DataFrame(
        {
            "DATE": [
                "2026-01-01",
                "2026-01-02",
            ],
            "CLOSE": [
                25000,
                25100,
            ],
        }
    )


def test_history():

    repo = Mock()

    repo.load.return_value = sample_df()

    provider = SpotProvider(repo)

    result = provider.history("NIFTY")

    assert len(result) == 2


def test_latest():

    repo = Mock()

    repo.latest.return_value = sample_df().tail(1)

    provider = SpotProvider(repo)

    result = provider.latest("NIFTY")

    assert len(result) == 1


def test_repository_property():

    repo = Mock()

    provider = SpotProvider(repo)

    assert provider.repository is repo


def test_repr():

    repo = Mock()

    provider = SpotProvider(repo)

    assert "SpotProvider" in repr(provider)
