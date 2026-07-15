"""
==============================================================
OptionForge
Market Regime Engine
==============================================================

Combines regime classification and confidence into a
single immutable RegimeResult.

Author
------
OptionForge Engineering Team
==============================================================
"""

from __future__ import annotations

from optionforge.common.enums import TrendDirection

from optionforge.intelligence.enums.dealer_state import (
    DealerState,
)
from optionforge.intelligence.enums.institutional_state import (
    InstitutionalState,
)
from optionforge.intelligence.enums.volatility_state import (
    VolatilityState,
)

from optionforge.regime.regime_classifier import (
    RegimeClassifier,
)
from optionforge.regime.regime_result import (
    RegimeResult,
)
from optionforge.regime.regime_score import (
    RegimeScore,
)


class RegimeEngine:
    """
    Market Regime Engine.
    """

    def __init__(
        self,
        *,
        institutional_state: InstitutionalState,
        trend: TrendDirection,
        volatility: VolatilityState,
        dealer_state: DealerState,
        institutional_score: float,
        trend_score: float,
        dealer_score: float,
        volatility_score: float,
    ) -> None:

        self.institutional_state = institutional_state
        self.trend = trend
        self.volatility = volatility
        self.dealer_state = dealer_state

        self.institutional_score = institutional_score
        self.trend_score = trend_score
        self.dealer_score = dealer_score
        self.volatility_score = volatility_score

    # ==========================================================
    # Calculate
    # ==========================================================

    def calculate(self) -> RegimeResult:

        regime = RegimeClassifier.classify(

            institutional_state=self.institutional_state,

            trend=self.trend,

            volatility=self.volatility,

            dealer_state=self.dealer_state,

        )

        confidence = RegimeScore(

            institutional=self.institutional_score,

            trend=self.trend_score,

            dealer=self.dealer_score,

            volatility=self.volatility_score,

        ).calculate()

        return RegimeResult(

            regime=regime,

            confidence=confidence,

        )

    # ==========================================================
    # Representation
    # ==========================================================

    def __repr__(self) -> str:

        return (

            "RegimeEngine("

            f"institutional_state={self.institutional_state.name}, "

            f"trend={self.trend.name}, "

            f"volatility={self.volatility.name}, "

            f"dealer_state={self.dealer_state.name})"

        )