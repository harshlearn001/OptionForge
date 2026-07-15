"""
==============================================================
OptionForge
models/option_contract.py
--------------------------------------------------------------
Option Contract Model
==============================================================
"""

from dataclasses import dataclass
from datetime import date


@dataclass(slots=True)
class OptionContract:
    """
    Represents a single option contract.
    """

    symbol: str

    trade_date: date

    expiry_date: date

    strike: float

    option_type: str  # "CE" or "PE"

    market_price: float

    spot_price: float

    risk_free_rate: float

    time_to_expiry: float
