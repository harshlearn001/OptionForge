"""
==============================================================
OptionForge
Master OI Analytics Engine
==============================================================
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from optionforge.optionchain import OptionChain


class OIByStrike:
    """
    Master OI Analytics Engine.

    One row = One Strike

    This is the single source of truth for every
    Open Interest based engine inside OptionForge.
    """

    # ==========================================================
    # Constructor
    # ==========================================================

    def __init__(self, chain: OptionChain):

        self.chain = chain

        self.df = self._build()
    # ==========================================================
    # Master Builder
    # ==========================================================

    def _build(self) -> pd.DataFrame:

        table = self._aggregate()

        table = self._calculate_totals(table)

        table = self._calculate_shares(table)

        table = self._calculate_pcr(table)

        table = self._calculate_net(table)

        table = self._calculate_dominance(table)

        table = (
            table
            .sort_values("STRIKE")
            .reset_index(drop=True)
        )

        return table
        # ==========================================================
    # Aggregate Option Chain
    # ==========================================================

    def _aggregate(self) -> pd.DataFrame:

        df = self.chain.dataframe()

        calls = (
            df[df["OPTION_TYPE"] == "CE"]
            .groupby("STRIKE", as_index=False)
            .agg(
                CALL_OI=("OI", "sum"),
                CALL_VOLUME=("VOLUME", "sum"),
                CALL_PREMIUM=("PREMIUM_VALUE", "sum"),
            )
        )

        puts = (
            df[df["OPTION_TYPE"] == "PE"]
            .groupby("STRIKE", as_index=False)
            .agg(
                PUT_OI=("OI", "sum"),
                PUT_VOLUME=("VOLUME", "sum"),
                PUT_PREMIUM=("PREMIUM_VALUE", "sum"),
            )
        )

        table = (
            calls
            .merge(
                puts,
                on="STRIKE",
                how="outer",
            )
            .fillna(0)
        )

        for column in [
            "CALL_OI",
            "PUT_OI",
            "CALL_VOLUME",
            "PUT_VOLUME",
        ]:
            table[column] = table[column].astype(int)

        return table
    
        # ==========================================================
    # Totals
    # ==========================================================

    def _calculate_totals(
        self,
        table: pd.DataFrame,
    ) -> pd.DataFrame:

        table["TOTAL_OI"] = (
            table["CALL_OI"] +
            table["PUT_OI"]
        )

        table["TOTAL_VOLUME"] = (
            table["CALL_VOLUME"] +
            table["PUT_VOLUME"]
        )

        table["TOTAL_PREMIUM"] = (
            table["CALL_PREMIUM"] +
            table["PUT_PREMIUM"]
        )

        return table

    # ==========================================================
    # Shares
    # ==========================================================

    def _calculate_shares(
        self,
        table: pd.DataFrame,
    ) -> pd.DataFrame:

        total_call = table["CALL_OI"].sum()
        total_put = table["PUT_OI"].sum()
        total_oi = table["TOTAL_OI"].sum()

        table["CALL_SHARE"] = (
            table["CALL_OI"] / total_call
            if total_call > 0 else 0.0
        )

        table["PUT_SHARE"] = (
            table["PUT_OI"] / total_put
            if total_put > 0 else 0.0
        )

        table["OI_SHARE"] = (
            table["TOTAL_OI"] / total_oi
            if total_oi > 0 else 0.0
        )

        return table

    # ==========================================================
    # Strike PCR
    # ==========================================================

    def _calculate_pcr(
        self,
        table: pd.DataFrame,
    ) -> pd.DataFrame:

        table["PCR"] = np.where(
            table["CALL_OI"] == 0,
            np.nan,
            table["PUT_OI"] / table["CALL_OI"],
        )

        return table

    # ==========================================================
    # Net Values
    # ==========================================================

    def _calculate_net(
        self,
        table: pd.DataFrame,
    ) -> pd.DataFrame:

        table["NET_OI"] = (
            table["PUT_OI"] -
            table["CALL_OI"]
        )

        table["NET_VOLUME"] = (
            table["PUT_VOLUME"] -
            table["CALL_VOLUME"]
        )

        return table

    # ==========================================================
    # Dominance
    # ==========================================================

    def _calculate_dominance(
        self,
        table: pd.DataFrame,
    ) -> pd.DataFrame:

        table["DOMINANCE"] = "BALANCED"

        table.loc[
            table["CALL_SHARE"] >
            table["PUT_SHARE"],
            "DOMINANCE"
        ] = "CALL"

        table.loc[
            table["PUT_SHARE"] >
            table["CALL_SHARE"],
            "DOMINANCE"
        ] = "PUT"

        return table
    
        # ==========================================================
    # Public API
    # ==========================================================

    def dataframe(self) -> pd.DataFrame:
        """
        Returns a copy of the Master OI table.
        """
        return self.df.copy()

    # ==========================================================
    # Top Call OI
    # ==========================================================

    def top_call_oi(
        self,
        n: int = 10,
    ) -> pd.DataFrame:

        return (
            self.df
            .nlargest(n, "CALL_OI")
            .reset_index(drop=True)
        )

    # ==========================================================
    # Top Put OI
    # ==========================================================

    def top_put_oi(
        self,
        n: int = 10,
    ) -> pd.DataFrame:

        return (
            self.df
            .nlargest(n, "PUT_OI")
            .reset_index(drop=True)
        )

    # ==========================================================
    # Top Total OI
    # ==========================================================

    def top_total_oi(
        self,
        n: int = 10,
    ) -> pd.DataFrame:

        return (
            self.df
            .nlargest(n, "TOTAL_OI")
            .reset_index(drop=True)
        )

    # ==========================================================
    # Support Candidates
    # ==========================================================

    def support_candidates(
        self,
        n: int = 10,
    ) -> pd.DataFrame:

        return self.top_put_oi(n)

    # ==========================================================
    # Resistance Candidates
    # ==========================================================

    def resistance_candidates(
        self,
        n: int = 10,
    ) -> pd.DataFrame:

        return self.top_call_oi(n)
    
        # ==========================================================
    # Number of Strikes
    # ==========================================================

    def __len__(self) -> int:

        return len(self.df)

    # ==========================================================
    # Representation
    # ==========================================================

    def __repr__(self) -> str:

        return (
            f"OIByStrike("
            f"rows={len(self.df)}, "
            f"columns={len(self.df.columns)})"
        )