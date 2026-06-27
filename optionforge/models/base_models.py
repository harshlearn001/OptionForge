"""
OptionForge
models/dataclasses.py
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class OptionRecord:

    # ==========================================================
    # BASIC INFORMATION
    # ==========================================================

    trade_date: str
    symbol: str
    expiry_date: str

    strike_price: float
    option_type: str      # CE / PE

    # ==========================================================
    # MARKET DATA
    # ==========================================================

    spot_close: float
    future_close: float
    option_close: float

    option_volume: float
    open_interest: float
    change_in_oi: float

    # ==========================================================
    # DERIVED DATA
    # ==========================================================

    days_to_expiry: float

    risk_free_rate: float

    dividend_yield: float = 0.0

    intrinsic_value: Optional[float] = None
    time_value: Optional[float] = None

    # ==========================================================
    # IMPLIED VOLATILITY
    # ==========================================================

    iv: Optional[float] = None

    # ==========================================================
    # FIRST ORDER
    # ==========================================================

    delta: Optional[float] = None

    # ==========================================================
    # SECOND ORDER
    # ==========================================================

    gamma: Optional[float] = None

    # ==========================================================
    # TIME GREEK
    # ==========================================================

    theta: Optional[float] = None

    # ==========================================================
    # VOLATILITY GREEK
    # ==========================================================

    vega: Optional[float] = None

    # ==========================================================
    # FUTURE GREEKS
    # ==========================================================

    vomma: Optional[float] = None
    vanna: Optional[float] = None
    charm: Optional[float] = None
    color: Optional[float] = None
    speed: Optional[float] = None
    zomma: Optional[float] = None
    ultima: Optional[float] = None