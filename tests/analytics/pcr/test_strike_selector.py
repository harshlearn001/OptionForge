import pandas as pd

from optionforge.analytics.pcr.strike_selector import (
    StrikeSelector,
)


def sample_df():

    return pd.DataFrame(
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


def test_available_strikes():

    selector = StrikeSelector(sample_df())

    assert selector.available_strikes() == [
        19400,
        19500,
        19600,
    ]


def test_atm():

    selector = StrikeSelector(sample_df())

    assert selector.atm_strike(19520) == 19500


def test_major_call():

    selector = StrikeSelector(sample_df())

    assert selector.major_call_strike() == 19500


def test_major_put():

    selector = StrikeSelector(sample_df())

    assert selector.major_put_strike() == 19500


def test_nearest():

    selector = StrikeSelector(sample_df())

    strikes = selector.nearest_strikes(
        19500,
        count=1,
    )

    assert strikes == [
        19400,
        19500,
        19600,
    ]


def test_repr():

    selector = StrikeSelector(sample_df())

    assert "StrikeSelector" in repr(selector)
