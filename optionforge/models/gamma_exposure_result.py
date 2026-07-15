"""
==============================================================
OptionForge
models/gamma_exposure_result.py
--------------------------------------------------------------
Gamma Exposure Result
==============================================================
"""

from dataclasses import dataclass


@dataclass(slots=True)
class GammaExposureResult:
    """
    Professional Gamma Exposure Result.
    """

    total_call_gex: float

    total_put_gex: float

    net_gex: float

    largest_positive_strike: float

    largest_negative_strike: float

    gamma_flip: float

    market_regime: str

    interpretation: str
