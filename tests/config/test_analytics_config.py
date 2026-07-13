import pytest

from optionforge.config.analytics_config import (
    AnalyticsConfig,
)


def test_defaults():

    cfg = AnalyticsConfig()

    assert cfg.risk_free_rate == 0.06

    assert cfg.trading_days_per_year == 252

    assert cfg.calendar_days_per_year == 365

    assert cfg.default_volatility == 0.20


def test_repr():

    cfg = AnalyticsConfig()

    assert "AnalyticsConfig" in repr(cfg)


def test_frozen():

    cfg = AnalyticsConfig()

    with pytest.raises(Exception):

        cfg.risk_free_rate = 0.07