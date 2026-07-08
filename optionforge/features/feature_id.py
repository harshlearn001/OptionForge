"""
============================================================
OptionForge
Feature Identifier Enumeration
============================================================

Author      : OptionForge
Module      : feature_id.py
Purpose     : Defines every quantitative feature used by the
              Feature Registry.

Each FeatureId represents a unique measurable quantity.

This file is the canonical vocabulary of OptionForge.

Do NOT duplicate identifiers.
Do NOT use string literals throughout the codebase.
============================================================
"""

from __future__ import annotations

from enum import Enum, auto


class FeatureId(Enum):
    """Unique identifiers for all OptionForge features."""

    # ==========================================================
    # GREEKS
    # ==========================================================
    DELTA_EXPOSURE = auto()
    GAMMA_EXPOSURE = auto()
    VEGA_EXPOSURE = auto()
    THETA_EXPOSURE = auto()

    VANNA_EXPOSURE = auto()
    CHARM_EXPOSURE = auto()
    VOMMA_EXPOSURE = auto()

    ZERO_GAMMA = auto()
    GAMMA_FLIP = auto()

    # ==========================================================
    # IMPLIED VOLATILITY
    # ==========================================================
    IMPLIED_VOLATILITY = auto()
    ATM_IV = auto()
    IV_RANK = auto()
    IV_PERCENTILE = auto()
    IV_SKEW = auto()
    IV_TERM_STRUCTURE = auto()

    HISTORICAL_VOLATILITY = auto()
    REALIZED_VOLATILITY = auto()

    # ==========================================================
    # OPEN INTEREST
    # ==========================================================
    PUT_OPEN_INTEREST = auto()
    CALL_OPEN_INTEREST = auto()

    PUT_OI_CHANGE = auto()
    CALL_OI_CHANGE = auto()

    PUT_WRITING = auto()
    CALL_WRITING = auto()

    PUT_UNWINDING = auto()
    CALL_UNWINDING = auto()

    OI_SHIFT = auto()
    OI_CONCENTRATION = auto()

    PCR = auto()
    MODIFIED_PCR = auto()

    # ==========================================================
    # MARKET STRUCTURE
    # ==========================================================
    MAX_PAIN = auto()

    SUPPORT_STRENGTH = auto()
    RESISTANCE_STRENGTH = auto()

    EXPECTED_MOVE = auto()

    ATM_DISTANCE = auto()

    TREND = auto()

    VWAP_DISTANCE = auto()

    ATR = auto()

    # ==========================================================
    # DEALER POSITIONING
    # ==========================================================
    DEALER_POSITION = auto()

    DEALER_PRESSURE = auto()

    DEALER_HEDGING_FLOW = auto()

    DEALER_GAMMA = auto()

    DEALER_DELTA = auto()

    # ==========================================================
    # INSTITUTIONAL
    # ==========================================================
    INSTITUTIONAL_SIGNAL = auto()

    INSTITUTIONAL_CONFIDENCE = auto()

    SMART_MONEY_SCORE = auto()

    # ==========================================================
    # LIQUIDITY
    # ==========================================================
    BID_ASK_SPREAD = auto()

    MARKET_DEPTH = auto()

    VOLUME = auto()

    TURNOVER = auto()

    # ==========================================================
    # VOLATILITY REGIME
    # ==========================================================
    VOLATILITY_STATE = auto()

    EXPLOSION_RISK = auto()

    COMPRESSION_SCORE = auto()

    # ==========================================================
    # DECISION
    # ==========================================================
    MARKET_STATE = auto()

    PROBABILITY = auto()

    RISK_SCORE = auto()

    CONFIDENCE_SCORE = auto()

    STRATEGY_SCORE = auto()

    # ==========================================================
    # RESEARCH
    # ==========================================================
    HISTORICAL_MATCH_SCORE = auto()

    BACKTEST_WIN_RATE = auto()

    SHARPE_RATIO = auto()

    PROFIT_FACTOR = auto()

    MAX_DRAWDOWN = auto()