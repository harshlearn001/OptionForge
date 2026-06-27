"""
==============================================================
OptionForge
models/iv_rank_result.py
--------------------------------------------------------------
IV Rank Result Model
==============================================================
"""

from dataclasses import dataclass


@dataclass(slots=True)
class IVRankResult:
    """
    Result returned by the IV Rank engine.
    """

    current_iv: float

    low_iv: float

    high_iv: float

    iv_rank: float

    status: str

    interpretation: str