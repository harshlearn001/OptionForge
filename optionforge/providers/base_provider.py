"""
============================================================
OptionForge
Base Provider
============================================================
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import Iterable

from optionforge.context.market_context import MarketContext
from optionforge.features.feature import Feature


class BaseProvider(ABC):
    """
    Base class for all Feature Providers.
    """

    @abstractmethod
    def calculate(
        self,
        context: MarketContext,
    ) -> Iterable[Feature]:
        """
        Produce Features from the supplied MarketContext.
        """
        raise NotImplementedError