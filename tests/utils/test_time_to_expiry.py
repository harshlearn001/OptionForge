from optionforge.utils.time_to_expiry import (
    TimeToExpiry,
)


def test_days():

    assert (
        TimeToExpiry.days(
            20260714,
            20260721,
        )
        == 7
    )


def test_years():

    value = TimeToExpiry.years(
        20260714,
        20260721,
    )

    assert abs(value - (7 / 365)) < 1e-8


def test_zero():

    assert (
        TimeToExpiry.days(
            20260714,
            20260714,
        )
        == 0
    )
