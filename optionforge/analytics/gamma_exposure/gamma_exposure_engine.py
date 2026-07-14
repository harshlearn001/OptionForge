"""
============================================================
OptionForge
Gamma Exposure Engine
============================================================

Institutional Gamma Exposure Engine

============================================================
"""

from __future__ import annotations

from optionforge.analytics.gamma_exposure.gamma_exposure_calculator import (
    GammaExposureCalculator,
)

from optionforge.analytics.gamma_exposure.gamma_exposure_result import (
    GammaExposureResult,
)


class GammaExposureEngine:
    """
    Institutional Gamma Exposure Engine.
    """

    def __init__(self):

        self._calculator = GammaExposureCalculator()

    @property
    def calculator(self):

        return self._calculator

    def calculate(
        self,
        *,
        symbol: str,
        trade_date: int,
        expiry: int,
        strike: float,
        gamma: float,
        open_interest: int,
        contract_size: int,
        spot: float,
    ) -> GammaExposureResult:

        exposure = self.calculator.calculate(

            gamma=gamma,

            open_interest=open_interest,

            contract_size=contract_size,

            spot=spot,

        )

        return GammaExposureResult(

            symbol=symbol,

            trade_date=trade_date,

            expiry=expiry,

            strike=strike,

            gamma=gamma,

            open_interest=open_interest,

            contract_size=contract_size,

            spot=spot,

            gamma_exposure=exposure,

        )

    def __repr__(self):

        return "GammaExposureEngine()"

    __str__ = __repr__