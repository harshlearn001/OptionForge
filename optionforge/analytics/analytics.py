"""
==============================================================
OptionForge
analytics/analytics.py
--------------------------------------------------------------
Complete Option Analytics Engine
==============================================================
"""

from optionforge.models import AnalyticsResult, OptionContract
from optionforge.quant.greeks import Greeks
from optionforge.quant.implied_volatility import ImpliedVolatility


class OptionAnalytics:

    @staticmethod
    def calculate(
        contract: OptionContract,
    ) -> AnalyticsResult:

        # --------------------------------------------------
        # Implied Volatility
        # --------------------------------------------------

        if contract.option_type.upper() == "CE":

            iv = ImpliedVolatility.call_iv(
                contract.market_price,
                contract.spot_price,
                contract.strike,
                contract.time_to_expiry,
                contract.risk_free_rate,
            )

        else:

            iv = ImpliedVolatility.put_iv(
                contract.market_price,
                contract.spot_price,
                contract.strike,
                contract.time_to_expiry,
                contract.risk_free_rate,
            )

        # --------------------------------------------------
        # Greeks
        # --------------------------------------------------

        delta = Greeks.delta(
            contract.spot_price,
            contract.strike,
            contract.time_to_expiry,
            contract.risk_free_rate,
            iv,
            contract.option_type,
        )

        gamma = Greeks.gamma(
            contract.spot_price,
            contract.strike,
            contract.time_to_expiry,
            contract.risk_free_rate,
            iv,
            contract.option_type,
        )

        theta = Greeks.theta(
            contract.spot_price,
            contract.strike,
            contract.time_to_expiry,
            contract.risk_free_rate,
            iv,
            contract.option_type,
        )

        vega = Greeks.vega(
            contract.spot_price,
            contract.strike,
            contract.time_to_expiry,
            contract.risk_free_rate,
            iv,
            contract.option_type,
        )

        # --------------------------------------------------
        # Intrinsic Value
        # --------------------------------------------------

        if contract.option_type.upper() == "CE":

            intrinsic = max(
                0.0,
                contract.spot_price - contract.strike,
            )

        else:

            intrinsic = max(
                0.0,
                contract.strike - contract.spot_price,
            )

        # --------------------------------------------------
        # Time Value
        # --------------------------------------------------

        time_value = contract.market_price - intrinsic

        # --------------------------------------------------
        # Return
        # --------------------------------------------------

        return AnalyticsResult(
            implied_volatility=iv,
            delta=delta,
            gamma=gamma,
            theta=theta,
            vega=vega,
            intrinsic_value=intrinsic,
            time_value=time_value,
        )
