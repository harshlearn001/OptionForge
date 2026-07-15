"""
============================================================
OptionForge
Smart PCR Engine
============================================================

Institutional Modified PCR Engine.

Uses:
    - StrikeSelector
    - OICalculator
    - WeightEngine

============================================================
"""

from __future__ import annotations

from optionforge.analytics.pcr.strike_selector import (
    StrikeSelector,
)

from optionforge.analytics.pcr.oi_calculator import (
    OICalculator,
)

from optionforge.analytics.pcr.weight_engine import (
    WeightEngine,
)

from optionforge.analytics.pcr.pcr_result import (
    InstitutionalPCRResult,
)


class SmartPCR:
    """
    Institutional PCR Engine.
    """

    def __init__(self):

        self.weights = WeightEngine()

    # -----------------------------------------------------

    def calculate(
        self,
        snapshot,
    ) -> InstitutionalPCRResult:

        df = snapshot.option_chain

        selector = StrikeSelector(df)

        oi = OICalculator(df)

        spot = float(snapshot.spot["CLOSE"].iloc[-1])

        atm = selector.atm_strike(spot)

        major_call = selector.major_call_strike()

        major_put = selector.major_put_strike()

        call_oi = oi.total_call_oi()

        put_oi = oi.total_put_oi()

        classic = oi.classic_pcr()

        call_weight = self.weights.weight(
            major_call,
            atm,
        )

        put_weight = self.weights.weight(
            major_put,
            atm,
        )

        weighted_call = call_oi * call_weight

        weighted_put = put_oi * put_weight

        if weighted_call == 0:

            weighted = 0.0

        else:

            weighted = round(
                weighted_put / weighted_call,
                4,
            )

        # ---------------------------------------------
        # Market Bias
        # ---------------------------------------------

        if weighted > 1.10:

            bias = "Bullish"

        elif weighted < 0.90:

            bias = "Bearish"

        else:

            bias = "Neutral"

        # ---------------------------------------------
        # Confidence
        # ---------------------------------------------

        confidence = min(
            abs(weighted - 1.0) * 100,
            100,
        )

        return InstitutionalPCRResult(
            symbol=snapshot.symbol,
            trade_date=snapshot.trade_date,
            expiry=snapshot.expiry,
            spot=spot,
            atm_strike=atm,
            major_call_strike=major_call,
            major_put_strike=major_put,
            call_oi=call_oi,
            put_oi=put_oi,
            classic_pcr=classic,
            weighted_pcr=weighted,
            institutional_bias=bias,
            confidence=round(
                confidence,
                2,
            ),
            contracts=len(df),
        )

    # -----------------------------------------------------

    def __repr__(self):

        return "SmartPCR()"

    __str__ = __repr__
