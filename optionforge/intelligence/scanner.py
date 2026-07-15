"""
==============================================================
OptionForge
intelligence/scanner.py
--------------------------------------------------------------
Professional Market Scanner
==============================================================
"""

from __future__ import annotations

from optionforge.models import (
    ProbabilityResult,
    StrategyResult,
    ScannerResult,
)


class Scanner:
    """
    Professional Market Scanner
    """

    @staticmethod
    def calculate(
        symbol: str,
        probability: ProbabilityResult,
        strategy: StrategyResult,
    ) -> ScannerResult:

        score = probability.bullish_probability

        recommendation = strategy.recommendation

        return ScannerResult(
            symbol=symbol,
            market_score=round(score, 2),
            bullish_probability=round(
                probability.bullish_probability,
                2,
            ),
            action=strategy.action,
            trade_quality=strategy.trade_quality,
            confidence=strategy.confidence,
            stars=strategy.stars,
            rank=0,
            recommendation=recommendation,
        )
