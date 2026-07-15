"""
optionforge.optionchain.chain_validator
=======================================

OptionChain Validator.

Validates a collection of MarketSnapshot objects before an
OptionChain is created.

Engineering Principles
----------------------
- Stateless
- Reusable
- Pure validation
- No mutation

Author
------
OptionForge Engineering Team
"""

from __future__ import annotations

from collections.abc import Iterable

from optionforge.market.market_snapshot import MarketSnapshot


class ChainValidator:
    """
    Validator for OptionChain snapshots.
    """

    @staticmethod
    def validate(
        snapshots: Iterable[MarketSnapshot],
    ) -> tuple[MarketSnapshot, ...]:
        """
        Validate snapshots and return them as an immutable tuple.

        Raises
        ------
        TypeError
            If an element is not a MarketSnapshot.

        ValueError
            If validation fails.
        """

        snapshots = tuple(snapshots)

        if not snapshots:
            raise ValueError("OptionChain cannot be empty.")

        first = snapshots[0]

        symbol = first.symbol
        expiry = first.expiry
        trading_date = first.trading_date

        seen = set()

        for snapshot in snapshots:

            if not isinstance(snapshot, MarketSnapshot):
                raise TypeError("All elements must be MarketSnapshot objects.")

            if snapshot.symbol != symbol:
                raise ValueError("All snapshots must belong to the same symbol.")

            if snapshot.expiry != expiry:
                raise ValueError("All snapshots must belong to the same expiry.")

            if snapshot.trading_date != trading_date:
                raise ValueError("All snapshots must belong to the same trading date.")

            if snapshot.contract in seen:
                raise ValueError("Duplicate option contract found.")

            seen.add(snapshot.contract)

        return snapshots
