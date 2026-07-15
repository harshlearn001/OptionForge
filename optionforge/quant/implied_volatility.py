"""
==============================================================
OptionForge
quant/implied_volatility.py
--------------------------------------------------------------
Implied Volatility Solver
==============================================================
"""

from optionforge.quant.black_scholes import BlackScholes
from optionforge.quant.root_solver import RootSolver


class ImpliedVolatility:

    @staticmethod
    def call_iv(
        market_price: float,
        spot: float,
        strike: float,
        time: float,
        rate: float,
    ) -> float:

        def objective(vol):

            return (
                BlackScholes.call_price(
                    spot,
                    strike,
                    time,
                    rate,
                    vol,
                )
                - market_price
            )

        return RootSolver.bisection(
            objective,
            lower=0.0001,
            upper=5.0,
        )

    @staticmethod
    def put_iv(
        market_price: float,
        spot: float,
        strike: float,
        time: float,
        rate: float,
    ) -> float:

        def objective(vol):

            return (
                BlackScholes.put_price(
                    spot,
                    strike,
                    time,
                    rate,
                    vol,
                )
                - market_price
            )

        return RootSolver.bisection(
            objective,
            lower=0.0001,
            upper=5.0,
        )
