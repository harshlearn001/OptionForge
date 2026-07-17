"""
============================================================
OptionForge
Evidence Provider Registry
============================================================

Author      : OptionForge
Module      : evidence_provider_registry.py
Purpose     : Maps analytics result types to Evidence providers.

============================================================
"""

from __future__ import annotations

from typing import Any


class EvidenceProviderRegistry:
    """
    Registry of Evidence providers.
    """

    def __init__(self) -> None:

        self._providers: dict[type, Any] = {}

    # -----------------------------------------------------

    def register(
        self,
        result_type: type,
        provider: Any,
    ) -> None:
        """
        Register provider for a result type.
        """

        self._providers[result_type] = provider

    # -----------------------------------------------------

    def resolve(
        self,
        result: Any,
    ) -> Any:
        """
        Return provider for a result instance.
        """

        result_type = type(result)

        if result_type not in self._providers:

            raise LookupError(
                f"No provider registered for "
                f"{result_type.__name__}."
            )

        return self._providers[result_type]

    # -----------------------------------------------------

    def exists(
        self,
        result_type: type,
    ) -> bool:

        return result_type in self._providers

    # -----------------------------------------------------

    def __len__(self) -> int:

        return len(self._providers)

    # -----------------------------------------------------

    def __repr__(self) -> str:

        return (
            f"EvidenceProviderRegistry("
            f"{len(self)} providers)"
        )

    __str__ = __repr__