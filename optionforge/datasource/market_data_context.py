"""
==============================================================
OptionForge
Datasource
Market Data Context
==============================================================

Normalized raw market data exchanged between the
Data Access Layer and the Pipeline.

Responsibilities
----------------
- Hold raw market datasets.
- No calculations.
- No validation.
- No business logic.

Version : 2.0
Author  : OptionForge
==============================================================
"""

from __future__ import annotations

from dataclasses import dataclass

import pandas as pd

from optionforge.common.enums import InstrumentType


@dataclass(slots=True)
class MarketDataContext:
    """
    Normalized market datasets required by OptionForge.

    Notes
    -----
    This object represents raw market data only.

    Derived values such as:

    - ATM Strike
    - ATM IV
    - Expected Move
    - Greeks
    - PCR
    - Max Pain

    are produced later by analytics engines.
    """

    # ==========================================================
    # Identity
    # ==========================================================

    symbol: str

    instrument_type: InstrumentType

    spot_data: pd.DataFrame

    futures_data: pd.DataFrame

    options_data: pd.DataFrame

    delivery_data: pd.DataFrame | None = None

    vix_data: pd.DataFrame | None = None
