"""
============================================================
OptionForge
IV Rank Provider
============================================================
"""

from __future__ import annotations

from collections.abc import Iterable

from optionforge.context.market_context import MarketContext
from optionforge.features.feature import Feature
from optionforge.features.feature_group import FeatureGroup
from optionforge.features.feature_id import FeatureId
from optionforge.providers.base_provider import BaseProvider

from optionforge.intelligence.iv_rank import IVRank


class IVRankProvider(BaseProvider):
    """
    Produces Implied Volatility Rank feature.
    """

    NAME = "IV Rank"

    VERSION = "1.0.0"

    GROUP = FeatureGroup.IMPLIED_VOLATILITY

    PRODUCES = (FeatureId.IV_RANK,)

    REQUIRES = (
        "current_iv",
        "historical_iv",
    )

    def calculate(
        self,
        context: MarketContext,
    ) -> Iterable[Feature]:

        result = IVRank.calculate(
            current_iv=context.snapshot.current_iv,
            historical_iv=context.snapshot.historical_iv,
        )

        return [
            Feature(
                id=FeatureId.IV_RANK,
                group=self.GROUP,
                value=result.iv_rank,
                metadata={
                    "current_iv": result.current_iv,
                    "lowest_iv": result.low_iv,
                    "highest_iv": result.high_iv,
                    "lookback": result.lookback,
                },
            )
        ]
