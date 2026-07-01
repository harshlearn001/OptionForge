"""
optionforge.optionchain.strike_selector
=======================================

Strike Selector.

Selects option contracts by strike from an OptionChain.

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

from optionforge.market.market_snapshot import MarketSnapshot
from optionforge.market.option_chain import OptionChain


class StrikeSelector:
    """
    Select contracts by strike.
    """

    @staticmethod
    def exact(
        chain: OptionChain,
        strike_price: float,
    ) -> tuple[MarketSnapshot, ...]:
        """
        Return contracts having exactly the given strike.
        """

        return tuple(
            snapshot
            for snapshot in chain
            if snapshot.contract.strike_price == strike_price
        )

    @staticmethod
    def between(
        chain: OptionChain,
        minimum: float,
        maximum: float,
    ) -> tuple[MarketSnapshot, ...]:
        """
        Return contracts whose strike lies within
        the inclusive range.
        """

        if minimum > maximum:
            raise ValueError(
                "Minimum strike cannot exceed maximum strike."
            )

        return tuple(
            snapshot
            for snapshot in chain
            if minimum
            <= snapshot.contract.strike_price
            <= maximum
        )

    @staticmethod
    def around(
        chain: OptionChain,
        center: float,
        width: int,
    ) -> tuple[MarketSnapshot, ...]:
        """
        Return contracts around the nearest strike.

        width = number of strikes on each side.

        Example
        -------
        center = 25000
        width = 2

        Returns

        24900
        24950
        25000
        25050
        25100
        """

        if width < 0:
            raise ValueError(
                "Width cannot be negative."
            )

        strikes = sorted(
            {
                snapshot.contract.strike_price
                for snapshot in chain
            }
        )

        nearest = min(
            strikes,
            key=lambda strike: abs(
                strike - center
            ),
        )

        index = strikes.index(nearest)

        left = max(0, index - width)
        right = min(
            len(strikes),
            index + width + 1,
        )

        selected = set(strikes[left:right])

        return tuple(
            snapshot
            for snapshot in chain
            if snapshot.contract.strike_price in selected
        )