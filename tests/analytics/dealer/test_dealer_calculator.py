import pandas as pd

from optionforge.analytics.dealer.dealer_calculator import (
    DealerCalculator,
)


def sample_chain():

    return pd.DataFrame(

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


def test_total_call_oi():

    calc = DealerCalculator(

        sample_chain(),

    )

    assert calc.total_call_oi() == 500


def test_total_put_oi():

    calc = DealerCalculator(

        sample_chain(),

    )

    assert calc.total_put_oi() == 750


def test_major_call_strike():

    calc = DealerCalculator(

        sample_chain(),

    )

    assert calc.major_call_strike() == 110


def test_major_put_strike():

    calc = DealerCalculator(

        sample_chain(),

    )

    assert calc.major_put_strike() == 110


def test_difference():

    calc = DealerCalculator(

        sample_chain(),

    )

    assert calc.call_put_difference() == 250


def test_repr():

    calc = DealerCalculator(

        sample_chain(),

    )

    assert "DealerCalculator" in repr(calc)