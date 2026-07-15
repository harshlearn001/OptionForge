"""
==============================================================
OptionForge
intelligence/oi_shift.py
--------------------------------------------------------------
OI Shift Intelligence Engine
==============================================================
"""

from __future__ import annotations

from optionforge.models import OIShiftResult


class OIShift:
    """
    Open Interest Shift Intelligence
    """

    @staticmethod
    def analyze(
        previous_support: float,
        current_support: float,
        previous_resistance: float,
        current_resistance: float,
    ) -> OIShiftResult:

        # -----------------------------------------
        # Calculate Shifts
        # -----------------------------------------

        support_shift = current_support - previous_support

        resistance_shift = current_resistance - previous_resistance

        # -----------------------------------------
        # Support Direction
        # -----------------------------------------

        if support_shift > 0:

            support_direction = "UP"

        elif support_shift < 0:

            support_direction = "DOWN"

        else:

            support_direction = "UNCHANGED"

        # -----------------------------------------
        # Resistance Direction
        # -----------------------------------------

        if resistance_shift > 0:

            resistance_direction = "UP"

        elif resistance_shift < 0:

            resistance_direction = "DOWN"

        else:

            resistance_direction = "UNCHANGED"

        # -----------------------------------------
        # Market Bias
        # -----------------------------------------

        if support_direction == "UP" and resistance_direction == "DOWN":

            bias = "STRONGLY BULLISH"

        elif support_direction == "DOWN" and resistance_direction == "UP":

            bias = "STRONGLY BEARISH"

        elif support_direction == "UP":

            bias = "BULLISH"

        elif resistance_direction == "DOWN":

            bias = "BULLISH"

        elif support_direction == "DOWN":

            bias = "BEARISH"

        elif resistance_direction == "UP":

            bias = "BEARISH"

        else:

            bias = "NEUTRAL"

        # -----------------------------------------
        # Interpretation
        # -----------------------------------------

        interpretation = (
            f"Support shifted {support_direction}. "
            f"Resistance shifted {resistance_direction}. "
            f"Overall market bias is {bias}."
        )

        return OIShiftResult(
            previous_support=float(previous_support),
            current_support=float(current_support),
            previous_resistance=float(previous_resistance),
            current_resistance=float(current_resistance),
            support_shift=float(support_shift),
            resistance_shift=float(resistance_shift),
            support_direction=support_direction,
            resistance_direction=resistance_direction,
            market_bias=bias,
            interpretation=interpretation,
        )
