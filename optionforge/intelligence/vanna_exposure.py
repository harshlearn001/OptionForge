"""
==============================================================
OptionForge
intelligence/vanna_exposure.py
--------------------------------------------------------------
Vanna Exposure Intelligence Engine
==============================================================
"""

from __future__ import annotations

from optionforge.models import VannaExposureResult


class VannaExposure:
    """
    Professional Vanna Exposure Engine.
    """

    @staticmethod
    def calculate(
        *,
        spot_price: float,
        option_chain: list[dict],
    ) -> VannaExposureResult:

        if spot_price <= 0:
            raise ValueError("Spot price must be positive.")

        if len(option_chain) == 0:
            raise ValueError("Option chain cannot be empty.")

        call_vanna = 0.0
        put_vanna = 0.0

        strike_vanna: dict[float, float] = {}

        for option in option_chain:

            strike = float(option["strike"])
            vanna = float(option["vanna"])
            oi = int(option["open_interest"])
            lot = int(option["lot_size"])
            option_type = option["option_type"]

            exposure = vanna * oi * lot * spot_price

            if option_type == "CE":

                call_vanna += exposure

                strike_vanna[strike] = strike_vanna.get(strike, 0.0) + exposure

            elif option_type == "PE":

                put_vanna += exposure

                strike_vanna[strike] = strike_vanna.get(strike, 0.0) - exposure

            else:

                raise ValueError(f"Unknown option type: {option_type}")

        net_vanna = call_vanna + put_vanna

        largest_positive = max(
            strike_vanna,
            key=strike_vanna.get,
        )

        largest_negative = min(
            strike_vanna,
            key=strike_vanna.get,
        )

        if net_vanna >= 0:

            regime = "POSITIVE VANNA"

            interpretation = (
                "Positive Vanna suggests volatility declines "
                "may reinforce dealer buying and support prices."
            )

        else:

            regime = "NEGATIVE VANNA"

            interpretation = (
                "Negative Vanna suggests volatility changes "
                "may reinforce dealer selling and increase "
                "market instability."
            )

        return VannaExposureResult(
            total_call_vanna=call_vanna,
            total_put_vanna=put_vanna,
            net_vanna=net_vanna,
            largest_positive_strike=largest_positive,
            largest_negative_strike=largest_negative,
            vanna_regime=regime,
            interpretation=interpretation,
        )
