"""
==============================================================
OptionForge
quant/black_scholes.py
--------------------------------------------------------------
Black-Scholes European Option Pricing Model
==============================================================
"""

import math

from optionforge.quant.distributions import NormalDistribution


class BlackScholes:
    """
    European Black-Scholes Pricing Engine
    """

    @staticmethod
    def d1(
        spot: float,
        strike: float,
        time: float,
        rate: float,
        volatility: float,
    ) -> float:

        return (
            math.log(spot / strike)
            + (rate + 0.5 * volatility ** 2) * time
        ) / (volatility * math.sqrt(time))

    @staticmethod
    def d2(
        spot: float,
        strike: float,
        time: float,
        rate: float,
        volatility: float,
    ) -> float:

        return (
            BlackScholes.d1(
                spot,
                strike,
                time,
                rate,
                volatility,
            )
            - volatility * math.sqrt(time)
        )

    @staticmethod
    def call_price(
        spot: float,
        strike: float,
        time: float,
        rate: float,
        volatility: float,
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

        return (
            spot * NormalDistribution.cdf(d1)
            - strike
            * math.exp(-rate * time)
            * NormalDistribution.cdf(d2)
        )

    @staticmethod
    def put_price(
        spot: float,
        strike: float,
        time: float,
        rate: float,
        volatility: float,
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

        return (
            strike
            * math.exp(-rate * time)
            * NormalDistribution.cdf(-d2)
            - spot
            * NormalDistribution.cdf(-d1)
        )