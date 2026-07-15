"""
==============================================================
Tests for WallClassifier
==============================================================
"""

from __future__ import annotations

from optionforge.common.enums import WallType
from optionforge.oi.wall_classifier import WallClassifier


# ==========================================================
# Call Wall
# ==========================================================

def test_call_wall():

    result = WallClassifier.classify(
        call_share=0.65,
        put_share=0.35,
    )

    assert result is WallType.CALL_WALL


# ==========================================================
# Put Wall
# ==========================================================

def test_put_wall():

    result = WallClassifier.classify(
        call_share=0.30,
        put_share=0.70,
    )

    assert result is WallType.PUT_WALL


# ==========================================================
# Balanced
# ==========================================================

def test_balanced():

    result = WallClassifier.classify(
        call_share=0.50,
        put_share=0.50,
    )

    assert result is WallType.BALANCED


# ==========================================================
# Zero Shares
# ==========================================================

def test_zero_shares():

    result = WallClassifier.classify(
        call_share=0.0,
        put_share=0.0,
    )

    assert result is WallType.BALANCED


# ==========================================================
# Equal Shares
# ==========================================================

def test_equal_shares():

    result = WallClassifier.classify(
        call_share=0.25,
        put_share=0.25,
    )

    assert result is WallType.BALANCED