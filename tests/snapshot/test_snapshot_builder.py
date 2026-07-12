from unittest.mock import Mock

import pandas as pd

from optionforge.snapshot.snapshot_builder import (
    SnapshotBuilder,
)


def option_df():

    return pd.DataFrame(
        {
            "STRIKE_PRICE": [
                25000,
                25100,
            ]
        }
    )


def spot_df():

    return pd.DataFrame(
        {
            "CLOSE": [25050]
        }
    )


def builder():

    option_provider = Mock()

    spot_provider = Mock()

    option_provider.option_chain.return_value = option_df()

    spot_provider.latest.return_value = spot_df()

    return SnapshotBuilder(
        option_provider,
        spot_provider,
    )


# =====================================================


def test_build():

    snapshot = builder().build(

        symbol="NIFTY",

        trade_date=20260101,

        expiry=20260129,

    )

    assert snapshot.symbol == "NIFTY"


def test_option_chain_loaded():

    snapshot = builder().build(

        "NIFTY",

        20260101,

        20260129,

    )

    assert len(snapshot.option_chain) == 2


def test_spot_loaded():

    snapshot = builder().build(

        "NIFTY",

        20260101,

        20260129,

    )

    assert snapshot.spot.iloc[0]["CLOSE"] == 25050


def test_repr():

    b = builder()

    assert "SnapshotBuilder" in repr(b)


def test_option_provider_property():

    b = builder()

    assert b.option_provider is not None


def test_spot_provider_property():

    b = builder()

    assert b.spot_provider is not None