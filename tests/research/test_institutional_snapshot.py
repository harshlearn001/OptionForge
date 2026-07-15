"""
==============================================================
OptionForge
Research
Institutional Snapshot Tests
==============================================================
"""

from dataclasses import FrozenInstanceError, replace
from datetime import date, datetime
from uuid import uuid4

import pytest

from optionforge.common.enums import InstrumentType
from optionforge.research.institutional_snapshot import (
    InstitutionalSnapshot,
)
from optionforge.research.signal import Signal


def make_snapshot():
    return InstitutionalSnapshot(
        snapshot_id=uuid4(),
        snapshot_version="1.0.0",
        trading_date=date(2026, 7, 6),
        expiry_date=date(2026, 7, 9),
        days_to_expiry=3,
        symbol="NIFTY",
        instrument_type=InstrumentType.INDEX,
        underlying_close=25640,
        atm_strike=25650,
        lot_size=65,
        strike_interval=50,
        open=25580,
        high=25700,
        low=25540,
        close=25640,
        volume=1_250_000,
        atm_iv=14.2,
        iv_rank=22,
        iv_percentile=18,
        expected_move=280,
        pcr=1.08,
        ce_oi=420_000,
        pe_oi=460_000,
        ce_volume=185_000,
        pe_volume=198_000,
        delta_exposure=2.4,
        gamma_exposure=128_000,
        vanna_exposure=5100,
        charm_exposure=-210,
        vomma_exposure=740,
        vega_exposure=18_500,
        theta_exposure=-6400,
        dealer_pressure=81.2,
        gamma_flip=25350,
        zero_gamma=25200,
        institutional_signal=Signal.BUY,
        confidence=84.5,
        data_quality=100.0,
        generated_at=datetime.now(),
    )


# ==========================================================
# Creation
# ==========================================================


def test_snapshot_creation():
    snapshot = make_snapshot()

    assert snapshot.symbol == "NIFTY"
    assert snapshot.instrument_type == InstrumentType.INDEX
    assert snapshot.institutional_signal == Signal.BUY
    assert snapshot.confidence == 84.5


# ==========================================================
# Frozen Dataclass
# ==========================================================


def test_snapshot_is_frozen():
    snapshot = make_snapshot()

    with pytest.raises(FrozenInstanceError):
        snapshot.symbol = "BANKNIFTY"


# ==========================================================
# Validation
# ==========================================================


def test_negative_days():
    snapshot = make_snapshot()

    with pytest.raises(ValueError):
        replace(snapshot, days_to_expiry=-1)


def test_negative_volume():
    snapshot = make_snapshot()

    with pytest.raises(ValueError):
        replace(snapshot, volume=-1)


def test_invalid_confidence():
    snapshot = make_snapshot()

    with pytest.raises(ValueError):
        replace(snapshot, confidence=120)


def test_invalid_data_quality():
    snapshot = make_snapshot()

    with pytest.raises(ValueError):
        replace(snapshot, data_quality=120)


def test_invalid_lot_size():
    snapshot = make_snapshot()

    with pytest.raises(ValueError):
        replace(snapshot, lot_size=0)


def test_invalid_strike_interval():
    snapshot = make_snapshot()

    with pytest.raises(ValueError):
        replace(snapshot, strike_interval=0)


def test_negative_call_oi():
    snapshot = make_snapshot()

    with pytest.raises(ValueError):
        replace(snapshot, ce_oi=-1)


def test_negative_put_oi():
    snapshot = make_snapshot()

    with pytest.raises(ValueError):
        replace(snapshot, pe_oi=-1)


def test_negative_call_volume():
    snapshot = make_snapshot()

    with pytest.raises(ValueError):
        replace(snapshot, ce_volume=-1)


def test_negative_put_volume():
    snapshot = make_snapshot()

    with pytest.raises(ValueError):
        replace(snapshot, pe_volume=-1)
