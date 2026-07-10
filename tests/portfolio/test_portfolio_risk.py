"""
============================================================
OptionForge
Portfolio Risk Tests
============================================================
"""

from optionforge.portfolio.portfolio_risk import (
    PortfolioRisk,
)


# ==========================================================
# Enum
# ==========================================================

def test_enum_members():

    assert len(

        PortfolioRisk,

    ) == 4


# ==========================================================
# Conservative
# ==========================================================

def test_conservative():

    risk = PortfolioRisk.CONSERVATIVE

    assert risk.is_conservative

    assert risk.score == 1

    assert risk.max_capital_per_trade == 2.0

    assert risk.max_portfolio_exposure == 40.0

    assert risk.requires_diversification

    assert not risk.allows_unlimited_risk


# ==========================================================
# Balanced
# ==========================================================

def test_balanced():

    risk = PortfolioRisk.BALANCED

    assert risk.is_balanced

    assert risk.score == 2

    assert risk.max_capital_per_trade == 5.0

    assert risk.max_portfolio_exposure == 70.0

    assert risk.requires_diversification


# ==========================================================
# Aggressive
# ==========================================================

def test_aggressive():

    risk = PortfolioRisk.AGGRESSIVE

    assert risk.is_aggressive

    assert risk.score == 3

    assert risk.max_capital_per_trade == 10.0

    assert risk.max_portfolio_exposure == 90.0

    assert not risk.requires_diversification


# ==========================================================
# Institutional
# ==========================================================

def test_institutional():

    risk = PortfolioRisk.INSTITUTIONAL

    assert risk.is_institutional

    assert risk.score == 4

    assert risk.max_capital_per_trade == 20.0

    assert risk.max_portfolio_exposure == 100.0

    assert risk.allows_unlimited_risk

    assert not risk.requires_diversification


# ==========================================================
# Factory
# ==========================================================

def test_from_score():

    assert (

        PortfolioRisk.from_score(1)

        is PortfolioRisk.CONSERVATIVE

    )

    assert (

        PortfolioRisk.from_score(2)

        is PortfolioRisk.BALANCED

    )

    assert (

        PortfolioRisk.from_score(3)

        is PortfolioRisk.AGGRESSIVE

    )

    assert (

        PortfolioRisk.from_score(4)

        is PortfolioRisk.INSTITUTIONAL

    )

    assert (

        PortfolioRisk.from_score(99)

        is PortfolioRisk.INSTITUTIONAL

    )


# ==========================================================
# String
# ==========================================================

def test_str():

    assert (

        str(

            PortfolioRisk.CONSERVATIVE,

        )

        == "Conservative"

    )

    assert (

        str(

            PortfolioRisk.INSTITUTIONAL,

        )

        == "Institutional"

    )


# ==========================================================
# Deterministic
# ==========================================================

def test_deterministic():

    assert (

        PortfolioRisk.BALANCED

        is PortfolioRisk.BALANCED

    )