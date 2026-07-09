"""
============================================================
OptionForge
Intelligence Type
============================================================

Author      : OptionForge
Module      : intelligence_type.py

Purpose
-------
Defines the major categories of institutional
intelligence produced by the Intelligence Engine.
============================================================
"""

from __future__ import annotations

from enum import Enum
from enum import auto


class IntelligenceType(Enum):
    """
    Categories of institutional intelligence.
    """

    # -----------------------------------------------------
    # Market Bias
    # -----------------------------------------------------

    BULLISH = auto()

    BEARISH = auto()

    NEUTRAL = auto()

    # -----------------------------------------------------
    # Dealer Intelligence
    # -----------------------------------------------------

    DEALER = auto()

    # -----------------------------------------------------
    # Volatility Intelligence
    # -----------------------------------------------------

    VOLATILITY = auto()

    # -----------------------------------------------------
    # Liquidity Intelligence
    # -----------------------------------------------------

    LIQUIDITY = auto()

    # -----------------------------------------------------
    # Trend Intelligence
    # -----------------------------------------------------

    TREND = auto()

    # -----------------------------------------------------
    # Market Structure
    # -----------------------------------------------------

    MARKET_STRUCTURE = auto()

    # -----------------------------------------------------
    # Risk Intelligence
    # -----------------------------------------------------

    RISK = auto()

    # -----------------------------------------------------
    # Composite
    # -----------------------------------------------------

    INSTITUTIONAL = auto()