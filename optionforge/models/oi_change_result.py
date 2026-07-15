"""
==============================================================
OptionForge
models/oi_change_result.py
--------------------------------------------------------------
OI Change Intelligence Result
==============================================================
"""

from dataclasses import dataclass


@dataclass(slots=True)
class OIChangeResult:
    """
    Open Interest Change Intelligence
    """

    strike: float

    option_type: str

    price_change: float

    oi_change: int

    classification: str

    sentiment: str

    interpretation: str
