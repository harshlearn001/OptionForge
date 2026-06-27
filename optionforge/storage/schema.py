"""
==============================================================
OptionForge
storage/schema.py
--------------------------------------------------------------
Master Storage Schema
==============================================================
"""

REQUIRED_COLUMNS = [

    "SYMBOL",
    "TRADE_DATE",
    "EXPIRY_DATE",

    "STRIKE_PRICE",
    "OPTION_TYPE",

    "OPTION_CLOSE",
    "SPOT_CLOSE",

    "OPEN_INTEREST",
    "CHANGE_IN_OI",
    "OPTION_VOLUME",

    "IV",
    "DELTA",
    "GAMMA",
    "THETA",
    "VEGA",

    "INTRINSIC_VALUE",
    "TIME_VALUE",
]