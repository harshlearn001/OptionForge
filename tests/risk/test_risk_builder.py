"""
============================================================
OptionForge
RiskBuilder Tests
============================================================
"""

from optionforge.risk.risk_builder import RiskBuilder
from optionforge.risk.risk_level import RiskLevel
from optionforge.risk.risk_result import RiskResult
from optionforge.risk.risk_type import RiskType
from optionforge.risk.rule_result import RuleResult


def passed_rule(
    score: float = 5.0,
) -> RuleResult:

    return RuleResult(
        rule_name="CapitalRule",
        score=score,
        passed=True,
        warnings=(),
        reasons=("Passed.",),
    )


def failed_rule(
    score: float = 90.0,
) -> RuleResult:

    return RuleResult(
        rule_name="MarginRule",
        score=score,
        passed=False,
        warnings=("Risk exceeded.",),
        reasons=("Rule failed.",),
    )


def test_build_approved():

    result = RiskResult(
        rule_results=(
            passed_rule(),
            passed_rule(),
        ),
    )

    risk = RiskBuilder().build(
        result=result,
    )

    assert risk.approved

    assert risk.risk_type is RiskType.APPROVED


def test_build_review():

    result = RiskResult(
        rule_results=(
            passed_rule(),
            failed_rule(
                score=40.0,
            ),
        ),
    )

    risk = RiskBuilder().build(
        result=result,
    )

    assert not risk.approved

    assert risk.risk_type is RiskType.REVIEW


def test_build_rejected():

    result = RiskResult(
        rule_results=(
            failed_rule(
                score=95.0,
            ),
        ),
    )

    risk = RiskBuilder().build(
        result=result,
    )

    assert not risk.approved

    assert risk.risk_type is RiskType.REJECTED


def test_risk_level():

    result = RiskResult(
        rule_results=(
            failed_rule(
                score=80.0,
            ),
        ),
    )

    risk = RiskBuilder().build(
        result=result,
    )

    assert isinstance(
        risk.risk_level,
        RiskLevel,
    )


def test_position_size_range():

    result = RiskResult(
        rule_results=(
            failed_rule(
                score=30.0,
            ),
        ),
    )

    risk = RiskBuilder().build(
        result=result,
    )

    assert 0.0 <= risk.recommended_position_size <= 100.0


def test_capital_allocation_range():

    result = RiskResult(
        rule_results=(
            failed_rule(
                score=30.0,
            ),
        ),
    )

    risk = RiskBuilder().build(
        result=result,
    )

    assert 0.0 <= risk.max_capital_allocation <= 100.0


def test_score_matches_result():

    result = RiskResult(
        rule_results=(
            failed_rule(
                score=70.0,
            ),
        ),
    )

    risk = RiskBuilder().build(
        result=result,
    )

    assert risk.risk_score == result.overall_score


def test_warning_forwarding():

    result = RiskResult(
        rule_results=(failed_rule(),),
    )

    risk = RiskBuilder().build(
        result=result,
    )

    assert risk.warning_count == 1


def test_reason_forwarding():

    result = RiskResult(
        rule_results=(failed_rule(),),
    )

    risk = RiskBuilder().build(
        result=result,
    )

    assert risk.reason_count == 1


def test_build_returns_risk():

    result = RiskResult(
        rule_results=(passed_rule(),),
    )

    risk = RiskBuilder().build(
        result=result,
    )

    assert risk.__class__.__name__ == "Risk"
