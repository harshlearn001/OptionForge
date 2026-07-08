"""
============================================================
OptionForge
Feature Registry
============================================================

Author      : OptionForge
Module      : registry.py

Purpose
-------
Immutable registry of all calculated quantitative features.

Every feature is calculated once and stored here.

Consumers:
    - Evidence Engine
    - MarketDNA
    - Decision Engine
    - Dashboard
    - Scanner
    - Research
    - Backtesting

============================================================
"""

from __future__ import annotations

from collections import defaultdict
from typing import Dict, Iterable

from optionforge.features.feature import Feature
from optionforge.features.feature_group import FeatureGroup
from optionforge.features.feature_id import FeatureId


class FeatureRegistry:
    """
    Central storage for all calculated features.

    Each FeatureId may exist only once.
    """

    def __init__(self) -> None:

        self._features: Dict[FeatureId, Feature] = {}

    # ---------------------------------------------------------
    # Add
    # ---------------------------------------------------------

    def add(self, feature: Feature) -> None:
        """
        Register a feature.

        Raises
        ------
        ValueError
            If FeatureId already exists.
        """

        if feature.id in self._features:
            raise ValueError(
                f"Feature already registered: {feature.id.name}"
            )

        self._features[feature.id] = feature

    # ---------------------------------------------------------
    # Update
    # ---------------------------------------------------------

    def replace(self, feature: Feature) -> None:
        """
        Replace an existing feature.
        """

        self._features[feature.id] = feature

    # ---------------------------------------------------------
    # Get
    # ---------------------------------------------------------

    def get(self, feature_id: FeatureId) -> Feature:
        """
        Retrieve feature.

        Raises
        ------
        KeyError
            If feature does not exist.
        """

        return self._features[feature_id]

    # ---------------------------------------------------------
    # Exists
    # ---------------------------------------------------------

    def has(self, feature_id: FeatureId) -> bool:

        return feature_id in self._features

    # ---------------------------------------------------------
    # Remove
    # ---------------------------------------------------------

    def remove(self, feature_id: FeatureId) -> None:

        self._features.pop(feature_id, None)

    # ---------------------------------------------------------
    # Group Lookup
    # ---------------------------------------------------------

    def group(
        self,
        feature_group: FeatureGroup,
    ) -> list[Feature]:

        return [
            feature
            for feature in self._features.values()
            if feature.group == feature_group
        ]

    # ---------------------------------------------------------
    # Export
    # ---------------------------------------------------------

    def to_dict(self) -> dict:

        return {
            feature.id.name: feature.to_dict()
            for feature in self._features.values()
        }

    def values(self) -> Iterable[Feature]:

        return self._features.values()

    def items(self):

        return self._features.items()

    def __len__(self) -> int:

        return len(self._features)

    def __contains__(self, feature_id: FeatureId) -> bool:

        return feature_id in self._features

    def __iter__(self):

        return iter(self._features.values())

    def __repr__(self) -> str:

        return (
            f"FeatureRegistry("
            f"{len(self._features)} features)"
        )