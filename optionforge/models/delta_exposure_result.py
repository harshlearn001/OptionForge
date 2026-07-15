"""
==============================================================
OptionForge
models/delta_exposure_result.py
--------------------------------------------------------------
Delta Exposure Result
==============================================================
"""

from dataclasses import dataclass


@dataclass(slots=True)
class DeltaExposureResult:
    """
    Professional Delta Exposure Result.
    """

    total_call_dex: float

    total_put_dex: float

    net_dex: float

    largest_positive_strike: float

    largest_negative_strike: float

    dealer_position: str

    interpretation: str
