"""
==============================================================
OptionForge
dashboard/dashboard.py
--------------------------------------------------------------
Professional Live Dashboard
==============================================================
"""

from __future__ import annotations

from optionforge.models import (
    MarketStructureResult,
    ProbabilityResult,
    StrategyResult,
)


class Dashboard:
    """
    Professional Dashboard Generator
    """

    @staticmethod
    def generate(
        market: MarketStructureResult,
        probability: ProbabilityResult,
        strategy: StrategyResult,
    ) -> str:

        dashboard = f"""
╔════════════════════════════════════════════════════════════╗
║                  OPTIONFORGE LIVE DASHBOARD               ║
╠════════════════════════════════════════════════════════════╣

 MARKET STRUCTURE

   Bias              : {market.bias}
   Score             : {market.score:.2f}/100
   Confidence        : {market.confidence}
   Stars             : {'★' * market.stars}

────────────────────────────────────────────────────────────

 PROBABILITY

   Bullish           : {probability.bullish_probability:.2f}%
   Bearish           : {probability.bearish_probability:.2f}%
   Trade Quality     : {probability.trade_quality}
   Risk              : {probability.risk_level}

────────────────────────────────────────────────────────────

 STRATEGY

   Action            : {strategy.action}
   Entry             : {strategy.entry_zone}
   Stop Loss         : {strategy.stop_loss:.2f}

   Target 1          : {strategy.target_1:.2f}
   Target 2          : {strategy.target_2:.2f}

   Risk Reward       : 1 : {strategy.risk_reward:.2f}

────────────────────────────────────────────────────────────

 Recommendation

   {strategy.recommendation}

────────────────────────────────────────────────────────────

 Interpretation

   {strategy.interpretation}

╚════════════════════════════════════════════════════════════╝
"""

        return dashboard.strip()
