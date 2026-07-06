"""
==============================================================
OptionForge
Research
Snapshot Builder
==============================================================

Builds immutable InstitutionalSnapshot objects.

Responsibilities
----------------
- Performs NO calculations.
- Performs NO analytics.
- Performs NO validation.
- Simply assembles already-computed values into an
  immutable InstitutionalSnapshot.

The SnapshotBuilder is intentionally lightweight.
All business logic belongs to the Pipeline and
individual engines.

Author : OptionForge
==============================================================
"""

from __future__ import annotations

from datetime import date, datetime
from uuid import UUID

from optionforge.common.enums import InstrumentType
from optionforge.research.institutional_snapshot import InstitutionalSnapshot
from optionforge.research.signal import Signal


class SnapshotBuilder:
    """
    Builder for immutable InstitutionalSnapshot objects.

    Notes
    -----
    - No calculations.
    - No business logic.
    - No validation.
    - No default timestamps.

    Every value supplied here is assumed to be
    validated by the Pipeline.
    """

    @staticmethod
    def build(
        *,
        # ==========================================================
        # Snapshot Identity
        # ==========================================================
        snapshot_id: UUID,
        snapshot_version: str,
        generated_at: datetime,

        # ==========================================================
        # Trading Information
        # ==========================================================
        trading_date: date,
        expiry_date: date,
        days_to_expiry: int,

        # ==========================================================
        # Instrument
        # ==========================================================
        symbol: str,
        instrument_type: InstrumentType,
        lot_size: int,
        strike_interval: int,

        # ==========================================================
        # Underlying Market
        # ==========================================================
        underlying_close: float,
        atm_strike: float,

        open: float,
        high: float,
        low: float,
        close: float,
        volume: int,

        # ==========================================================
        # Volatility
        # ==========================================================
        atm_iv: float,
        iv_rank: float,
        iv_percentile: float,
        expected_move: float,

        # ==========================================================
        # Open Interest
        # ==========================================================
        pcr: float,
        ce_oi: int,
        pe_oi: int,
        ce_volume: int,
        pe_volume: int,

        # ==========================================================
        # Greeks Exposure
        # ==========================================================
        delta_exposure: float,
        gamma_exposure: float,
        vanna_exposure: float,
        charm_exposure: float,
        vomma_exposure: float,
        vega_exposure: float,
        theta_exposure: float,

        # ==========================================================
        # Institutional Intelligence
        # ==========================================================
        dealer_pressure: float,
        gamma_flip: float,
        zero_gamma: float,

        institutional_signal: Signal,
        confidence: float,
        data_quality: float,
    ) -> InstitutionalSnapshot:
        """
        Assemble and return an immutable InstitutionalSnapshot.

        Parameters
        ----------
        Every parameter supplied to this method must already
        be validated and calculated by the Pipeline.

        Returns
        -------
        InstitutionalSnapshot
            Immutable research snapshot.
        """

        return InstitutionalSnapshot(

            # ======================================================
            # Identity
            # ======================================================
            snapshot_id=snapshot_id,
            snapshot_version=snapshot_version,
            generated_at=generated_at,

            # ======================================================
            # Trading Information
            # ======================================================
            trading_date=trading_date,
            expiry_date=expiry_date,
            days_to_expiry=days_to_expiry,

            # ======================================================
            # Instrument
            # ======================================================
            symbol=symbol,
            instrument_type=instrument_type,
            lot_size=lot_size,
            strike_interval=strike_interval,

            # ======================================================
            # Market
            # ======================================================
            underlying_close=underlying_close,
            atm_strike=atm_strike,

            open=open,
            high=high,
            low=low,
            close=close,
            volume=volume,

            # ======================================================
            # Volatility
            # ======================================================
            atm_iv=atm_iv,
            iv_rank=iv_rank,
            iv_percentile=iv_percentile,
            expected_move=expected_move,

            # ======================================================
            # Open Interest
            # ======================================================
            pcr=pcr,
            ce_oi=ce_oi,
            pe_oi=pe_oi,
            ce_volume=ce_volume,
            pe_volume=pe_volume,

            # ======================================================
            # Greeks
            # ======================================================
            delta_exposure=delta_exposure,
            gamma_exposure=gamma_exposure,
            vanna_exposure=vanna_exposure,
            charm_exposure=charm_exposure,
            vomma_exposure=vomma_exposure,
            vega_exposure=vega_exposure,
            theta_exposure=theta_exposure,

            # ======================================================
            # Institutional Intelligence
            # ======================================================
            dealer_pressure=dealer_pressure,
            gamma_flip=gamma_flip,
            zero_gamma=zero_gamma,

            institutional_signal=institutional_signal,
            confidence=confidence,
            data_quality=data_quality,
        )