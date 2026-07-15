"""
============================================================
OptionForge
Portfolio Type Tests
============================================================
"""

from optionforge.portfolio.portfolio_type import (
    PortfolioType,
)

# ==========================================================
# Enum
# ==========================================================


def test_enum_members():

    assert (
        len(
            PortfolioType,
        )
        == 6
    )


# ==========================================================
# Directional
# ==========================================================


def test_directional():

    portfolio = PortfolioType.DIRECTIONAL

    assert portfolio.is_directional

    assert portfolio.requires_active_management

    assert portfolio.allows_leverage


# ==========================================================
# Income
# ==========================================================


def test_income():

    portfolio = PortfolioType.INCOME

    assert portfolio.is_income

    assert portfolio.is_defensive

    assert not portfolio.allows_leverage


# ==========================================================
# Volatility
# ==========================================================


def test_volatility():

    portfolio = PortfolioType.VOLATILITY

    assert portfolio.is_volatility

    assert portfolio.requires_active_management

    assert portfolio.allows_leverage


# ==========================================================
# Hedging
# ==========================================================


def test_hedging():

    portfolio = PortfolioType.HEDGING

    assert portfolio.is_hedging

    assert portfolio.requires_active_management

    assert portfolio.is_defensive


# ==========================================================
# Market Neutral
# ==========================================================


def test_market_neutral():

    portfolio = PortfolioType.MARKET_NEUTRAL

    assert portfolio.is_market_neutral

    assert not portfolio.allows_leverage


# ==========================================================
# Cash
# ==========================================================


def test_cash():

    portfolio = PortfolioType.CASH

    assert portfolio.is_cash

    assert portfolio.is_defensive

    assert not portfolio.requires_active_management


# ==========================================================
# String
# ==========================================================


def test_str():

    assert (
        str(
            PortfolioType.MARKET_NEUTRAL,
        )
        == "Market Neutral"
    )


# ==========================================================
# Deterministic
# ==========================================================


def test_deterministic():

    assert PortfolioType.CASH is PortfolioType.CASH
