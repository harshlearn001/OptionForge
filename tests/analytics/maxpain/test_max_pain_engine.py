import pandas as pd

from optionforge.analytics.maxpain.max_pain_engine import (
    MaxPainEngine,
)


class Snapshot:

    symbol = "NIFTY"

    trade_date = 20260713

    expiry = 20260716

    option_chain = pd.DataFrame(

        {

            "STRIKE_PRICE": [

                100,
                110,
                120,

                100,
                110,
                120,

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
                200,
                300,

                150,
                250,
                350,

            ],

        }

    )

    spot = pd.DataFrame(

        {

            "CLOSE": [

                112.5,

            ]

        }

    )


def test_engine():

    engine = MaxPainEngine()

    result = engine.calculate(

        Snapshot(),

    )

    assert result.symbol == "NIFTY"

    assert result.contracts == 6

    assert result.max_pain_strike in [

        100,
        110,
        120,

    ]


def test_repr():

    engine = MaxPainEngine()

    assert "MaxPainEngine" in repr(engine)