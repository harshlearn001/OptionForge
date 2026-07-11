"""
============================================================
OptionForge
Research Registry
============================================================

Author      : OptionForge
Module      : research_registry.py

Purpose
-------
Registry for ResearchBuilder.

Contains NO business logic.

============================================================
"""

from __future__ import annotations

from optionforge.research.research_builder import (
    ResearchBuilder,
)


class ResearchRegistry:
    """
    Registry of research builders.
    """

    def __init__(self) -> None:

        self._builder = ResearchBuilder()

    @property
    def builder(self) -> ResearchBuilder:
        """
        Default research builder.
        """

        return self._builder

    def get_builder(self) -> ResearchBuilder:
        """
        Return the registered builder.
        """

        return self._builder

    def __repr__(self) -> str:

        return (

            f"ResearchRegistry("

            f"builder={self._builder.__class__.__name__})"

        )