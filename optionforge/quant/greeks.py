"""
==============================================================
OptionForge
quant/greeks.py
--------------------------------------------------------------
European Black-Scholes Greeks
==============================================================
"""

import math

from optionforge.quant.black_scholes import BlackScholes
from optionforge.quant.distributions import NormalDistribution


class Greeks:
    """
    Black-Scholes Greeks
    """

    @staticmethod
    def delta(
        spot: float,
        strike: float,
        time: float,
        rate: float,
        volatility: float,
        option_type: str,
    ) -> float:

        d1 = BlackScholes.d1(
            spot,
            strike,
            time,
            rate,
            volatility,
        )

        if option_type.upper() == "CE":
            return NormalDistribution.cdf(d1)

        return NormalDistribution.cdf(d1) - 1.0

    @staticmethod
    def gamma(
        spot: float,
        strike: float,
        time: float,
        rate: float,
        volatility: float,
        option_type: str,
    ) -> float:

        d1 = BlackScholes.d1(
            spot,
            strike,
            time,
            rate,
            volatility,
        )

        return NormalDistribution.pdf(d1) / (spot * volatility * math.sqrt(time))

    @staticmethod
    def vega(
        spot: float,
        strike: float,
        time: float,
        rate: float,
        volatility: float,
        option_type: str,
    ) -> float:

        d1 = BlackScholes.d1(
            spot,
            strike,
            time,
            rate,
            volatility,
        )

        return spot * NormalDistribution.pdf(d1) * math.sqrt(time)

    @staticmethod
    def theta(
        spot: float,
        strike: float,
        time: float,
        rate: float,
        volatility: float,
        option_type: str,
    ) -> float:

        d1 = BlackScholes.d1(
            spot,
            strike,
            time,
            rate,
            volatility,
        )

        d2 = BlackScholes.d2(
            spot,
            strike,
            time,
            rate,
            volatility,
        )

        first_term = (
            -spot * NormalDistribution.pdf(d1) * volatility / (2 * math.sqrt(time))
        )

        if option_type.upper() == "CE":

            second_term = (
                rate * strike * math.exp(-rate * time) * NormalDistribution.cdf(d2)
            )

            return first_term - second_term

        second_term = (
            rate * strike * math.exp(-rate * time) * NormalDistribution.cdf(-d2)
        )

        return first_term + second_term
