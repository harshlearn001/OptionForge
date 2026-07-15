"""
optionforge.optionchain.atm_selector
===================================

ATM Selector.

Selects the At-The-Money (ATM) option contracts from an
OptionChain.

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


class ATMSelector:
    """
    Select ATM contracts from an OptionChain.
    """

    @staticmethod
    def select(
        chain: OptionChain,
        reference_price: float,
    ) -> tuple[MarketSnapshot, ...]:
        """
        Return the ATM Call and Put contracts nearest to the
        supplied reference price.
        """

        if reference_price <= 0:
            raise ValueError("Reference price must be positive.")

        nearest_strike = min(
            chain.strikes,
            key=lambda strike: abs(strike.strike_price - reference_price),
        )

        return tuple(
            snapshot for snapshot in chain if snapshot.strike == nearest_strike
        )
