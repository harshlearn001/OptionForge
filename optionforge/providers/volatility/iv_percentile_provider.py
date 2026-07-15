"""
============================================================
OptionForge
IV Percentile Provider
============================================================

Converts IV Percentile analytics into immutable Features.
============================================================
"""

from __future__ import annotations

from collections.abc import Iterable

from optionforge.context.market_context import MarketContext
from optionforge.features.feature import Feature
from optionforge.features.feature_group import FeatureGroup
from optionforge.features.feature_id import FeatureId
from optionforge.providers.base_provider import BaseProvider

from optionforge.intelligence.iv_percentile import IVPercentile


class IVPercentileProvider(BaseProvider):
    """
    Produces Implied Volatility Percentile feature.
    """

    NAME = "IV Percentile"

    VERSION = "1.0.0"

    GROUP = FeatureGroup.IMPLIED_VOLATILITY

    PRODUCES = (FeatureId.IV_PERCENTILE,)

    REQUIRES = (
        "current_iv",
        "historical_iv",
    )

    def calculate(
        self,
        context: MarketContext,
    ) -> Iterable[Feature]:

        result = IVPercentile.calculate(
            current_iv=context.snapshot.current_iv,
            historical_iv=context.snapshot.historical_iv,
        )

        return [
            Feature(
                id=FeatureId.IV_PERCENTILE,
                group=self.GROUP,
                value=result.iv_percentile,
                metadata={
                    "current_iv": result.current_iv,
                    "lookback": result.lookback,
                    "observations": result.observations,
                },
            )
        ]
