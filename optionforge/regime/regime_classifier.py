"""
==============================================================
OptionForge
Market Regime Classifier
==============================================================

Classifies the overall market regime using multiple
independent intelligence inputs.

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


from optionforge.regime.enums.regime_state import (
    RegimeState,
)


class RegimeClassifier:
    """
    Multi-factor market regime classifier.
    """

    @staticmethod
    def classify(
        *,
        institutional_state: InstitutionalState,
        trend: TrendDirection,
        volatility: VolatilityState,
        dealer_state: DealerState,
    ) -> RegimeState:
        """
        Classify market regime.
        """

        # ==================================================
        # Strong Uptrend
        # ==================================================

        if (
            institutional_state
            is InstitutionalState.STRONGLY_BULLISH
            and trend
            is TrendDirection.STRONG_BULLISH
            and dealer_state
            is DealerState.LONG_GAMMA
        ):
            return RegimeState.STRONG_UPTREND

        # ==================================================
        # Uptrend
        # ==================================================

        if (
            institutional_state
            in (
                InstitutionalState.BULLISH,
                InstitutionalState.STRONGLY_BULLISH,
            )
            and trend
            in (
                TrendDirection.BULLISH,
                TrendDirection.STRONG_BULLISH,
            )
        ):
            return RegimeState.UPTREND

        # ==================================================
        # Strong Downtrend
        # ==================================================

        if (
            institutional_state
            is InstitutionalState.STRONGLY_BEARISH
            and trend
            is TrendDirection.STRONG_BEARISH
            and dealer_state
            is DealerState.SHORT_GAMMA
        ):
            return RegimeState.STRONG_DOWNTREND

        # ==================================================
        # Downtrend
        # ==================================================

        if (
            institutional_state
            in (
                InstitutionalState.BEARISH,
                InstitutionalState.STRONGLY_BEARISH,
            )
            and trend
            in (
                TrendDirection.BEARISH,
                TrendDirection.STRONG_BEARISH,
            )
        ):
            return RegimeState.DOWNTREND

        # ==================================================
        # Volatility Expansion
        # ==================================================

        if volatility in (
            VolatilityState.EXPENSIVE,
            VolatilityState.VERY_EXPENSIVE,
        ):
            return RegimeState.VOLATILITY_EXPANSION

        # ==================================================
        # Volatility Compression
        # ==================================================

        if volatility in (
            VolatilityState.CHEAP,
            VolatilityState.VERY_CHEAP,
        ):
            return RegimeState.VOLATILITY_COMPRESSION

        # ==================================================
        # Default
        # ==================================================

        return RegimeState.RANGE_BOUND