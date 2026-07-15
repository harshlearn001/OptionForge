"""
==============================================================
OptionForge
intelligence/charm_exposure.py
--------------------------------------------------------------
Charm Exposure Intelligence Engine
==============================================================
"""

from __future__ import annotations

from optionforge.models import CharmExposureResult


class CharmExposure:
    """
    Professional Charm Exposure Engine.
    """

    @staticmethod
    def calculate(
        *,
        spot_price: float,
        option_chain: list[dict],
    ) -> CharmExposureResult:

        if spot_price <= 0:
            raise ValueError("Spot price must be positive.")

        if len(option_chain) == 0:
            raise ValueError("Option chain cannot be empty.")

        call_charm = 0.0
        put_charm = 0.0

        strike_charm: dict[float, float] = {}

        for option in option_chain:

            strike = float(option["strike"])
            charm = float(option["charm"])
            oi = int(option["open_interest"])
            lot = int(option["lot_size"])
            option_type = option["option_type"]

            exposure = charm * oi * lot * spot_price

            if option_type == "CE":

                call_charm += exposure

                strike_charm[strike] = strike_charm.get(strike, 0.0) + exposure

            elif option_type == "PE":

                put_charm += exposure

                strike_charm[strike] = strike_charm.get(strike, 0.0) - exposure

            else:

                raise ValueError(f"Unknown option type: {option_type}")

        net_charm = call_charm + put_charm

        largest_positive = max(
            strike_charm,
            key=strike_charm.get,
        )

        largest_negative = min(
            strike_charm,
            key=strike_charm.get,
        )

        if net_charm >= 0:

            regime = "POSITIVE CHARM"

            interpretation = (
                "Positive Charm suggests time decay may lead "
                "to dealer buying, helping stabilize prices."
            )

        else:

            regime = "NEGATIVE CHARM"

            interpretation = (
                "Negative Charm suggests time decay may lead "
                "to dealer selling, increasing directional pressure."
            )

        return CharmExposureResult(
            total_call_charm=call_charm,
            total_put_charm=put_charm,
            net_charm=net_charm,
            largest_positive_strike=largest_positive,
            largest_negative_strike=largest_negative,
            charm_regime=regime,
            interpretation=interpretation,
        )
