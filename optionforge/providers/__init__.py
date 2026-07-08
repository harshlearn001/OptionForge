"""
============================================================
OptionForge
Providers Package
============================================================

Feature Providers convert market data into immutable
Feature objects.

Each provider is responsible for one quantitative domain.

Examples
--------
- ExpectedMoveProvider
- GammaExposureProvider
- IVRankProvider
- DealerPositionProvider
- ModifiedPCRProvider
============================================================
"""

from optionforge.providers.base_provider import BaseProvider

__all__ = [
    "BaseProvider",
]