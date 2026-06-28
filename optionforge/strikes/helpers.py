"""
==============================================================
OptionForge
Strike Helpers
--------------------------------------------------------------
Professional Strike Utility Functions
==============================================================
"""

from __future__ import annotations

import pandas as pd


# ==========================================================
# Basic Validation
# ==========================================================

def validate_dataframe(df: pd.DataFrame) -> None:
    """
    Ensure dataframe contains STRIKE column.
    """

    if "STRIKE" not in df.columns:
        raise ValueError("DataFrame must contain STRIKE column.")


# ==========================================================
# Strike Increment
# ==========================================================

def strike_step(df: pd.DataFrame) -> int:
    """
    Detect minimum strike interval automatically.

    Example

    50
    100
    """

    validate_dataframe(df)

    strikes = sorted(df["STRIKE"].unique())

    if len(strikes) < 2:
        return 50

    diffs = []

    for i in range(1, len(strikes)):
        d = strikes[i] - strikes[i - 1]
        if d > 0:
            diffs.append(d)

    if not diffs:
        return 50

    return int(min(diffs))


# ==========================================================
# Round Strike
# ==========================================================

def round_strike(price: float, step: int) -> int:
    """
    Round price to nearest strike.
    """

    return int(round(price / step) * step)


# ==========================================================
# Nearest Strike
# ==========================================================

def nearest_strike(df: pd.DataFrame, spot: float) -> int:
    """
    Return nearest available strike.
    """

    validate_dataframe(df)

    strikes = df["STRIKE"].unique()

    return int(
        min(
            strikes,
            key=lambda x: abs(x - spot)
        )
    )


# ==========================================================
# ATM Strike
# ==========================================================

def atm_strike(df: pd.DataFrame, spot: float) -> int:
    """
    ATM strike from available strikes.
    """

    return nearest_strike(df, spot)


# ==========================================================
# Previous Strike
# ==========================================================

def previous_strike(df: pd.DataFrame, strike: int) -> int | None:

    validate_dataframe(df)

    strikes = sorted(df["STRIKE"].unique())

    idx = strikes.index(strike)

    if idx == 0:
        return None

    return strikes[idx - 1]


# ==========================================================
# Next Strike
# ==========================================================

def next_strike(df: pd.DataFrame, strike: int) -> int | None:

    validate_dataframe(df)

    strikes = sorted(df["STRIKE"].unique())

    idx = strikes.index(strike)

    if idx == len(strikes) - 1:
        return None

    return strikes[idx + 1]


# ==========================================================
# Strike Exists
# ==========================================================

def strike_exists(df: pd.DataFrame, strike: int) -> bool:

    validate_dataframe(df)

    return strike in df["STRIKE"].unique()


# ==========================================================
# All Strikes
# ==========================================================

def available_strikes(df: pd.DataFrame):

    validate_dataframe(df)

    return sorted(df["STRIKE"].unique())