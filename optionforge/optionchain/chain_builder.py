"""
optionforge.optionchain.chain_builder
=====================================

OptionChain Builder.

Builds immutable OptionChain objects from a collection
of MarketSnapshot objects.

Engineering Principles
----------------------
- Stateless
- Builder Pattern
- Immutable output
- Delegates validation

Author
------
OptionForge Engineering Team
"""

from __future__ import annotations

from collections.abc import Iterable

from optionforge.market.market_snapshot import MarketSnapshot
from optionforge.market.option_chain import OptionChain
from optionforge.optionchain.chain_validator import ChainValidator


class ChainBuilder:
    """
    Builder for immutable OptionChain objects.
    """

    @staticmethod
    def build(
        snapshots: Iterable[MarketSnapshot],
    ) -> OptionChain:
        """
        Build an OptionChain.

        Parameters
        ----------
        snapshots
            Iterable of MarketSnapshot objects.

        Returns
        -------
        OptionChain

        Raises
        ------
        TypeError
            Invalid snapshot type.

        ValueError
            Validation failed.
        """

        validated = ChainValidator.validate(
            snapshots
        )

        return OptionChain(
            snapshots=validated
        )