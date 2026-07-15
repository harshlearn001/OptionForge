"""
==============================================================
OptionForge
models/strategy_result.py
--------------------------------------------------------------
Strategy Result
==============================================================
"""

from dataclasses import dataclass


@dataclass(slots=True)
class StrategyResult:
    """
    Professional Strategy Intelligence Result
    """

    action: str

    entry_zone: str

    stop_loss: float

    target_1: float

    target_2: float

    risk_reward: float

    trade_quality: str

    confidence: str

    stars: int

    recommendation: str

    interpretation: str
