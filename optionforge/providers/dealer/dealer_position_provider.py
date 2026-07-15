"""
============================================================
OptionForge
Dealer Position Provider
============================================================

Converts DealerPosition intelligence into immutable Features.
============================================================
"""

from __future__ import annotations

from collections.abc import Iterable

from optionforge.context.market_context import MarketContext
from optionforge.features.feature import Feature
from optionforge.features.feature_group import FeatureGroup
from optionforge.features.feature_id import FeatureId
from optionforge.providers.base_provider import BaseProvider

from optionforge.intelligence.dealer_position import DealerPosition


class DealerPositionProvider(BaseProvider):
    """
    Produces Dealer Position features.
    """

    NAME = "Dealer Position"

    VERSION = "1.0.0"

    GROUP = FeatureGroup.DEALER

    PRODUCES = (FeatureId.DEALER_POSITION,)

    REQUIRES = (
        "gamma_result",
        "delta_result",
        "vanna_result",
        "charm_result",
    )

    def calculate(
        self,
        context: MarketContext,
    ) -> Iterable[Feature]:

        result = DealerPosition.calculate(
            gamma=context.snapshot.gamma_result,
            delta=context.snapshot.delta_result,
            vanna=context.snapshot.vanna_result,
            charm=context.snapshot.charm_result,
        )

        return [
            Feature(
                id=FeatureId.DEALER_POSITION,
                group=self.GROUP,
                value=result.dealer_position,
                metadata={
                    "dealer_delta": result.dealer_delta,
                    "dealer_gamma": result.dealer_gamma,
                    "net_exposure": result.net_exposure,
                    "position_strength": result.position_strength,
                    "institutional_score": result.institutional_score,
                    "dealer_bias": result.dealer_bias,
                    "dealer_direction": result.dealer_direction,
                    "market_condition": result.market_condition,
                    "market_stability": result.market_stability,
                    "directional_risk": result.directional_risk,
                    "confidence": result.confidence,
                    "recommendation": result.recommendation,
                    "interpretation": result.interpretation,
                },
            )
        ]
