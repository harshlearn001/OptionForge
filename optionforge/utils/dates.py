from datetime import date

class DateUtils:

    @staticmethod
    def year_fraction(
        trade_date: date,
        expiry_date: date,
    ) -> float:

        return (expiry_date - trade_date).days / 365.0