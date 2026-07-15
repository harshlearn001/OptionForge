"""
==============================================================
OptionForge
intelligence/gamma_exposure.py
--------------------------------------------------------------
Gamma Exposure Intelligence Engine
==============================================================
"""

from __future__ import annotations

from optionforge.models import GammaExposureResult


class GammaExposure:
    """
    Professional Gamma Exposure Engine.
    """

    @staticmethod
    def calculate(
        *,
        spot_price: float,
        option_chain: list[dict],
    ) -> GammaExposureResult:

        if spot_price <= 0:
            raise ValueError("Spot price must be positive.")

        if len(option_chain) == 0:
            raise ValueError("Option chain cannot be empty.")

        call_gex = 0.0
        put_gex = 0.0

        strike_gex: dict[float, float] = {}

        for option in option_chain:

            strike = float(option["strike"])
            gamma = float(option["gamma"])
            oi = int(option["open_interest"])
            lot = int(option["lot_size"])
            option_type = option["option_type"]

            exposure = gamma * oi * lot * (spot_price**2) * 0.01

            if option_type == "CE":
                call_gex += exposure
            else:
                put_gex += exposure

            strike_gex[strike] = strike_gex.get(strike, 0.0) + exposure

        net_gex = call_gex - put_gex

        largest_positive = max(
            strike_gex,
            key=strike_gex.get,
        )

        largest_negative = min(
            strike_gex,
            key=strike_gex.get,
        )

        gamma_flip = 0.0

        if net_gex >= 0:

            regime = "POSITIVE GAMMA"

            interpretation = (
                "Dealers are likely long gamma. "
                "Market may remain stable and mean reverting."
            )

        else:

            regime = "NEGATIVE GAMMA"

            interpretation = (
                "Dealers are likely short gamma. "
                "Market may become directional with higher volatility."
            )

        return GammaExposureResult(
            total_call_gex=call_gex,
            total_put_gex=put_gex,
            net_gex=net_gex,
            largest_positive_strike=largest_positive,
            largest_negative_strike=largest_negative,
            gamma_flip=gamma_flip,
            market_regime=regime,
            interpretation=interpretation,
        )
