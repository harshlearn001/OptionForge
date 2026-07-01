"""
optionforge.market.option_chain
===============================

Immutable Option Chain domain object.

Represents one complete option chain for a single
underlying symbol, expiry and trading date.

Engineering Principles
----------------------
- Immutable
- Fully validated
- Domain object
- Collection semantics
- No analytics
- No filtering

Author
------
OptionForge Engineering Team
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import Iterable, Iterator

from optionforge.common.enums import Exchange, OptionType
from optionforge.kernel.expiry import Expiry
from optionforge.kernel.option_contract import OptionContract
from optionforge.kernel.strike import Strike
from optionforge.kernel.symbol import Symbol
from optionforge.market.market_snapshot import MarketSnapshot


@dataclass(frozen=True, slots=True)
class OptionChain:
    """
    Immutable collection of MarketSnapshot objects.

    Every snapshot must belong to the same

    • Symbol
    • Expiry
    • Trading Date
    """

    snapshots: tuple[MarketSnapshot, ...]

    def __post_init__(self) -> None:
        """
        Validate OptionChain.
        """

        # Accept list, tuple or any iterable
        object.__setattr__(
            self,
            "snapshots",
            tuple(self.snapshots),
        )

        if not self.snapshots:
            raise ValueError(
                "OptionChain cannot be empty."
            )

        first = self.snapshots[0]

        symbol = first.symbol
        expiry = first.expiry
        trading_date = first.trading_date

        seen: set[OptionContract] = set()

        for snapshot in self.snapshots:

            if snapshot.symbol != symbol:
                raise ValueError(
                    "All snapshots must belong "
                    "to the same symbol."
                )

            if snapshot.expiry != expiry:
                raise ValueError(
                    "All snapshots must belong "
                    "to the same expiry."
                )

            if snapshot.trading_date != trading_date:
                raise ValueError(
                    "All snapshots must belong "
                    "to the same trading date."
                )

            if snapshot.contract in seen:
                raise ValueError(
                    "Duplicate option contract found."
                )

            seen.add(snapshot.contract)

    # =====================================================
    # Identity
    # =====================================================

    @property
    def symbol(self) -> Symbol:
        """
        Underlying symbol.
        """
        return self.snapshots[0].symbol

    @property
    def exchange(self) -> Exchange:
        """
        Exchange.
        """
        return self.snapshots[0].exchange

    @property
    def expiry(self) -> Expiry:
        """
        Expiry.
        """
        return self.snapshots[0].expiry

    @property
    def trading_date(self) -> date:
        """
        Trading date.
        """
        return self.snapshots[0].trading_date

    # =====================================================
    # Collection
    # =====================================================

    @property
    def snapshot_count(self) -> int:
        """
        Number of snapshots.
        """
        return len(self.snapshots)

    @property
    def contracts(self) -> tuple[OptionContract, ...]:
        """
        Option contracts.
        """
        return tuple(
            snapshot.contract
            for snapshot in self.snapshots
        )

    @property
    def strikes(self) -> tuple[Strike, ...]:
        """
        Strike objects.
        """
        return tuple(
            snapshot.strike
            for snapshot in self.snapshots
        )

    @property
    def option_types(self) -> tuple[OptionType, ...]:
        """
        Unique option types.
        """
        return tuple(
            sorted(
                {
                    snapshot.option_type
                    for snapshot in self.snapshots
                },
                key=lambda x: x.value,
            )
        )

    def __len__(self) -> int:
        return len(self.snapshots)

    def __iter__(self) -> Iterator[MarketSnapshot]:
        return iter(self.snapshots)

    def __contains__(
        self,
        snapshot: MarketSnapshot,
    ) -> bool:
        return snapshot in self.snapshots

    # =====================================================
    # Lookup
    # =====================================================

    def get(
        self,
        contract: OptionContract,
    ) -> MarketSnapshot | None:
        """
        Returns snapshot for a contract.
        """

        for snapshot in self.snapshots:
            if snapshot.contract == contract:
                return snapshot

        return None

    def exists(
        self,
        contract: OptionContract,
    ) -> bool:
        """
        Returns True if contract exists.
        """

        return self.get(contract) is not None

    # =====================================================
    # Serialization
    # =====================================================

    def to_list(self) -> list[dict[str, object]]:
        """
        Convert chain to list.
        """

        return [
            snapshot.to_dict()
            for snapshot in self.snapshots
        ]

    def to_dict(self) -> dict[str, object]:
        """
        Convert chain to dictionary.
        """

        return {
            "symbol": self.symbol.ticker,
            "exchange": self.exchange.value,
            "expiry_date": self.expiry.expiry_date.isoformat(),
            "trading_date": self.trading_date.isoformat(),
            "snapshot_count": self.snapshot_count,
            "snapshots": self.to_list(),
        }

    # =====================================================
    # Representation
    # =====================================================

    def __str__(self) -> str:
        """
        Human-readable representation.
        """

        return (
            f"{self.symbol.ticker} | "
            f"{self.expiry.expiry_date} | "
            f"{self.snapshot_count} Contracts"
        )

    def __repr__(self) -> str:
        """
        Developer representation.
        """

        return (
            "OptionChain("
            f"symbol='{self.symbol.ticker}', "
            f"expiry='{self.expiry.expiry_date}', "
            f"contracts={self.snapshot_count})"
        )