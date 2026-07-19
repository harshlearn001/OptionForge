"""
============================================================
OptionForge
Snapshot Builder Latest Tests
============================================================
"""

import pandas as pd

from optionforge.snapshot.institutional_snapshot_builder import (
    SnapshotBuilder,
)

# ============================================================
# Dummy Providers
# ============================================================


class DummyOptionProvider:

    def latest_trade_date(self, symbol):

        return 20201228

    def latest_expiry(self, symbol, trade_date):

        return 20201231

    def option_chain(
        self,
        symbol,
        trade_date,
        expiry,
    ):

        return pd.DataFrame(
            {
                "TRADE_DATE": [trade_date],
                "EXP_DATE": [expiry],
                "STRIKE_PRICE": [19500],
                "OPT_TYPE": ["CE"],
                "OPEN_INT": [1000],
            }
        )


class DummySpotProvider:

    def latest(self, symbol):

        return pd.DataFrame(
            {
                "TRADE_DATE": [20201228],
                "SYMBOL": [symbol],
                "CLOSE": [19520.0],
            }
        )


# ============================================================
# Tests
# ============================================================


def test_build_latest():

    builder = SnapshotBuilder(
        DummyOptionProvider(),
        DummySpotProvider(),
    )

    snapshot = builder.build_latest(
        "NIFTY",
    )

    assert snapshot.symbol == "NIFTY"

    assert snapshot.trade_date == 20201228

    assert snapshot.expiry == 20201231

    assert len(snapshot.option_chain) == 1

    assert len(snapshot.spot) == 1


def test_repr():

    builder = SnapshotBuilder(
        DummyOptionProvider(),
        DummySpotProvider(),
    )

    assert "SnapshotBuilder" in repr(builder)
