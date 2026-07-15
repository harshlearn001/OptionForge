"""
optionforge.optionchain.expiry_selector
=======================================

Expiry Selector.

Provides reusable expiry selection operations for
OptionChain objects.

Engineering Principles
----------------------
- Stateless
- Pure selection
- Immutable
- No mutation

Author
------
OptionForge Engineering Team
"""

from __future__ import annotations

from optionforge.kernel.expiry import Expiry
from optionforge.market.option_chain import OptionChain


class ExpirySelector:
    """
    Select OptionChains by expiry.
    """

    @staticmethod
    def exact(
        chains: tuple[OptionChain, ...],
        expiry: Expiry,
    ) -> OptionChain:
        """
        Return the OptionChain matching the given expiry.

        Raises
        ------
        LookupError
            If expiry is not found.
        """

        for chain in chains:
            if chain.expiry == expiry:
                return chain

        raise LookupError(f"Expiry '{expiry.expiry_date}' not found.")

    @staticmethod
    def nearest(
        chains: tuple[OptionChain, ...],
    ) -> OptionChain:
        """
        Return the nearest expiry chain.

        Raises
        ------
        ValueError
            If no chains are supplied.
        """

        if not chains:
            raise ValueError("No OptionChains supplied.")

        return min(
            chains,
            key=lambda chain: chain.expiry.expiry_date,
        )

    @staticmethod
    def weekly(
        chains: tuple[OptionChain, ...],
    ) -> tuple[OptionChain, ...]:
        """
        Return all weekly expiry chains.
        """

        return tuple(chain for chain in chains if chain.expiry.is_weekly)

    @staticmethod
    def monthly(
        chains: tuple[OptionChain, ...],
    ) -> tuple[OptionChain, ...]:
        """
        Return all monthly expiry chains.
        """

        return tuple(chain for chain in chains if chain.expiry.is_monthly)
