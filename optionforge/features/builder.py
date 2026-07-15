"""
============================================================
OptionForge
Feature Registry Builder
============================================================

Purpose
-------
Builds a complete FeatureRegistry from an
InstitutionalSnapshot.

Responsibilities
----------------
- Execute all feature providers
- Validate generated features
- Prevent duplicate FeatureIds
- Build immutable FeatureRegistry

This class is the ONLY place responsible for
assembling the FeatureRegistry.
============================================================
"""

from __future__ import annotations

from typing import Iterable, Protocol

from optionforge.features.feature import Feature
from optionforge.features.registry import FeatureRegistry
from optionforge.models.institutional_snapshot import InstitutionalSnapshot

# ==========================================================
# Feature Provider Interface
# ==========================================================


class FeatureProvider(Protocol):
    """
    Every feature engine implements this interface.
    """

    def calculate(
        self,
        snapshot: InstitutionalSnapshot,
    ) -> Iterable[Feature]: ...


# ==========================================================
# Feature Registry Builder
# ==========================================================


class FeatureRegistryBuilder:
    """
    Builds a FeatureRegistry.

    The builder itself performs NO calculations.

    It simply orchestrates feature providers.
    """

    def __init__(
        self,
        providers: Iterable[FeatureProvider],
    ) -> None:

        self._providers = tuple(providers)

    # ------------------------------------------------------

    def build(
        self,
        snapshot: InstitutionalSnapshot,
    ) -> FeatureRegistry:
        """
        Build complete FeatureRegistry.
        """

        registry = FeatureRegistry()

        for provider in self._providers:

            features = provider.calculate(snapshot)

            for feature in features:

                registry.add(feature)

        return registry
