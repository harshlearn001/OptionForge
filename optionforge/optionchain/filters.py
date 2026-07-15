"""
optionforge.optionchain.filters
===============================

OptionChain Filters.

Provides reusable filtering operations for immutable
OptionChain objects.

Engineering Principles
----------------------
- Stateless
- Pure functions
- Immutable
- Reusable

Author
------
OptionForge Engineering Team
"""

from __future__ import annotations

from optionforge.common.enums import OptionType
from optionforge.market.market_snapshot import MarketSnapshot
from optionforge.market.option_chain import OptionChain


class ChainFilters:
    """
    Reusable filters for OptionChain.
    """

    @staticmethod
    def calls(
        chain: OptionChain,
    ) -> tuple[MarketSnapshot, ...]:

        return tuple(
            snapshot for snapshot in chain if snapshot.option_type is OptionType.CALL
        )

    @staticmethod
    def puts(
        chain: OptionChain,
    ) -> tuple[MarketSnapshot, ...]:

        return tuple(
            snapshot for snapshot in chain if snapshot.option_type is OptionType.PUT
        )


    @staticmethod
    def by_strike(
        chain: OptionChain,
        strike_price: float,
    ) -> tuple[MarketSnapshot, ...]:
        """
        Return snapshots for one strike.
        """

        return tuple(
            snapshot
            for snapshot in chain
            if snapshot.contract.strike_price == strike_price
        )

    @staticmethod
    def by_option_type(
        chain: OptionChain,
        option_type: OptionType,
    ) -> tuple[MarketSnapshot, ...]:
        """
        Generic option type filter.
        """

        return tuple(
            snapshot for snapshot in chain if snapshot.option_type is option_type
        )

    @staticmethod
    def by_open_interest(
        chain: OptionChain,
        minimum: int,
    ) -> tuple[MarketSnapshot, ...]:
        """
        Return contracts with OI >= minimum.
        """

        return tuple(
            snapshot for snapshot in chain if snapshot.open_interest >= minimum
        )

    @staticmethod
    def by_volume(
        chain: OptionChain,
        minimum: int,
    ) -> tuple[MarketSnapshot, ...]:
        """
        Return contracts with Volume >= minimum.
        """

        return tuple(snapshot for snapshot in chain if snapshot.volume >= minimum)
