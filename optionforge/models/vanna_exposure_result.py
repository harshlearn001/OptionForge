"""
==============================================================
OptionForge
models/vanna_exposure_result.py
--------------------------------------------------------------
Vanna Exposure Result
==============================================================
"""

from dataclasses import dataclass


@dataclass(slots=True)
class VannaExposureResult:
    """
    Professional Vanna Exposure Result.
    """

    total_call_vanna: float

    total_put_vanna: float

    net_vanna: float

    largest_positive_strike: float

    largest_negative_strike: float

    vanna_regime: str

    interpretation: str
