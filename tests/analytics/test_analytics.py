from datetime import date

from optionforge.analytics import OptionAnalytics
from optionforge.models import (
    AnalyticsResult,
    OptionContract,
)
from optionforge.quant.black_scholes import BlackScholes


def build_contract() -> OptionContract:

    spot = 25000
    strike = 25000
    rate = 0.06
    time = 30 / 365
    volatility = 0.20

    market_price = BlackScholes.call_price(
        spot,
        strike,
        time,
        rate,
        volatility,
    )

    return OptionContract(
        symbol="NIFTY",
        trade_date=date(2026, 6, 27),
        expiry_date=date(2026, 7, 2),
        strike=strike,
        option_type="CE",
        market_price=market_price,
        spot_price=spot,
        risk_free_rate=rate,
        time_to_expiry=time,
    )


def test_returns_result():

    result = OptionAnalytics.calculate(build_contract())

    assert isinstance(
        result,
        AnalyticsResult,
    )


def test_iv_positive():

    result = OptionAnalytics.calculate(build_contract())

    assert result.implied_volatility > 0


def test_delta_range():

    result = OptionAnalytics.calculate(build_contract())

    assert 0 <= result.delta <= 1


def test_gamma_positive():

    result = OptionAnalytics.calculate(build_contract())

    assert result.gamma > 0


def test_vega_positive():

    result = OptionAnalytics.calculate(build_contract())

    assert result.vega > 0


def test_intrinsic_value():

    result = OptionAnalytics.calculate(build_contract())

    assert result.intrinsic_value == 0


def test_time_value_positive():

    result = OptionAnalytics.calculate(build_contract())

    assert result.time_value > 0
