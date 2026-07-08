"""
============================================================
OptionForge
Future Repository Tests
============================================================
"""

import pandas as pd
import pytest

from optionforge.repository import (
    RepositoryContext,
    FutureRepository,
)

from optionforge.repository.repository_exception import (
    RepositoryNotFoundError,
)


# ==========================================================
# Fixture
# ==========================================================

@pytest.fixture
def repository(tmp_path):

    root = tmp_path / "MarketForge"

    folder = (
        root
        / "data"
        / "master"
        / "Futures_master_three_expiries"
        / "FUTIDX"
    )

    folder.mkdir(parents=True)

    pd.DataFrame(
        {
            "Close": [25000],
            "OI": [150000],
        }
    ).to_csv(
        folder / "NIFTY.csv",
        index=False,
    )

    ctx = RepositoryContext(
        marketforge_root=root,
    )

    return FutureRepository(ctx)


# ==========================================================
# Load
# ==========================================================

def test_load(repository):

    df = repository.load("NIFTY")

    assert isinstance(df, pd.DataFrame)

    assert len(df) == 1


# ==========================================================
# Exists
# ==========================================================

def test_exists(repository):

    assert repository.exists("NIFTY")


# ==========================================================
# Missing
# ==========================================================

def test_missing_symbol(repository):

    with pytest.raises(
        RepositoryNotFoundError,
    ):
        repository.load("INVALID")


# ==========================================================
# Latest
# ==========================================================

def test_latest(repository):

    df = repository.latest("NIFTY")

    assert len(df) == 1


# ==========================================================
# Deterministic
# ==========================================================

def test_deterministic(repository):

    first = repository.load("NIFTY")

    second = repository.load("NIFTY")

    pd.testing.assert_frame_equal(
        first,
        second,
    )