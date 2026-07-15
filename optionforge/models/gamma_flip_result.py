"""
==============================================================
OptionForge
models/gamma_flip_result.py
--------------------------------------------------------------
Gamma Flip Result
==============================================================
"""

from dataclasses import dataclass


@dataclass(slots=True)
class GammaFlipResult:
    """
    Professional Gamma Flip Result.
    """

    gamma_flip: float

    current_spot: float

    distance: float

    flip_status: str

    dealer_regime: str

    interpretation: str
