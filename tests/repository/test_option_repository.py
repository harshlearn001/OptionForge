"""
============================================================
OptionForge
Option Repository Tests
============================================================
"""

from pathlib import Path

import pandas as pd

import pytest

from optionforge.repository import (
    RepositoryContext,
    OptionRepository,
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
        / "Options_master"
        / "INDICES"

    )

    folder.mkdir(parents=True)

    pd.DataFrame(

        {

            "Strike": [25000],

            "OI": [1000],

        }

    ).to_parquet(

        folder / "NIFTY.parquet",

    )

    ctx = RepositoryContext(

        marketforge_root=root,

    )

    return OptionRepository(ctx)


# ==========================================================
# Load
# ==========================================================

def test_load(repository):

    df = repository.load(

        "NIFTY",

    )

    assert isinstance(

        df,

        pd.DataFrame,

    )

    assert len(df) == 1


# ==========================================================
# Exists
# ==========================================================

def test_exists(repository):

    assert repository.exists(

        "NIFTY",

    )


# ==========================================================
# Missing
# ==========================================================

def test_missing_symbol(repository):

    with pytest.raises(

        RepositoryNotFoundError,

    ):

        repository.load(

            "INVALID",

        )


# ==========================================================
# Latest
# ==========================================================

def test_latest(repository):

    df = repository.latest(

        "NIFTY",

    )

    assert len(df) == 1


# ==========================================================
# Deterministic
# ==========================================================

def test_deterministic(repository):

    first = repository.load(

        "NIFTY",

    )

    second = repository.load(

        "NIFTY",

    )

    pd.testing.assert_frame_equal(

        first,

        second,

    )