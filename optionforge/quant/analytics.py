"""
==============================================================
OptionForge
quant/analytics.py
--------------------------------------------------------------
Unified Quantitative Analytics API

Combines:

- Black-Scholes
- Greeks
- Implied Volatility

==============================================================
"""

from __future__ import annotations

from dataclasses import dataclass

from optionforge.quant.black_scholes import (
    BlackScholes,
)

from optionforge.quant.greeks import (
    Greeks,
)

from optionforge.quant.implied_volatility import (
    ImpliedVolatility,
)

# ==============================================================
# Result Object
# ==============================================================


@dataclass(
    frozen=True,
    slots=True,
)
class AnalyticsResult:
    """
    Unified quantitative analytics result.
    """

    price: float

    delta: float

    gamma: float

    theta: float

    vega: float

    implied_volatility: float | None = None


# ==============================================================
# Analytics
# ==============================================================


class OptionAnalytics:
    """
    Unified quantitative analytics.
    """

    def calculate(
        self,
        *,
        spot: float,
        strike: float,
        time: float,
        rate: float,
        volatility: float,
        option_type: str,
        market_price: float | None = None,
    ) -> AnalyticsResult:

        option_type = option_type.upper()

        if option_type == "CE":

            price = BlackScholes.call_price(
                spot,
                strike,
                time,
                rate,
                volatility,
            )

        else:

            price = BlackScholes.put_price(
                spot,
                strike,
                time,
                rate,
                volatility,
            )

        delta = Greeks.delta(
            spot,
            strike,
            time,
            rate,
            volatility,
            option_type,
        )

        gamma = Greeks.gamma(
            spot,
            strike,
            time,
            rate,
            volatility,
            option_type,
        )

        theta = Greeks.theta(
            spot,
            strike,
            time,
            rate,
            volatility,
            option_type,
        )

        vega = Greeks.vega(
            spot,
            strike,
            time,
            rate,
            volatility,
            option_type,
        )

        iv = None

        if market_price is not None:

            if option_type == "CE":

                iv = ImpliedVolatility.call_iv(
                    market_price,
                    spot,
                    strike,
                    time,
                    rate,
                )

            else:

                iv = ImpliedVolatility.put_iv(
                    market_price,
                    spot,
                    strike,
                    time,
                    rate,
                )

        return AnalyticsResult(
            price=price,
            delta=delta,
            gamma=gamma,
            theta=theta,
            vega=vega,
            implied_volatility=iv,
        )

    def __repr__(self):

        return "OptionAnalytics()"

    __str__ = __repr__
