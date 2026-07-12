from dataclasses import FrozenInstanceError

import pandas as pd

from optionforge.analytics.base_engine import (
    AnalyticsEngine,
)

from optionforge.snapshot.institutional_snapshot import (
    InstitutionalSnapshot,
)


class DummyEngine(AnalyticsEngine):

    def calculate(self, snapshot):

        return snapshot.symbol


def snapshot():

    return InstitutionalSnapshot(

        symbol="NIFTY",

        trade_date=20260101,

        expiry=20260129,

        spot=pd.DataFrame(
            {"CLOSE": [25000]}
        ),

        option_chain=pd.DataFrame(
            {
                "STRIKE_PRICE": [
                    25000
                ]
            }
        ),
    )


# ---------------------------------------------------------


def test_engine_name():

    engine = DummyEngine()

    assert engine.name == "DummyEngine"


# ---------------------------------------------------------


def test_repr():

    engine = DummyEngine()

    assert "DummyEngine" in repr(engine)


# ---------------------------------------------------------


def test_calculate():

    engine = DummyEngine()

    assert (
        engine.calculate(snapshot())
        == "NIFTY"
    )