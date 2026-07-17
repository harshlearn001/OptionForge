"""
============================================================
OptionForge
Evidence Source
============================================================

Author      : OptionForge
Module      : evidence_source.py
Purpose     : Standard source of institutional evidence.

Each Evidence object originates from exactly one
EvidenceSource.

============================================================
"""

from __future__ import annotations

from enum import StrEnum


class EvidenceSource(StrEnum):
    """
    Standard evidence producers.
    """

    # =====================================================
    # Analytics
    # =====================================================

    GREEKS = "Greeks"

    IMPLIED_VOLATILITY = "Implied Volatility"

    IV_RANK = "IV Rank"

    IV_PERCENTILE = "IV Percentile"

    EXPECTED_MOVE = "Expected Move"

    GAMMA_EXPOSURE = "Gamma Exposure"

    MAX_PAIN = "Max Pain"

    SMART_PCR = "Smart PCR"

    # =====================================================
    # Future Analytics
    # =====================================================

    DEALER_GAMMA = "Dealer Gamma"

    DELTA_EXPOSURE = "Delta Exposure"

    VOLUME_PROFILE = "Volume Profile"

    LIQUIDITY = "Liquidity"

    VOLATILITY_SURFACE = "Volatility Surface"

    SKEW = "Skew"

    TERM_STRUCTURE = "Term Structure"

    OPEN_INTEREST = "Open Interest"

    def __str__(self) -> str:

        return self.value