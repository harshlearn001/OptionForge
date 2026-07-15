"""
==============================================================
OptionForge
models/iv_percentile_result.py
--------------------------------------------------------------
IV Percentile Result Model
==============================================================
"""

from dataclasses import dataclass


@dataclass(slots=True)
class IVPercentileResult:
    """
    Result returned by the IV Percentile engine.
    """

    current_iv: float

    observations: int

    below_count: int

    iv_percentile: float

    status: str

    interpretation: str
