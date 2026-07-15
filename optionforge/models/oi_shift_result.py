"""
==============================================================
OptionForge
models/oi_shift_result.py
--------------------------------------------------------------
Open Interest Shift Intelligence Result
==============================================================
"""

from dataclasses import dataclass


@dataclass(slots=True)
class OIShiftResult:
    """
    OI Shift Intelligence
    """

    previous_support: float

    current_support: float

    previous_resistance: float

    current_resistance: float

    support_shift: float

    resistance_shift: float

    support_direction: str

    resistance_direction: str

    market_bias: str

    interpretation: str
