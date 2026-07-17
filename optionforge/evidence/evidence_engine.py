"""
============================================================
OptionForge
Evidence Engine
============================================================

Author      : OptionForge
Module      : evidence_engine.py
Purpose     : Convert analytical results into evidence.

============================================================
"""

from __future__ import annotations

from optionforge.evidence.evidence_registry import (
    EvidenceRegistry,
)

from optionforge.evidence.evidence_provider_registry import (
    EvidenceProviderRegistry,
)


class EvidenceEngine:
    """
    Converts analytical results into institutional evidence.
    """

    def __init__(
        self,
        registry: EvidenceProviderRegistry,
    ) -> None:

        self._providers = registry

    @property
    def providers(self) -> EvidenceProviderRegistry:

        return self._providers

    def build(
        self,
        results,
    ) -> EvidenceRegistry:
        """
        Build EvidenceRegistry from ResultCollection.
        """

        registry = EvidenceRegistry()

        for execution in results:

            if not execution.succeeded:

                continue

            provider = self.providers.resolve(
                execution.result,
            )

            collection = provider.build(
                execution.result,
            )

            for evidence in collection:

                registry.add(
                    evidence,
                )

        return registry

    def __repr__(self):

        return "EvidenceEngine()"

    __str__ = __repr__