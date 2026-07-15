import pandas as pd

from optionforge.analytics.pcr.oi_calculator import (
    OICalculator,
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


def test_total_call():

    calc = OICalculator(sample_df())

    assert calc.total_call_oi() == 900


def test_total_put():

    calc = OICalculator(sample_df())

    assert calc.total_put_oi() == 1300


def test_call_oi():

    calc = OICalculator(sample_df())

    assert calc.call_oi(19500) == 500


def test_put_oi():

    calc = OICalculator(sample_df())

    assert calc.put_oi(19500) == 700


def test_max_call():

    calc = OICalculator(sample_df())

    assert calc.max_call_oi() == 500


def test_max_put():

    calc = OICalculator(sample_df())

    assert calc.max_put_oi() == 700


def test_classic_pcr():

    calc = OICalculator(sample_df())

    assert calc.classic_pcr() == round(1300 / 900, 4)


def test_repr():

    calc = OICalculator(sample_df())

    assert "OICalculator" in repr(calc)
