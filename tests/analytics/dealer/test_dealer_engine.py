import pandas as pd

from optionforge.analytics.dealer.dealer_engine import (
    DealerEngine,
)


class Snapshot:

    symbol = "NIFTY"

    trade_date = 20260714

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
                250,
                150,

                200,
                300,
                250,

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

    engine = DealerEngine()

    result = engine.calculate(

        Snapshot(),

    )

    assert result.symbol == "NIFTY"

    assert result.total_call_oi == 500

    assert result.total_put_oi == 750

    assert result.major_call_strike == 110

    assert result.major_put_strike == 110

    assert result.dealer_bias == "Bullish"

    assert result.contracts == 6


def test_repr():

    engine = DealerEngine()

    assert "DealerEngine" in repr(engine)