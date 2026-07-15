"""
============================================================
OptionForge
MarketForge CSV Schema
============================================================

Author      : OptionForge
Module      : schema.py

Purpose
-------
Defines the official MarketForge CSV schema used by
OptionForge Integration Layer.

============================================================
"""

from __future__ import annotations

# ============================================================
# REQUIRED COLUMNS
# ============================================================

REQUIRED_COLUMNS = [
    # General
    "Date",
    "Symbol",
    # Prices
    "Spot",
    "Future",
    # ATM
    "ATM Strike",
    # PCR
    "PCR",
    "Modified PCR",
    # Open Interest
    "Call OI",
    "Put OI",
    "Call Change OI",
    "Put Change OI",
    # Greeks
    "IV",
    "Delta",
    "Gamma",
    "Theta",
    "Vega",
]

# ============================================================
# OPTIONAL COLUMNS
# ============================================================

OPTIONAL_COLUMNS = [
    "Volume",
    "VWAP",
    "Max Call OI",
    "Max Put OI",
    "Expected Move",
    "Support",
    "Resistance",
]

# ============================================================
# NUMERIC COLUMNS
# ============================================================

NUMERIC_COLUMNS = [
    "Spot",
    "Future",
    "ATM Strike",
    "PCR",
    "Modified PCR",
    "Call OI",
    "Put OI",
    "Call Change OI",
    "Put Change OI",
    "IV",
    "Delta",
    "Gamma",
    "Theta",
    "Vega",
]

# ============================================================
# DATE COLUMNS
# ============================================================

DATE_COLUMNS = [
    "Date",
]
