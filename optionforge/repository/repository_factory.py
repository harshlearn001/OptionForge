"""
============================================================
OptionForge
Repository Factory
============================================================

Author      : OptionForge
Module      : repository_factory.py
Purpose     : Central factory for repository creation.

Responsibilities
----------------
- Create repositories
- Share RepositoryContext
- Centralize repository construction

Contains NO business logic.

============================================================
"""

from __future__ import annotations

from optionforge.repository.repository_context import (
    RepositoryContext,
)

from optionforge.repository.option_repository import (
    OptionRepository,
)

from optionforge.repository.future_repository import (
    FutureRepository,
)

from optionforge.repository.spot_repository import (
    SpotRepository,
)


class RepositoryFactory:
    """
    Factory for creating repositories.

    One shared RepositoryContext is used by all
    repositories.
    """

    def __init__(
        self,
        context: RepositoryContext,
    ) -> None:

        self._context = context

    # =====================================================
    # Option Repository
    # =====================================================

    def option(self) -> OptionRepository:
        """
        Return OptionRepository.
        """

        return OptionRepository(

            self._context,

        )

    # =====================================================
    # Future Repository
    # =====================================================

    def future(self) -> FutureRepository:
        """
        Return FutureRepository.
        """

        return FutureRepository(

            self._context,

        )

    # =====================================================
    # Spot Repository
    # =====================================================

    def spot(self) -> SpotRepository:
        """
        Return SpotRepository.
        """

        return SpotRepository(

            self._context,

        )