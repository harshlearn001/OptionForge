import pandas as pd

from optionforge.analytics.modified_pcr import (
    ModifiedPCREngine,
)

from optionforge.snapshot.institutional_snapshot import (
    InstitutionalSnapshot,
)


def snapshot():

    option_chain = pd.DataFrame(

        {

            "OPT_TYPE": [
                "CE",
                "CE",
                "PE",
                "PE",
            ],

            "OPEN_INT": [
                100,
                300,
                200,
                400,
            ],

            "STRIKE_PRICE": [
                25000,
                25100,
                25000,
                25100,
            ],

        }

    )

    return InstitutionalSnapshot(

        symbol="NIFTY",

        trade_date=20260101,

        expiry=20260129,

        spot=pd.DataFrame(
            {"CLOSE": [25050]}
        ),

        option_chain=option_chain,

    )


def test_calculate():

    engine = ModifiedPCREngine()

    result = engine.calculate(
        snapshot()
    )

    assert result.call_oi == 400

    assert result.put_oi == 600

    assert result.pcr == 1.5

    assert result.contracts == 4


def test_symbol():

    engine = ModifiedPCREngine()

    result = engine.calculate(
        snapshot()
    )

    assert result.symbol == "NIFTY"


def test_engine_name():

    engine = ModifiedPCREngine()

    assert engine.name == "ModifiedPCREngine"