"""
============================================================
OptionForge
Feature Group Enumeration
============================================================

Author      : OptionForge
Module      : feature_group.py
Purpose     : Categorizes FeatureIds into logical groups.

These groups are used for filtering, reporting,
dashboard visualization, evidence generation,
and decision making.
============================================================
"""

from __future__ import annotations

from enum import Enum


class FeatureGroup(str, Enum):
    """
    Logical grouping of OptionForge features.
    """

    GREEKS = "Greeks"

    IMPLIED_VOLATILITY = "Implied Volatility"

    OPEN_INTEREST = "Open Interest"

    MARKET_STRUCTURE = "Market Structure"

    DEALER = "Dealer"

    INSTITUTIONAL = "Institutional"

    VOLATILITY = "Volatility"

    TREND = "Trend"

    LIQUIDITY = "Liquidity"

    PRICE = "Price"

    PROBABILITY = "Probability"

    RISK = "Risk"

    STRATEGY = "Strategy"

    RESEARCH = "Research"

    SYSTEM = "System"
