"""
==============================================================
OptionForge
intelligence/iv_rank.py
--------------------------------------------------------------
IV Rank Intelligence Engine
==============================================================
"""

from optionforge.models import IVRankResult


class IVRank:

    @staticmethod
    def calculate(
        *,
        current_iv: float,
        low_iv: float,
        high_iv: float,
    ) -> IVRankResult:

        if high_iv <= low_iv:
            raise ValueError("High IV must be greater than Low IV.")

        iv_rank = ((current_iv - low_iv) / (high_iv - low_iv)) * 100

        iv_rank = max(
            0.0,
            min(100.0, iv_rank),
        )

        if iv_rank < 20:

            status = "VERY LOW"

            interpretation = (
                "Volatility is inexpensive. "
                "Long volatility strategies may become attractive."
            )

        elif iv_rank < 40:

            status = "LOW"

            interpretation = "Volatility is below average."

        elif iv_rank < 60:

            status = "NORMAL"

            interpretation = "Volatility is near its historical average."

        elif iv_rank < 80:

            status = "HIGH"

            interpretation = "Volatility is elevated."

        else:

            status = "VERY HIGH"

            interpretation = (
                "Volatility is expensive. "
                "Premium selling strategies may deserve consideration."
            )

        return IVRankResult(
            current_iv=current_iv,
            low_iv=low_iv,
            high_iv=high_iv,
            iv_rank=iv_rank,
            status=status,
            interpretation=interpretation,
        )
