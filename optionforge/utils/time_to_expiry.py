"""
============================================================
OptionForge
Time To Expiry Utility
============================================================
"""

from __future__ import annotations

from datetime import datetime

DATE_FORMAT = "%Y%m%d"


class TimeToExpiry:
    """
    Utility for converting trade date and expiry
    into year fraction.
    """

    DAYS_PER_YEAR = 365.0

    @classmethod
    def years(
        cls,
        trade_date: int,
        expiry: int,
    ) -> float:

        trade = datetime.strptime(
            str(trade_date),
            DATE_FORMAT,
        )

        exp = datetime.strptime(
            str(expiry),
            DATE_FORMAT,
        )

        days = (exp - trade).days

        return (
            max(
                days,
                0,
            )
            / cls.DAYS_PER_YEAR
        )

    @classmethod
    def days(
        cls,
        trade_date: int,
        expiry: int,
    ) -> int:

        trade = datetime.strptime(
            str(trade_date),
            DATE_FORMAT,
        )

        exp = datetime.strptime(
            str(expiry),
            DATE_FORMAT,
        )

        return max(
            (exp - trade).days,
            0,
        )

    def __repr__(self):

        return "TimeToExpiry()"

    __str__ = __repr__
