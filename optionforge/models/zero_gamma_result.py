"""
==============================================================
OptionForge
models/zero_gamma_result.py
--------------------------------------------------------------
Zero Gamma Result
==============================================================
"""

from dataclasses import dataclass


@dataclass(slots=True)
class ZeroGammaResult:
    """
    Professional Zero Gamma Result.
    """

    zero_gamma: float

    current_spot: float

    distance: float

    status: str

    dealer_regime: str

    interpretation: str