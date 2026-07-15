"""
optionforge.integration.file_resolver
=====================================

Production-grade MarketForge file resolver.

Responsibilities
----------------
* Resolve MarketForge file locations.
* Prefer Parquet over CSV.
* Resolve INDICES vs STOCKS automatically.
* Resolve Spot / Options / Futures / Delivery files.
* Validate configured repositories.
* Never load market data.

This module NEVER imports pandas.
This module NEVER performs business logic.
"""

from __future__ import annotations

from pathlib import Path
from typing import Iterator

# ============================================================================
# Exceptions
# ============================================================================


class FileResolverError(Exception):
    """Base exception for the FileResolver."""


class RepositoryNotConfiguredError(FileResolverError):
    """Raised when an optional repository has not been configured."""


class RepositoryNotFoundError(FileResolverError):
    """Raised when a repository directory does not exist."""


class FileNotFoundInRepository(FileResolverError):
    """Raised when a symbol cannot be located inside a repository."""


# ============================================================================
# File Resolver
# ============================================================================


class FileResolver:
    """
    Resolves MarketForge files.

    The resolver knows ONLY the repository layout.

    It does NOT:

    - load files
    - use pandas
    - calculate ATM
    - calculate PCR
    - know expiry rules

    Search priority
    ---------------
    1. Parquet
    2. CSV
    """

    def __init__(
        self,
        option_root: Path,
        index_spot_root: Path,
        equity_spot_root: Path,
        future_root: Path | None = None,
        delivery_root: Path | None = None,
    ) -> None:

        self.option_root = Path(option_root)
        self.index_spot_root = Path(index_spot_root)
        self.equity_spot_root = Path(equity_spot_root)

        self.future_root = Path(future_root) if future_root is not None else None

        self.delivery_root = Path(delivery_root) if delivery_root is not None else None

    # ------------------------------------------------------------------
    # Option Repository
    # ------------------------------------------------------------------

    def resolve_option(self, symbol: str) -> Path:
        """
        Resolve an option history file.

        Searches:

            option_root/
                INDICES/
                STOCKS/

        Preference:

            *.parquet
            *.csv
        """

        return self._resolve_symbol_file(
            root=self.option_root,
            symbol=symbol,
        )

    # ------------------------------------------------------------------
    # Futures Repository
    # ------------------------------------------------------------------

    def resolve_future(self, symbol: str) -> Path:
        """
        Resolve futures history.
        """

        if self.future_root is None:
            raise RepositoryNotConfiguredError("Future repository is not configured.")

        return self._resolve_symbol_file(
            root=self.future_root,
            symbol=symbol,
        )

    # ------------------------------------------------------------------
    # Delivery Repository
    # ------------------------------------------------------------------

    def resolve_delivery(self, symbol: str) -> Path:
        """
        Resolve delivery history.
        """

        if self.delivery_root is None:
            raise RepositoryNotConfiguredError("Delivery repository is not configured.")

        return self._resolve_symbol_file(
            root=self.delivery_root,
            symbol=symbol,
        )

    # ------------------------------------------------------------------
    # Spot Repositories
    # ------------------------------------------------------------------

    def resolve_index_spot(self, symbol: str) -> Path:
        """
        Resolve index spot history.
        """

        return self._resolve_file(
            root=self.index_spot_root,
            symbol=symbol,
        )

    def resolve_equity_spot(self, symbol: str) -> Path:
        """
        Resolve equity spot history.
        """

        return self._resolve_file(
            root=self.equity_spot_root,
            symbol=symbol,
        )

    # ------------------------------------------------------------------
    # Repository Existence
    # ------------------------------------------------------------------

    def exists_option(self, symbol: str) -> bool:
        try:
            self.resolve_option(symbol)
            return True
        except FileResolverError:
            return False

    def exists_future(self, symbol: str) -> bool:
        try:
            self.resolve_future(symbol)
            return True
        except FileResolverError:
            return False

    def exists_delivery(self, symbol: str) -> bool:
        try:
            self.resolve_delivery(symbol)
            return True
        except FileResolverError:
            return False

    def exists_index(self, symbol: str) -> bool:
        try:
            self.resolve_index_spot(symbol)
            return True
        except FileResolverError:
            return False

    def exists_equity(self, symbol: str) -> bool:
        try:
            self.resolve_equity_spot(symbol)
            return True
        except FileResolverError:
            return False
        # ------------------------------------------------------------------

    # Internal Helpers
    # ------------------------------------------------------------------

    @staticmethod
    def normalize_symbol(symbol: str) -> str:
        """
        Normalize a market symbol.

        Examples
        --------
        >>> normalize_symbol("nifty")
        'NIFTY'

        >>> normalize_symbol(" reliance ")
        'RELIANCE'
        """
        return symbol.strip().upper()

    @staticmethod
    def _candidate_files(base: Path, symbol: str) -> Iterator[Path]:
        """
        Yield candidate files in priority order.

        Search priority
        ---------------
        1. Parquet
        2. CSV
        """

        yield base / f"{symbol}.parquet"
        yield base / f"{symbol}.csv"

    def _resolve_file(
        self,
        root: Path,
        symbol: str,
    ) -> Path:
        """
        Resolve a file inside a single repository.

        Parameters
        ----------
        root
            Repository root.

        symbol
            Market symbol.

        Returns
        -------
        Path

        Raises
        ------
        FileNotFoundInRepository
        """

        symbol = self.normalize_symbol(symbol)

        for candidate in self._candidate_files(root, symbol):

            if candidate.exists():
                return candidate

        raise FileNotFoundInRepository(f"Unable to locate '{symbol}' in:\n{root}")

    def _resolve_symbol_file(
        self,
        root: Path,
        symbol: str,
    ) -> Path:
        """
        Resolve a symbol from repositories containing
        INDICES and STOCKS folders.

        Example
        -------
        option_master/

            INDICES/

            STOCKS/
        """

        symbol = self.normalize_symbol(symbol)

        for folder in ("INDICES", "STOCKS"):

            base = root / folder

            try:
                return self._resolve_file(base, symbol)

            except FileNotFoundInRepository:
                pass

        raise FileNotFoundInRepository(f"Unable to locate '{symbol}' under:\n{root}")

    # ------------------------------------------------------------------
    # Repository Validation
    # ------------------------------------------------------------------

    @staticmethod
    def validate_repository(path: Path) -> None:
        """
        Validate repository existence.
        """

        if not path.exists():

            raise RepositoryNotFoundError(f"Repository not found:\n{path}")

        if not path.is_dir():

            raise RepositoryNotFoundError(f"Repository is not a directory:\n{path}")

    def validate(self) -> None:
        """
        Validate all configured repositories.
        """

        self.validate_repository(self.option_root)
        self.validate_repository(self.index_spot_root)
        self.validate_repository(self.equity_spot_root)

        if self.future_root is not None:
            self.validate_repository(self.future_root)

        if self.delivery_root is not None:
            self.validate_repository(self.delivery_root)

    # ------------------------------------------------------------------
    # Diagnostics
    # ------------------------------------------------------------------

    def repository_summary(self) -> dict[str, str | None]:
        """
        Return configured repositories.
        """

        return {
            "option_root": str(self.option_root),
            "index_spot_root": str(self.index_spot_root),
            "equity_spot_root": str(self.equity_spot_root),
            "future_root": (str(self.future_root) if self.future_root else None),
            "delivery_root": (str(self.delivery_root) if self.delivery_root else None),
        }

    def print_summary(self) -> None:
        """
        Pretty-print repository configuration.
        """

        print("=" * 70)
        print("MarketForge Repository")
        print("=" * 70)

        for key, value in self.repository_summary().items():
            print(f"{key:<20} : {value}")

        print("=" * 70)

    # ------------------------------------------------------------------
    # Representation
    # ------------------------------------------------------------------

    def __repr__(self) -> str:

        return (
            f"{self.__class__.__name__}("
            f"option_root={self.option_root!r}, "
            f"index_spot_root={self.index_spot_root!r}, "
            f"equity_spot_root={self.equity_spot_root!r}, "
            f"future_root={self.future_root!r}, "
            f"delivery_root={self.delivery_root!r})"
        )
