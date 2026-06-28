"""
==============================================================
OptionForge
models/scanner_result.py
--------------------------------------------------------------
Scanner Result
==============================================================
"""

from dataclasses import dataclass


@dataclass(slots=True)
class ScannerResult:
    """
    Professional Scanner Result
    """

    symbol: str

    market_score: float

    bullish_probability: float

    action: str

    trade_quality: str

    confidence: str

    stars: int

    rank: int

    recommendation: str