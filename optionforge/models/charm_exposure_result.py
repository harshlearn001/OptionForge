"""
==============================================================
OptionForge
models/charm_exposure_result.py
--------------------------------------------------------------
Charm Exposure Result
==============================================================
"""

from dataclasses import dataclass


@dataclass(slots=True)
class CharmExposureResult:
    """
    Professional Charm Exposure Result.
    """

    total_call_charm: float

    total_put_charm: float

    net_charm: float

    largest_positive_strike: float

    largest_negative_strike: float

    charm_regime: str

    interpretation: str