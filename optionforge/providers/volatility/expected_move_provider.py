"""
============================================================
OptionForge
Expected Move Provider
============================================================

Converts Expected Move analytics into immutable Features.
============================================================
"""

from __future__ import annotations

from collections.abc import Iterable

from optionforge.context.market_context import MarketContext
from optionforge.features.feature import Feature
from optionforge.features.feature_group import FeatureGroup
from optionforge.features.feature_id import FeatureId
from optionforge.providers.base_provider import BaseProvider

from optionforge.intelligence.expected_move import ExpectedMove


class ExpectedMoveProvider(BaseProvider):
    """
    Produces Expected Move features.
    """

    NAME = "Expected Move"

    VERSION = "1.0.0"

    GROUP = FeatureGroup.IMPLIED_VOLATILITY

    PRODUCES = (FeatureId.EXPECTED_MOVE,)

    REQUIRES = (
        "spot_price",
        "atm_iv",
        "days_to_expiry",
    )

    def calculate(
        self,
        context: MarketContext,
    ) -> Iterable[Feature]:

        result = ExpectedMove.calculate(
            spot=context.snapshot.spot,
            atm_iv=context.snapshot.atm_iv,
            days=context.snapshot.days_to_expiry,
        )

        return [
            Feature(
                id=FeatureId.EXPECTED_MOVE,
                group=self.GROUP,
                value=result.expected_move,
                metadata={
                    "upper68": result.upper_68,
                    "lower68": result.lower_68,
                    "upper95": result.upper_95,
                    "lower95": result.lower_95,
                    "daily": result.one_day_move,
                    "weekly": result.weekly_move,
                    "monthly": result.monthly_move,
                },
            )
        ]
