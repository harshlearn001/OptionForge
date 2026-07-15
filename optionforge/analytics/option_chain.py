"""
==============================================================
OptionForge
analytics/option_chain.py
--------------------------------------------------------------
Option Chain Analytics Engine
==============================================================
"""

from __future__ import annotations

import pandas as pd

from optionforge.models import OptionContract
from optionforge.analytics.analytics import OptionAnalytics


class OptionChainAnalytics:
    """
    Processes an entire option chain and enriches it
    with quantitative analytics.
    """

    REQUIRED_COLUMNS = [
        "SYMBOL",
        "TRADE_DATE",
        "EXPIRY_DATE",
        "STRIKE_PRICE",
        "OPTION_TYPE",
        "OPTION_CLOSE",
        "SPOT_CLOSE",
        "RISK_FREE_RATE",
        "TIME_TO_EXPIRY",
    ]

    @staticmethod
    def calculate(option_chain: pd.DataFrame) -> pd.DataFrame:

        df = option_chain.copy()

        missing = [
            c for c in OptionChainAnalytics.REQUIRED_COLUMNS if c not in df.columns
        ]

        if missing:
            raise ValueError(f"Missing required columns: {missing}")

        iv = []
        delta = []
        gamma = []
        theta = []
        vega = []
        intrinsic = []
        time_value = []

        for row in df.itertuples(index=False):

            contract = OptionContract(
                symbol=row.SYMBOL,
                trade_date=row.TRADE_DATE,
                expiry_date=row.EXPIRY_DATE,
                strike=row.STRIKE_PRICE,
                option_type=row.OPTION_TYPE,
                market_price=row.OPTION_CLOSE,
                spot_price=row.SPOT_CLOSE,
                risk_free_rate=row.RISK_FREE_RATE,
                time_to_expiry=row.TIME_TO_EXPIRY,
            )

            result = OptionAnalytics.calculate(contract)

            iv.append(result.implied_volatility)
            delta.append(result.delta)
            gamma.append(result.gamma)
            theta.append(result.theta)
            vega.append(result.vega)
            intrinsic.append(result.intrinsic_value)
            time_value.append(result.time_value)

        df["IV"] = iv
        df["DELTA"] = delta
        df["GAMMA"] = gamma
        df["THETA"] = theta
        df["VEGA"] = vega
        df["INTRINSIC_VALUE"] = intrinsic
        df["TIME_VALUE"] = time_value

        return df
