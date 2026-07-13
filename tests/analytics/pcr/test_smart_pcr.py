import pandas as pd

from optionforge.analytics.pcr.smart_pcr import (
    SmartPCR,
)


class Snapshot:

    symbol = "NIFTY"

    trade_date = 20201228

    expiry = 20201231

    option_chain = pd.DataFrame(

        {

            "STRIKE_PRICE": [

                19400,
                19500,
                19600,

                19400,
                19500,
                19600,

            ],

            "OPT_TYPE": [

                "CE",
                "CE",
                "CE",

                "PE",
                "PE",
                "PE",

            ],

            "OPEN_INT": [

                100,
                500,
                300,

                200,
                700,
                400,

            ],

        }

    )

    spot = pd.DataFrame(

        {

            "CLOSE": [

                19520,

            ]

        }

    )


def test_engine():

    engine = SmartPCR()

    result = engine.calculate(

        Snapshot(),

    )

    assert result.symbol == "NIFTY"

    assert result.atm_strike == 19500

    assert result.major_call_strike == 19500

    assert result.major_put_strike == 19500

    assert result.classic_pcr > 1

    assert result.weighted_pcr > 1


def test_repr():

    engine = SmartPCR()

    assert "SmartPCR" in repr(engine)