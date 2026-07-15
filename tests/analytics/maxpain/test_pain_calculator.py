import pandas as pd

from optionforge.analytics.maxpain.pain_calculator import (
    PainCalculator,
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
                200,
                300,
                150,
                250,
                350,
            ],
        }
    )


def test_calculate():

    calc = PainCalculator(
        sample_chain(),
    )

    result = calc.calculate()

    assert len(result) == 3

    assert "CALL_PAIN" in result.columns

    assert "PUT_PAIN" in result.columns

    assert "TOTAL_PAIN" in result.columns


def test_repr():

    calc = PainCalculator(
        sample_chain(),
    )

    assert "PainCalculator" in repr(calc)
