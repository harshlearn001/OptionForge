import pandas as pd

import pytest

from optionforge.snapshot.institutional_snapshot import (
    InstitutionalSnapshot,
)


def option_df():

    return pd.DataFrame(
        {
            "STRIKE_PRICE": [
                25000,
                25100,
                25100,
            ]
        }
    )


def spot_df():

    return pd.DataFrame({"CLOSE": [25050]})


def test_creation():

    snapshot = InstitutionalSnapshot(
        symbol="NIFTY",
        trade_date=20260101,
        expiry=20260129,
        spot=spot_df(),
        option_chain=option_df(),
    )

    assert snapshot.symbol == "NIFTY"


def test_contract_count():

    snapshot = InstitutionalSnapshot(
        symbol="NIFTY",
        trade_date=20260101,
        expiry=20260129,
        spot=spot_df(),
        option_chain=option_df(),
    )

    assert snapshot.contract_count == 3


def test_strike_count():

    snapshot = InstitutionalSnapshot(
        symbol="NIFTY",
        trade_date=20260101,
        expiry=20260129,
        spot=spot_df(),
        option_chain=option_df(),
    )

    assert snapshot.strike_count == 2


def test_has_vix_false():

    snapshot = InstitutionalSnapshot(
        symbol="NIFTY",
        trade_date=20260101,
        expiry=20260129,
        spot=spot_df(),
        option_chain=option_df(),
    )

    assert snapshot.has_vix is False


def test_has_vix_true():

    snapshot = InstitutionalSnapshot(
        symbol="NIFTY",
        trade_date=20260101,
        expiry=20260129,
        spot=spot_df(),
        option_chain=option_df(),
        vix=pd.DataFrame({"CLOSE": [13.2]}),
    )

    assert snapshot.has_vix is True


def test_snapshot_is_frozen():

    snapshot = InstitutionalSnapshot(
        symbol="NIFTY",
        trade_date=20260101,
        expiry=20260129,
        spot=spot_df(),
        option_chain=option_df(),
    )

    with pytest.raises(Exception):

        snapshot.symbol = "BANKNIFTY"


def test_repr():

    snapshot = InstitutionalSnapshot(
        symbol="NIFTY",
        trade_date=20260101,
        expiry=20260129,
        spot=spot_df(),
        option_chain=option_df(),
    )

    assert "InstitutionalSnapshot" in repr(snapshot)
