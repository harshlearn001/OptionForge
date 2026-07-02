"""
==============================================================
OptionForge
intelligence/delta_exposure.py
--------------------------------------------------------------
Delta Exposure Intelligence Engine
==============================================================
"""

from __future__ import annotations

from optionforge.models import DeltaExposureResult


class DeltaExposure:
    """
    Professional Delta Exposure Engine.
    """

    @staticmethod
    def calculate(
        *,
        spot_price: float,
        option_chain: list[dict],
    ) -> DeltaExposureResult:

        if spot_price <= 0:
            raise ValueError(
                "Spot price must be positive."
            )

        if len(option_chain) == 0:
            raise ValueError(
                "Option chain cannot be empty."
            )

        call_dex = 0.0
        put_dex = 0.0

        strike_dex: dict[float, float] = {}

        for option in option_chain:

            strike = float(option["strike"])
            delta = float(option["delta"])
            oi = int(option["open_interest"])
            lot = int(option["lot_size"])
            option_type = option["option_type"]

            exposure = (
                delta
                * oi
                * lot
                * spot_price
            )

            if option_type == "CE":

                call_dex += exposure
                strike_dex[strike] = (
                    strike_dex.get(strike, 0.0)
                    + exposure
                )

            elif option_type == "PE":

                put_dex += exposure
                strike_dex[strike] = (
                    strike_dex.get(strike, 0.0)
                    - exposure
                )

            else:

                raise ValueError(
                    f"Unknown option type: {option_type}"
                )

        net_dex = call_dex + put_dex

        largest_positive = max(
            strike_dex,
            key=strike_dex.get,
        )

        largest_negative = min(
            strike_dex,
            key=strike_dex.get,
        )

        if net_dex >= 0:

            dealer_position = "LONG DELTA"

            interpretation = (
                "Dealers are net long delta. "
                "Hedging activity may provide buying support during declines."
            )

        else:

            dealer_position = "SHORT DELTA"

            interpretation = (
                "Dealers are net short delta. "
                "Hedging activity may reinforce directional moves and increase volatility."
            )

        return DeltaExposureResult(

            total_call_dex=call_dex,

            total_put_dex=put_dex,

            net_dex=net_dex,

            largest_positive_strike=largest_positive,

            largest_negative_strike=largest_negative,

            dealer_position=dealer_position,

            interpretation=interpretation,
        )