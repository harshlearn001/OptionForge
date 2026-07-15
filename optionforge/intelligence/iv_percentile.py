"""
==============================================================
OptionForge
intelligence/iv_percentile.py
--------------------------------------------------------------
IV Percentile Intelligence Engine
==============================================================
"""

from optionforge.models import IVPercentileResult


class IVPercentile:

    @staticmethod
    def calculate(
        *,
        current_iv: float,
        historical_iv: list[float],
    ) -> IVPercentileResult:

        if len(historical_iv) == 0:
            raise ValueError("Historical IV data cannot be empty.")

        below = sum(1 for iv in historical_iv if iv < current_iv)

        observations = len(historical_iv)

        percentile = (below / observations) * 100

        if percentile < 20:

            status = "VERY LOW"

            interpretation = "Current IV is lower than most historical observations."

        elif percentile < 40:

            status = "LOW"

            interpretation = "Current IV is below average."

        elif percentile < 60:

            status = "NORMAL"

            interpretation = "Current IV is near its historical average."

        elif percentile < 80:

            status = "HIGH"

            interpretation = "Current IV is above average."

        else:

            status = "VERY HIGH"

            interpretation = "Current IV is higher than most historical observations."

        return IVPercentileResult(
            current_iv=current_iv,
            observations=observations,
            below_count=below,
            iv_percentile=percentile,
            status=status,
            interpretation=interpretation,
        )
