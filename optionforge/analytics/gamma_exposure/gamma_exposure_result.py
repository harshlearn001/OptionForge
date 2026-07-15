"""
============================================================
OptionForge
Gamma Exposure Result
============================================================

Immutable result object for Gamma Exposure.

============================================================
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    frozen=True,
    slots=True,
)
class GammaExposureResult:
    """
    Result returned by GammaExposureEngine.
    """

    symbol: str

    trade_date: int

    expiry: int

    strike: float

    gamma: float

    open_interest: int

    contract_size: int

    spot: float

    gamma_exposure: float

    def __repr__(self):

        return (
            f"GammaExposureResult("
            f"symbol={self.symbol}, "
            f"strike={self.strike}, "
            f"gamma_exposure={self.gamma_exposure:.2f})"
        )

    __str__ = __repr__
