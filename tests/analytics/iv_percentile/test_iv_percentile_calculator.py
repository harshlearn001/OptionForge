from optionforge.analytics.iv_percentile.iv_percentile_calculator import (
    IVPercentileCalculator,
)


def test_percentile():

    value = IVPercentileCalculator.calculate(

        current_iv=30,

        historical_iv=[

            10,
            12,
            18,
            20,
            25,
            28,
            30,
            35,
            40,
            45,

        ],

    )

    assert value == 60.0


def test_empty():

    value = IVPercentileCalculator.calculate(

        current_iv=20,

        historical_iv=[],

    )

    assert value == 0.0


def test_lowest():

    value = IVPercentileCalculator.calculate(

        current_iv=5,

        historical_iv=[

            10,
            20,
            30,

        ],

    )

    assert value == 0.0


def test_highest():

    value = IVPercentileCalculator.calculate(

        current_iv=100,

        historical_iv=[

            10,
            20,
            30,

        ],

    )

    assert value == 100.0


def test_repr():

    calc = IVPercentileCalculator()

    assert "IVPercentileCalculator" in repr(calc)