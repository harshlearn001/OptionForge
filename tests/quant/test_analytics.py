"""
==============================================================
OptionForge
tests/quant/test_analytics.py
==============================================================
"""

from optionforge.quant.analytics import (
    OptionAnalytics,
)


def test_call():

    analytics = OptionAnalytics()

    result = analytics.calculate(
        spot=25000,
        strike=25000,
        time=30 / 365,
        rate=0.06,
        volatility=0.20,
        option_type="CE",
    )

    assert result.price > 0

    assert result.delta > 0

    assert result.gamma > 0

    assert result.vega > 0


# ------------------------------------------------------------


def test_put():

    analytics = OptionAnalytics()

    result = analytics.calculate(
        spot=25000,
        strike=25000,
        time=30 / 365,
        rate=0.06,
        volatility=0.20,
        option_type="PE",
    )

    assert result.price > 0

    assert result.delta < 0

    assert result.gamma > 0

    assert result.vega > 0


# ------------------------------------------------------------


def test_implied_volatility():

    analytics = OptionAnalytics()

    result = analytics.calculate(
        spot=25000,
        strike=25000,
        time=30 / 365,
        rate=0.06,
        volatility=0.20,
        option_type="CE",
        market_price=633.98,
    )

    assert result.implied_volatility is not None

    assert abs(result.implied_volatility - 0.20) < 0.01


# ------------------------------------------------------------


def test_repr():

    analytics = OptionAnalytics()

    assert "OptionAnalytics" in repr(
        analytics,
    )
