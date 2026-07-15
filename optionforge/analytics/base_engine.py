"""
============================================================
OptionForge
Analytics Base Engine
============================================================

Author      : OptionForge
Module      : base_engine.py

Purpose
-------
Base class for every analytics engine inside
OptionForge.

Responsibilities
----------------
✓ Standard analytics interface
✓ Consume InstitutionalSnapshot
✓ Return calculation results
✓ Never load files
✓ Never access repositories
✓ Never access providers

============================================================
"""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from optionforge.snapshot.institutional_snapshot import (
    InstitutionalSnapshot,
)


class AnalyticsEngine(ABC):
    """
    Base class for every analytics engine.
    """

    @abstractmethod
    def calculate(
        self,
        snapshot: InstitutionalSnapshot,
    ):
        """
        Perform analytics using an immutable
        InstitutionalSnapshot.

        Parameters
        ----------
        snapshot
            Immutable market snapshot.

        Returns
        -------
        Analytics result.
        """

        raise NotImplementedError

    # -----------------------------------------------------

    @property
    def name(self) -> str:
        """
        Engine name.
        """

        return self.__class__.__name__

    # -----------------------------------------------------

    def __repr__(self) -> str:

        return f"{self.name}()"

    __str__ = __repr__
