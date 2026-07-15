"""
==============================================================
OptionForge
Tests - OI Summary Engine
==============================================================
"""

from optionforge.oi.oi_by_strike import OIByStrike
from optionforge.oi.oi_summary_engine import OISummaryEngine
from optionforge.oi.oi_summary_result import OISummaryResult

from tests.fixtures.option_chain_fixture import build_option_chain


def test_returns_result():

    chain = build_option_chain()

    oi = OIByStrike(chain)

    result = OISummaryEngine.calculate(oi)

    assert isinstance(result, OISummaryResult)


def test_total_oi():

    chain = build_option_chain()

    oi = OIByStrike(chain)

    result = OISummaryEngine.calculate(oi)

    assert result.total_oi > 0


def test_pcr():

    chain = build_option_chain()

    oi = OIByStrike(chain)

    result = OISummaryEngine.calculate(oi)

    assert result.pcr >= 0


def test_strikes():

    chain = build_option_chain()

    oi = OIByStrike(chain)

    result = OISummaryEngine.calculate(oi)

    assert result.strikes == len(oi)


def test_dominant_side():

    chain = build_option_chain()

    oi = OIByStrike(chain)

    result = OISummaryEngine.calculate(oi)

    assert result.dominant_side in (
        "CALL",
        "PUT",
        "BALANCED",
    )
