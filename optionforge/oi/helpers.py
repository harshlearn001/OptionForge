"""
==============================================================
OptionForge
OI Helpers
--------------------------------------------------------------
Professional Open Interest Utility Functions
==============================================================
"""

from __future__ import annotations

import pandas as pd

# ==========================================================
# Validation
# ==========================================================

REQUIRED_COLUMNS = [
    "option_type",
    "open_interest",
    "volume",
    "contracts",
    "trades",
]


def validate(df: pd.DataFrame) -> None:
    """
    Validate required columns.
    """

    missing = [c for c in REQUIRED_COLUMNS if c not in df.columns]

    if missing:
        raise ValueError(f"Missing columns: {missing}")


# ==========================================================
# Calls / Puts
# ==========================================================


def calls(df: pd.DataFrame) -> pd.DataFrame:

    validate(df)

    return df[df["option_type"].isin(["CALL", "CE"])].copy().reset_index(drop=True)


def puts(df: pd.DataFrame) -> pd.DataFrame:

    validate(df)

    return df[df["option_type"].isin(["PUT", "PE"])].copy().reset_index(drop=True)


# ==========================================================
# Total OI
# ==========================================================


def total_call_oi(df: pd.DataFrame) -> int:

    return int(calls(df)["open_interest"].sum())


def total_put_oi(df: pd.DataFrame) -> int:

    return int(puts(df)["open_interest"].sum())


# ==========================================================
# Volume
# ==========================================================


def total_call_volume(df: pd.DataFrame) -> int:

    return int(calls(df)["volume"].sum())


def total_put_volume(df: pd.DataFrame) -> int:

    return int(puts(df)["volume"].sum())


# ==========================================================
# Contracts
# ==========================================================


def total_contracts(df: pd.DataFrame) -> int:

    validate(df)

    return int(df["contracts"].sum())


# ==========================================================
# Trades
# ==========================================================


def total_trades(df: pd.DataFrame) -> int:

    validate(df)

    return int(df["trades"].sum())


# ==========================================================
# PCR
# ==========================================================


def pcr(df: pd.DataFrame) -> float:
    """
    Put Call Ratio using Open Interest.
    """

    call_oi = total_call_oi(df)

    put_oi = total_put_oi(df)

    if call_oi == 0:
        return 0.0

    return round(put_oi / call_oi, 4)
