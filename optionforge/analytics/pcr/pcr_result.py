"""
============================================================
OptionForge
Institutional PCR Result
============================================================

Immutable result object for Institutional PCR.

============================================================
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    frozen=True,
    slots=True,
)
class InstitutionalPCRResult:
    """
    Result returned by Smart PCR engine.
    """

    symbol: str

    trade_date: int

    expiry: int

    spot: float

    atm_strike: int

    major_call_strike: int

    major_put_strike: int

    call_oi: int

    put_oi: int

    classic_pcr: float

    weighted_pcr: float

    institutional_bias: str

    confidence: float

    contracts: int

    def __repr__(self) -> str:

        return (
            f"InstitutionalPCRResult("
            f"symbol={self.symbol}, "
            f"weighted_pcr={self.weighted_pcr:.4f}, "
            f"bias='{self.institutional_bias}')"
        )

    __str__ = __repr__