"""
==============================================================
OptionForge
models/oi_wall_result.py
--------------------------------------------------------------
Open Interest Wall Result Model
==============================================================
"""

from dataclasses import dataclass


@dataclass(slots=True)
class OIWallResult:
    """
    Open Interest Wall Analysis Result
    """

    strongest_support: float

    strongest_resistance: float

    support_oi: int

    resistance_oi: int

    total_put_oi: int

    total_call_oi: int

    put_call_ratio: float

    market_bias: str

    interpretation: str
