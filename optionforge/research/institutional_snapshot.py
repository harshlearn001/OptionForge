"""
==============================================================
OptionForge
Research
Institutional Snapshot
==============================================================

Immutable research snapshot representing everything
OptionForge knew after market close.

Author : OptionForge
==============================================================
"""

from dataclasses import dataclass
from datetime import date, datetime
from uuid import UUID

from optionforge.common.enums import InstrumentType
from optionforge.research.signal import Signal


@dataclass(frozen=True, slots=True)
class InstitutionalSnapshot:
    """
    Immutable research snapshot.

    One Symbol
    One Trading Date
    One Expiry
    """

    # ======================================================
    # Identity
    # ======================================================

    snapshot_id: UUID
    snapshot_version: str

    trading_date: date
    expiry_date: date
    days_to_expiry: int

    symbol: str
    instrument_type: InstrumentType

    # ======================================================
    # Contract
    # ======================================================

    underlying_close: float
    atm_strike: float
    lot_size: int
    strike_interval: int

    # ======================================================
    # Market
    # ======================================================

    open: float
    high: float
    low: float
    close: float

    volume: int

    # ======================================================
    # Options
    # ======================================================

    atm_iv: float

    iv_rank: float
    iv_percentile: float

    expected_move: float

    pcr: float

    ce_oi: int
    pe_oi: int

    ce_volume: int
    pe_volume: int

    # ======================================================
    # Greeks
    # ======================================================

    delta_exposure: float
    gamma_exposure: float

    vanna_exposure: float
    charm_exposure: float

    vomma_exposure: float

    vega_exposure: float
    theta_exposure: float

    # ======================================================
    # Dealer
    # ======================================================

    dealer_pressure: float
    gamma_flip: float
    zero_gamma: float

    # ======================================================
    # Institutional
    # ======================================================

    institutional_signal: Signal

    confidence: float

    # ======================================================
    # Metadata
    # ======================================================

    data_quality: float

    generated_at: datetime

    def __post_init__(self):
        """Validate snapshot."""

        if self.days_to_expiry < 0:
            raise ValueError("days_to_expiry cannot be negative")

        if self.lot_size <= 0:
            raise ValueError("lot_size must be positive")

        if self.strike_interval <= 0:
            raise ValueError("strike_interval must be positive")

        if self.volume < 0:
            raise ValueError("volume cannot be negative")

        if self.ce_oi < 0:
            raise ValueError("ce_oi cannot be negative")

        if self.pe_oi < 0:
            raise ValueError("pe_oi cannot be negative")

        if self.ce_volume < 0:
            raise ValueError("ce_volume cannot be negative")

        if self.pe_volume < 0:
            raise ValueError("pe_volume cannot be negative")

        for name, value in (
            ("confidence", self.confidence),
            ("data_quality", self.data_quality),
        ):
            if not (0.0 <= value <= 100.0):
                raise ValueError(f"{name} must be between 0 and 100")

    def __str__(self) -> str:
        return (
            f"{self.symbol} | "
            f"{self.trading_date} | "
            f"{self.institutional_signal.value} | "
            f"Confidence={self.confidence:.1f}%"
        )
