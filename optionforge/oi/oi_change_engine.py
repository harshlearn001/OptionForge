"""
==============================================================
OptionForge
OI Change Engine
==============================================================
"""

from __future__ import annotations

import pandas as pd

from optionforge.market.option_chain import OptionChain
from optionforge.oi.oi_change_result import OIChangeResult


class OIChangeEngine:
    """
    Strike-wise OI Change analytics.
    """

    def __init__(self, chain: OptionChain):

        self.chain = chain

    # ------------------------------------------------------

    def calculate(self) -> OIChangeResult:

        df = self.chain.to_dataframe()

        # --------------------------------------------------
        # Temporary placeholder table
        # --------------------------------------------------

        table = pd.DataFrame({

            "strike_price": df["strike_price"],

            "call_oi": 0,

            "put_oi": 0,

            "call_change": 0,

            "put_change": 0,

            "total_change": 0,

            "call_volume": 0,

            "put_volume": 0,

            "pcr": 0.0,

            "dominance": "BALANCED",

            "buildup": "UNKNOWN",

        })

        return OIChangeResult(table)