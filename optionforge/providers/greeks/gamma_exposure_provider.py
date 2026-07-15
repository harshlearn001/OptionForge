"""
============================================================
OptionForge
Gamma Exposure Provider
============================================================

Converts Gamma Exposure analytics into immutable Features.
============================================================
"""

from __future__ import annotations

from collections.abc import Iterable

from optionforge.context.market_context import MarketContext
from optionforge.features.feature import Feature
from optionforge.features.feature_group import FeatureGroup
from optionforge.features.feature_id import FeatureId
from optionforge.providers.base_provider import BaseProvider

from optionforge.intelligence.gamma_exposure import GammaExposure


class GammaExposureProvider(BaseProvider):
    """
    Produces gamma-related features.
    """

    NAME = "Gamma Exposure"

    VERSION = "1.0.0"

    GROUP = FeatureGroup.GREEKS

    PRODUCES = (
        FeatureId.GAMMA_EXPOSURE,
        FeatureId.ZERO_GAMMA,
        FeatureId.GAMMA_FLIP,
    )

    REQUIRES = (
        "option_chain",
        "spot_price",
    )

    def calculate(
        self,
        context: MarketContext,
    ) -> Iterable[Feature]:

        result = GammaExposure.calculate(
            option_chain=context.snapshot.option_chain,
            spot=context.snapshot.spot,
        )

        return [
            Feature(
                id=FeatureId.GAMMA_EXPOSURE,
                group=self.GROUP,
                value=result.gamma_exposure,
                metadata={
                    "dealer_gamma": result.dealer_gamma,
                    "call_gamma": result.call_gamma,
                    "put_gamma": result.put_gamma,
                },
            ),
            Feature(
                id=FeatureId.ZERO_GAMMA,
                group=self.GROUP,
                value=result.zero_gamma,
            ),
            Feature(
                id=FeatureId.GAMMA_FLIP,
                group=self.GROUP,
                value=result.gamma_flip,
            ),
        ]
