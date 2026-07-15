"""
==============================================================
OptionForge
models/market_structure_result.py
--------------------------------------------------------------
Market Structure Result
==============================================================
"""

from dataclasses import dataclass


@dataclass(slots=True)
class MarketStructureResult:
    """
    Overall Market Structure Intelligence
    """

    score: float

    bias: str

    confidence: str

    stars: int

    recommendation: str

    support_strength: float

    resistance_strength: float

    expected_move: float

    iv_rank: float

    iv_percentile: float

    max_pain: float

    interpretation: str
